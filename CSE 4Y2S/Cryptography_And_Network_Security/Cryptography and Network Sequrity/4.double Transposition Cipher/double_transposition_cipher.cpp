#include<bits/stdc++.h>
using namespace std;

string encryption(string msg, int width)
{
    string cipher = "";
    int trailing_space = width - msg.size()%width;

    for(int i = 0; i<trailing_space; i++)
    {
        msg+= ' ';
    }

    for(int i = 0; i<width; i++)
    {
        for (int j = i; j<msg.size(); j+= width)
        {
            cipher+= msg[j];
        }
    }
    return cipher;
}

string decryption(string cipher,int widht)
{
    string msg = "";
    int rows = ceil(cipher.size()/(double)(widht));

    for(int i = 0; i<rows; i++)
    {
        for(int j = i;j<cipher.size();j+=rows)
        {
            msg+= cipher[j];
        }
    }

    int cnt = 0;
    for(int i = msg.size()-1; i>=0; i--)
    {
        if(msg[i]==' ')cnt++;
        else break;
    }
    msg = msg.substr(0,msg.size()-cnt);
    return msg;
}


int main()
{
    string plaintext, ciphertext;

    ifstream input;
    ofstream output;

    input.open("input.txt");
    output.open("output.txt");
    
    getline(input,plaintext);

    ciphertext = encryption(encryption(plaintext,3),3);
    plaintext  = decryption(decryption(ciphertext,3),3);

    cout<<"Original msg : "<<plaintext<<"\n";
    cout<<"Ciphertext msg : "<<ciphertext<<"\n";

    input.close();
    output.close();

}