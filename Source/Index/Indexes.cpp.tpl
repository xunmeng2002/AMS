#include "Indexes.h"


!!entry tables!!
!!travel!!
!!tableName = @name!!
!!entry indexes!!
!!travel!!
void !!$tableName!!Index!!@name!!::Insert(!!$tableName!!* const record)
{
	m_Index.insert(record);
}
void !!$tableName!!Index!!@name!!::Erase(!!$tableName!!* const record)
{
	m_Index.erase(record);
}
bool !!$tableName!!Index!!@name!!::NeedUpdate(const !!$tableName!!* const oldRecord, const !!$tableName!!* const newRecord)
{
	return !(!!$tableName!!EqualFor!!@name!!Index()(oldRecord, newRecord));
}

!!leave!!
!!leave!!

!!leave!!
!!leave!!

