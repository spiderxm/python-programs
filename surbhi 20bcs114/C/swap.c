#include<stdio.h>
void main()
{
	int a,b,temp;
	a=5;
	b=7;
	temp=b;
	b=a;
	a=temp;
	printf("a=%d",a);
	printf("b=%d",b);
}
