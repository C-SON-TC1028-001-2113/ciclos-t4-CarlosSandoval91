
def main():
    #escribe tu código abajo de esta línea
    h= int(input('Enter triangle height: '))
    for i in range (1,h+1):
        print(' '*(h-i)+'*'*i)

if __name__=='__main__':
    main()
