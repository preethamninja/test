import os
from PyPDF2 import PdfFileReader, PdfFileWriter



path = "D:/webprojects/projecttest/python/book1-exercises-master/chp11/practice_files"

input_file_name = os.path.join(path,"The Emperor.pdf")
input_file = PdfFileReader(open(input_file_name,"rb"))
output_pdf = PdfFileWriter()

cover_file_name = os.path.join(path, "Emperor cover sheet.pdf")
cover_file = PdfFileReader(open(cover_file_name, "rb"))

output_pdf = PdfFileWriter()


cover_page = cover_file.getPage(0)
output_pdf.addPage(cover_page)

for pagenum in range(0, input_file.getNumPages()):
	page = input_file.getPage(pagenum)
	output_pdf.addPage(page)

output_file_name = os.path.join(path, "output/EmperorCombined.pdf")
output_file = open(output_file_name, "wb")

output_pdf.write(output_file)
output_file.close()