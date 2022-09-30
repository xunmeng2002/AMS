#include "DataStruct.h"
#include <string>

thread_local char t_DataStringBuffer[1024];


const char* Account::GetString() const
{
	sprintf(t_DataStringBuffer, "%s, %d, %s, %s, %c, %c, %s, %c, %s, %d\n",
		OrgID, BrokerID, AccountID, AccountName, AccountClass, AccountType, PrimaryAccountID, AccountStatus, CurrencyID, DeleteFlag);
	return t_DataStringBuffer;
}


