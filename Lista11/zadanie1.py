import urllib.request

try:
    if urllib.request.urlopen("https://www.google.com/").getcode() == 200:
        print("Strona istnieje")
except:
    print("Strona nie istnieje")