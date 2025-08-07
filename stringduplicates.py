word=input("Enter a word:")
new_word=''
for char in word:
    if char not in new_word:
        new_word+=char
print(new_word)