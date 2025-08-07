sentence=input("Enter a sentence:")
words=sentence.split(" ")
words.sort()
for i in words:
    print(i.capitalize())

