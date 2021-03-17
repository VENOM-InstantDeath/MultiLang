#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

int id(char *c) {
	for (int i=0;i<strlen(c);i++) {
		if (isdigit(c[i]) == 0) {
			return 0;
		}
	}
	return 1;
}

int main() {
	char t[10];
	printf("Input time in seconds: ");
	fgets(t, 10, stdin);
	fflush(stdin);
	t[strcspn(t, "\n")] = 0;
	if (! id(t)) {
		printf("No se ha ingresado un número\n");
		return 1;
	}
	int it = atoi(t);
	printf("%d:%d\n", it/60, it%60);
	return 0;
}
