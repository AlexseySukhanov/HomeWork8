rom={
    "M":1000,
    "D":500,
    "C":100,
    "L":50,
    "X":10,
    "V":5,
    "I":1
}
rnum=input("Input roman number ").upper()
sum=0
i=0
while i< len(rnum)-1:
    if rom.get(rnum[i])<rom.get(rnum[i+1]):
        sum -= rom.get(rnum[i])
    else:
        sum+=rom.get(rnum[i])
    i+=1
sum+=rom.get(rnum[i])
print(sum)