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
	using iterator = std::multiset<!!$tableName!!*, !!$tableName!!LessFor!!@name!!Index>::iterator;
public:
	void Insert(!!$tableName!!* const record);
	void Erase(!!$tableName!!* const record);
	bool NeedUpdate(const !!$tableName!!* const oldRecord, const !!$tableName!!* const newRecord);
	iterator LowerBound(!!$tableName!!* const record);
	iterator UpperBound(!!$tableName!!* const record);
	std::pair<iterator, iterator> EqualRange(!!$tableName!!* const record);

private:
	multiset<!!$tableName!!*, !!$tableName!!LessFor!!@name!!Index> m_Index;
};
!!leave!!
!!leave!!

!!leave!!
!!leave!!

