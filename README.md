# ECE230

## Introduction

This repository contains all ECE 230 Labs taught at Duke University as of Spring 2020.

Lab manuals were originally written in Microsoft Word by several different authors. 

Conversion from Word to LaTeX was done by Januario Carreiro.

## Instructions

`manual.cls` must be in a parent directory to the Lab folders for the LaTeX documents to compile. Compile LaTeX using 

```
pdflatex [filename].tex
```

You may have to compile 3 times in order for the Table of Contents and List of Figures to be populated with correct content.

To get a seperate file containing only the grading rubric, use

```
python splitGradingRubric.py
```

You may have to run `pip install PyPDF2` if you do not have PyPDF2 already installed.

