from urllib.parse import urlparse
import logging
import yaml
import pickle
import urllib.request
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import os
from collections import Counter
from tld import get_tld
import tkinter as tk
from database import select_from_db
import argparse


def parse_tagcounter_args():
    """Create the arguments parser, adds 2 arguments."""
    # create the arguments parser
    my_parser = argparse.ArgumentParser(prog='tagcounter', description='Count tags of an html-file')
    # add the --get argument
    my_parser.add_argument('--get', type=str, help='get tags and their counts')
    # add the --view argument
    my_parser.add_argument('--view', help='fetch data from the database')
    # execute the parse_args() methodte

    return my_parser.parse_args()


def add_protocol_to_url(url):
    """Add http:// protocol to url."""
    if not urlparse(url).scheme:
        url = 'http://' + url

    return url


def parse_yaml_file():
    """Parse yaml-file."""
    # move up directory to find synonyms.yaml
    path = os.path.abspath((os.path.dirname(os.getcwd()) + '\\synonyms.yaml'))
    a_yaml_file = open(path, 'r', encoding="utf8")
    parsed_yaml_file = yaml.load(a_yaml_file, Loader=yaml.FullLoader)

    return parsed_yaml_file


def get_synonym(url):
    """Check if synonym exists in synonyms.yaml, then use it to build an object."""
    synonyms = parse_yaml_file()

    return synonyms.get(url, url)  # returns value or default value if doesn't exist in yaml file


def get_domain_site_by_url(url):
    """Extract 2nd level domain name: 'google'."""
    site = get_tld(url, as_object=True)
    domain = site.domain

    return domain


def pickle_tag_dict(tag_dict):
    """Pickle the Python object: convert the dictionary into a byte stream"""
    pickled_tag_dict = pickle.dumps(tag_dict, protocol=None, fix_imports=True)

    return pickled_tag_dict


def unpickle_db_results(results):
    """Unpickle results from DB."""
    unpickled_list = pickle.loads(results, fix_imports=True,
                                  encoding="ASCII", errors="strict",
                                  buffers=None)

    return unpickled_list


class CountTags:

    def __init__(self, url):
        self.url = url
        self.arquivos = []
        self.tags = []

    def count_tags(self):
        """Count tags of a webpage."""
        url = add_protocol_to_url(self.url)      # add protocol to url if needed
        logging.info(url)                        # use declared url variable
        response = urllib.request.urlopen(url)   # download html content: request - response
        web_content = response.read()
        f = open('webpage.html', 'wb')           # write to a file
        f.write(web_content)
        f.close

        class MyHTMLParser(HTMLParser):

            def handle_starttag(self, tag, attrs):
                count.append(tag)

            def handle_endtag(self, tag):
                count.append(tag)

        parser = MyHTMLParser()

        for file in os.listdir(path=os.getcwd()):
            if file.endswith(".html"):
                self.arquivos.append(file)
                path = os.getcwd() + "\\" + file
                doc = open(path, "r", encoding="utf8")
                soup = BeautifulSoup(doc, 'html.parser')
                count = []
                parser.feed(soup.prettify())
                self.tags.append(count)

        z = []                                 # list with the collections.Counter Object

        for i, item in enumerate(self.tags):
            z.append(Counter(self.tags[i]))

        tag_dict = dict(z[0])                  # list with the collections.Counter Object to a dict

        return tag_dict


class GuiWindow:
    def start(self):
        window = tk.Tk()
        window.title("Welcome to Tagcounter!")
        window.geometry('600x450')
        text = tk.Label(window, text="Enter url, please")
        text.grid(column=1,
                  row=0,
                  columnspan=2,
                  sticky=tk.E,
                  pady=10,
                  padx=10)
        self.txt = tk.Entry(window, width=30)
        self.txt.focus()
        self.txt.grid(column=3,
                      row=0,
                      columnspan=2,
                      sticky=tk.W+tk.E,
                      pady=10,
                      padx=10)
        self.output = tk.Text(window, height=10, width=45)
        self.output.grid(column=2, row=4, columnspan=3, pady=10, padx=10)
        scroll = tk.Scrollbar(command=self.output.yview)
        scroll.grid(column=5, row=4)
        self.output.config(yscrollcommand=scroll.set)
        self.statusbar = tk.Label(window,
                                  text="waiting for the url…",
                                  bd=1, relief=tk.SUNKEN,
                                  anchor=tk.W)
        self.statusbar.grid(column=0,
                            row=6,
                            columnspan=5,
                            sticky=tk.W+tk.E,
                            pady=10,
                            padx=10)
        btn_internet = tk.Button(window,
                                 text="Download From Internet",
                                 command=self.load_from_internet)
        btn_internet.grid(column=4, row=3, padx=10, pady=10, sticky=tk.E)
        btn_db = tk.Button(window, text="Show From DB", command=self.load_from_db)
        btn_db.grid(column=3, row=3, sticky=tk.W, pady=10, padx=10)
        window.mainloop()

    def load_from_db(self):
        gui_user_input = self.txt.get()
        gui_user_input = get_synonym(gui_user_input)               # check synonym in yaml file
        gui_full_url = add_protocol_to_url(gui_user_input)         # add protocol to url
        gui_results = select_from_db(gui_full_url)                 # select from DB
        gui_unpickled_result = unpickle_db_results(gui_results)    # unpickle results
        self.output.delete(1.0, tk.END)                            # clean output box before insert
        # create output
        result_load_from_db = "{}: ".format(self.txt.get()) + str(gui_unpickled_result)
        self.output.insert(tk.END, result_load_from_db)              # insert output to the textbox
        self.statusbar.configure(text="I've counted tags for you!")  # update status bar

    def load_from_internet(self):
        gui_user_input_inet = self.txt.get()
        gui_user_input_inet = get_synonym(gui_user_input_inet)
        count_tags_gui = CountTags(gui_user_input_inet)
        gui_tagcount_dict = count_tags_gui.count_tags()
        result_load_from_internet = "{}: ".format(self.txt.get()) + str(gui_tagcount_dict)
        self.output.delete(1.0, tk.END)                             # clean output box before insert
        self.output.insert(tk.END, result_load_from_internet)
        self.statusbar.configure(text="I've counted tags for you!")
