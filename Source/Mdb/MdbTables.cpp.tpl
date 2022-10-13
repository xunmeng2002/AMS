#include "MdbTables.h"
#include <string>

using std::string;


!!entry tables!!
!!travel!!
!!tableName = @name!!
!!className = @name + 'Table'!!
!!$className!!::!!$className!!()
{
}
!!@name!!* !!$className!!::Alloc()
{
	!!@name!!* record = m_MemCache.Allocate();
	::memset(record, 0, sizeof(!!@name!!));
	return record;
}
void !!$className!!::Free(!!@name!!* record)
{
	m_MemCache.Free(record);
}
bool !!$className!!::Insert(!!@name!!* record)
{
!!entry primarykeys!!
	if (!!travel!!!!if $pumpid > 0:!!!!inc indent!! && !!dec indent!!(!m_!!@name!!PrimaryKey.CheckInsert(record))!!leave!!)
	{
		printf("!!$className!! Insert Failed for !!$tableName!!:[%s]\n", record->GetString());
		return false;
	}
!!travel!!
	m_!!@name!!PrimaryKey.Insert(record);
!!leave!!
!!leave!!

!!entry indexes!!
!!travel!!
	m_!!@name!!Index.Insert(record);
!!leave!!
!!leave!!

	return true;
}
bool !!$className!!::Erase(!!@name!!* record)
{
!!entry primarykeys!!
!!travel!!
	if (!m_!!@name!!PrimaryKey.Erase(record))
	{
		printf("!!$className!! Erase Failed for !!$tableName!!:[%s]\n", record->GetString());
		return false;
	}
!!leave!!
!!leave!!

!!entry indexes!!
!!travel!!
	m_!!@name!!Index.Erase(record);
!!leave!!
!!leave!!

	return true;
}
bool !!$className!!::Update(const !!@name!!* oldRecord, const !!@name!!* newRecord)
{
!!entry primarykeys!!
!!travel!!
	if (!m_!!@name!!PrimaryKey.CheckUpdate(oldRecord, newRecord))
	{
		printf("!!$className!! Update Failed for !!$tableName!!:[%s], [%s]\n", oldRecord->GetString(), newRecord->GetString());
		return false;
	}
!!leave!!
!!leave!!

!!entry indexes!!
!!travel!!
	bool !!@name!!IndexUpdate = m_!!@name!!Index.NeedUpdate(oldRecord, newRecord);
	if (!!@name!!IndexUpdate)
	{
		m_!!@name!!Index.Erase((!!$tableName!!*)oldRecord);
	}
!!leave!!
!!leave!!

	::memcpy((void*)oldRecord, newRecord, sizeof(!!@name!!));
	
!!entry indexes!!
!!travel!!
	if (!!@name!!IndexUpdate)
	{
		m_!!@name!!Index.Insert((!!$tableName!!*)oldRecord);
	}
!!leave!!
!!leave!!
	
	m_MemCache.Free((!!$tableName!!*)newRecord);
	return true;
}
void !!$className!!::Dump(const char* dir)
{
	string fileName = string(dir) + "//t_!!@name!!.csv";
	FILE* dumpFile = fopen(fileName.c_str(), "w");
	if (dumpFile == nullptr)
	{
		return;
	}

	fprintf(dumpFile, "!!entry fields!!!!travel!!!!if $pumpid > 0:!!!!inc indent!!, !!dec indent!!!!@name!!!!leave!!!!leave!!\n");
	char buff[4096] = { 0 };
	for (auto it = m_DefaultPrimaryKey.m_Index.begin(); it != m_DefaultPrimaryKey.m_Index.end(); ++it)
	{
		fprintf(dumpFile, "%s\n", (*it)->GetString());
	}
	fclose(dumpFile);
}

!!leave!!
!!leave!!

