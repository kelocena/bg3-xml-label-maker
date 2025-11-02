import io
import json
from bs4 import BeautifulSoup

def build_loca_index():
    loca_index = {}
    with io.open("resources/english.loca.xml", mode="r", encoding="utf-8") as eng:

        loca = BeautifulSoup(eng, 'xml')

        print('indexing all handles')
        for tag in loca.find_all("content"):
            handle = tag['contentuid']
            text = tag.string
            loca_index[handle] = text
    
    with open("indices/loca_index.txt",  mode="w", encoding="utf-8") as f:
        f.write(json.dumps(loca_index))

    print('loca file indexed and written to indices/loca_index.txt as JSON')
# build_loca_index()

def test_read():
    with io.open("indices/loca_index.txt", mode="r", encoding="utf-8") as f:
        li = json.loads(f.read())
        print(li['hffff8e50gcd5ag4d97gbc03gf783776542b4'])

test_read()