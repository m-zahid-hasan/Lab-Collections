


def encription(plain_text, key, alphabet):
    encryp = ""
    for char in plain_text:
        position = alphabet.index(char)
        new_position = (position + key)%26
        encryp += alphabet[new_position]
    
    return encryp
    


def decription(ciper_text, key, alphabet):
    decrypt = ""
    for char in ciper_text:
        position = alphabet.index(char)
        new_position = (position-key)%26
        decrypt += alphabet[new_position]
    
    return decrypt
    
    
    
    

def main():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    text = input("enter the message : ")
    encrypt = encription(text, 3, alphabet)
    print(f'After encryption : {encrypt}') 
    decrypt = decription(encrypt, 3, alphabet)
    print(f'After decryption : {decrypt}')
    


if __name__=='__main__':
    main()