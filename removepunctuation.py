punctuations='''!~@#$%^&*()_-{}[]:;"'|\,<>?./`'''
sentence=input("Enter a sentence:")
words=sentence.split(" ")
sentences=""
for word in words:
    new_sentence=""
    for char in word:
        if char not in punctuations:
            new_sentence+=char
    sentences+=new_sentence
print(sentences)