st=input("Input a string ")
chars={}
for ch in st:
    if ch not in chars:
        chars[ch]=1
    else:
        chars[ch]=chars[ch]+1
print(chars)