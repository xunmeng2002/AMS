#include <cstdio>
#include "CgiConn.h"
#include "Logger.h"



int main()
{
    Logger::GetInstance().Init("TestProcessPool");
    Logger::GetInstance().SetLogLevel(LogLevel::Info, LogLevel::Info);
    Logger::GetInstance().Start();

    const char* ip = "192.168.2.238";
    int port = 10000;

    int listenFd = socket(PF_INET, SOCK_STREAM, 0);
    assert(listenFd >= 0);
    assert(SetSockReuse(listenFd));
    int ret = 0;
    sockaddr_in address;
    bzero(&address, sizeof(address));
    address.sin_family = AF_INET;
    inet_pton(AF_INET, ip, &address.sin_addr);
    address.sin_port = htons(port);

    ret = bind(listenFd, (sockaddr*)&address, sizeof(address));
    assert(ret != -1);
    ret = listen(listenFd, 5);
    ProcessPool<CgiConn>* pool = ProcessPool<CgiConn>::Create(listenFd);
    if (pool)
    {
        pool->Run();
        delete pool;
    }

    close(listenFd);

    Logger::GetInstance().Stop();
    Logger::GetInstance().Join();
    return 0;
}