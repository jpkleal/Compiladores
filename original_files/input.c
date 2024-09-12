#include <stdio.h>

int main() {
	float a;
	float b;
	float c;
	float d;
	printf("%s", "Programa Teste");
	printf("%s", "Digite A");
	scanf("%f", &a);
	a = 2;
	printf("%s", "Digite B");
	scanf("%f", &b);
	b = 2;
	if(a<b){
		c = a+b;
	}
	else {
		c = a-b;
	}
	printf("%s", "C e igual a ");
	printf("%f", c);
	d = a+b;
	printf("%s", "D e igual a ");
	printf("%f", d);
	do {
		d = 2*d;
	} while(0);
	printf("%f", d);
	while(d>0){
		d = d-1;
		printf("%f", d);
	}
	return 0;
}