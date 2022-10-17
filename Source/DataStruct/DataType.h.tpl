#pragma once

!!entry types!!
!!entry bools!!
!!travel!!
!!if @desc != '':!!
!!inc indent!!
//!!@desc!!
!!dec indent!!
typedef bool C!!@name!!Type;
!!leave!!
!!leave!!

!!entry ints!!
!!travel!!
!!if @desc != '':!!
!!inc indent!!
//!!@desc!!
!!dec indent!!
typedef int C!!@name!!Type;
!!leave!!
!!leave!!

!!entry int64s!!
!!travel!!
!!if @desc != '':!!
!!inc indent!!
//!!@desc!!
!!dec indent!!
typedef long long C!!@name!!Type;
!!leave!!
!!leave!!

!!entry doubles!!
!!travel!!
!!if @desc != '':!!
!!inc indent!!
//!!@desc!!
!!dec indent!!
typedef double C!!@name!!Type;
!!leave!!
!!leave!!

!!entry strings!!
!!travel!!
!!if @desc != '':!!
!!inc indent!!
//!!@desc!!
!!dec indent!!
typedef char C!!@name!!Type[!!@len!!];
!!leave!!
!!leave!!

!!entry enums!!
!!travel!!
!!if @desc != '':!!
!!inc indent!!
//!!@desc!!
!!dec indent!!
enum class C!!@name!!Type : char
{
!!travel!!
!!if @desc != '':!!
!!inc indent!!
	//!!@desc!!
!!dec indent!!
	!!@name!! = '!!@value!!',
!!leave!!
};
!!leave!!
!!leave!!

!!leave!!
