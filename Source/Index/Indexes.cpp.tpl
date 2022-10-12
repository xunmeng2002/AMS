#include "Indexes.h"


!!entry tables!!
!!travel!!
!!tableName = @name!!
!!entry indexes!!
!!travel!!
!!className = tableName + 'Index' + @name!!
void !!$className!!::Insert(!!$tableName!!* const record)
{
	m_Index.insert(record);
}
void !!$className!!::Erase(!!$tableName!!* const record)
{
	m_Index.erase(record);
}
bool !!$className!!::NeedUpdate(const !!$tableName!!* const oldRecord, const !!$tableName!!* const newRecord)
{
	return !(!!$tableName!!EqualFor!!@name!!Index()(oldRecord, newRecord));
}
!!$className!!::iterator !!$className!!::LowerBound(!!$tableName!!* const record)
{
	return m_Index.lower_bound(record);
}
!!$className!!::iterator !!$className!!::UpperBound(!!$tableName!!* const record)
{
	return m_Index.upper_bound(record);
}
std::pair<!!$className!!::iterator, !!$className!!::iterator> !!$className!!::EqualRange(!!$tableName!!* const record)
{
	return m_Index.equal_range(record);
}

!!leave!!
!!leave!!

!!leave!!
!!leave!!
