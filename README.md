---
what: Computing Fundamentals for Human(s|ists)
where: University of Victoria, BC
when: June 11-15, 2018
---

John Simpson | john.simpson@computecanada.ca | [Twitter](https://twitter.com/symulation)  
Jessica Otis | jmotis13@gmail.com | [Twitter](https://twitter.com/jotis13)

[Class Etherpad](http://pad.software-carpentry.org/Coding_Fundamentals_DHSI2018)


## Class Description

This course is intended for humanities-based researchers who do not have a programming background, but would like to understand how programs work "behind
the scenes." Over the week, the emphasis will be on understanding how computer programmers think so that participants will be able to participate in high-level
conceptual discussions with more confidence. These general concepts will be reinforced and illustrated with hands-on development of
simple programs that can be used to assist with text-based research and analysis. Participants will work on larger projects of their own choosing for about a day and a half at the end of the course.

The programming language used for most of the course will be Python. Python has an easy-to-learn and 
gentle syntax, and powerful extensions. Use of the command-line interface
and regular expressions will also be demonstrated and emphasized. 

## Learning Outcomes

You should walk away from this course with the following knowledge:
  - Using the command line to automate tasks, manage files and folders, and run scripts.
  - Installing and accessing Python via multiple platforms.
  - Learn to write psuedocode to map out your program.
  - Understanding of the Python 3.x programming language, including the ability to write simple scripts.

## Reading Material

[This is the 2017 Coursepak link.  Need the 2018 link from Dan.  Update entire section once available.] 

The main book for our course is called *Think Python: How to Think Like a Computer Scientist* by Allen B. Downey. We're using the 2nd Edition, as it was updated for version 3.x of Python. There are four places you can get this book:

  1. Via the coursepak provided by DHSI [here](http://dhsi.org/content/2017Curriculum/4.%20Fundamentals%20of%20Programming:Coding%20for%20Human(s%7Cists).pdf ). You can download the coursepak as a PDF and use it on your computer, you can print it yourself, or you can ask the UVic Bookstore to print you a copy.

  2. Via the book publisher's website [HERE](http://greenteapress.com/thinkpython2/thinkpython2.pdf ). The PDF or ePub versions can be downloaded for free and used on your computer or printed if you'd like.

  3. Via a bookstore like [Amazon.ca](https://www.amazon.ca/Think-Python-Like-Computer-Scientist/dp/1491939362/ref=sr_1_1?ie=UTF8&qid=1495505046&sr=8-1&keywords=think+python ) or [Indigo.ca](https://www.chapters.indigo.ca/en-ca/books/think-python-how-to-think/9781491939369-item.html?ikwid=think+python&ikwsec=Home&ikwidx=0 ) if you prefer a hard copy. 

  4. Via the ProQuest database called [Safari Books Online](https://www.safaribooksonline.com ). Most academic libraries should have access to this database, and possibly even some public libraries. To access the database via a library, make sure to sign into your personal library account first, then search for and go to the database. To access it on your own, you can use the link provided [HERE](https://www.safaribooksonline.com ) and sign-up for a personal trial account.

## Before Day 1

On Day 1 of this course we'll be learning how to use the command line (aka., terminal, BASH, shell). Not every operating system will have this installed by default so we will be using a Mac computer lab for the first two days of the course.  We will help participants install these tools on their own machine later in the course, if there is interest.
 
## Day 1: Shell (4.25 hrs)

We will spend the day working with the terminal, learning the basics of the file system, data flow programming, and text manipulation. The goal is to get comfortable with the conversational, call, and response style of programming.

1. Welcome
  1. [Course Philosophy](https://github.com/ComputeCanada/dhsi-coding-fundamentals-2018/blob/master/book-chapter/main.md )
  2. Goals
  3. Schedule
2. Intro to the Shell
  1. [Shell Walkthrough](https://github.com/ComputeCanada/dhsi-coding-fundamentals-2018/blob/master/_Command_Line/CommandLineWalkThrough.md )

| When to use Shell?                | When to use Python       |
------------------------------------|--------------------------|
| - automate daily tasks            | - data science           |
| - manage files & folders          | - app development        |
| - remote server admin             | - NLTK                   |
| - data munging                    | - data visualization     |
| - quick & dirty text manipulation | - glue code              |
|                                   | - everything else        |

***[Command Line Cheat Sheets](https://github.com/ComputeCanada/dhsi-coding-fundamentals-2018/blob/master/cheatsheets/ )*** (downloadable PDFs) [These need to be revisited. eg wget]

  2. Shell programming example
  3. Shell wrap-up
  
  Tomorrow we'll clean up some overflow from today's shell activities and then switch focus to coding in Python. We'll be using both the command line with a text editor and then move to an integrated development environment (IDE). In order to be prepared for tomorrow, please make sure you have the following items installed on your laptop:

**Anaconda** - You may have already installed Anaconda before this course began. If you didn't install it, please do so tonight. You can find the free download at -> https://www.continuum.io/downloads. Make sure to download version 5.1 (or greater) of Anaconda and choose the Python 3.6 (or greater) version.  If you have trouble with the install then you can continue to use the lab machines in the morning and we will help you complete the install later in the day.

**Text Editor** - Most operating systems come pre-installed with at least one version of a text editor. However, programmers tend to like to use more complex text editors that are designed to work with programming languages and provide helpful visual cues that alert users to potential errors in their code. There are a lot of options to use, as you can see from this [list](https://en.wikipedia.org/wiki/List_of_text_editors ) but for this class we will be using [Sublime Text 3] (https://www.sublimetext.com/3 ) for both uniformity across platforms and a nice combination of a simple interface and powerful extensions.

## Day 2: Python I (5.5 hrs)

- [2.1 **Python Programming for Everyone**](https://github.com/ComputeCanada/dhsi-coding-fundamentals-2017/blob/master/Day%202%20Material/Section%202.1/Section%202.1%20README.md)

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
    - 2.1.12 Libraries and Methods

- 2.2 Pseudocode and Commenting

- 2.3 **Preparing for Tomorrow**

Tomorrow we'll start the day by writing a script that will convert early modern Gregorian dates to the British, Julian equivalents. A script or program like this will require the use of many of the things we learned today. Think about how we might approach this tonight and come prepared tomorrow to share your ideas.

## Day 3: Python II (5.5 hrs)

- 3.1 [Calendar Reform](https://github.com/ComputeCanada/dhsi-coding-fundamentals-2018/tree/master/_Python/python-live-code/earlyModernCalendar )

We will be using the shell and a text editor for this session.  If you are using Windows, it will make sense to use the command prompt rather than MobaXterm because it will give you easier access to the Anaconda installs of Python.  You can use many of your Bash Shell commands in the Windows Command Prompt but you'll find a crash course [HERE](http://www.cs.princeton.edu/courses/archive/spr05/cos126/cmd-prompt.html ).

- 3.2 Code Annotation Practice / Faded examples / Broken code

Short pieces of code without comments.  Task is to figure out what the code does and add the comments.

- 3.3 [**Integrated Development Environments** or IDEs](https://en.wikipedia.org/wiki/Integrated_development_environment) [update this once confirm we are using Video Studio Code that comes with anaconda 5.1+ install]

  In addition to using a text editor and the command line, you can also use an IDE. We'll provide an overview of Video Studio Code, which comes with the Anaconda 5.1+ install, so you have an idea of the PROs and CONs of each method, then you can choose which option you'd like to use for your project. Just like text editors, there are a lot of IDEs you can choose from, a list of some are compared here -> [https://en.wikipedia.org/wiki/Comparison_of_integrated_development_environments]()

- 3.4 Thinking about projects

Examples of "real world" projects so they can see/hear how the skills they are developing are / might be used.  Want to be able to share the code-part of whatever we share with them.

http://cwrc.ca/rsc-src/ 

- 3.5 Individual Projects: Brainstorming and Planning

Tomorrow you'll get your first crack at your individual projects. Take the time tonight to think about what sort of a project you'd like to take on. If you're having trouble coming up with a project, ask us and we can provide you with some options.
  
- 3.6 **Describing Your Individual Project**

  - 3.6.1 Write a short description of your individual project, in words. At this point, don't worry about the *how*, just think about the *what*.
  - 3.6.2 Discuss your project with your classmates. Provide feedback to each other, and update your project description if needed.

- 3.7 **Planning Your Individual Project**

  - 3.7.1 Reminder: what is psuedocode?
  - 3.7.2 Plan the *logic* of your project using step-by-step instructions, with psuedocode, or using a flow chart. At this stage, start to think about the *how*.
  - 3.7.3 Discuss your plan with your classmates. Do they have any suggestions on *how* to implement your project? 

## Day 4: Individual Projects (5.5 hrs)

- [4.1 **Getting Help**](https://github.com/ComputeCanada/dhsi-coding-fundamentals-2017/blob/master/Day%202%20Material/Section%202.2/Section%202.2%20README.md )

  - 4.1.1 Google
  - 4.1.2 StackExchange
  - 4.1.3 Python.org website
  - 4.1.4 Online Education
  - 4.1.5 Books

- 4.2 **Coding Your Individual Project**

  - 4.2.1 Decide which software or environment you want to use: text editor or IDE.
  - 4.2.2 Start coding your script by translating your description into comments.
  - 4.2.3 Add the proper syntax to your script by translating your plan and/or pseudocode into Python.

  **If you're using a text editor, don't forget to SAVE often!**

## Day 5: Race to the Finish (3 hrs)

- 5.1 **Continue Working on Your Projects** (1.5 hrs)

- 5.2 **Project Review** (1 hr)
  - Was the scope of my project too big or too small?
  - Did I add enough comments that a non-programmer can understand what the code does? Can I still understand it if I look at it again in 6 months?
  - What do I still need to do? Make a plan to finish your project (if you haven't already done so) after you leave DHSI and put this plan in your code.

- 5.3 **Where to go from here** (30 mins)
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
