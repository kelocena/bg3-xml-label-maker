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
    #flag_db = flags dictionary
    #tag_db = tag dictionary

    #filename = name of the file, str
    def __init__(self, filename):
        with io.open("indices/loca_index.txt", mode="r", encoding="utf-8") as l:
            self.loca_db = json.loads(l.read())

        with io.open("indices/flag_index.txt", mode="r", encoding="utf-8") as f:
            self.flag_db = json.loads(f.read())

        with io.open("indices/tag_index.txt", mode="r", encoding="utf-8") as t:
            self.tag_db = json.loads(t.read())
        
        self.filename = filename

    def add_labels(self):
        missing_labels = set()
        print('Begin labeling...', self.filename)

        # EDIT the file prefix here
        filepath = 'resources/' + self.filename
        with io.open(filepath, mode="r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, 'xml')

            # label text handles
            print('Labeling Text Handles...')
            for tagtext in soup.find_all(self.get_taggedtext):
                handle = tagtext['handle']
                eng_line = "Handle Text Not Found"

                try:
                    eng_line = self.loca_db[handle]
                except:
                    missing_labels.add(handle)

                self.add_comment_label(tagtext, eng_line)

            # label flags
            print('Labeling Flags...')
            for flag in soup.find_all(self.get_flag_nodes):
                flag_uuid = flag.attribute['value']
                flag_name = 'Flag Label Not Found'

                try:
                    flag_name = self.flag_db[flag_uuid]
                except:
                    try:
                        flag_name = self.tag_db[flag_uuid]
                    except:
                        missing_labels.add(flag_uuid)

                
                self.add_comment_label(flag.attribute, flag_name)

            # label tags
            print('Labeling Tags...')
            for tag in soup.find_all(self.get_tag_nodes):
                tag_uuid = tag.attribute['value']
                tag_name = 'Tag Label Not Found'

                try:
                    tag_name = self.tag_db[tag_uuid]
                except:
                    try:
                        tag_name = self.flag_db[tag_uuid]
                    except:
                        missing_labels.add(tag_uuid)


                self.add_comment_label(tag.attribute, tag_name)
            
            print('Formatting results before saving.')
            formatter = CustomFormatter(indent=4)
            self.labeled_soup = soup.prettify(formatter=formatter)

        self.save_labeled_xml()
        print('Finish labeling!!', self.filename)

        missing_count = len(missing_labels)
        if missing_count > 0:
            print(missing_count, 'IDs were unable to be identified :( \nLabels Missing:', missing_labels)

    def save_labeled_xml(self):
        
        # EDIT the output path as desired
        filepath = 'labeled/' + self.filename
        with open(filepath,  mode="w", encoding="utf-8") as f:
            f.write(self.labeled_soup)

    def get_taggedtext(self, tag):
        return tag.has_attr("handle") and tag.has_attr("type") and tag['type'] == "TranslatedString" and tag['id'] == "TagText"

    def get_flag_nodes(self, tag):
        return tag.has_attr('id') and tag['id'] == 'flag'

    def get_tag_nodes(self, tag):
        return tag.has_attr('id') and tag['id'] == 'Tag'

    def add_comment_label(self, tag, label):
        new_comment = Comment(" " + label + " ")
        tag.insert_before(new_comment)


    # for tags and flags, they would be attributes of id=Tag and id=Flag respectively

# EDIT pass the file name in here
lm = LabelMaker('SHA_NightsongPrison_PAD_Prayer.lsx')

lm.add_labels()

# https://www.geeksforgeeks.org/python/python-loop-through-folders-and-files-in-directory/