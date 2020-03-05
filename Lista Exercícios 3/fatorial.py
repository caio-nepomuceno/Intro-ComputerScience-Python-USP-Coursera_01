n = int(input("Fatorial de: "))
nfat = 1
count = 1

if n==0:
    nfat = 1
    print(nfat)
    
else:
    while count <= n:
        nfat = nfat*count
        count = count + 1

print(nfat)