jednosci = {1:"jeden",2:"dwa",3:"trzy",4:"cztery",5:"piec",6:"szesc",7:"siedem",8:"osiem",9:"dziewiec",0:""}
dziesiatki = {2:"dziescia",3:"dziesci",4:"dziesci",5:"dziesiat",6:"dziesiat",7:"dziesiat",8:"dziesiat",9:"dziesiat"}
nastki = {11:"jedenacie",12:"dwanascie",13:"trzynascie",14:"czternascie",15:"pietnascie",16:"szesnascie",17:"siedemnascie",18:"osiemnascie",19:"dziewietnascie",10:"dziesiec"}
setki = {1:"sto",2:"dwiescie",3:"trzysta",4:"czterysta",5:"piecset",6:"szescset",7:"siedemset",8:"osiemset",9:"dziewiecset"}

liczba = int(input("Podaj liczbe z przedzialu (1-1999): "))
slownie = ""

if liczba>=1 and liczba<=1999:
    jed = liczba%10
    liczba = liczba//10
    dz = liczba%10
    liczba = liczba//10
    st = liczba%10
    liczba = liczba//10

    slownie = jednosci[jed]

    if dz==1:
        slownie = nastki[dz*10+jed]
    elif dz != 0:
        slownie = jednosci[dz]+dziesiatki[dz]+" "+slownie

    if st !=0:
        slownie = setki[st]+" "+slownie
    
    if liczba == 1:
        slownie = "tysiac "+slownie

    print(slownie)
else:
    print("Liczba nie jest z przedziału")