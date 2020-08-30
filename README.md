# ECE230

## Introduction

This repository contains all ECE 230 Labs taught at Duke University as of Spring 2020.

Lab manuals were originally written in Microsoft Word by several different authors. 

Conversion from Word to LaTeX was done by Januario Carreiro.

## Instructions

You must have a LaTeX distribution installed in order to compile LaTeX documents. If you do not already have a distribution, consider [MiKTeX](https://miktex.org/download).

Note that `manual.cls` must be in a parent directory to the Lab folders for the LaTeX documents to compile. In other words, do not modify the file structure. Compile LaTeX using 

```shell
pdflatex [filename].tex
```

You may have to compile 3 times in order for the Table of Contents and List of Figures to be populated with correct content.

In order to create a separate grading rubric file for each Lab manual, use

```shell
python splitGradingRubric.py
```

You can also specify to split the grading rubric of only a specific file, say Lab4.pdf, by using

```
python splitGradingRubric.py 4
```

You may have to run `pip install PyPDF2` if you do not have PyPDF2 already installed.