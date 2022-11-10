#pragma once
#include <string>
#include <vector>


constexpr int BuffSize = 64 * 1024;

struct Event
{
	int EventID;

	static Event* Allocate();
	virtual void Free();
};

struct TcpEvent : public Event
{
	TcpEvent(int buffSize = BuffSize);
	~TcpEvent();
	int SessionID;
	std::string IP;
	std::string Port;
	char* ReadPos;
	char* Buff;
	int Length;


	static TcpEvent* Allocate();
	virtual void Free() override;
	virtual void Shift(int len);
};

struct MyEvent : public Event
{
	void* Field;
	std::vector<int> NumParams;
	std::vector<std::string> StringParams;

	static MyEvent* Allocate();
	virtual void Free() override;
};

!!entry events!!
!!travel!!
!!startID = @startID!!
!!travel!!
!!id = int(startID) + pumpid!!
constexpr int Event!!@name!! = !!$id!!;		//!!@desc!!
!!leave!!


!!leave!!
!!leave!!
