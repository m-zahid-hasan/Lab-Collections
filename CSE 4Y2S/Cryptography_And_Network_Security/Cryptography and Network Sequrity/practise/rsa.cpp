#include<bits/stdc++.h>
using namespace std;
#define ll long long

ll bigmood(ll en, ll r, ll m)
{
    if(r==0)return 1;
    if(r==1)return en%m;
    if(r%2==1)
    {
        ll a =en%m;
        ll b =bigmood(en ,r-1,m);
        return (a*b)%m;
    }
    else if(r%2==0)
    {
        ll a = bigmood(en,r/2,m);
        return (a*a)%m;
    }
}


string encryption(string msg, int block_size,ll e,ll n)
{
    string cipher ="";
    char str[10];
    for(int i = 0;i<msg.size();i+=block_size)
    {
        int j = 0;
        for( j = 0;j<block_size&&(i+j)<msg.size();j++)
        {
            str[j] = msg[j+i];
        }
        str[j]= '\0';
       ll en = atol(str);
       en = bigmood(en,e,n);
       ltoa(en,str,10);

       for(j = 0; str[j];j++)
       {
        cipher+=str[j];
       }
       cipher+=" ";
    }
    return cipher;
}

string decryption(string cipher ,ll d,ll n)
{
    string msg ="";
    char str[10];
    for(int i = 0;i<cipher.size();i++)
    {
        int j = 0;
        while(cipher[i]!=' ' && i<cipher.size())
        {
            str[j]=cipher[i];
            i++;
            j++;
        }
        str[j] = '\0';
        ll en = atol(str);
        en = bigmood(en,d,n);
        ltoa(en,str,10);
        for(j = 0; str[j];j++)
        {
            msg+= str[j];
        }
    }
    return msg;
}


int main()
{
    string p,c,d;
    ifstream input;
    ofstream output;

    input.open("input.txt");
    output.open("output.txt");

    getline(input,p);
    c = encryption(p,3,79,3337);
    d = decryption(c,1019,3337);

    output<<p<<"\n";
    output<<c<<"\n";
    output<<d<<"\n";
    input.close();
    output.close();
}
