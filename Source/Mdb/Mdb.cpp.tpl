#include "Mdb.h"


!!entry tables!!

Mdb::Mdb()
{
!!travel!!
	t_!!@name!! = new !!@name!!Table();
!!leave!!
}
void Mdb::Dump(const char* dir)
{
!!travel!!
	t_!!@name!!->Dump(dir);
!!leave!!
}
void Mdb::Clear()
{

}

!!leave!!
