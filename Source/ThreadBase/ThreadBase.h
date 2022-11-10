#pragma once
#include <thread>
#include <atomic>
#include <string>
#include <list>
#include <mutex>
#include <condition_variable>
#include "Event.h"



class ThreadBase
{
public:
	ThreadBase(const char* name);
	virtual ~ThreadBase();
	
	void SetTimeOut(int milliSeconds);
	virtual bool Start();
	virtual void Stop();
	virtual void Join();
	
	virtual void OnEvent(Event* event);
protected:
	void ThreadFunc();
	virtual void ThreadInit();
	virtual void Run();
	virtual void ThreadExit();

	virtual void CheckEvent();
	virtual void HandleEvent() = 0;
	virtual Event* GetEvent();
	

protected:
	std::thread m_Thread;
	std::string m_ThreadName;
	std::atomic<bool> m_ShouldRun;
	std::chrono::milliseconds m_TimeOut;

	std::mutex m_ThreadMutex;
	std::condition_variable m_ThreadConditionVariable;

	std::list<Event*> m_Events;
	std::mutex m_EventMutex;
};

