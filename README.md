---
what: Computing Fundamentals for Human(s|ists)
where: University of Victoria, BC
when: June 5-9, 2017
---

[John Simpson](https://twitter.com/symulation)  
[Alicia Cappello](https://twitter.com/aliciavc99)

-_-_-_-_-_ ALL CONTENT IS CURRENTLY UNDER REVISION _-_-_-_-_-

## Class Description

This course is intended for humanities-based researchers who do not have a programming
background, but would like to understand how programs work "behind
the scenes." Over the
week, the emphasis will be on understanding how computer programmers think so
that participants will be able to participate in high-level
conceptual discussions with more confidence. These general
concepts will be reinforced and illustrated with hands-on development of
simple programs that can be used to assist with text-based research and analysis.

The programming language used for most of the course will be Python. Python has an easy-to-learn and 
gentle syntax, and powerful extensions. Use of the command-line interface
and regular expressions will also be demonstrated and emphasized. 

## Learning Outcomes

You should walk away from this course with the following knowledge:
  - Using the command line to automate tasks, manage files and folders, access a remote server, and run Python scripts.
  - Installing and accessing Python via multiple platforms for the purpose of code development and execution.
  - Thinking like a computer science in order to map out your code and its structure in advance of writing scripts.
  - Understanding of the Python 3.x programming language, including the ability to write simple scripts for use in data analysis.

## Reading Material



## Before Day 1

Before attending this course, you may wish to install the following items on your laptop:

  1. MobaXterm - Is only needed for Windows users. This program provides a command link or terminal window for you to use when we go through the material on Day 1. You may also find it useful to continue using MobaXterm as you write various Python scripts throughout the weeek. You can download a free version of the software here -> http://mobaxterm.mobatek.net/download.html.

  2. Anaconda - Will be required for users of all operating systems. Anaconda is an open data science platform that is powered by Python. In addition to being able to write Python scripts, Anaconda also contains hundreds of packages that are either pre-installed or can be easily downloaded and used with Python. You can download a free version of Anaconda here -> https://www.continuum.io/downloads. Make sure to download version 3.x.
 
## Day 1: Shell (4.5 hrs)

We will spend the day working with the terminal, learning the basics of the
file system, data flow programming, and text manipulation. The goal is to get
comfortable with the conversational, call and response style of programming.

- 1.1 Welcome
  - 1.1.1 Introductions & Resources
  - [1.1.2](https://github.com/xpmethod-workshops/dhsi-coding-fundamentals/blob/master/book-chapter/main.md#1-critical-computing-principles) Course Philosophy
  - [1.1.3](https://github.com/xpmethod-workshops/dhsi-coding-fundamentals/blob/master/book-chapter/main.md#2-digital-humanities-core) DH Core
  - 1.1.4 Goals & Schedule
  - [1.1.5](https://github.com/dh-notes/dhnotes/blob/master/tutorials/command-line/000-cli.md) Why the command
    line?

| When to use Shell?                | When to use Python       |
------------------------------------|--------------------------|
| - automate daily tasks            | - data science           |
| - manage files & folders          | - app development        |
| - remote server admin             | - NLTK                   |
| - data munging                    | - data visualization     |
| - quick & dirty text manipulation | - glue code              |
|                                   | - everything else        |

- 1.2 Introduction to the Shell
  - [1.2.1](https://github.com/dh-notes/dhnotes/blob/master/tutorials/command-line/100-plain-text.md)
    Conversing in Plain Text
  - [1.2.2](https://github.com/dh-notes/dhnotes/blob/master/tutorials/command-line/101-gps.md)
    Finding your way
  - [1.2.3](https://github.com/dh-notes/dhnotes/blob/master/tutorials/command-line/102-files.md)
    Files, Paths, & Folders
  - [1.2.4](https://github.com/dh-notes/dhnotes/blob/master/tutorials/command-line/104-pipes.md)
    Pipes and redirects
  - [1.2.5](https://github.com/dh-notes/dhnotes/blob/master/tutorials/command-line/106-filters.md)
    Filters
  - [1.2.7](https://github.com/dh-notes/dhnotes/blob/master/tutorials/command-line/109-text.md)
    Basic Text Manipulation

- 1.3 Coding with John: [Hunting the Whale](https://github.com/xpmethod-workshops/dhsi-coding-fundamentals/blob/master/CLI/CommandLineWalkThrough.md)  
- 1.4 Simple Scripting and Regular Expressions

- 1.5 Code Review: [Prosecheck](https://github.com/xpmethod/prosecheck)

- 1.6 Concluding Remarks & Preparing for Tomorrow
  
  Tomorrow we'll be focusing on coding in Python. We'll be using both the command line to do this, and Jupyter Notebooks, which is included in Anaconda. In order to be prepared, please make sure you have the following items installed on your laptop:

  - 1. Python - Comes pre-installed on macOS and Linux platforms, so no additional downloads are required. For Windows users, you will need to install a Plugin for MobaXterm. Go to the following URL -> http://mobaxterm.mobatek.net/plugins.html <- click on the Python plugin (listed in alphabetical order) and download the plugin to your computer. Once the plugin is downloaded, move the file to the same folder where the MobaXterm executable file is located. The executable will have the following name -> mobaxterm.exe <- search for its location on your laptop if you aren't sure where MobaXterm was installed.

  - 2. Anaconda - You may have already installed Anaconda before this course began. If you didn't install it, please do so tonight. You can find the free download at -> https://www.continuum.io/downloads. Make sure to download version 3.x.
  
  - 3. Text Editor - Most operating systems come pre-installed with at least one version of a text editor. However, "real programmers" tend to like to use more complex text editors that are designed to work with programming languages. There are a lot of options to use, as you can see from this list -> https://en.wikipedia.org/wiki/List_of_text_editors. If you're unsure which text editor to download, start with Sublime Text.
      - Sublime Text -> https://www.sublimetext.com/3
      - BBEdit -> http://www.barebones.com/products/bbedit/
      - Atom -> https://atom.io

## Day 2: Python I (6 hrs)

- 2.1 Python Programming for Everyone

test test test

- 2.2 Getting Help

- 2.3 Preparing for Tomorrow

    Tomorrow we'll start the day by writing a script that will determine a user's Chinese Zodiac sign after they have entered their year of their birth. A script or program like this will require the use of many of the things we learned today. We will use the following input file -> TBD <- to determine which Chinese Zodiac signs go with which years. Think about how we might approach this tonight and come prepared tomorrow to share your ideas.

## Day 3: Python II (6hr)

- 2.2 Coding with John: [Zodiac](https://github.com/xpmethod-workshops/dhsi-coding-fundamentals/tree/master/python-live-code/zodiac).  We will be using the shell and a text editor for this session.  If you are using windows then it will make sense to use the command prompt rather than MobaXterm because it will give you easier access to the Anaconda installs of Python.  You can use many of your Bash Shell commands in the Windows Command Prompt but you'll find a crash course [HERE](http://www.cs.princeton.edu/courses/archive/spr05/cos126/cmd-prompt.html).

- 2.3 Code Review:
[RikersBot](https://github.com/xpmethod/rikersbot/blob/master/rikersbot.py)

- 2.4 Code Annotation/Templates.  [Version with small data files]() (98.7MB, GitHub). [Version with full data files](https://owncloud.westgrid.ca/index.php/s/V3OkC0uCbTU20Oh) (2.4GB, Compute Canada's OwnCloud)

- 3.1 Lab: Essay Grader Handout

- 3.2 Thinking Like a Programmer: From Comments to Code

- 3.3 Project brainstorm and initial planning

We will complete any remaining steps from the Zodiac tool demo and then move
to an activity where the participants are given working code examples and
asked to add comments to these.  This exercise will help participants
understand the structure of programs better while underscoring the importance
of commenting code in the first place.

Today we will also move from a command line + text editor environment for
programming to the Jupyter Notebook environment that is provided within the
Anaconda install.

In the afternoon participants will begin planning their project for Day four
and five.

## Day 4: Individual Projects (6hr)

The bulk of today will be spent by participants in teams developing the
projects that they began planning the day before. Participants will also be
introduced to an *Integrated Development Environment (IDE)*, so there will be
three options for how to develop a program:

1. Command line + text editor
2. Jupyter notebooks
3. [PyCharm](https://www.jetbrains.com/pycharm/) (a Python specific IDE)

There is no wrong answer here. Try to choose tools that are 
[FOSS](http://en.wikipedia.org/wiki/Free_and_open-source_software), universal, and
extensible.

- 1hr write a short 1-2 paragraph description of your project. Concentrate on
the goals of the *what* you are trying to accomplish, not the technical
details. Spend some time discussing what tools and datasets you would need for
the project. For example a simple project description may be:

> Using Python NLTK, our group would like to build an "essay grader" which
> would take as its input a sample essay and output a score, based on several
> parameters like sentence length variation and richness of vocabulary.

- 1hr translate or "formalize" your goals into a series of step by step
instructions in pseudocode.

- project work for the rest of the day

## Day 5: Race to Finish (3h)

**9:30 - 11:30am**

Reevaluate the scope of your project. Cut out inessential functionality. We are 
trying to get to a "minimally viable" prototype stage. Take notes via code comments 
throughout.

**11:3 - noon**

Concluding remarks. Showcase and Plenary meeting after.

## Project Code Share

Projects will go here.

## Next Steps

- [What a well-informed person ought to know
about computers and communications](http://dl.acm.org/citation.cfm?id=2380975) by Brian Kirnighan
- [Data Science at the Command Line](http://datascienceatthecommandline.com/) by Jeroen Jannsens
- [DH Notes](https://github.com/denten/dhnotes/wiki)
- [Digital Humanities Research Portal](https://www.computecanada.ca/research-portal/digital-humanities-working-group/), Compute Canada
- [Foundations of Statistical Natural Language Processing](http://nlp.stanford.edu/fsnlp/) by Chris Manning and Hinrich Schütze
- [Natural Language Processing with Python](http://www.nltk.org/book/) by  Steven Bird, Ewan Klein, and Edward Loper
- [CODE
The Hidden Language of Computer Hardware and Software](http://www.charlespetzold.com/code/) by Charles Petzold 
- [Project Jupyter](https://github.com/jupyter)
- [PyLadies](https://github.com/pyladies)
- [Python Software Foundation](https://www.python.org/psf/)
- [The Programming Historian](http://http://programminghistorian.org)
- [Think Python: How to Think Like a Computer Scientist](by Allen B. Downey) by Allen B. Downey

[1]: https://piazza.com/class/ia5h507lfcr47d 

[2]: https://github.com/denten-workshops/dh-core 

[3]: https://github.com/denten/dhnotes/wiki
