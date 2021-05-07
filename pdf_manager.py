# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import sys
import time
from os import listdir
from os.path import isfile, join


def process_directory(input_path: str, output_path: str):
    filenames = [f for f in listdir(input_path) if isfile(join(input_path, f))]
    if len(filenames) > 0:
        for filename in filenames:
            if filename.endswith(".pdf"):
                print("Starting OCR for Document " + filename)
                command = f"ocrmypdf -l deu+eng --rotate-pages --deskew {input_path + filename} {output_path + filename}"
                print(command)
                os.system(command)
                print("Deleting the Document " + filename)
                os.system(f"rm {input_path + filename}")
            else:
                print("Found the Document " + filename + "but it has the wrong file-ending")
        print("Waiting for more documents...")


def main():
    while True:
        process_directory(sys.argv[1],sys.argv[2])
        time.sleep(5)


if __name__ == '__main__':
    main()

