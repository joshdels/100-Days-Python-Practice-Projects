import os
path = os.chdir(r"C:\Users\deleo\OneDrive\Documents\GitHub\100-Days-Python-Practice-Projects\Day_24\Mail Merge Project Start")
print(os.getcwd())

#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

list_of_names = []

# reading and writing with python
with open(r"Input\Names\invited_names.txt", mode="r") as names:
    names = names.readlines()
    for i in names:
        stripped = i.strip('\n')
        list_of_names.append(stripped) 


with open("Input\Letters\starting_letter.txt", mode="r") as letter:
    context = letter.read()
    for name in list_of_names:
        with open(f"Output\ReadyToSend\letter_for_{name}.txt", mode="w") as letter:
            updated_context = context.replace("[name]", name)
            letter.write(updated_context)
            
# Very easy practice only problem is the venv
  
    
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp