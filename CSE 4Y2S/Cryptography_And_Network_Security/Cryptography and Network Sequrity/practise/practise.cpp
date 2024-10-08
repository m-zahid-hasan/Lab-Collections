#include<bits/stdc++.h>
using namespace std;

string encryption(string msg, int width)
{
    string cipher ="";
    for(int i = 0;i<width; i++)
    {
        for(int j = i ;j<msg.size();j+=width)
        {
            cipher+= msg[j];
        }
    }
    return cipher;
}

string decryption(string cipher, int width)
{
    int rows = cipher.size()/width;
    int extra = cipher.size()%width;
    string msg = "";
    
    for(int i =0; i<rows;i++)
    {
        int temp = extra,h=rows;
        for(int j = i;j<cipher.size();j+=h)
        {
            h = (temp-->0)? rows+1:rows;
            msg+= cipher[j];
        }
    }

    for(int i = 0,j=rows+1;i<extra;i++,j+=rows+1)
    {
        msg+= cipher[j-1];
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
    c = encryption(encryption(p,10),10);
    d = decryption(decryption(c,10),10);

    output<<p<<"\n";
    output<<c<<"\n";
    output<<d<<"\n";

    input.close();
    output.close();

}