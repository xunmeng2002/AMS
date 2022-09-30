#pragma once

#include "DataStruct.h"


!!entry tables!!
!!travel!!
!!tableName = @name!!
!!entry indexes!!
!!travel!!
struct !!$tableName!!EqualFor!!@name!!
{
	bool operator()(const !!$tableName!!* const left, const !!$tableName!!* const right) const;
};
struct !!$tableName!!LessFor!!@name!!
{
	bool operator()(const !!$tableName!!* const left, const !!$tableName!!* const right) const;
};

!!leave!!
!!leave!!
!!leave!!
!!leave!!
