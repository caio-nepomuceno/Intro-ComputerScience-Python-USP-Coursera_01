def main():

    numero = int(input("Informe um número para saber se é primo: "))
    primo = False

    if numero > 1:
        if numero == 2:
            primo = True
        else:

            i = 2
            while i <= numero and not primo:

                if (numero % 2 != 0): 
                    if (numero % i == 0):   # divisivel por multiplo
                        if (i == numero):   # e mesmo numero
                            primo = True
                        else:               # divisivel por multiplo
                            break           # não é o mesmo numero

                i += 1

    if primo:
        print("primo")
    else:
        print("não primo")

main()