#include "UniqueKeyComp.h"
#include <string>
#include <string.h>
#include <functional>

using std::string;

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
!!fieldTypes[@name] = types[@type]!!
!!leave!!
!!leave!!
!!entry uniquekeys!!
!!travel!!
bool !!$tableName!!EqualFor!!@name!!UniqueKey::operator()(const !!$tableName!!* const left, const !!$tableName!!* const right) const
{
	return !!travel!!!!if pumpid > 0:!!!!inc indent!! && !!dec indent!!!!type = fieldTypes[@name]!!!!if type == 'string':!!!!inc indent!!strcmp(left->!!@name!!, right->!!@name!!) == 0!!dec indent!!!!else:!!!!inc indent!!left->!!@name!! == right->!!@name!!!!dec indent!!!!leave!!;
}
size_t !!$tableName!!HashFor!!@name!!UniqueKey::operator()(const !!$tableName!!* const record) const
{
	return !!travel!!!!type = fieldTypes[@name]!!!!if pumpid > 0:!!!!inc indent!! + !!dec indent!!!!if type == 'int64':!!!!inc indent!!std::hash<long long>()(record->!!@name!!)!!dec indent!!!!elif type == 'enum':!!!!inc indent!!std::hash<char>()((char)record->!!@name!!)!!dec indent!!!!else:!!!!inc indent!!std::hash<!!$type!!>()(record->!!@name!!)!!dec indent!!!!leave!!;
}

!!leave!!
!!leave!!
!!leave!!
!!leave!!
