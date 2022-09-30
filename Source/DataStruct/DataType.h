#pragma once

typedef bool CBoolType;

typedef int CBrokerIDType;


typedef double CPriceType;

typedef char CAccountIDType[32];
typedef char CDateType[9];
typedef char COrgIDType[16];
typedef char CAccountNameType[128];
typedef char CCurrencyIDType[8];

enum class CAccountTypeType : char
{
	AT_Primary = '0',
	AT_Sub = '1',
};
enum class CAccountClassType : char
{
	AC_Future = '0',
	AC_Security = '1',
};
enum class CAccountStatusType : char
{
	AS_Normal = '0',
	AS_Forbbiden = '1',
};

