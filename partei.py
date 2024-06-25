import json
import re
from collections import Counter
from itertools import islice

class Partei:
    def __init__(self, name="", wahlprogrammLoc="", wordCount=0, haeufigsteWoerter=None, dreiGramme=None, vierGramme=None, fuenfGramme=None):
        self._name = name
        self._wahlprogrammLoc = wahlprogrammLoc
        self._wahlprogramm = self.read_Wahlprogramm()
        self._haeufigsteWoerter = haeufigsteWoerter if haeufigsteWoerter is not None else []
        self._3Gramme = dreiGramme if dreiGramme is not None else []
        self._4Gramme = vierGramme if vierGramme is not None else []
        self._5Gramme = fuenfGramme if fuenfGramme is not None else []
        self._wordCount = wordCount

    # Getter and setter for name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # Getter and setter for wahlprogrammLoc
    @property
    def wahlprogrammLoc(self):
        return self._wahlprogrammLoc

    @wahlprogrammLoc.setter
    def wahlprogrammLoc(self, value):
        self._wahlprogrammLoc = value
        self._wahlprogramm = self.read_Wahlprogramm()  # Refresh the wahlprogramm when location changes

    # Getter for wahlprogramm (no setter, as it's read-only based on wahlprogrammLoc)
    @property
    def wahlprogramm(self):
        return self._wahlprogramm

    # Getter and setter for haeufigsteWoerter
    @property
    def haeufigsteWoerter(self):
        return self._haeufigsteWoerter

    @haeufigsteWoerter.setter
    def haeufigsteWoerter(self, value):
        self._haeufigsteWoerter = value

    # Getter and setter for dreiGramme
    @property
    def dreiGramme(self):
        return self._dreiGramme

    @dreiGramme.setter
    def dreiGramme(self, value):
        self._dreiGramme = value

    # Getter and setter for vierGramme
    @property
    def vierGramme(self):
        return self._vierGramme

    @vierGramme.setter
    def vierGramme(self, value):
        self._vierGramme = value

    # Getter and setter for fuenfGramme
    @property
    def fuenfGramme(self):
        return self._fuenfGramme

    @fuenfGramme.setter
    def fuenfGramme(self, value):
        self._fuenfGramme = value

    # Getter and setter for wordCount
    @property
    def wordCount(self):
        return self._wordCount

    @wordCount.setter
    def wordCount(self, value):
        self._wordCount = value

    def read_from_txt(self, filename):
        content = None
        try:
            with open(filename, 'r') as file:
                content = file.read()
        except FileNotFoundError:
            print(f"The file {filename} does not exist.")
        return content

    def read_Wahlprogramm(self):
        content = None
        try:
            with open(self._wahlprogrammLoc, 'r') as file:
                content = file.read()
        except FileNotFoundError:
            print(f"The file {self._wahlprogrammLoc} does not exist.")
        return content

    def save_to_txt(self, filename, content):
        with open(filename, 'w') as file:
            file.write(content)

    def save_Data_to_json(self, json_filename):
        data = {
            'name': self.name,
            'wahlProgrammLoc': self.wahlprogrammLoc,
            'wordCount': self.wordCount,
            'haeufigsteWoerter': self.haeufigsteWoerter,
            'dreiGramme': self._3Gramme,
            'vierGramme': self._4Gramme,
            'fuenfGramme': self._5Gramme
        }
        with open(json_filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)

