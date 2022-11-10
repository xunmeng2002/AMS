#pragma once


int SetNonBlocking(int fd);
bool SetSockReuse(int fd, int resue = 1);
void AddFd(int epollFd, int fd);
void RemoveFd(int epollFd, int fd);
void SigHandler(int sig);
void AddSig(int sig, void (handler)(int), bool restart = true);



