#!/usr/bin/env python3

import PyPDF2
import json

def getTextFromPdf():
  filename = input("Gimme the file name:\n>")

  with open(filename, 'rb') as pdf_file:
      pdf_reader  = PyPDF2.PdfReader(pdf_file)

      text_list = []

      for i in range(10, len(pdf_reader.pages)):
        #  page = pdf_reader.getPage(page_num)
          text = pdf_reader.pages[i].extract_text()
          text_list.append(text)

      data = {}
      lines = ''.join(text_list)
      lines = lines[lines.find("\n1000"):lines.find("\nThe economic table")]
      lines = lines.replace("WSCSS- Economic Table 01/2019", "").replace("  ", " ").replace('\n \n \n ','').replace('\n ', '\n').replace('\n\n', '\n').replace(" \n", '\n').replace('\n\n', '\n')
    #   print(lines)
      lines = lines.split('\n')
      for line in lines:
          if line:
            line = line.split(' ')
            # print(line)
            data[line[0]] = {
                "1": line[1],
                "2": line[2],
                "3": line[3],
                "4": line[4],
                "5": line[5]
            }
      with open(f'{filename}.json', 'w') as json_file:
          json.dump(data, json_file, indent=4)

def main():
    getTextFromPdf()

if __name__ == "__main__":
    main()
