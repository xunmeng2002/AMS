#pragma once
#include "DataStruct.h"
#include "PrimaryKeys.h"
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
!!entry primarykeys!!
!!travel!!
	!!$tableName!!PrimaryKeyFor!!@name!! m_!!@name!!PrimaryKey;
!!leave!!
!!leave!!

!!entry indexes!!
!!travel!!
	!!$tableName!!IndexFor!!@name!! m_!!@name!!Index;
!!leave!!
!!leave!!

private:
	MemCacheTemplate<Account> m_MemCache;
};

!!leave!!
!!leave!!
