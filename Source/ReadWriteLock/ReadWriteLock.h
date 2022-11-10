#pragma once
#include <atomic>
#include <mutex>
#include <condition_variable>


class ReadWriteLock
{
public:
	ReadWriteLock(bool preferWriter = true);
	void ReadLock();
	void ReadUnLock();
	void WriteLock();
	void WriteUnLock();

private:
	std::mutex m_Mutex;
	std::condition_variable m_ConditionVariable;
	bool m_PreferWriter;

	std::atomic<int> m_WaitingReaders;
	std::atomic<int> m_ReadingReaders;
	std::atomic<int> m_WaitingWriters;
	std::atomic<int> m_WritingWriters;
};

class AutoReadLock
{
public:
	AutoReadLock(ReadWriteLock* rwLock);
	~AutoReadLock();

private:
	ReadWriteLock* m_ReadWriteLock;
};

class AutoWriteLock
{
public:
	AutoWriteLock(ReadWriteLock* rwLock);
	~AutoWriteLock();

private:
	ReadWriteLock* m_ReadWriteLock;
};
