#  Write a Python program to print all pronic numbers between 1 and 100.
#  A pronic number, also known as an oblong number or rectangular number, is a type of
#  figurate number that represents a rectangle. It is the product of two consecutive integers, n
#  and (n + 1). Mathematically, a pronic number can be expressed as:
#  𝑃𝑛= 𝑛∗(𝑛+1)
li=[]
for i in range(1,101):
    for j in range(i+1):
        pro=j*(j+1)
        if pro==i:
            li.append(i)
            break
print(li)
