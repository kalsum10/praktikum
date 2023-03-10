import math
def linearsearch(arr,x):
    for l in range(len(arr)):
        if type(arr[l]) == list:
            searchdata = linearsearch(arr[l],x)
            if searchdata == -1:
                return -1
            else:
                print(x, "ditemukan di indeks" ,l, "kolom" ,searchdata,)
                exit()
        elif arr[l] == x:
            return l
    return -1
def jumpSearch( arr , x , v ):
    langkah = math.sqrt(v)
    p = 0
    for j in range(len(arr)):
        if type(arr[j]) == list:  
            Searchingdata = jumpSearch(arr[int(j)],x,len(arr[int(j)]))
            if Searchingdata == -1:
                arr[int(j)] = "z"
                print()
            else:
                print(x ,"Ditemukan di index", {int(j)} ,"kolom" ,{Searchingdata})
                exit()
    while arr[int(min(langkah, v)-1)] < x:
                p = langkah
                langkah += math.sqrt(v)
                if p >= v:
                    return -1
    while arr[int(p)] < x:        
                p += 1
                if p == min(langkah, v):
                    return -1
    if arr[int(p)] == x:
            return int(p)
    return -1
def Linesearch(a1,m):
    dicari = linearsearch(a1,m)
    if dicari == -1:
        print({m}," Tidak ditemukan")
    else:
        print({m}, "Ditemukan Di Index", {dicari})
def searchjump(b1,l,g):
    h = jumpSearch(b1,l,g)
    if h == -1:
        print(l,"Tidak ditemukan")
    else:
        print(l," Ditemukan Di Index", h)

Array = ["Arsel","Avivah","Daiva",["Wahyu","Wibi"]]

print("""
Data atau elemen yang bisa di searching
=======================================
|Arsel | Avivah | Daiva | Wahyu | Wibi|
=======================================
""")

g = len(Array)
while True:
    print("""
    Metode Yang Bisa Digunakan
    1. LinearSearch
    2. Jumpsearch
    """)
    searching = input("Masukan searching yang ingin anda gunakan: ")
    elemen = input("Masukan Data atau elemen Yang Ingin Disearching: ")
    if searching == "1":
        Linesearch(Array,elemen)
        break
    elif searching == "2":
        searchjump(Array,elemen,g)
        break