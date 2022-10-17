#pragma once
#include "DataStruct.h"


!!entry tables!!
!!travel!!
!!tableName = @name!!
!!entry uniquekeys!!
!!travel!!
struct !!$tableName!!EqualFor!!@name!!UniqueKey
{
	bool operator()(const !!$tableName!!* const left, const !!$tableName!!* const right) const;
};
struct !!$tableName!!HashFor!!@name!!UniqueKey
{
	size_t operator()(const !!$tableName!!* const record) const;
};

!!leave!!
!!leave!!
!!leave!!
!!leave!!


