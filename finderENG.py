import glob
import os

continua = "yes"

def nomi(nomiFILE):
    control = "valvole\*.txt"
    control = control[7]
    finito = []
    for x in nomiFILE:
            leng = len(x)-1
            vuoto = ""
            for y in range(leng):
                if x[leng - y] ==  control:
                    for z in range(y):
                        vuoto = x[leng-z] + vuoto
                    break
            finito.append(vuoto)
    return finito

while continua == "yes":
    print("which mode do you wanna use? \n \n 1:")
    print("     you will get a summary about ALL similarities \n     between ALL txt files in a directory \n \n 2:")
    print("     you will have to give the name of a file   \n     (for example myfile.txt \n     if you can find it in the same direcory \n     as the code else do mydirecory/...txt)\n     in wich you can fin the codes you want to \n     find in other text files ")
    mod = input()
    while not mod == "1" and not mod == "2":
        print("the input you gave is not a valid mode, try again")
        mod = input()
    if mod == "1":
        #chosing the direcotry
        print("\n")
        presente = False
        while presente == False:
            print("in wich directory are you looking for similarities")
            path = input()
            if len(glob.glob(path + "\*.txt")):
                presente = True
            else:
                print("\n this directory does not exist, his empty or only has 1 file \n")

        print("\n")


        #opening all txt files
        files = []
        fileraw = []

        for x in glob.glob(path + "\*.txt"):
            fileraw.append(x)
            files.append(open(x, "r"))


        elementi = []
        


        #this creates an array of arrays with all the codes of al the files
        for x in range(len(files)):
            elementi.append(files[x].readlines())

        control = "valvole\*.txt"
        control = control[7]

        #this creates an array of the name of all the files without the last name and .txt
        valv = nomi(fileraw)

        riassunto = {}
        riassunto2 = {}
        #this does the actual comparision and prints results
        for x in range(len(elementi)-1):
            for y in elementi[x]:
                for z in elementi[x+1]:
                    if y.replace("\n","")==z.replace("\n",""):
                        if y.replace("\n","") in riassunto:
                            riassunto[y.replace("\n","")] += 1
                        else:
                            riassunto[y.replace("\n","")] = 1
                        if y.replace("\n","") in riassunto2:
                            riassunto2[y.replace("\n","")] = riassunto2[y.replace("\n","")].replace(valv[x] + "\n","")
                            riassunto2[y.replace("\n","")] = riassunto2[y.replace("\n","")].replace(valv[x+1]+ "\n","")
                            riassunto2[y.replace("\n","")] +=  valv[x] + "\n" +"     " + valv[x+1] + "\n"
                        else:
                            riassunto2[y.replace("\n","")] = valv[x] + "\n" + "     " + valv[x+1] + "\n"
                        print("the file " + valv[x] + " has " + z.replace("\n","") + " in common with " + valv[x+1] + "\n")
        
        
        #prints the summary
        print("summary: code/times \n")
        for x in riassunto:
            print(x + " = " +str(riassunto[x])+"\n")

        for x in riassunto2:
            print(x + ":")
            print("     " + riassunto2[x])    




    if mod == "2":
        print("\nwhat is the path to the file with the codes? \n (remember the rules i gave earlier)")
        path = input()
        while not os.path.exists(path):
            print("\nthis path is not valid, try again")
            path = input()
        
        prefab = open(path, "r").readlines()
        for x in range(len(prefab)):
            prefab[x] = prefab[x].replace("\n", "")
        
        print("\ntell the directory with the other files")
        path = input()
        while len(glob.glob(path+"\*.txt")) <0:
            print("\nthis direcotry doesn't exist or is emply")

        #apro tutti i file txt
        files = []
        fileraw = []

        for x in glob.glob(path + "\*.txt"):
            fileraw.append(x)
            files.append(open(x, "r"))

        elementi = []
        valv = []

        #creo una lista di liste con ogni lista composta dai codici dei file txt
        for x in range(len(files)):
            elementi.append(files[x].readlines())

        control = "valvole\*.txt"
        control = control[7]

        #crea una lista dei nomi da dare ad ogni file (ultima parte del path)
        valv = nomi(fileraw)

        presente3 = []
        presente2 = []
        presente0 = []

        quali = []

        for elemento in range(len(elementi)):
            pres = 0
            for cod in elementi[elemento]:
                if cod.replace("\n","") in prefab:
                    pres +=1
                    quali.append(cod.replace("\n",""))
            if pres == len(prefab):
                presente3.append(valv[elemento])
            elif pres < len(prefab) and pres > 1:
                presente2.append(valv[elemento] + " has " + str(pres) + " elements = ")
                for x in quali:
                    presente2[len(presente2)-1] += "\n                               " + x
            elif pres == 1:
                presente2.append(valv[elemento] + " has " + str(pres) + " code = \n                               " + quali[0])
            else:
                presente0.append(valv[elemento])


        if len(presente0):
            print("\nthere are " + str(len(presente0)) + " files that have zeo codes")
            for x in presente0:
                print("     "+x)    


        if len(presente2):
            print("\nthere are" + str(len(presente2)) + " files which have only some codes")
            for x in presente2:
                print("     "+ x)


        if len(presente3):
            print("\nthere are " + str(len(presente3)) + " files that have all the codes")
            for x in presente3:
                print("     "+ x)


        

    print("\n continue? (yes/no) \n")
    continua = input()
    
    
