#pragma once
#include "DataStruct.h"
#include "IndexComp.h"
#include <set>

using std::multiset;

!!entry tables!!
!!travel!!
!!tableName = @name!!
!!entry indexes!!
!!travel!!
class !!$tableName!!Index!!@name!!
{
public:
	void Insert(!!$tableName!!* const record);
	void Erase(!!$tableName!!* const record);
	bool NeedUpdate(const !!$tableName!!* const oldRecord, const !!$tableName!!* const newRecord);

private:
	multiset<!!$tableName!!*, !!$tableName!!LessFor!!@name!!Index> m_Index;
};
!!leave!!
!!leave!!

!!leave!!
!!leave!!

