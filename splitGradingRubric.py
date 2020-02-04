from PyPDF2 import PdfFileReader, PdfFileWriter

filename = input("Filename: ")

filepath = filename + "/" + filename + ".pdf"
filepathOut = filename + "/" + filename + "Rubric.pdf"

with open(filepath, 'rb') as infile:
	reader = PdfFileReader(infile)
	writer = PdfFileWriter()
	writer.addPage(reader.getPage(-1))

	with open(filepathOut, 'wb') as outfile:
		writer.write(outfile)