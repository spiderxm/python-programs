#include<iostream>
#include<fstream>
using namespace std;
int main(){
 ofstream fout1,fout2;
 fout1.open("EVEN.txt");
 fout2.open("ODD.txt");
 
 int arr[10]={1,2,3,4,5,6,7,8,9,10},i;
for(i=0;i<10;i++){
 if(arr[i]%2==0){
 fout1<<arr[i]<<endl;
 }
 else{
 fout2<<arr[i]<<endl;
 }
 }
 return 0;
}
