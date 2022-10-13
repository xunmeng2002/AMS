#include "IndexComp.h"
#include <string>

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
!!entry indexes!!
!!travel!!
bool !!$tableName!!EqualFor!!@name!!Index::operator()(const !!$tableName!!* const left, const !!$tableName!!* const right) const
{
	return !!travel!!!!if $pumpid > 0:!!!!inc indent!!&& !!dec indent!!!!type = fieldTypes[@name]!!!!if type == 'string':!!!!inc indent!!strcmp(left->!!@name!!, right->!!@name!!) == 0!!dec indent!!!!else:!!!!inc indent!!left->!!@name!! == right->!!@name!! !!dec indent!!!!leave!!;
}
bool !!$tableName!!LessFor!!@name!!Index::operator()(const !!$tableName!!* const left, const !!$tableName!!* const right) const
{
!!travel!!
!!type = fieldTypes[@name]!!
!!if type == 'string':!!
!!inc indent!!
	if (strcmp(left->!!@name!!, right->!!@name!!) < 0)
		return true;
	else if (strcmp(left->!!@name!!, right->!!@name!!) > 0)
		return false;
!!dec indent!!
!!else:!!
!!inc indent!!
	if (left->!!@name!! < right->!!@name!!)
		return true;
	else if (left->!!@name!! > right->!!@name!!)
		return false;
!!dec indent!!
!!leave!!
	return false;
}

!!leave!!
!!leave!!
!!leave!!
!!leave!!
