# author: Januario Carreiro
# date: 8 Feb 2020

from PyPDF2 import PdfFileReader, PdfFileWriter

for i in range(1,8) :
	filename = 'Lab' + str(i)
	filepath = filename + '/' + filename

	try:
		with open(filepath + '.pdf', 'rb') as infile:
			reader = PdfFileReader(infile)
			writer = PdfFileWriter()
			writer.addPage(reader.getPage(-1))

			with open(filepath + 'Rubric.pdf', 'wb') as outfile:
				writer.write(outfile)
	except FileNotFoundError:
		print(filename + '.pdf does not exist')