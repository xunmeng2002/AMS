#pragma once
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/epoll.h>
#include <sys/wait.h>
#include <sys/stat.h>
#include <assert.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>
#include <arpa/inet.h>
#include <fcntl.h>
#include <stdlib.h>
#include <signal.h>
#include "SocketUtility.h"
#include "Logger.h"

extern int SigPipeFd[2];

class Process
{
public:
	Process() : m_Pid(-1) {}

public:
	pid_t m_Pid;
	int m_pipefd[2];
};

template<typename T>
class ProcessPool
{
private:
	ProcessPool(int listenFd, int processNumber = 8);
public:
	static ProcessPool<T>* Create(int listenFd, int processNumber = 8)
	{
		if (!m_Instance)
		{
			m_Instance = new ProcessPool<T>(listenFd, processNumber);
		}
		return m_Instance;
	}
	~ProcessPool()
	{
		delete[] m_SubProcess;
	}
	void Run();

private:
	void SetupSigPipe();
	void RunParent();
	void RunChild();

private:
	static const int MaxProcessNumber = 16;
	static const int UserPerProcess = 65536;
	static const int MaxEventNumber = 10000;
	int m_ProcessNumber;
	int m_Index;
	int m_EpollFd;
	int m_ListenFd;
	int m_Stop;
	Process* m_SubProcess;
	static ProcessPool<T>* m_Instance;
};

