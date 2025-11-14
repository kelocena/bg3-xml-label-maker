import io
import json
from bs4 import BeautifulSoup

def build_loca_index():
    loca_index = {}

    # replace with the path to the loca file you wish to index
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

build_loca_index()

# Check it worked
def test_read():
    with io.open("indices/flag_index.txt", mode="r", encoding="utf-8") as f:
        idx = json.loads(f.read())
        print(idx['fff32281-b937-22d0-b283-29e547cb2765'])

test_read()

# functions to index the tags and flags

def build_flag_index():
    flag_index = {}

    print('Building Flag index...')
    with open("resources/flags_list.txt", mode="r", encoding="utf-8") as fl:
        for f in fl:
            (uuid, name) = separate_uuid_and_name(f)

            flag_index[uuid] = name
    
    with open("indices/flag_index.txt",  mode="w", encoding="utf-8") as fi:
        fi.write(json.dumps(flag_index))

def build_tag_index():
    tag_index = {}

    print('Building Tag index...')
    with open("resources/tags_list.txt", mode="r", encoding="utf-8") as tl:
        for t in tl:
            (uuid, name) = separate_uuid_and_name(t)

            tag_index[uuid] = name
    
    with open("indices/tag_index.txt",  mode="w", encoding="utf-8") as ti:
        ti.write(json.dumps(tag_index))

def separate_uuid_and_name(flag):
    split_flag = flag.split('_')

    uuid = split_flag.pop().strip()
    name = '_'.join(split_flag)

    return (uuid, name)

build_flag_index()
build_tag_index()
