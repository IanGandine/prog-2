
def main():
    idade=int(input())
    npessoas=0
    idadegeral=0
    while idade!=0:
        npessoas=npessoas+1
        idadegeral=idadegeral+idade
        idade=int(input())
    print(idadegeral/npessoas)
    
if __name__ == '__main__':
    main()

#coment