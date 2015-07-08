/**
  * Given a string consisting of ascii characters, determine if the string comprises only of unique characters or not.	
  *
 **/ 

#include<iostream>

using namespace std;

bool areStringsUniques(const string& str1)
{

 	unsigned long long int bitmap = 0;

 	if (str1.length() > 128)
 	{
 		return false;
 	}
 	for (char symbol : str1)
 	{
 		int code = (int) symbol;
 		if ((bitmap & (1 << code)) > 0)
 		{
 			return false;
 		}

 		bitmap = bitmap | (1 << code);
 	}

 	return true;
}

int main(int argc, char** argv)
{
	string str1 = "??what";
	bool unique = areStringsUniques(str1);
	cout << "'" << str1 << "' is " << (unique ? "":"not ") << "unique" << endl;

	str1 = "what?";
	unique = areStringsUniques(str1);
	cout << "'" << str1 << "' is " << (unique ? "":"not ") << "unique" << endl;

	return 0;
}
