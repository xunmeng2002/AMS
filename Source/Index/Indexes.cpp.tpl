#include "Indexes.h"


!!entry tables!!
!!travel!!
!!tableName = @name!!
!!entry indexes!!
!!travel!!
void !!$tableName!!IndexFor!!@name!!::Insert(!!$tableName!!* const record)
{
	m_Index.insert(record);
}
void !!$tableName!!IndexFor!!@name!!::Erase(!!$tableName!!* const record)
{
	m_Index.erase(record);
}
bool !!$tableName!!IndexFor!!@name!!::NeedUpdate(const !!$tableName!!* const oldRecord, const !!$tableName!!* const newRecord)
{
	return !(!!$tableName!!EqualFor!!@name!!()(oldRecord, newRecord));
}

!!leave!!
!!leave!!

!!leave!!
!!leave!!

