#include <iostream>
#include <stdlib.h>
#include <ctype.h>
using namespace std;

bool id(string c) {
	for (int i=0;i<c.size();i++) {
		if (isdigit(c[i]) == 0) {
			return false;
		}
	}
	return true;
}

int main(){
	string t;
	cout << "Input time in seconds: ";
	getline(cin, t);
	if (! id(t)) {
		cout << "No se ha ingresado un número" << endl;
		return 1;
	}
	int it = stoi(t);
	cout << it / 60 << ":" << it%60 << endl;
	return 0;
}
