#include<bits/stdc++.h>
using namespace std;

int encrypt(int ch)
{
    return ch%26;
}


int decrypt(int ch)
{
    return (ch+26)%26;
}


string encryption(string msg)
{
    string cipher = "", pad;

    ifstream input;
    input.open("pad.txt");
    getline(input,pad);

    for(int i = 0; i<msg.size(); i++)
    {
        if(isupper(msg[i]))
        {
            cipher += (char)(encrypt( (msg[i]-'A')+(pad[i]-'A') )+'A');
        }
        else if(islower(msg[i]))
        {
            cipher += (char)(encrypt((msg[i]-'a')+(pad[i]-'A'))+'a');
        }
        else cipher += msg[i];
    }
    return cipher;
}

string decryption(string cipher)
{
    string msg = "",pad;

    ifstream input;
    input.open("pad.txt");
    getline(input,pad);

    for(int i = 0; i<cipher.size(); i++)
    {
        if(isupper(cipher[i]))
        {
            msg += (char)(decrypt((cipher[i]-'A')-(pad[i]-'A'))+'A');
        }
        else if(islower(cipher[i]))
        {
            msg += (char)(decrypt((cipher[i]-'a')-(pad[i]-'A'))+'a');
        }
        else msg += cipher[i];
    }
    return msg;
}


int main()
{
    string plaintext, ciphertext;

    ifstream input;
    ofstream output;

    input.open("input.txt");
    getline(input,plaintext);



    ciphertext = encryption(plaintext);
    plaintext  = decryption(ciphertext);

    cout<<"Original msg : "<<plaintext<<"\n";
    cout<<"Ciphertext msg : "<<ciphertext;

    input.close();
    output.close();

}