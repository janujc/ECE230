\ProvidesClass{manual}[30/10/2019]

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax
\LoadClass{article}

\RequirePackage[letterpaper, margin=1.0in]{geometry}
\RequirePackage{appendix}
\RequirePackage[utf8]{inputenc}
\RequirePackage[T1]{fontenc}
\RequirePackage{newtxtext}
\RequirePackage{newtxmath}
\RequirePackage{siunitx}
\RequirePackage{caption}
\RequirePackage{moreverb}
\RequirePackage{parskip}
\RequirePackage{multirow}
\RequirePackage{adjustbox}
\RequirePackage{enumerate}
\RequirePackage{listings}
\RequirePackage{graphicx}
\RequirePackage{pdfpages}
\RequirePackage[american,straightlabels]{circuitikz}
\RequirePackage{fancyhdr}
\RequirePackage[explicit]{titlesec}
\RequirePackage{xcolor}
\RequirePackage[many]{tcolorbox}
\RequirePackage{eqparbox}
\RequirePackage{hyperref}

\hypersetup{
    colorlinks=true,
    linkcolor=black,
    filecolor=magenta,      
    urlcolor=blue,
}

\titleformat{name=\section}{\large\bfseries}{}{0pt}{\begin{tcolorbox}[nobeforeafter, boxrule=0.5mm, colframe=black]\thesection\hskip1em#1\end{tcolorbox}}

\titleformat{name=\section,numberless}{\large\bfseries}{}{0pt}{\begin{tcolorbox}[nobeforeafter, boxrule=0.5mm, colframe=black]#1\end{tcolorbox}}

\titleformat{name=\subsection}{\large\bfseries}{}{0pt}{\hskip1.5em\begin{tcolorbox}[nobeforeafter, boxrule=0.5mm, colframe=black, hbox]\thesubsection\hskip1em#1\end{tcolorbox}}

\titleformat{name=\subsection,numberless}{\large\bfseries}{}{0pt}{\hskip1.5em\begin{tcolorbox}[nobeforeafter, boxrule=0.5mm, colframe=black, hbox]#1\end{tcolorbox}}

\titleformat{name=\subsubsection}{\large\bfseries}{}{0pt}{\hskip3em\begin{tcolorbox}[nobeforeafter, boxrule=0.5mm, colframe=black, hbox]\thesubsubsection\end{tcolorbox} \hskip1em\raisebox{0.7\height}{#1}}

\newtcolorbox[blend into=figures]{myfigure}[3][]{enhanced, float=htb!, colframe=black, colbacktitle=black, capture=hbox, blend before title=colon, attach boxed title to bottom, list text={#2}, title={#3}, every float=\centering,#1}

\setlength{\parindent}{0 cm}
\setlength{\headheight}{14.5pt}

\pagestyle{fancy}

\renewcommand{\headrulewidth}{0.5mm}
\renewcommand{\footrulewidth}{0.5mm}

\newcommand{\makeheader}[2]{ % Takes arguments {Lab #} and {Semester Year}
	\fancyhead[L]{\textbf{ECE230L}}
	\fancyhead[R]{\textbf{#2}}
	\fancyfoot[L]{\textbf{ECE230L Lab Manual}}
	\fancyfoot[C]{\textbf{#1}}
	\fancyfoot[R]{\textbf{Page \thepage}}
}

\newcommand{\incfig}[1]{
    \def\svgwidth{\columnwidth}
    \import{./figures/}{#1.pdf_tex}
}

\def\arraystretch{1.5}
