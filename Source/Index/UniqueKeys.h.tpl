#pragma once
#include <unordered_set>
#include "DataStruct.h"
#include "UniqueKeyComp.h"


!!entry tables!!
!!travel!!
!!tableName = @name!!
!!fieldTypes = {}!!
!!entry fields!!
!!travel!!
!!fieldTypes[@name] = @type!!
!!leave!!
!!leave!!
!!entry uniquekeys!!
!!travel!!
class !!$tableName!!UniqueKey!!@name!!
{
	friend class !!$tableName!!Table;
public:
	!!$tableName!!UniqueKey!!@name!!(size_t buckets = 1000);
	bool Insert(!!$tableName!!* const record);
	bool Erase(!!$tableName!!* const record);
	bool CheckInsert(!!$tableName!!* const record);
	bool CheckUpdate(const !!$tableName!!* const oldRecord, const !!$tableName!!* const newRecord);
	const !!$tableName!!* Select(!!travel!!!!fieldType=fieldTypes[@name]!!!!if pumpid > 0:!!!!inc indent!!, !!dec indent!!const C!!$fieldType!!Type& !!@name!!!!leave!!);

private:
	!!$tableName!! m_Select!!$tableName!!;
	std::unordered_set<!!$tableName!!*, !!$tableName!!HashFor!!@name!!UniqueKey, !!$tableName!!EqualFor!!@name!!UniqueKey> m_Index;
};

!!leave!!
!!leave!!
!!leave!!
!!leave!!
