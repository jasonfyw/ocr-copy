import argparse

from ocrcopy.controller import Controller

def main():
    parser = argparse.ArgumentParser(description = "A program that uses OCR to copy text from a screen selection")
    parser.add_argument('-l', nargs = '?', const = 'eng+ara+chi-sim+rus+ell+jpn+hin', default = 'eng', help = 'Languages to be checked for by the OCR engine, separated by "+". Available language codes at https://github.com/tesseract-ocr/tessdata. See README for more details')

    args = parser.parse_args()

    ocrcopy = Controller(args.l)

if __name__ == "__main__":
    main()