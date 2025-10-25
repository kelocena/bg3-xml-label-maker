
## build loca db? Would be nice to have a dictionary to index faster than iterating through the loca every time.
import io
from bs4 import BeautifulSoup

def index_loca():
    with io.open("resources/english.loca.xml", mode="r", encoding="utf-8") as eng:
        # read_data = eng.read()
        # print(read_data)
        # thing = eng.decode('utf8')
        print(eng)
        # eng.decode('utf8')
        loca = BeautifulSoup(eng, 'xml')
        print(loca)
    

index_loca()