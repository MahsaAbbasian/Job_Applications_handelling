from docx import Document
from typing import Dict, List
import json


def extract_info_from_cv(cv_file_path: str) -> Dict[str, List[str]]:
    sections = {
        "Objective": [],
        "Experience": [],
        "Skills": [],
        "Languages": [],
        "Education": [],
        "References": [],
        "Contact Information": []
    }

    current_section = None

    document = Document(cv_file_path)
    for paragraph in document.paragraphs:
        line = paragraph.text.strip()

        if not line:
            continue

        if line.endswith(":"):
            current_section = line[:-1]
        elif current_section is not None:
            sections[current_section].append(line)
        else:
            # If current_section is None, add the line to a default section
            sections["Objective"].append(line)

    return sections


if __name__ == "__main__":
    cv_file_path = r"c:/Users/AUTSAMO/Desktop/job application/cvFile/cvChangeFormat.docx"
    extracted_info = extract_info_from_cv(cv_file_path)

    print("Extracted information from CV:")
    for section, content in extracted_info.items():
        print(f"{section}: {content}")

    # Convert the dictionary to JSON
    json_data = json.dumps(extracted_info)

    # Print the JSON data
    print(json_data)
