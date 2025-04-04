#FileNotFound
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except KeyError as error_message:
    print(f"The key {error_message} does not found")
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("some")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was close")
    raise KeyError("This is an error I made up")    






        
    
#KeyError
#IndexError
#Type Error


