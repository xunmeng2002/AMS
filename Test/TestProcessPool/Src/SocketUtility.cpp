#include "SocketUtility.h"
#include "Logger.h"
#include <fcntl.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/epoll.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <signal.h>
#include <assert.h>
#include <stdio.h>


extern int SigPipeFd[2];

int SetNonBlocking(int fd)
{
	int oldOption = fcntl(fd, F_GETFL);
	int newOption = oldOption | O_NONBLOCK;
	fcntl(fd, F_SETFL, newOption);
	return oldOption;
}
bool SetSockReuse(int fd, int resue)
{
	auto ret = ::setsockopt(fd, SOL_SOCKET, SO_REUSEADDR, (char*)&resue, sizeof(int));
	if (ret < 0)
	{
		WRITE_LOG(LogLevel::Info, "setsockopt SO_REUSEADDR[%d] Failed. Ret:[%d]", resue, ret);
		return false;
	}
	return true;
}
void AddFd(int epollFd, int fd)
{
	epoll_event event;
	event.data.fd = fd;
	event.events = EPOLLIN | EPOLLET;
	epoll_ctl(epollFd, EPOLL_CTL_ADD, fd, &event);
	SetNonBlocking(fd);
}
void RemoveFd(int epollFd, int fd)
{
	epoll_ctl(epollFd, EPOLL_CTL_DEL, fd, 0);
	close(fd);
}
void SigHandler(int sig)
{
	int saveErrno = errno;
	int msg = sig;
	send(SigPipeFd[1], (char*)&msg, 1, 0);
	errno = saveErrno;
}
void AddSig(int sig, void (handler)(int), bool restart)
{
	struct sigaction sa;
	::memset(&sa, 0, sizeof(sa));
	sa.sa_handler = handler;
	if (restart)
	{
		sa.sa_flags != SA_RESTART;
	}
	sigfillset(&sa.sa_mask);
	assert(sigaction(sig, &sa, nullptr) != -1);
}
