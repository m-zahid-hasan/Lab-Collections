#include<bits/stdc++.h>
#define ll long long
using namespace std;

ll bigmod(ll n, ll r,ll m)
{
    if(r==0)return 1;
    if(r==1)return n%m;
    if(r%2==1)
    {
        ll a = n%m;
        ll b = bigmod(n,r-1,m);
        return (a*b)%m;
    }
    else if(r%2==0)
    {
        ll c = bigmod(n,r/2,m);
        return (c*c)%m;
    }

}


int main()
{
   ll p = 97, r = 27;


   ll xa = 2 +rand()%(97-4);
   ll xb = 2+rand()%(97-4);

   ll ya = bigmod(r,xa,p);
   ll yb = bigmod(r,xb,p);

   ll ka = bigmod(yb,xa,p);
   ll kb = bigmod(ya,xb,p);

   cout<<"Alice key :"<<ka<<"\n";
   cout<<"Bob key :"<<kb<<"\n";

}