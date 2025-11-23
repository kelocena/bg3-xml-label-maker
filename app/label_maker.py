import io
import json
import os
import sys
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
    #missing_labels = set of ids

    def __init__(self):
        li_path = 'app/indices/loca_index.txt'
        fi_path = 'app/indices/flag_index.txt'
        ti_path = 'app/indices/tag_index.txt'

        if getattr(sys, 'frozen', False):
            li_path = os.path.join(sys._MEIPASS, li_path)
            fi_path = os.path.join(sys._MEIPASS, fi_path)
            ti_path = os.path.join(sys._MEIPASS, ti_path)

        with io.open(li_path, mode="r", encoding="utf-8") as l:
            self.loca_db = json.loads(l.read())

        with io.open(fi_path, mode="r", encoding="utf-8") as f:
            self.flag_db = json.loads(f.read())

        with io.open(ti_path, mode="r", encoding="utf-8") as t:
            self.tag_db = json.loads(t.read())

        self.missing_labels = set()

    def label_multiple(self, directory_path, save_directory):
        for root, _, files in os.walk(directory_path):

            relpath = os.path.relpath(root, start=directory_path)

            for f in files:
                if f.endswith('.lsx'):
                    filepath = os.path.join(root, f)
                    savepath = os.path.join(save_directory, f) if relpath == '.' else os.path.join(save_directory, relpath, f)

                    try:
                        self.add_labels_to_file(filepath, savepath)
                    except FileNotFoundError:
                        new_folders = os.path.join(save_directory, relpath)
                        os.makedirs(new_folders, exist_ok=True)
                        self.add_labels_to_file(filepath, savepath)
        
        self.print_missing_labels()


    def label_single(self, filepath, save_location):
        self.add_labels_to_file(filepath, save_location)
        self.print_missing_labels()

    def add_labels_to_file(self, filepath, save_location):
        print('Begin labeling...', filepath)

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
                    self.missing_labels.add(handle)

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
                        self.missing_labels.add(flag_uuid)

                
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
                        self.missing_labels.add(tag_uuid)


                self.add_comment_label(tag.attribute, tag_name)
            
            print('Formatting results before saving.')
            formatter = CustomFormatter(indent=4)
            labeled_soup = soup.prettify(formatter=formatter)

        self.save_labeled_xml(save_location, labeled_soup)
        print('Finish labeling!!', save_location)

    def save_labeled_xml(self, filepath, labeled_soup):
        with io.open(filepath,  mode="w", encoding="utf-8") as f:
            f.write(labeled_soup)

    def print_missing_labels(self):
        missing_count = len(self.missing_labels)
        if missing_count > 0:
            print(missing_count, 'IDs were unable to be identified :( \nLabels Missing:', self.missing_labels)
        self.missing_labels = set()

    def get_taggedtext(self, tag):
        return tag.has_attr("handle") and tag.has_attr("type") and tag['type'] == "TranslatedString" and tag['id'] == "TagText"

    def get_flag_nodes(self, tag):
        return tag.has_attr('id') and tag['id'] == 'flag'

    def get_tag_nodes(self, tag):
        return tag.has_attr('id') and tag['id'] == 'Tag'

    def add_comment_label(self, tag, label):
        new_comment = Comment(" " + label + " ")
        tag.insert_before(new_comment)

# lm = LabelMaker()
# lm.label_multiple('resources', 'labeled')
# https://www.geeksforgeeks.org/python/python-loop-through-folders-and-files-in-directory/