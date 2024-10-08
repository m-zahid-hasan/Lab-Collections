#include<bits/stdc++.h>
using namespace std;
string encryption(string msg,int w){
    string ans="";
    for(int i=0;i<w;i++){
        for(int j=i;j<msg.size();j+=w){
            ans+=msg[j];
        }
    }
    return ans;
}
string decryption(string msg,int w){
    string ans="";
    int height=msg.size()/w;
    int extra=msg.size()%w;
    for(int i=0;i<height;i++){
         int tmp=extra,h=height;
         for(int j=i;j<msg.size();j+=h){
            h=(tmp-- > 0) ? height+1 : height;
            ans+=msg[j];
         }
    }
    for(int i=0,j=height+1;i<extra;i++,j+=height+1){
        ans+=msg[j-1];
    }
    return ans;
}
int main(){
    freopen("example.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);

    string plaintext;
    int width=10;

    getline(cin, plaintext);
    // cin>>width;

    cout<<"Original Text:"<<plaintext<<endl;
    string en_text = encryption(encryption(plaintext, width),width);
    cout<<"Cipher Text:"<<en_text<<endl;
    string dec_text =decryption(decryption(en_text, width),width) ;
    cout<<"Decrypted Text:"<<dec_text<<endl;
}


// DEPARTMENTOFCOMPUTERSCIENCEANDENGINEERING


// Original msg : DEPARTMENTOFCOMPUTERSCIENCEANDENGINEERING
//Ciphertext msg : DTEAEROINGNTEE ACCENEUCNPFSDI MPNIEORNRTMEG 
// Decrypted Text:DEPARTMENTOFCOMPUTERSCIENCEANDENGINEERING