#include "Dir.h"
#ifdef WINDOWS
#include <direct.h>
#include <io.h>
#include <sys/stat.h>
#include <sys/types.h>
#endif
#ifdef LINUX
#include <sys/stat.h>
#include <unistd.h>
#endif // LINUX




bool Dir::IsDir(const char* path)
{
	return access(path, 00) == 0;
}
bool Dir::Create(const char* path, int mode)
{
#ifdef WINDOWS
	return mkdir(path) == 0;
#endif
#ifdef LINUX
	return mkdir(path, mode) == 0;
#endif
	return false;
}
