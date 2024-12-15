import pandas as pd
import chardet

file_path = '/Users/student/Desktop/CourseFinderPython/Course_class_F23_Alok_9.18.23.csv'

with open(file_path, 'rb') as file:
    raw_data = file.read()
encoding_info = chardet.detect(raw_data)
detected_encoding = encoding_info['encoding']

try:
    csv_data = pd.read_csv(file_path, encoding=detected_encoding)
    txt_content = csv_data.to_string(index=False)
    txt_file_path = '/path/to/your/output.txt'
    with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(txt_content)
    print(f"Plain text file saved at: {txt_file_path}")
except Exception as e:
    with open(file_path, 'r', errors='ignore') as file:
        raw_content = file.readlines()
    raw_txt_file_path = '/path/to/your/raw_output.txt'
    with open(raw_txt_file_path, 'w', encoding='utf-8') as raw_txt_file:
        raw_txt_file.writelines(raw_content)
    print(f"Raw text file saved at: {raw_txt_file_path}")
