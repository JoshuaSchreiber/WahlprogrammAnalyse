import json


class Partei:
    def __init__(self, name, wahlprogrammLoc):
        self.name = name
        self.wahlprogrammLoc = wahlprogrammLoc
        self.wahlprogramm = self.read_Wahlprogramm()
        self.haufigsteWorter = self.haufigsteWorter()

    def haufigsteWorter(self):
        h = HaeufigeWoerter();

        return "Pup"

    def read_from_txt(self, filename):
        content = None;
        try:
            with open(filename, 'r') as file:
                content = file.read()
        except FileNotFoundError:
            print(f"The file {filename} does not exist.")
        return content;

    def read_Wahlprogramm(self):
        content = None;
        try:
            with open(self.wahlprogrammLoc, 'r') as file:
                content = file.read()
        except FileNotFoundError:
            print(f"The file {self.wahlprogrammLoc} does not exist.")
        return content;

    def save_to_txt(self, filename, content):
        with open(filename, 'w') as file:
            file.write(content)

    def save_Data_to_json(self, json_filename):
        data = {
            'name': self.name,
            'wahlProgrammLoc': self.wahlprogrammLoc
        }
        with open(json_filename, 'w') as json_file:
            json.dump(data, json_file)
