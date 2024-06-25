import pandas as pd
import json

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def extract_data(json_data):
    return {
        "name": json_data["name"],
        "wahlProgrammLoc": json_data["wahlProgrammLoc"],
        "wordCount": json_data["wordCount"],
        "haeufigsteWoerter": json_data["haeufigsteWoerter"],
        "dreiGramme": json_data["dreiGramme"],
        "vierGramme": json_data["vierGramme"],
        "fuenfGramme": json_data["fuenfGramme"]
    }

def create_combined_table(json_files, output_file):
    combined_data = []
    html = []

    for file in json_files:
        json_data = load_json(file)
        extracted_data = extract_data(json_data)
        combined_data.append(extracted_data)

    df = pd.DataFrame(combined_data)
    df.to_json(output_file, orient='records', indent=4)
    df.to_html(output_file.replace('.json', '.html'), index=False)



