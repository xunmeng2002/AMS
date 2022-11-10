#include "Logger.h"
#include "Utility.h"
#include <assert.h>
#include <iostream>
#include "LogData.h"
#include "TimeUtility.h"
#include <stdarg.h>
#include <filesystem>

#define LOG_LINE_LENGTH 64 * 1024
#define MAX_LOG_FORMAT_LENGTH 1024
#define MAX_LOG_LINE_CONTENT_LENGTH (LOG_LINE_LENGTH - MAX_LOG_FORMAT_LENGTH)

static std::map<LogLevel, std::string> s_LogLevelName = {
	{ LogLevel::Ignore, "IGNORE"},
	{ LogLevel::Debug, "DEBUG"},
	{ LogLevel::Info, "INFO"},
	{ LogLevel::Warning, "WARNING"},
	{ LogLevel::Error, "ERROR"},
	{ LogLevel::Critical, "CRITICAL"},
	{ LogLevel::Emergency, "EMERGENCY"},
};

thread_local char* t_LogBuffer = new char[LOG_LINE_LENGTH];


Logger Logger::m_Instance;
LogLevel Logger::s_LogLevel = LogLevel::Info;
LogLevel Logger::s_LogLevelConsole = LogLevel::Warning;

Logger::Logger()
	:ThreadBase("Logger"), m_ProcessName(""), m_CreateLogFileTime(), m_LogData(nullptr)
{
}
Logger::~Logger()
{

}

Logger& Logger::GetInstance()
{
	return m_Instance;
}
bool Logger::Init(const char* fullProcessName)
{
	ParseProcessName(fullProcessName, m_ProcessName, 128);
	m_LogData = new LogData();
	CreateLogDir("log");
	return true;
}
void Logger::SetLogLevel(LogLevel logLevel, LogLevel logLevelConsole)
{
	s_LogLevel = logLevel;
	s_LogLevelConsole = logLevelConsole;
}
void Logger::WriteLog(LogLevel level, const char* file, int line, const char* func, const char* formatStr, ...)
{
	va_list va;
	va_start(va, formatStr);
	WriteToLog(level, file, line, func, formatStr, va);
	va_end(va);
	if (level >= s_LogLevelConsole)
	{
		va_start(va, formatStr);
		WriteToConsole(level, formatStr, va);
		va_end(va);
	}
}
void Logger::ThreadInit()
{
	m_CreateLogFileTime = *GetLocalTm();
	CreateLogFile();
}
void Logger::Run()
{
	SwapInnerLogBuffers();
	FlushBuffers();

	static int count = 0;
	if (++count >= 120)
	{
		count = 0;
		auto currTime = *GetLocalTm();
		if (m_CreateLogFileTime.tm_mday != currTime.tm_mday)
		{
			m_CreateLogFileTime = currTime;
			CreateLogFile();
		}
	}
}
void Logger::ThreadExit()
{
	if (m_LogData)
	{
		delete m_LogData;
	}
	m_LogData = nullptr;
}

bool Logger::CreateLogDir(const std::string& path)
{
	return std::filesystem::create_directories(path);
}
void Logger::SwapInnerLogBuffers()
{
	std::unique_lock<std::mutex> lock(m_LogData->Mutex);
	if (m_LogData->LogBuffers.empty())
	{
		m_LogData->ConditionVariable.wait_for(lock, std::chrono::seconds(1));
		if (m_LogData->CurrBuffer->Length() > 0)
		{
			m_LogData->PushBuffer();
		}
	}
	m_LogData->InnerLogBuffers.swap(m_LogData->LogBuffers);
}
void Logger::FlushBuffers()
{
	for (auto& buffer : m_LogData->InnerLogBuffers)
	{
		fwrite(buffer->GetData(), buffer->Length(), 1, m_LogData->LogFile);
		m_LogData->FreeBuffer(buffer);
	}
	m_LogData->InnerLogBuffers.clear();
	fflush(m_LogData->LogFile);
}

void Logger::WriteToLog(LogLevel level, const char* file, int line, const char* func, const char* format, va_list va)
{
	if (level < s_LogLevel)
		return;
	for (auto p = file; *p != '\0'; p++)
		if (*p == '\\' || *p == '/')
			file = p + 1;
	int len1 = snprintf(t_LogBuffer, MAX_LOG_FORMAT_LENGTH, "%s %d %s ", GetLocalDateTimeWithMilliSecond().c_str(), GetCurrentThreadID(), s_LogLevelName[level].c_str());

	int len2 = vsnprintf(t_LogBuffer + len1, MAX_LOG_LINE_CONTENT_LENGTH, format, va);
	if (len2 > MAX_LOG_LINE_CONTENT_LENGTH)
	{
		len2 = MAX_LOG_LINE_CONTENT_LENGTH;
	}
	int len3 = snprintf(t_LogBuffer + len1 + len2, LOG_LINE_LENGTH - len1 - len2 - 1, "\t\t---%s:%d[%s]\n", file, line, func);
	int len = len1 + len2 + len3;
	std::lock_guard<std::mutex> guard(m_LogData->Mutex);
	if (m_LogData->CurrBuffer->Available() < len)
	{
		m_LogData->PushBuffer();
	}
	m_LogData->CurrBuffer->Append(t_LogBuffer, len);
	m_LogData->ConditionVariable.notify_one();
}
void Logger::WriteToConsole(LogLevel level, const char* formatStr, va_list va)
{
	static char* logString = new char[LOG_LINE_LENGTH] {0};
	int len = snprintf(logString, MAX_LOG_FORMAT_LENGTH, "ThreadID[%06d] ", GetCurrentThreadID());
	len += vsnprintf(logString + len, LOG_LINE_LENGTH - len -1, formatStr, va);

	printf("%s\n", logString);
}
void Logger::CreateLogFile()
{
	if (m_LogData->LogFile)
	{
		fclose(m_LogData->LogFile);
		m_LogData->LogFile = nullptr;
	}
	char timeBuff[32];
	strftime(timeBuff, 32, "%Y%m%d-%H%M%S", &m_CreateLogFileTime);
	char fileName[256];		
	snprintf(fileName, sizeof(fileName), "log/%s.%s.log", m_ProcessName, timeBuff);
	m_LogData->LogFile = fopen(fileName, "a+");
	assert(m_LogData->LogFile != nullptr);
}
uint32_t Logger::GetCurrentThreadID()
{
	auto id = std::this_thread::get_id();
	return *(uint32_t*)(&id);
}
