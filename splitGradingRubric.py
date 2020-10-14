#!/usr/bin/env python3

# author: Januario Carreiro
# date: 19 March 2020

import sys
import argparse
from PyPDF2 import PdfFileReader, PdfFileWriter


def getGradingRubric(first, last, path=None):
    """Returns the grading rubric for labs first through last."""
    if path is not None:
        file = path.split(".")

        try:
            with open(path, 'rb') as infile:
                reader = PdfFileReader(infile)
                writer = PdfFileWriter()
                writer.addPage(reader.getPage(-1))

                with open(file[0] + 'Rubric.pdf', 'wb') as outfile:
                    writer.write(outfile)
        except FileNotFoundError:
            print(path + ' does not exist')
    else:
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
    
def getArguments():
    parser = argparse.ArgumentParser(
        prog="splitGradingRubric",
        description="Creates new PDF of only the lab's grading rubric",
        usage="\n".join([
            "\tgenerate all grading rubrics: splitGradingRubric.py",
            "\tgenerate grading rubric for singular lab n: splitGradingRubric.py -n n",
            "\tgenerate grading rubric for lab with relative path p: splitGradingRubric.py --path p"
        ])
    )

    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('-n', nargs=1, type=int, help="Generates rubric for lab labNum")
    group.add_argument('--path', nargs=1, type=str, help="Generate rubric for lab with path labPath")

    return parser.parse_args()

if __name__ == '__main__':
    args = getArguments()
    print(args)
    if args.path:
        getGradingRubric(0,0,args.path[0])
    elif args.n:
        lab = args.n[0]
        if lab < 1 or lab > 7:
            print("only labs 1-7 have grading rubrics")
        else:
            getGradingRubric(lab, lab + 1)
    else:
        getGradingRubric(1, 8)
