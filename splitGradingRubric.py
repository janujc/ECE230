from PyPDF2 import PdfFileReader, PdfFileWriter

for i in range(1,8) :
	filename = "Lab" + str(i)
	filepath = filename + "/" + filename

	with open(filepath + ".pdf", 'rb') as infile:
		reader = PdfFileReader(infile)
		writer = PdfFileWriter()
		writer.addPage(reader.getPage(-1))

		with open(filepath + "Rubric.pdf", 'wb') as outfile:
			writer.write(outfile)