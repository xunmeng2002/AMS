#pragma once
#include "DataStruct.h"
#include <stddef.h>


!!entry tables!!
!!travel!!
!!tableName = @name!!
!!entry primarykey!!
struct !!$tableName!!EqualFor!!@name!!PrimaryKey
{
	bool operator()(const !!$tableName!!* const left, const !!$tableName!!* const right) const;
};
struct !!$tableName!!HashFor!!@name!!PrimaryKey
{
	size_t operator()(const !!$tableName!!* const record) const;
};

!!leave!!
!!leave!!
!!leave!!


