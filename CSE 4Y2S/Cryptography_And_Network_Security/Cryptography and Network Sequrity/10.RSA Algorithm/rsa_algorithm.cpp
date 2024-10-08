#include<bits/stdc++.h>
using namespace std;
#define ll long long

ll e, n;

ll bigmod(ll en,ll r,ll m)
{
    if(r==0)return 1;
    if(r==1)return en%m;
    if(r%2==1)
    {
        ll a = en;
        ll b = bigmod(en,r-1,m);
        return (a*b)%m;
    }
    else if(r%2==0)
    {
        ll a = bigmod(en,r/2,m);
        return (a*a)%m;
    }

}


// ll coprime(ll n)
// {
//     ll x = rand()%(n-1)+2;
//     while(__gcd(x,n)!=1)
//     {
//         x = rand()%(n-1)+2;
//     }
//     return x;
// }


// ll inverse_mod(ll e,ll m )
// {
//     for(int i = 1;i<m;i++)
//     {
//         if((e*i)%m==1)return i;
//     }
//     return -1;

// }


// ll key_generation(ll p, ll q)
// {
//     ll d,phi;

//     n = p*q;
//     phi = (p-1)*(q-1);
//     e = coprime(phi);
//     d = inverse_mod(e, phi);

//     return d;
    
// }



string encryption(string msg, int block_size)
{
    string cipher;
    char str[block_size+1];
    ll en,j,k;
    for(int i = 0; i<msg.size();i += block_size)
    {
        
        for( j = 0; j<block_size && (i+j)<msg.size();j++)
        {
            str[j] = msg[i+j];
        }
        str[j]='\0';
        en = atol(str);
        e = 79;
        n = 3337;
        en = bigmod(en,e,n);

        
        ltoa(en,str,10);

        for(int k = 0;str[k];k++)
        {
            cipher+= str[k];

        }

        cipher+= " ";
    }
    return cipher;
}


string decryption(string cipher,ll d)
{
    string msg ="";
    char str[100];
    ll k,en;
    for(int i = 0;i<cipher.size();i++)
    {
        k = 0;
        while(cipher[i]!= ' ' && i<cipher.size())
        {
            str[k] = cipher[i];
            i++;
            k++;
        }
        str[k] = '\0';
        en = atol(str);
        en = bigmod(en,d,n);
        itoa(en,str,10);

        for(int k=0;str[k]; k++)
        {
            msg+= str[k];
        }

    }
    return msg;
}



int main()
{
    string plaintext,ciphertext;
    // ll d;
    ll d=1019;
    
    ifstream input;
    ofstream output;

    input.open("input.txt");

    getline(input,plaintext);

    // d = key_generation(97,23);

    ciphertext = encryption(plaintext,3);
    plaintext = decryption(ciphertext,d);

    cout<<"Original msg : "<<plaintext<<"\n";
    cout<<"Ciphertext msg : "<<ciphertext;

    input.close();
}