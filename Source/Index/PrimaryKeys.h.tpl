#pragma once
#include <unordered_set>
#include "DataStruct.h"
#include "PrimaryKeyComp.h"


!!entry tables!!
!!travel!!
!!tableName = @name!!
!!fieldTypes = {}!!
!!entry fields!!
!!travel!!
!!fieldTypes[@name] = @type!!
!!leave!!
!!leave!!
!!entry primarykeys!!
!!travel!!
class !!$tableName!!PrimaryKeyFor!!@name!!
{
	friend class !!$tableName!!Table;
public:
	!!$tableName!!PrimaryKeyFor!!@name!!(size_t buckets = 1000);
	bool Insert(!!$tableName!!* const record);
	bool Erase(!!$tableName!!* const record);
	bool CheckUpdate(const !!$tableName!!* const oldRecord, const !!$tableName!!* const newRecord);
	const !!$tableName!!* Select(!!travel!!!!fieldType=fieldTypes[@name]!!!!if $pumpid >= '1':!!!!inc indent!!, !!dec indent!!const C!!$fieldType!!Type& !!@name!!!!leave!!);

private:
	!!$tableName!! m_Select!!$tableName!!;
	std::unordered_set<!!$tableName!!*, !!$tableName!!HashFor!!@name!!, !!$tableName!!EqualFor!!@name!!> m_Index;
};

!!leave!!
!!leave!!
!!leave!!
!!leave!!