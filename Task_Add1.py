dig={
    1:"one ",
    2:"two ",
    3:"three ",
    4:"four ",
    5:"five ",
    6:"six ",
    7:"seven ",
    8:"eigth ",
    9:"nine ",
    10:"ten",
    11:"eleven ",
    12:"twelve ",
    13:"thirteen ",
    14:"fourteen ",
    15:"fifteen ",
    16:"sixteen ",
    17:"seventeen ",
    18:"eighteen ",
    19:"nineteen ",
    20:"twenty ",
    30:"thirty ",
    40:"fourty ",
    50:"fifty ",
    60:"sixty ",
    70:"seventy ",
    80:"eighty ",
    90:"ninty ",
}
num=float(input("Input number "))
st=str


str_hun_tho=""
str_hun_tho=str(dig.get(num//100000))
if str_hun_tho!="":
    str_hun_tho+="hundreed "

st_tho=""
if num//1000<20:
    st_tho=str(dig.get(num//1000))
if num//1000>=20 and num//1000<100:
    st_tho=str(dig.get(num//10000*10))+str(dig.get(num//1000-(num//10000)*10))
if num//1000>100:
    st_tho = str(dig.get(((num//10000) % 10)*10)) + str(dig.get(num // 1000 - (num // 10000) * 10))

if st_tho!="" or str_hun_tho!="":
    st_tho+="thousand "

st_hun=""
st_hun=str(dig.get((num-(num//1000*1000))//100))
if st_hun!="" and st_hun!="None":
    st_hun+="hundreed "

st_dig=""
if num%100<20:
    st_dig=str(dig.get(int(num%10)))
if int(num%100)>=20 and int(num%100)<100:
    st_dig=str(dig.get(int(num%100)-int(num%10)))+str(dig.get(int(num%10)))

cents=int(round(num%1,2)*100)
st_cents=""
if cents%100<20:
    st_cents=str(dig.get(cents%10))
if cents%100>=20 and cents%100<100:
    st_cents=str(dig.get(cents%100-cents%10))+str(dig.get(cents%10))
if st_cents!="" and st_cents!="None":
    st_cents+="cents "
st=str_hun_tho+st_tho+st_hun+st_dig+'dollars '+st_cents
st=st.replace("None","")
st=st.replace("  "," ")

print(st)
