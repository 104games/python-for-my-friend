import glob

continua = "si"

while continua == "si":
    #scegliere la cartella
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

    control = "valvole\*.txt"
    control = control[7]

    #crea una lista dei nomi da dare ad ogni file (ultima parte del path)
    for x in fileraw:
        leng = len(x)-1
        vuoto = ""
        for y in range(leng):
            if x[leng - y] ==  control:
                for z in range(y):
                    vuoto = x[leng-z] + vuoto
                break
        valv.append(vuoto)

    riassunto = {}
    #questo effettivamente trova i codici uguali
    for x in range(len(elementi)-1):
        for y in elementi[x]:
            for z in elementi[x+1]:
                if y.replace("\n","")==z.replace("\n",""):
                    if y.replace("\n","") in riassunto:
                        riassunto[y.replace("\n","")] += 1
                    else:
                        riassunto[y.replace("\n","")] = 1
                    print("il file " + valv[x] + " ha " + z.replace("\n","") + " in comune con " + valv[x+1] + "\n")
        

    #scrive il riassunto
    print("riassunto: codice/volte \n")
    for x in riassunto:
        print(x + " = " +str(riassunto[x])+"\n")

    print("\n vuoi continuare? (si/no) \n")
    continua = input()
    