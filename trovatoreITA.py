import glob
import os.path

continua = "si"

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


if continua == "si":
#scegliere la cartella
    print("che modalità vuoi usare? \n \n 1:")
    print("     resoconto di TUTTI i codici in comune \n     tra tutti quelle delle cartelle \n \n 2:")
    print("     dovrai fornire al programma il nome del  \n     file (esempio = prefabbricato.txt, se si trova \n     nella STESSA cartella del programma, \n     altrimente nomeCartella/...txt)\n     in cui ci sono i codici che cerchi nelgli \n     altri file di testo")
    mod = input()
    while not mod == "1" and not mod == "2":
        print("non hai insterito una modalità valida!")
        mod = input()
    while mod == "1":
        print("\n")
        presente = False
        while presente == False:
            print("in quale cartella sono presenti i file in cui cerchi similitudini?")
            path = input()
            if len(glob.glob(path + "\*.txt")):
                presente = True
            else:
                print("\n cartella non esistente o vuota \n")

        print("\n")


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

        

        #crea una lista dei nomi da dare ad ogni file (ultima parte del path)
        valv = nomi(fileraw)

        riassunto = {}
        riassunto2 = {}
        #questo effettivamente trova i codici uguali
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
                        print("il file " + valv[x] + " ha " + z.replace("\n","") + " in comune con " + valv[x+1] + "\n")
            

        #scrive il riassunto
        print("riassunto: codice/volte \n")
        for x in riassunto:
            print(x + " = " +str(riassunto[x]+1))
            
            
        print("\n")
        for x in riassunto2:
            print(x + ":")
            print("     " + riassunto2[x])

        

    
    if mod == "2":
        print("\ncome si chiama il file di testo in cui ci sono i codici? \n (ricorda le instruzioni di prima)")
        path = input()
        while not os.path.exists(path):
            print("\npercorso non valido! inseriscine un altro")
            path = input()
        
        prefab = open(path, "r").readlines()
        for x in range(len(prefab)):
            prefab[x] = prefab[x].replace("\n", "")
        
        print("\nbene, ora dimmi la cartella in cui cercare i file")
        path = input()
        while len(glob.glob(path+"\*.txt")) <0:
            print("\ncartella non esistente o vuota, inseriscine un altra")

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

        

        for elemento in range(len(elementi)):
            pres = 0
            quali = []
            for cod in elementi[elemento]:
                if cod.replace("\n","") in prefab:
                    pres +=1
                    quali.append(cod.replace("\n",""))
            if pres == len(prefab):
                presente3.append(valv[elemento])
            elif pres < len(prefab) and pres > 1:
                presente2.append(valv[elemento] + " ha " + str(pres) + " elementi = ")
                for x in quali:
                    presente2[len(presente2)-1] += "\n                               " + x
            elif pres == 1:
                presente2.append(valv[elemento] + " ha " + str(pres) + " solo un codice = \n                               " + quali[0])
            else:
                presente0.append(valv[elemento])
            
        if len(presente2):
            print("\nci sono " + str(len(presente2)) + " che hanno solo alcuni codici, però senza averceli tutti")
            for x in presente2:
                print("     "+ x)

        if len(presente0):
            print("\nquesti sono " + str(len(presente0)) + " file che non hanno neanche un codice")
            for x in presente0:
                print("     "+x)


        if len(presente3):
            print("\nci sono " + str(len(presente3)) + " file che hanno tutti i codici")
            for x in presente3:
                print("     "+ x)

        

    print("\n vuoi continuare? (si/no) \n")
    continua = input()
    

    
