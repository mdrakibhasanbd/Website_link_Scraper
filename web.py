import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import json
file1 = open('input2.txt', 'r')
Lines = file1.readlines() 
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    http = httplib2.Http()
    response, content = http.request(line)
    links=[]

    for link in BeautifulSoup(content).find_all( href=True):
        links.append(link['href'])
        
    for link in links:
        # print(link)
        # print(line.join(link))
        page = "{}{}".format(line,link.strip())
        print(page)
        # print(page.join(page))
        f = open("output.txt", "a")
        f.writelines(page + '\n')
        f.close()


