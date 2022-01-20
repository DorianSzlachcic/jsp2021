from fileinput import filename
import urllib.request
import urllib.parse
import sys
import re

url = sys.argv[1]
if url[len(url)-1] == "/":
    fileName = "index.html"
else:
    path = urllib.parse.urlparse(url).path
    i = len(path)-1
    fileName = ""
    while path[i] != "/":
        fileName = path[i]+fileName
        i -= 1

urllib.request.urlretrieve(url,fileName)