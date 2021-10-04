#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    int arr1[20];
    int arr2[20];
    fstream fin;
    fin.open("Source1.txt");
    int i = 0;
    cout<<"\nData received from Source1.txt"<<endl;
    while (fin.eof()==0)
    {
        fin >> arr1[i];
        cout<<arr1[i]<<" ";
        i++;
    }
    fin.close();
    cout<<"\n\nData received from Source2.txt"<<endl;
    fin.open("Source2.txt");
    int j = 0;
    while (fin.eof()==0)
    {
        fin >> arr2[j];
        cout<<arr2[j]<<" ";
        j++;
    }
    fin.close();
    cout << "\n\nThe Merged Array that will be stored in Target.txt: " << endl;
    fstream fout;
    fout.open("Target.txt");
    int a = 0, b = 0;
    while(a<i || b<j)
    {
        if(a<i && b<j)
        {
        	 if(arr1[a]<arr2[b])
            {
                fout<<arr1[a]<<" ";
                cout<<arr1[a]<<" ";
                a++;
            }
            else
            {
                fout<<arr2[b]<<" ";
                cout<<arr2[b]<<" ";
                b++;
            }
        }
        else if(a<i && b>=j)
        {
            fout<<arr1[a]<<" ";
            cout<<arr1[a]<<" ";
            a++;
        }
        else if(a>=i && b<j)
        {
            fout<<arr2[b]<<" ";
            cout<<arr2[b]<<" ";
            b++;
        }
    }
    fout.close();
}
