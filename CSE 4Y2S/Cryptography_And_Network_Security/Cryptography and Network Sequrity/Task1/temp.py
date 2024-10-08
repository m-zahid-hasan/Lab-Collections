def encryption(plain_text, key):
    encrypt = ''
    for char in plain_text :
        if char.isdigit():
            encrypt += char
            
        elif char.isupper():
            encrypt += char((ord(char)+3)%26)
            
        elif char.islower():
            encrypt += char((ord(char)+3)%26)
        
    return encrypt



def main():
    plain_text = input('type message : ')
    encrypt = encryption(plain_text,3)
    print(f'After the encryption : {encrypt}')


if __name__=='__main__':
    main()
    
            
    