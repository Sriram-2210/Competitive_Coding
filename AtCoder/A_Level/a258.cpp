#include<iostream>
using namespace std;
int main(){
    int k;
    cin >> k;
    if(k<10) cout << 21 <<":" <<0 << k;
    else if(k>=10 && k<60) cout << 21 <<":" <<k;
    else if(k==60) cout <<"22:00";
    else if(k>60 && k<70) cout << 22 << ":" <<0 <<k-60;
    else if(k>=70 && k<=100) cout <<22 <<":" <<k-60;
    return 0;
}
