def Convert(string):
    list1=[]
    list1[:0]=string
    return list1
with open('two_cities_ascii.txt', 'r') as file:
    data = file.read()
list = (Convert(data))
#print(list)
#two_cities_list
nstr = ['' for y in range(0, len(data))]
for x in range(0, len(data)):   
    nstr[x] = format(ord(list[x]), 'b')
    if ord(list[x]) < 64 and ord(list[x]) >= 32:
        nstr[x] = "0" + nstr[x]
    elif nstr[x] == '1010':
        nstr[x] = "000" + nstr[x]
#print(nstr)
#two_cities_bin
z= len(data)//4
hexstr = ['' for y in range(0, z)]
for i in range(0, z):
    for j in range(0,4):
        hexstr[i] += nstr[i*4+j][:2] + nstr[i*4+j][-2:]
    hexstr[i] = int(hexstr[i])
#print(hexstr)
#two_cities_hex  
m2, m3, m5, m7 = (0, 0, 0, 0)
for i in range(0, z):
    if hexstr[i]%2 == 0:
        m2 += 1
    if hexstr[i]%3 == 0:
        m3 += 1
    if hexstr[i]%5 == 0:
        m5 += 1
    if hexstr[i]%7 == 0:
        m7 += 1
print("Το", (m2/z)*100, "% είναι ζυγοί")
print("Το", (m3/z)*100, "% διαιρούνται με το 3")
print("Το", (m5/z)*100, "% διαιρούνται με το 5")
print("Το", (m7/z)*100, "% διαιρούνται με το 7")
