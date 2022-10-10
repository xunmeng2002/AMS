#pragma once

!!entry types!!
!!entry bools!!
!!travel!!
typedef bool C!!@name!!Type;
!!leave!!
!!leave!!

!!entry ints!!
!!travel!!
typedef int C!!@name!!Type;
!!leave!!
!!leave!!

!!entry int64s!!
!!travel!!
typedef long long C!!@name!!Type;
!!leave!!
!!leave!!

!!entry doubles!!
!!travel!!
typedef double C!!@name!!Type;
!!leave!!
!!leave!!

!!entry strings!!
!!travel!!
typedef char C!!@name!!Type[!!@len!!];
!!leave!!
!!leave!!

!!entry enums!!
!!travel!!
enum class C!!@name!!Type : char
{
!!travel!!
	!!@name!! = '!!@value!!',
!!leave!!
};
!!leave!!
!!leave!!

!!leave!!
