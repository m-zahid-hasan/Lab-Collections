#include<bits/stdc++.h>
using namespace std;

map<string,string>en_dictionary,dec_dictionary;

void create_dictionary()
{
    string w1,w2;
    ifstream input;
    input.open("dictionary.txt");
    while(input>>w1>>w2)
    {
        en_dictionary[w1] = w2;
        dec_dictionary[w2] = w1;
    }
    input.close();
}


string encryption(string msg)
{
    string cipher = "", temp = "";

    for(int i = 0; i<msg.size(); i++)
    {
        if(msg[i]>='A' && msg[i]<='Z' || msg[i]>='a' && msg[i]<='z')
        {
            temp+= msg[i];

            if(en_dictionary.find(temp)!=en_dictionary.end())
            {
                cipher+=en_dictionary[temp];
                temp = "";
            }
        }
        else cipher+= msg[i]; 
    }
    return cipher;
}

string decryption(string cipher)
{
    string msg = "", temp ="";
    for(int i = 0; i<cipher.size(); i++)
    { 
        if(cipher[i]>='A' && cipher[i]<='Z' || cipher[i]>='a' && cipher[i]<='z')
        {
            temp+= cipher[i];
            
            if(dec_dictionary.find(temp)!=dec_dictionary.end())
            {
                msg+= dec_dictionary[temp];
                temp = "";
            }
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
    output.open("ouput.txt");

    getline(input,plaintext);

    create_dictionary();

    ciphertext = encryption(plaintext);
    plaintext  = decryption(ciphertext);

    cout<<"Original msg : "<<plaintext<<"\n";
    cout<<"Ciphertext msg :"<<ciphertext;

    input.close();
    output.close();
}
