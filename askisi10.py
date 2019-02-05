import urllib.request
import re
synd=input("Δωστε ενα link: ")
page=urllib.request.urlopen(synd)
content=page.read()
content=str(content,'utf-8')
links=len(re.findall("<a",content))+len(re.findall("<link",content))
allag_gramm=len(re.findall("<br>",content))+len(re.findall("</p>",content))
print("Οι συνδεσμοι μεσα στον κωδικα ειναι ",links," και οι αλλαγες γραμμης ειναι ",allag_gramm)
