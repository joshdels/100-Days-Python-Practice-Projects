alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


index_list = []
index_encrypted = []
decrypted_list = []


def encode(text, shift):
    '''
    original_text: Is the text to be  encrypted
    number_of_shifts: (Number) to be shifted right
    '''
    
    encrypted_list = []
    
    for i in range(len(text)):
        letter = text[0+i]
        index = alphabet.index(str(letter))
        index_list.append(index)
        
    # letter to be reciprocated
    for letter in index_list:
        new_letter = alphabet[letter+shift]
        encrypted_list.append(new_letter)
    
    encrypted_word = ''.join(encrypted_list)
    print(f"Your encrypted word: {encrypted_word}")
    return encrypted_word
    

def decrypt(encrypted_word, reshift):
    '''
    '''
    index_encrypted = []
    decrypted_list = []
    
    encrypted_list = list(encrypted_word)
    for i in encrypted_list:
        letter = alphabet.index(i)
        index_encrypted.append(letter)

    for i in index_encrypted:
        new_letter = alphabet[int(i)-reshift]
        decrypted_list.append(new_letter)
    
    decrypted_word = ''.join(decrypted_list)
    print(decrypted_word)
    
    return decrypted_word

# bottom finals
if direction == 'encode':
    qencrypted_word = encode(text, shift)

elif direction == 'decode':
    reshift = int(input("Type the reshift number:\n"))
    decrypt(encrypted_word, reshift)