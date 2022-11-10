#include "ReadWriteLock.h"
#include <assert.h>


ReadWriteLock::ReadWriteLock(bool preferWriter)
	:m_PreferWriter(preferWriter)
{
}
void ReadWriteLock::ReadLock()
{
	++m_WaitingReaders;
	while (m_WritingWriters > 0 || (m_PreferWriter && m_WaitingWriters > 0))
	{
		std::unique_lock<std::mutex> lk(m_Mutex);
		m_ConditionVariable.wait(lk, [&] {return !(m_WritingWriters > 0 || (m_PreferWriter && m_WaitingWriters > 0)); });
	}
	assert(!(m_WritingWriters > 0 || (m_PreferWriter && m_WaitingWriters > 0)));
	++m_ReadingReaders;
	--m_WaitingReaders;
}
void ReadWriteLock::ReadUnLock()
{
	--m_ReadingReaders;
	m_ConditionVariable.notify_all();
}
void ReadWriteLock::WriteLock()
{
	++m_WaitingWriters;
	while (m_WritingWriters > 0 || m_ReadingReaders > 0)
	{
		std::unique_lock<std::mutex> lk(m_Mutex);
		m_ConditionVariable.wait(lk, [&] {return !(m_WritingWriters > 0 || m_ReadingReaders > 0); });
	}
	assert(!(m_WritingWriters > 0 || m_ReadingReaders > 0));
	++m_WritingWriters;
	--m_WaitingWriters;
}
void ReadWriteLock::WriteUnLock()
{
	--m_WritingWriters;
	m_ConditionVariable.notify_all();
}

AutoReadLock::AutoReadLock(ReadWriteLock* rwLock) :m_ReadWriteLock(rwLock)
{
	m_ReadWriteLock->ReadLock();
}
AutoReadLock::~AutoReadLock()
{
	m_ReadWriteLock->ReadUnLock();
}

AutoWriteLock::AutoWriteLock(ReadWriteLock* rwLock) :m_ReadWriteLock(rwLock)
{
	m_ReadWriteLock->WriteLock();
}
AutoWriteLock::~AutoWriteLock()
{
	m_ReadWriteLock->WriteUnLock();
}


