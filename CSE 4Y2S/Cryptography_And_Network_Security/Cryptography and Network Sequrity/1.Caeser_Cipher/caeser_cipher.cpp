#include<bits/stdc++.h>
using namespace std;

// g++ -o caeser_cipher caeser_cipher.cpp
// ./caeser_cipher

int encrypt(int ch)
{
    return (ch+3)%26;
}

int decrypt(int ch)
{
    return (ch-3+26)%26;
}

string ecnryption(string msg)
{
    string cipher = "";
    for(int i = 0; i<msg.size(); i++)
    {
        if(isupper(msg[i]))
        {
            cipher+= (char)(encrypt(msg[i]-'A')+'A');
        }
        else if(islower(msg[i]))
        {
            cipher+= (char)(encrypt(msg[i]-'a')+'a');
        }
        else cipher+= msg[i];
    }
    return cipher;
}

string decryption(string cipher)
{
    string msg="";
    for(int i = 0; i<cipher.size(); i++)
    {
        if(isupper(cipher[i]))
        {
            msg+= (char)(decrypt(cipher[i]-'A')+'A');
        }
        else if(islower(cipher[i]))
        {
            msg+= (char)(decrypt(cipher[i]-'a')+'a');
        }
        else msg+= cipher[i];
    }
    return msg;
}

int main()
{
    string plaintext,ciphertext;
    ifstream input;
    ofstream output;
    
    input.open("input.txt");
    getline(input,plaintext);
    // cout<<plaintext;

    ciphertext = ecnryption(plaintext);
    plaintext = decryption(ciphertext);

    cout<<"Original msg : "<<plaintext<<"\n";
    cout<<"Ciphertext msg : "<<ciphertext<<"\n";

    input.close();
    output.close();
}