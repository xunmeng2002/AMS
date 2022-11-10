#include <functional>
#include "ThreadBase.h"
#include "Logger.h"


ThreadBase::ThreadBase(const char* name)
	:m_ShouldRun(false), m_TimeOut(100)
{
	m_ThreadName = name;
}
ThreadBase::~ThreadBase()
{
}

void ThreadBase::SetTimeOut(int milliSeconds)
{
	m_TimeOut = std::chrono::milliseconds(milliSeconds);
}
bool ThreadBase::Start()
{
	if (m_ShouldRun.load())
		return false;

	m_ShouldRun.store(true);
	m_Thread = std::thread(std::bind(&ThreadBase::ThreadFunc, this));
	return true;
}
void ThreadBase::Stop()
{
	m_ShouldRun.store(false);
}
void ThreadBase::Join()
{
	if (m_Thread.joinable())
		m_Thread.join();
}

void ThreadBase::ThreadFunc()
{
	ThreadInit();
	while (m_ShouldRun.load())
	{
		Run();
	}
	ThreadExit();
}
void ThreadBase::ThreadInit()
{
	WRITE_LOG(LogLevel::Info, "Thread[%d]:%s Start", m_Thread.get_id(), m_ThreadName.c_str());
}
void ThreadBase::Run()
{
	CheckEvent();
	HandleEvent();
}
void ThreadBase::ThreadExit()
{
	WRITE_LOG(LogLevel::Info, "Thread[%d]:%s Exit", m_Thread.get_id(), m_ThreadName.c_str());
}

void ThreadBase::CheckEvent()
{
	std::unique_lock<std::mutex> guard(m_ThreadMutex);
	m_ThreadConditionVariable.wait_for(guard, m_TimeOut, [&] {return !m_Events.empty();});
}
Event* ThreadBase::GetEvent()
{
	std::lock_guard<std::mutex> guard(m_EventMutex);
	if (m_Events.empty())
	{
		return nullptr;
	}
	auto myEvent = m_Events.front();
	m_Events.pop_front();
	return myEvent;
}
void ThreadBase::OnEvent(Event* event)
{
	std::lock_guard<std::mutex> guard(m_EventMutex);
	m_Events.push_back(event);

	m_ThreadConditionVariable.notify_one();
}