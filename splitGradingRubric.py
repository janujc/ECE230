# author: Januario Carreiro
# date: 19 March 2020

import sys
from PyPDF2 import PdfFileReader, PdfFileWriter


def getGradingRubric(first, last):
    """Returns the grading rubric for labs first through last."""
    for i in range(first, last):
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


if __name__ == '__main__':
    if len(sys.argv) == 1:
        getGradingRubric(1, 8)
    elif len(sys.argv) == 2:
        lab = int(sys.argv[1])
        if lab < 1 or lab > 7:
            print("only labs 1-7 have grading rubrics")
        else:
            getGradingRubric(lab, lab + 1)
    else:
        print("splitGradingRubric only accepts 0 or 1 arguments")
