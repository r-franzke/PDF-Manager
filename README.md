# PDF Manager
A simple script, that looks for PDFs in an Input directory. 
The software [OCRmyPDF ](https://github.com/jbarlow83/OCRmyPDF) will be used to optimice the dokument and moves it to the output Directory.
After that the file in the input Dir will be deleted.

## Usuage
1. Install OCRmyPDF for the languages english and german. Instructions can be found [here](https://ocrmypdf.readthedocs.io/en/latest/installation.html).
2. Run `python pdf_manager.py <input_dir> <output_dir>`