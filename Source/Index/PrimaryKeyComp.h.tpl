#pragma once
#include "DataStruct.h"


!!entry tables!!
!!travel!!
!!tableName = @name!!
!!entry primarykeys!!
!!travel!!
struct !!$tableName!!EqualFor!!@name!!
{
	bool operator()(const !!$tableName!!* const left, const !!$tableName!!* const right) const;
};
struct !!$tableName!!HashFor!!@name!!
{
	size_t operator()(const !!$tableName!!* const record) const;
};

!!leave!!
!!leave!!
!!leave!!
!!leave!!

