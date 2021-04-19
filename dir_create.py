

#Ask for a sentence
#Print the lnegth of the sentence
#Ask for a file name (.txt)
#Write the sentence to the file
#Run the program from your cmd line

sentence = input("Enter a sentence: ")
sentence_length = len(sentence)
print(sentence_length)

file_name = input("Enter a file name: ")
file_name = f"{file_name}.txt" #using fstrings

with open(file_name, "w") as file:
    file.write(sentence)
    file.close()

with open(file_name, 'r') as file:
    read = file.read()
    file.close()
print(f"contents :{read}")

print(f"You've written {sentence_length} characters to {file_name}")