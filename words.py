# Write a Python program to find words which are greater than given length k.
sentence=input("Enter a sentence:")
words=sentence.split(" ")
k=int(input("Enter which length of you want:"))
for word in words:
    if len(word)>=k:
        print(word)