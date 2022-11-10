#pragma once
#include "ProcessPool.h"


class CgiConn
{
public:
	CgiConn();
	~CgiConn();

	void Init(int epollFd, int sockFd, const sockaddr_in& clientAddr);
	void Process();


private:
	static const int BufferSize = 1024;
	static int m_EpollFd;
	int m_SockFd;
	sockaddr_in m_Address;
	char m_Buf[BufferSize];
	int m_ReadIndex;
};

