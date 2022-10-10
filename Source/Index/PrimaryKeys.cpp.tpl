#include "PrimaryKeys.h"

using std::unordered_set;

!!types={}!!
!!entry types!!
!!entry bools!!
!!travel!!
!!types[@name] = 'bool'!!
!!leave!!
!!leave!!
!!entry ints!!
!!travel!!
!!types[@name] = 'int'!!
!!leave!!
!!leave!!
!!entry int64s!!
!!travel!!
!!types[@name] = 'int64'!!
!!leave!!
!!leave!!
!!entry doubles!!
!!travel!!
!!types[@name] = 'double'!!
!!leave!!
!!leave!!
!!entry strings!!
!!travel!!
!!types[@name] = 'string'!!
!!leave!!
!!leave!!
!!entry enums!!
!!travel!!
!!types[@name] = 'enum'!!
!!leave!!
!!leave!!
!!leave!!


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
!!$tableName!!PrimaryKey!!@name!!::!!$tableName!!PrimaryKey!!@name!!(size_t buckets)
	:m_Index(buckets), m_Select!!$tableName!!()
{
}
bool !!$tableName!!PrimaryKey!!@name!!::Insert(!!$tableName!!* const record)
{
	return m_Index.insert(record).second;
}
bool !!$tableName!!PrimaryKey!!@name!!::Erase(!!$tableName!!* const  record)
{
	return  m_Index.erase(record) > 0;
}
bool !!$tableName!!PrimaryKey!!@name!!::CheckInsert(!!$tableName!!* const record)
{
	return m_Index.find(record) == m_Index.end();
}
bool !!$tableName!!PrimaryKey!!@name!!::CheckUpdate(const !!$tableName!!* const oldRecord, const !!$tableName!!* const newRecord)
{
	return !!$tableName!!EqualFor!!@name!!PrimaryKey()(oldRecord, newRecord);
}
const !!$tableName!!* !!$tableName!!PrimaryKey!!@name!!::Select(!!travel!!!!fieldType=fieldTypes[@name]!!!!if $pumpid >= '1':!!!!inc indent!!, !!dec indent!!const C!!$fieldType!!Type& !!@name!!!!leave!!)
{
!!travel!!
!!fieldType=fieldTypes[@name]!!
!!type = types[fieldType]!!
!!if $type == 'string':!!
!!inc indent!!
	strcpy(m_Select!!$tableName!!.!!@name!!, !!@name!!);
!!dec indent!!
!!else:!!
!!inc indent!!
	m_Select!!$tableName!!.!!@name!! = !!@name!!;
!!dec indent!!
!!leave!!

	auto it = m_Index.find(&m_Select!!$tableName!!);
	if (it == m_Index.end())
	{
		return nullptr;
	}
	return *it;
}


!!leave!!
!!leave!!
!!leave!!
!!leave!!
