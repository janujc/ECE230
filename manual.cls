\ProvidesClass{manual}[30/10/2019]

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax
\LoadClass[twoside]{article}

\RequirePackage[letterpaper, margin=1.0in]{geometry}
\RequirePackage{appendix}
\RequirePackage[utf8]{inputenc}
\RequirePackage[T1]{fontenc}
\RequirePackage{siunitx}
\RequirePackage{mathtools,amssymb}
\RequirePackage{caption}
\RequirePackage{moreverb}
\RequirePackage{parskip}
\RequirePackage{array}
\RequirePackage{multirow}
\RequirePackage{enumerate}
\RequirePackage{graphicx}
\RequirePackage{xcolor}
\RequirePackage[american,straightlabels]{circuitikz}
\RequirePackage{fancyhdr}
\RequirePackage[explicit]{titlesec}
\RequirePackage{hyperref}

\hypersetup{
    colorlinks=true,
    linkcolor=black,
    filecolor=magenta,      
    urlcolor=blue,
}

\setlength{\parindent}{0 cm}
\setlength{\headheight}{14.5pt}

\pagestyle{fancy}

\renewcommand{\headrulewidth}{0.5mm}
\renewcommand{\footrulewidth}{0.5mm}

\newcommand{\makeheader}[1]{ % Takes arguments {Lab #} and {Semester Year}
	\fancyhead[L]{ECE230L}
	\fancyhead[C]{}
	\fancyhead[R]{Duke University}
	\fancyfoot[L]{Lab Manual}
	\fancyfoot[C]{#1}
	\fancyfoot[R]{Page \thepage}
}

\newcommand{\incfig}[1]{
    \def\svgwidth{\columnwidth}
    \import{./figures/}{#1.pdf_tex}
}

\def\arraystretch{1.5}
