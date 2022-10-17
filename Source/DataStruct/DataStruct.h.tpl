#pragma once
#include "DataType.h"

!!entry tables!!
!!travel!!
struct !!@name!!
{
public:
!!entry fields!!
!!travel!!
!!if @desc != '':!!
!!inc indent!!
	//!!@desc!!
!!dec indent!!
	C!!@type!!Type !!@name!!;
!!leave!!
!!leave!!
	
	const char* GetString() const;
	const char* GetDebugString() const;
};
!!leave!!
!!leave!!

