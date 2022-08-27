#include<iostream>
using namespace std;
int main(){
    int n,x,m,t,d;
    cin >> n >> m >> x >> t >> d;
    if(m>=x) cout << t;
    else cout << t-x*d+m;
    return 0;
}