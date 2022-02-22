##Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def calculation(s):
    uppercase=0
    lowercase=0
    for i in s:
        if i.isupper():
            uppercase+=1
        elif i.islower():
            lowercase +=1
        else:
            pass
    print("Total number of uppercase alphates are ", uppercase)
    print("Total number of lower case alphabates are ", lowercase)

calculation('The quick Brow Fox')
