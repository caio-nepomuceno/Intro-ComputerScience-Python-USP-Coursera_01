seg = int(input("Digite os segundos: "))

a = seg//60//60//24
b = (seg//60//60)%24
c = (seg//60)%60
d = seg%60

print(a,"dias,",b,"horas,",c,"minutos e",d,"segundos.")
