#include<bits/stdc++.h>
#define ll long long
using namespace std;

ll bigmod(ll n,ll r, ll m)
{
    if(r==0)return 1;
    if(r==1)return n%m;
    if(r%2==1)
    {
        ll a = n%m;
        ll b =bigmod(n,r-1,m);
        return (a*b)%m;
    }
    else if(r%2==0)
    {
        ll c= bigmod(n,r/2,m);
        return (c*c)%m;
    }

}


bool isPrime(ll p)
{
    if(p==2||p==3)return true;
    if(p<=1||p%2==0)return false;
    
    ll a, temp, x, m = p-1;
    while(m%2==0)
    {
        m/=2;
    }

    for (int i = 0;i<100; i++)
    {
        // a = 2+rand()%(p-3);
        a = 2 + rand() % (p - 3); 
        temp = m;
        x = bigmod(a,m,p);
        if(x ==1||x==p-1)continue;
        while(temp!=p-1)
        {
            x =(x*x)%p;
            temp*=2;
            if(x==1)return false;
            if(x==p-1)break;
        }
        if(x!=p-1)return false;
        
    }
    return true;
    
}



int main()
{
    ll p;
    cin>>p;

    if(isPrime(p))cout<<"Prime number";
    else cout<<"Not a prime number";
    
}
