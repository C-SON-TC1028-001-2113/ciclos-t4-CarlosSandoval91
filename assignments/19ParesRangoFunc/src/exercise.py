
def main():
    num = int(input("Valor 1: ")) 
    nim = int(input("Valor 2: ")) 
    if num>0 and nim>0:
        if nim!=num:
            if num>nim:
                for i in range (nim,num+1):
                    if i%2==0:
                        print(i)
                
            elif nim>num:
                for i in range (num,nim+1):
                    if i%2==0:
                        print(i)
        else:
            print('No hay pares')

if __name__=='__main__':
    main()