template<typename T>
ProcessPool<T>* ProcessPool<T>::m_Instance = nullptr;
template<typename T>
ProcessPool<T>::ProcessPool(int listenFd, int processNumber)
	: m_ListenFd(listenFd), m_ProcessNumber(processNumber), m_Index(-1)
{
	assert((processNumber > 0) && (processNumber <= MaxProcessNumber));
	m_SubProcess = new Process[processNumber];
	assert(m_SubProcess);

	for (auto i = 0; i < processNumber; i++)
	{
		int ret = socketpair(PF_UNIX, SOCK_STREAM, 0, m_SubProcess[i].m_pipefd);
		assert(ret == 0);

		m_SubProcess[i].m_Pid = fork();
		assert(m_SubProcess[i].m_Pid >= 0);
		if (m_SubProcess[i].m_Pid > 0)
		{
			close(m_SubProcess[i].m_pipefd[1]);
			WRITE_LOG(LogLevel::Info, "SubProcess [%d] Start.\n", i);
			continue;
		}
		else
		{
			close(m_SubProcess[i].m_pipefd[0]);
			m_Index = i;
			WRITE_LOG(LogLevel::Info, "Parent Process\n");
			break;
		}
	}
}
template<typename T>
void ProcessPool<T>::Run()
{
	WRITE_LOG(LogLevel::Info, "ProcessPool<T>::Run Index:[%d]\n", m_Index);
	if (m_Index != -1)
	{
		RunChild();
	}
	else
	{
		RunParent();
	}
}
template<typename T>
void ProcessPool<T>::SetupSigPipe()
{
	m_EpollFd = epoll_create(5);
	int ret = socketpair(PF_UNIX, SOCK_STREAM, 0, SigPipeFd);
	assert(ret != -1);
	SetNonBlocking(SigPipeFd[1]);
	AddFd(m_EpollFd, SigPipeFd[0]);
	AddSig(SIGCHLD, SigHandler);
	AddSig(SIGTERM, SigHandler);
	AddSig(SIGINT, SigHandler);
	AddSig(SIGPIPE, SIG_IGN);
}
template<typename T>
void ProcessPool<T>::RunParent()
{
	SetupSigPipe();
	AddFd(m_EpollFd, m_ListenFd);
	epoll_event events[MaxEventNumber];
	int subProcessCounter = 0;
	int newConn = 1;
	int number = 0;
	int ret = -1;

	while (!m_Stop)
	{
		number = epoll_wait(m_EpollFd, events, MaxEventNumber, -1);
		if (number < 0 && errno != EINTR)
		{
			WRITE_LOG(LogLevel::Info, "m_Index:[%d] epoll failed\n", m_Index);
			break;
		}
		WRITE_LOG(LogLevel::Info, "m_Index:[%d] epoll_wait number:[%d]\n", m_Index, number);
		for (int i = 0; i < number; i++)
		{
			int sockFd = events[i].data.fd;
			if (sockFd == m_ListenFd)
			{
				int j = subProcessCounter;
				do
				{
					if (m_SubProcess[j].m_Pid != -1)
					{
						break;
					}
					j = (j + 1) % m_ProcessNumber;
				} while (j != subProcessCounter);
				if (m_SubProcess[j].m_Pid == -1)
				{
					m_Stop = true;
					break;
				}
				subProcessCounter = (j + 1) % m_ProcessNumber;
				send(m_SubProcess[j].m_pipefd[0], (char*)&newConn, sizeof(newConn), 0);
				WRITE_LOG(LogLevel::Info, "m_Index:[%d] send request to child % d\n", m_Index, j);
			}
			else if (sockFd == SigPipeFd[0] && events[i].events & EPOLLIN)
			{
				WRITE_LOG(LogLevel::Info, "m_Index:[%d] SigPipeFd[0] Recv.\n", m_Index);
				int sig;
				char signals[1024];
				ret = recv(SigPipeFd[0], signals, sizeof(signals), 0);
				if (ret <= 0)
				{
					WRITE_LOG(LogLevel::Info, "m_Index:[%d] recv Failed. ret:[%d]\n", m_Index, ret);
					continue;
				}
				else
				{
					WRITE_LOG(LogLevel::Info, "m_Index:[%d] recv Success. signals: [%s]\n", m_Index, signals);
					for (int i = 0; i < ret; i++)
					{
						WRITE_LOG(LogLevel::Info, "m_Index:[%d] signals[%d]:[%d]\n", m_Index, i, signals[i]);
						switch (signals[i])
						{
						case SIGCHLD:
						{
							pid_t pid;
							int stat;
							while ((pid = waitpid(-1, &stat, WNOHANG)) > 0)
							{
								for (int i = 0; i < m_ProcessNumber; ++i)
								{
									if (m_SubProcess[i].m_Pid == pid)
									{
										WRITE_LOG(LogLevel::Info, "m_Index:[%d] child %d join\n", i, m_Index);
										close(m_SubProcess[i].m_pipefd[0]);
										m_SubProcess[i].m_Pid = -1;
									}
								}
							}
							m_Stop = true;
							for (int i = 0; i < m_ProcessNumber; i++)
							{
								if (m_SubProcess[i].m_Pid != -1)
								{
									m_Stop = false;
								}
							}
							break;
						}
						case SIGTERM:
						case SIGINT:
						{
							WRITE_LOG(LogLevel::Info, "m_Index:[%d] kill all the child now\n", m_Index);
							for (int i = 0; i < m_ProcessNumber; i++)
							{
								int pid = m_SubProcess[i].m_Pid;
								if (pid != -1)
								{
									kill(pid, SIGTERM);
								}
							}
							break;
						}
						default:
							break;
						}
					}
				}
			}
			else
			{
				continue;
			}
		}
	}
	close(m_EpollFd);
}
template<typename T>
void ProcessPool<T>::RunChild()
{
	SetupSigPipe();
	int pipeFd = m_SubProcess[m_Index].m_pipefd[1];
	AddFd(m_EpollFd, pipeFd);

	epoll_event events[MaxEventNumber];
	T* users = new T[UserPerProcess];
	assert(users);
	int number = 0;
	int ret = -1;
	while (!m_Stop)
	{
		number = epoll_wait(m_EpollFd, events, MaxEventNumber, -1);
		if (number < 0 && errno != EINTR)
		{
			WRITE_LOG(LogLevel::Info, "m_Index:[%d] epoll failed\n", m_Index);
			break;
		}
		WRITE_LOG(LogLevel::Info, "m_Index:[%d] epoll_wait number:[%d]\n", m_Index, number);
		for (int i = 0; i < number; i++)
		{
			int sockFd = events[i].data.fd;
			if (sockFd == pipeFd && (events[i].events & EPOLLIN))
			{
				WRITE_LOG(LogLevel::Info, "m_Index:[%d] recv Event.\n", m_Index);
				int client = 0;
				ret = recv(sockFd, (char*)&client, sizeof(client), 0);
				if ((ret < 0 && errno != EAGAIN) || ret == 0)
				{
					WRITE_LOG(LogLevel::Info, "m_Index:[%d] recv failed. ret:[%d], errno:[%d]\n", m_Index, ret, errno);
					continue;
				}
				else
				{
					sockaddr_in clientAddress;
					socklen_t clientAddressLen = sizeof(sockaddr_in);
					int connFd = accept(m_ListenFd, (struct sockaddr*)&clientAddress, &clientAddressLen);
					if (connFd < 0)
					{
						WRITE_LOG(LogLevel::Info, "m_Index:[%d] accept Failed. connFd:%d, errno: %d\n", m_Index, connFd, errno);
						continue;
					}
					WRITE_LOG(LogLevel::Info, "m_Index:[%d] accept Success. connFd:%d, errno: %d\n", m_Index, connFd, errno);
					AddFd(m_EpollFd, connFd);
					users[connFd].Init(m_EpollFd, connFd, clientAddress);
				}
			}
			else if ((sockFd == SigPipeFd[0]) && (events[i].events & EPOLLIN))
			{
				WRITE_LOG(LogLevel::Info, "m_Index:[%d] SigPipeFd[0] sockFd:[%d].\n", m_Index, sockFd);
				int sig;
				char signals[1024];
				ret = recv(SigPipeFd[0], signals, sizeof(signals), 0);
				if (ret <= 0)
				{
					WRITE_LOG(LogLevel::Info, "m_Index:[%d] recv failed. ret:[%d], errno:[%d]\n", m_Index, ret, errno);
					continue;
				}
				else
				{
					WRITE_LOG(LogLevel::Info, "m_Index:[%d] recv Success. signals: [%s]\n", m_Index, signals);
					for (int i = 0; i < ret; i++)
					{
						WRITE_LOG(LogLevel::Info, "m_Index:[%d] signals[%d]:[%d]\n", m_Index, i, signals[i]);
						switch (signals[i])
						{
						case SIGCHLD:
						{
							pid_t pid;
							int stat;
							while ((pid = waitpid(-1, &stat, WNOHANG)) > 0)
							{
								continue;
							}
							break;
						}
						case SIGTERM:
						case SIGINT:
						{
							m_Stop = true;
							break;
						}
						default:
							break;
						}
					}
				}
			}
			else if (events[i].events & EPOLLIN)
			{
				WRITE_LOG(LogLevel::Info, "m_Index:[%d] users[%d].Process()\n", m_Index, sockFd);
				users[sockFd].Process();
			}
			else
			{
				WRITE_LOG(LogLevel::Info, "m_Index:[%d] else Contiunue\n", m_Index);
				continue;
			}
		}
	}

	delete[] users;
	users = nullptr;
	close(pipeFd);
	close(m_EpollFd);
}





