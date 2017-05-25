---
what: Computing Fundamentals for Human(s|ists)
where: University of Victoria, BC
when: June 5-9, 2017
---

John Simpson | john.simpson@computecanada.ca | [Twitter](https://twitter.com/symulation)  
Alicia Cappello | cappello@ualberta.ca | [Twitter](https://twitter.com/aliciavc99)

-_-_-_-_-_ Content updated May 22nd, but not complete. _-_-_-_-_-

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

The main book for our course is called *Think Python: How to Think Like a Computer Scientist* by Allen B. Downey. We're using the 2nd Edition, as it was updated for version 3.x of Python. There are four places you can get this book:

  1. Via the coursepak provided by DHSI [here](http://dhsi.org/content/2017Curriculum/4.%20Fundamentals%20of%20Programming:Coding%20for%20Human(s%7Cists).pdf). You can download the coursepak as a PDF and use it on your computer, you can print it yourself, or you can ask the UVic Bookstore to print you a copy. The instructions for getting a copy printed at UVic are in Ray Siemens email dated May 17th, 2017.

  2. Via the book publisher's website [here](http://greenteapress.com/thinkpython2/thinkpython2.pdf). The PDF or ePub versions can be downloaded for free and used on your computer or printed if you'd like.

  3. Via a bookstore like [Amazon.ca](https://www.amazon.ca/Think-Python-Like-Computer-Scientist/dp/1491939362/ref=sr_1_1?ie=UTF8&qid=1495505046&sr=8-1&keywords=think+python) or [Indigo.ca](https://www.chapters.indigo.ca/en-ca/books/think-python-how-to-think/9781491939369-item.html?ikwid=think+python&ikwsec=Home&ikwidx=0) if you prefer a hard copy. 

  4. Via the ProQuest database called [Safari Books Online](https://www.safaribooksonline.com). Most academic libraries should have access to this database, and possibly even some public libraries. To access the database via a library, make sure to sign into your personal library account first, then search for and go to the database. To access it on your own, you can use the link provided [here](https://www.safaribooksonline.com) and sign-up for a personal trial account.

## Before Day 1

On Day 1 of this course we'll be learning how to use the command line (aka., terminal, BASH, shell). macOS and Linux users will already have software installed that will easily allow them to do this, but Windows users need to install some additional software. For the purpose of this course, we'll use software called MobaXterm to mimic the command line on a Windows machine. You can download a FREE version of MobaXterm here -> http://mobaxterm.mobatek.net/download.html.
 
## Day 1: Shell (4.25 hrs)

We will spend the day working with the terminal, learning the basics of the file system, data flow programming, and text manipulation. The goal is to get comfortable with the conversational, call, and response style of programming.

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
  
  Tomorrow we'll be focusing on coding in Python. We'll be using both the command line and Jupyter Notebooks to do this. Jupyter Notebooks is included with the Anaconda software noted below. In order to be prepared for tomorrow, please make sure you have the following items installed on your laptop:

    - 1.6.1. **Python** - Comes pre-installed on macOS and Linux platforms -- no additional downloads required. For Windows users, you will need to install a Plugin for MobaXterm. Go to the following URL -> http://mobaxterm.mobatek.net/plugins.html <- click on the **Python** plugin (listed in alphabetical order) and download the plugin file to your computer. Once the file is downloaded, move it to the same folder where the MobaXterm executable file is located. The executable will have the following name -> mobaxterm.exe. Search for its location on your laptop if you aren't sure where MobaXterm was installed.

    - 1.6.2. **Anaconda** - You may have already installed Anaconda before this course began. If you didn't install it, please do so tonight. You can find the free download at -> https://www.continuum.io/downloads. Make sure to download version 3.x. 
  
    - 1.6.3. **Text Editor** - Most operating systems come pre-installed with at least one version of a text editor. However, "real programmers" tend to like to use more complex text editors that are designed to work with programming languages. There are a lot of options to use, as you can see from this [list](https://en.wikipedia.org/wiki/List_of_text_editors). If you're unsure which text editor to download, start with Sublime Text.
        - Sublime Text -> https://www.sublimetext.com/3
        - BBEdit -> http://www.barebones.com/products/bbedit/
        - Atom -> https://atom.io

## Day 2: Python I (5.5 hrs)

- 2.1 **Python Programming for Everyone**

    - 2.1.1 Why do I need to know how to program?
    - 2.1.2 Variables, Expressions, and Statements
    - 2.1.3 Conditional Expressions, i.e., IF statements
    - 2.1.4 Functions
    - 2.1.5 Iterations and Loops
    - 2.1.6 Strings
    - 2.1.7 Files
    - 2.1.8 Lists
    - 2.1.9 Dictionaries
    - 2.1.10 Tuples
    - 2.1.11 Object-oriented Programming

- 2.2 **Getting Help**

  - 2.2.1 Python.org website
  - 2.2.2 StackExchange
  - 2.2.3 Books
  - 2.2.4 Google
  - 2.2.5 Help Desk (maybe)

- 2.3 **Preparing for Tomorrow**

  Tomorrow we'll start the day by writing a script that will determine a user's Chinese Zodiac sign after they have entered their year of their birth. A script or program like this will require the use of many of the things we learned today. We will use the following input file -> TBD <- to determine which Chinese Zodiac signs go with which years. Think about how we might approach this tonight and come prepared tomorrow to share your ideas.

## Day 3: Python II (5.5 hrs)

- 3.1 [Chinese Zodiac](https://github.com/xpmethod-workshops/dhsi-coding-fundamentals/tree/master/python-live-code/zodiac)

  We will be using the shell and a text editor for this session.  If you are using Windows, it will make sense to use the command prompt rather than MobaXterm because it will give you easier access to the Anaconda installs of Python.  You can use many of your Bash Shell commands in the Windows Command Prompt but you'll find a crash course [HERE](http://www.cs.princeton.edu/courses/archive/spr05/cos126/cmd-prompt.html).


- 3.2 Code Annotation/Templates

  [Version with small data files]() (98.7MB, GitHub). [Version with full data files](https://owncloud.westgrid.ca/index.php/s/V3OkC0uCbTU20Oh) (2.4GB, Compute Canada's OwnCloud)


- 3.3 Individual Projects: Brainstorming and Planning

  Tomorrow you'll get your first crack at your individual projects. Take the time tonight to think about what sort of a project you'd like to take on. If you're having trouble coming up with a project, ask us and we can provide you with some options.


## Day 4: Individual Projects (5.5 hrs)

- 4.1 [**Integrated Development Environments** or IDEs](https://en.wikipedia.org/wiki/Integrated_development_environment)

  In addition to using (a) a text editor and the command line, or (b) Jupyter Notebooks, to write and execute scripts, you can also use an IDE. We'll provide an overview of one IDE, either [PyCharm](https://www.jetbrains.com/pycharm/) or [Spyder](https://pythonhosted.org/spyder/), so you have an idea of the PROs and CONs of each method, then you can choose which option you'd like to use for your project. Just like text editors, there are a lot of IDEs you can choose from, a list of some are compared here -> [https://en.wikipedia.org/wiki/Comparison_of_integrated_development_environments]()

- 4.2 **Describing Your Individual Project**

  - 4.2.1 Write a short description of your individual project, in words. At this point, don't worry about the *how*, just think about the *what*.
  - 4.2.2 Discuss your project with your classmates. Provide feedback to each other, and update your project description if needed.

- 4.3 **Planning Your Individual Project**

  - 4.3.1 What is psuedocode?
  - 4.3.2 Plan the *logic* of your project using step-by-step instructions, with psuedocode, or using a flow chart. At this stage, start to think about the *how*.
  - 4.3.3 Discuss your plan with your classmates. Do they have any suggestions on *how* to implement your project? 

- 4.4 **Coding Your Individual Project**

  - 4.4.1 Decide which software or environment you want to use: text editor, Jupyter Notebooks, or IDE.
  - 4.4.2 Start coding your script by translating your description into comments.
  - 4.4.3 Add the proper syntax to your script by translating your plan and/or pseudocode into Python.

  **If you're using a text editor, don't forget to SAVE once in a while!**

## Day 5: Race to the Finish (3 hrs)

- 5.1 **Continue Working on Your Projects** (1.5 hrs)

- 5.2 **Start Thinking About ...** (1 hr)
  - Was the scope of my project too big or too small?
  - Can I make my code/script more compact, concise, or efficient?
  - Did I add enough comments that a non-programmer can understand what the code does?
  - What do I still need to do? Make a plan to finish your project (if you haven't already done so) after you leave DHSI.

- 5.3 **Finishing Up** (30 mins)
  - Keep working on your projects!
  - Email us if you have questions or need help.
  - Send us your script when you're done, and we'll post it on this website.
  - And most importantly ... have fun!

## Project Code Share

Project scripts will go here.

## Other Resources about Python

- [What a well-informed person ought to know about computers and communications](http://dl.acm.org/citation.cfm?id=2380975) by Brian Kirnighan
- [Data Science at the Command Line](http://datascienceatthecommandline.com/) by Jeroen Jannsens
- [DH Notes](https://github.com/denten/dhnotes/wiki)
- [Digital Humanities Research Portal](https://www.computecanada.ca/research-portal/digital-humanities-working-group/), Compute Canada
- [Foundations of Statistical Natural Language Processing](http://nlp.stanford.edu/fsnlp/) by Chris Manning and Hinrich Schütze
- [Natural Language Processing with Python](http://www.nltk.org/book/) by Steven Bird, Ewan Klein, and Edward Loper
- [CODE: The Hidden Language of Computer Hardware and Software](http://www.charlespetzold.com/code/) by Charles Petzold 
- [Project Jupyter](https://github.com/jupyter)
- [PyLadies](https://github.com/pyladies)
- [Python Software Foundation](https://www.python.org/psf/)
- [The Programming Historian](http://http://programminghistorian.org)

[1]: https://piazza.com/class/ia5h507lfcr47d 

[2]: https://github.com/denten-workshops/dh-core 

[3]: https://github.com/denten/dhnotes/wiki
