from num2words import num2words
import string
import re
import os
from pdfminer.high_level import extract_text

def replace_digits_with_words(text):
    processed_text = ""
    for character in text:
        if character.isnumeric():
            processed_text += num2words(character)
        else:
            processed_text += character
    return processed_text

def replace_numbers_with_words(text):
    processed_text = ""
    pointer = 0
    while pointer != len(text):
        if text[pointer].isnumeric():
            num_substring = ""
            while(text[pointer].isnumeric()):
                num_substring += text[pointer]
                pointer += 1
            processed_text += num2words(num_substring)
        else:
            processed_text += text[pointer]
            pointer += 1
    return processed_text

transcript_dir = input("transcript directory: ")
output_dir = input("output directory: ")
files = list()
for file in os.listdir(transcript_dir):
    if file.endswith(".pdf"):
        files.append(file)
for file in files:
    file_name = file.split(".")[0]
    raw_text = extract_text(transcript_dir + "/" + file)
    preprocessed_text = raw_text.lower()
    preprocessed_text = re.sub(".+\\n","", preprocessed_text,count=6)
    preprocessed_text = re.sub("\\n\\n","\n", preprocessed_text)
    preprocessed_text = re.sub("\\(.+\\)","\n", preprocessed_text)
    preprocessed_text = replace_numbers_with_words(preprocessed_text)
    for punctuation in string.punctuation:
        preprocessed_text = preprocessed_text.replace(punctuation, ' ')

    output_file = open(output_dir + "/" + file_name + ".txt","w")
    output_file.write(preprocessed_text)
    output_file.close()
