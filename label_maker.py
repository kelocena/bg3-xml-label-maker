import io
import json
from bs4 import BeautifulSoup
from bs4 import Comment
from bs4 import Formatter

class CustomFormatter(Formatter):
    def attributes(self, tag):
        for k, v in tag.attrs.items():
            yield k, v

class LabelMaker:
    #loca_db = dictionary of handles
    #filename = name of the file, str
    def __init__(self, filename):
        with io.open("indices/loca_index.txt", mode="r", encoding="utf-8") as f:
            self.loca_db = json.loads(f.read())
            self.filename = filename

    # open and read the file we want to label
    # look for attribute tags with id TagText and TranslatedString, and a handle.
    # pull from the handle 'class' to get the loca handle ID
    # Get English line from DB
    # add new line to XML (below might be easier but w/e) with the English
    # Save as new file? idk? w/e?

    def add_labels(self):
        print('Begin labeling %s', self.filename)

        # Edit the file prefix here
        filepath = 'resources/' + self.filename
        with io.open(filepath, mode="r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, 'xml')
            for tagtext in soup.find_all(self.get_taggedtext):
                handle = tagtext['handle']
                eng_line = self.loca_db[handle]

                new_comment = Comment(eng_line)
                tagtext.insert_before(new_comment)
            
            formatter = CustomFormatter(indent=4)
            self.labeled_soup = soup.prettify(formatter=formatter)


        self.save_labeled_xml()
        print(print('Finish labeling %s', self.filename))

    def save_labeled_xml(self):
        
        # Edit the output path as desired
        filepath = 'labeled/' + self.filename
        with open(filepath,  mode="w", encoding="utf-8") as f:
            f.write(self.labeled_soup)

    def get_taggedtext(self, tag):
        return tag.has_attr("handle") and tag.has_attr("type") and tag['type'] == "TranslatedString"


    # for tags and flags, they would be attributes of id=Tag and id=Flag respectively

# pass the file name in here
lm = LabelMaker('Karlach_InParty.lsx')

lm.add_labels()