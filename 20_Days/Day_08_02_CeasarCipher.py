alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

# store the index list of the encoded
index_list = []
encrypted_list = []
index_encrypted = []
decrypted_list = []


if direction == 'encode':
    print("Encoding......")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    # for indexcing 
    for i in range(len(text)):
        letter = text[0+i]
        index = alphabet.index(str(letter))
        index_list.append(index)

    # print(index_list)

    # letter to be reciprocated
    for letter in index_list:
        new_letter = alphabet[letter+shift]
        encrypted_list.append(new_letter)
        
    # for encrypted word
    encrypted_word = ''.join(encrypted_list)
    print(f"Your Encrypted Word: {encrypted_word}")
    
    decision = input("Would you like to decode the encrypted word?: (Y/N)").lower()
    if decision == 'y':
        
        print(encrypted_list)
        encrypted_word = ''.join(encrypted_list)
        print("Your encrypted word: " + encrypted_word)
        
        for i in encrypted_list:
            letter = alphabet.index(i)
            index_encrypted.append(letter)
        
        # check what is passed in the index encrypted
        print(index_encrypted)
        
        reshift = int(input("Type the reshift number:\n"))

        ## for reciprocating the values NEED TO DEBUG
        for i in index_encrypted:
            new_letter = alphabet[int(i)-reshift]
            decrypted_list.append(new_letter)
            
        decrypted_word = ''.join(decrypted_list)    
        print(f"Your Encrypted Word: {decrypted_word}")
            
elif direction == 'decode':
    encrypted_word = ''.join(encrypted_list)
    print("Your encrypted word: " + encrypted_word)
    reshift = int(input("Type the reshift number:\n"))
    
else:
    print("Your words are hidden to the public, rest assure")
    
    
# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.