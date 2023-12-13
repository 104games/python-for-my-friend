import glob

continua = "yes"

while continua == "yes":
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
    valv = []


    #this creates an array of arrays with all the codes of al the files
    for x in range(len(files)):
        elementi.append(files[x].readlines())

    control = "valvole\*.txt"
    control = control[7]

    #this creates an array of the name of all the files without the last name and .txt
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
    #this does the actual comparision and prints results
    for x in range(len(elementi)-1):
        for y in elementi[x]:
            for z in elementi[x+1]:
                if y.replace("\n","")==z.replace("\n",""):
                    if y.replace("\n","") in riassunto:
                        riassunto[y.replace("\n","")] += 1
                    else:
                        riassunto[y.replace("\n","")] = 1
                    print("the file " + valv[x] + " has " + z.replace("\n","") + " in common with " + valv[x+1] + "\n")
        

    #prints the summary
    print("summary: code/times \n")
    for x in riassunto:
        print(x + " = " +str(riassunto[x])+"\n")

    print("\n continue? (yes/no) \n")
    continua = input()
    