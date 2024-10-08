#include<bits/stdc++.h>
#define ll long long
using namespace std;


ll bigmod(ll n,ll r,ll m)
{
    if(r==0)return 1;
    if(r==1)return n%m;
    if(r%2==1)
    {
        ll a = n%m;
        ll b =(bigmod(n,r-1,m));
        return (a*b)%m;
    }
    else if(r%2 == 0)
    {
        ll c =bigmod(n,r/2,m);
        return (c*c)%m;
    }

}



bool isPrime(ll p)
{
    if(p<=1||p%2==0)return false;
    if(p==2||p==3)return true;
    ll x,a;
    for(int i = 0; i<100;i++)
    {
        a = 2+rand()%(p-3);
        x = bigmod(a,(p-1)/2,p);
        if(x!=1 && x!=-1 && x!=(p-1))return false;

    }
    return true;

    
}



int main()
{
    ll p;
    cin>>p;
    if(isPrime(p))
    {
        cout<<"Prime";

    }
    else cout<<"Not a prime number";
}