#include<bits/stdc++.h>
using namespace std;

string encrypt(string msg)
{

    string cipher = "", pad;
    ifstream input;
    input.open("random_string.txt");
    input>>pad;

    for (int i = 0;i<msg.size(); i++)
    {
        if(isupper(msg[i]))
        {
            cipher+= char(((msg[i]-'A')+(pad[i]-'A'))%26+'A');
        }
        else if(islower(msg[i]))
        {
            cipher+= char(((msg[i]-'a')+(pad[i]-'A'))%26+'a');
        }
        else cipher+=msg[i];
    }

    input.close();
    return cipher;

}


string decrypt(string cipher)
{
    string msg = "",pad;
    ifstream input;
    input.open("random_string.txt");
    input>>pad;

    for(int i = 0 ; i<cipher.size();i++)
    {
        if(isupper(cipher[i]))
        {
            msg+= char(((cipher[i]-'A')-(pad[i]-'A')+26)%26+'A');

        }
        else if(islower(cipher[i]))
        {
             msg+= char(((cipher[i]-'a')-(pad[i]-'A')+26)%26+'a');
        }
        else msg+= cipher[i];
    } 
    input.close();
    return msg;
}



int main()
{
    string msg,cipher,s;
    // ifstream input;
    ofstream output;

    // input.open("input.txt");
     output.open("output.txt");
    freopen("input.txt","r",stdin);
    while(cin>>s)
    {
        msg+= s+" ";

    }

    cipher = encrypt(msg);
    cout<<"Cipher message :"<<cipher<<"\n";
    msg = decrypt(cipher);
    cout<<"Original message :"<<msg;

    output.close();
    
}