#include "CgiConn.h"
#include "Logger.h"


int CgiConn::m_EpollFd = -1;

CgiConn::CgiConn()
{}
CgiConn::~CgiConn()
{}
void CgiConn::Init(int epollFd, int sockFd, const sockaddr_in& clientAddr)
{
	m_EpollFd = epollFd;
	m_SockFd = sockFd;
	m_Address = clientAddr;
	memset(m_Buf, 0, BufferSize);
	m_ReadIndex = 0;
}
void CgiConn::Process()
{
	int index = 0;
	int ret = -1;
	while (true)
	{
		index = m_ReadIndex;
		ret = recv(m_SockFd, m_Buf + index, BufferSize - 1 - index, 0);
		WRITE_LOG(LogLevel::Info, "m_SockFd:[%d] recv ret:[%d], errno:[%d]\n", ret, errno);
		if (ret < 0)
		{
			if (errno != EAGAIN)
			{
				RemoveFd(m_EpollFd, m_SockFd);
			}
			break;
		}
		else if (ret == 0)
		{
			RemoveFd(m_EpollFd, m_SockFd);
			break;
		}
		else
		{
			m_ReadIndex += ret;
			WRITE_LOG(LogLevel::Info, "User Content is [%s]\n", m_Buf);
			for (; index < m_ReadIndex; ++index)
			{
				if (index >= 1 && m_Buf[index - 1] == '\r' && m_Buf[index] == '\n')
				{
					break;
				}
			}
			if (index == m_ReadIndex)
			{
				WRITE_LOG(LogLevel::Info, "m_SockFd:[%d] Continue, Recv more data\n", m_SockFd);
				continue;
			}
			m_Buf[index - 1] = '\0';
			char* fileName = m_Buf;
			if (access(fileName, F_OK) == -1)
			{
				WRITE_LOG(LogLevel::Info, "m_SockFd:[%d] access Failed. fileName:[%s]\n", m_SockFd, fileName);
				RemoveFd(m_EpollFd, m_SockFd);
				break;
			}
			WRITE_LOG(LogLevel::Info, "m_SockFd:[%d] access Successed. fileName:[%s]\n", m_SockFd, fileName);
			ret = fork();
			if (ret == -1)
			{
				RemoveFd(m_EpollFd, m_SockFd);
				break;
			}
			else if (ret > 0)
			{
				RemoveFd(m_EpollFd, m_SockFd);
				break;
			}
			else
			{
				close(STDOUT_FILENO);
				dup(m_SockFd);
				execl(m_Buf, m_Buf, 0);
				exit(0);
			}
		}
	}
}


