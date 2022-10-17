#pragma once
#include "DataStruct.h"
#include "PrimaryKeys.h"
#include "UniqueKeys.h"
#include "Indexes.h"
#include "MemCacheTemplate.h"


!!entry tables!!
!!travel!!
!!tableName = @name!!
class !!@name!!Table
{
public:
	!!@name!!Table();
	!!@name!!* Alloc();
	void Free(!!@name!!* record);
	bool Insert(!!@name!!* record);
	bool Erase(!!@name!!* record);
	bool Update(const !!@name!!* oldRecord, const !!@name!!* newRecord);
	void Dump(const char* dir);

public:
	!!$tableName!!PrimaryKey m_PrimaryKey;

!!entry uniquekeys!!
!!travel!!
	!!$tableName!!UniqueKey!!@name!! m_!!@name!!UniqueKey;
!!leave!!
!!leave!!

!!entry indexes!!
!!travel!!
	!!$tableName!!Index!!@name!! m_!!@name!!Index;
!!leave!!
!!leave!!

private:
	MemCacheTemplate<!!$tableName!!> m_MemCache;
};

!!leave!!
!!leave!!

