#include "DataStruct.h"
#include <string>

thread_local char t_DataStringBuffer[1024];

!!formats={}!!
!!entry types!!
!!entry bools!!
!!travel!!
!!formats[@name] = '%d'!!
!!leave!!
!!leave!!
!!entry ints!!
!!travel!!
!!formats[@name] = '%d'!!
!!leave!!
!!leave!!
!!entry int64s!!
!!travel!!
!!formats[@name] = '%lld'!!
!!leave!!
!!leave!!
!!entry doubles!!
!!travel!!
!!formats[@name] = '%f'!!
!!leave!!
!!leave!!
!!entry strings!!
!!travel!!
!!formats[@name] = '%s'!!
!!leave!!
!!leave!!
!!entry enums!!
!!travel!!
!!formats[@name] = '%c'!!
!!leave!!
!!leave!!
!!leave!!

!!entry tables!!
!!travel!!
const char* Account::GetString() const
{
!!entry fields!!
	sprintf(t_DataStringBuffer, "!!travel!!!!if $pumpid >= '1':!!!!inc indent!!, !!dec indent!!!!format = formats[@type]!!!!$format!!!!leave!!\n",
		!!travel!!!!if $pumpid >= '1':!!!!inc indent!!, !!dec indent!!!!@name!!!!leave!!);
	return t_DataStringBuffer;
!!leave!!
}

!!leave!!
!!leave!!

