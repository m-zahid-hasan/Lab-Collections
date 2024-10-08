#include<bits/stdc++.h>
using namespace std;

int enrypt(int ch)
{
    return (ch+3)%26;
}
int decrypt(int ch)
{
    return (ch-3+26)%26;
}

void encryption(string str)
{
    for (int i = 0; str[i];i++)
    {
        if(isupper(str[i]))
        {
            str[i] = char(enrypt(str[i]-'A')+'A');

        }
        else if (islower(str[i]))
        {
            str[i] = char(enrypt(str[i]-'a')+'a');
        }
    }
    cout<<"Encryption : "<<str<<"\n";
}


void decyption(string str)
{
    for (int i = 0;str[i]; i++)
    {
        if(isupper(str[i]))
        {
            str[i] = char(decrypt(str[i]-'A')+'A');

        }
        else if(islower(str[i]))
        {
            str[i] = char(decrypt(str[i]-'a')+'a');
        }
    }

    cout<<"Decrypted Text : "<<str;

}


int main()
{
    string str;
     cin>>str;
     encryption(str);
     decyption(str);
}