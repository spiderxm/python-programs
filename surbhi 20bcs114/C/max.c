#include<stdio.h>
void main()
{
	int a[4],n,i,max,sum=0;
	printf("how many times want to enter\n");
	scanf("%d",&n);
	printf("enter 1D array\n");
	for(i=0; i<n; i++)
	{
		scanf("%d",&a[i]);
	}
	printf("display 1D array\n");
	for(i=0; i<n; i++)
	{
		printf("%d",a[i]);
	}
	printf("\n");
	for (i=0; i<n; i++)
	{
		sum=sum+a[i];
	}
	printf("sum of 1D array =%d",sum);
	max=a[0];
	for (i=1; i<n; i++)
	{
		if (max<a[i])
		max= a [i];
	}
	printf("max=%d",max);
	
}
