Syllabus
========

**Introduction to Python Programming - BIOF309 - FAES**

**Spring 2020**

**Time: Thursday 6:00PM - 8:00PM**

*This document is subject to revision!*

Changes are tracked using the [git version control system](https://git-scm.com/). Material for this syllabus  is drawn from pre-existing courses [here](https://github.com/biof309/fall2019) and [here](https://github.com/marskar/biof309_fall2018)

Instructors
-----------

* John Lee 
* -
* -

Course Description
------------------

This course is designed for non-programmers, biologists, or those without specific knowledge of Python to learn how to program. Emphasis is placed on foundational skills for automation, reproducibility, and sustainable development of code for scientific analysis.

There will be in-class demonstrations, and teaching using [JupyterLab](http://jupyterlab.readthedocs.io). The course also consists of out of class learning using the [DataCamp](https://www.datacamp.com) learning platform. This allows students to practice and learn at your their pace with programming exercises that provide realtime feedback on mistakes.

Learning Objectives
-------------------

By the end of this course you should be able to:
1. Look at a task and determine if you can or should automate it
1. Use [git](https://git-scm.com/) for keeping track of changes in your project and collaborating with others
1. Create working Python programs
1. Develop strategies for leveraging pre-existing solutions to analysing your scientific data
1. Be aware of tools and strategies that help sustainably develop robust software for scientific analysis
1. Have a deep understanding of the basic structures in Python (e.g. lists, dicts, etc)
1. Perform data analysis and visualization with Python
1. Demonstrate your Python skills with a project

Communication
------------

Please try to ask your questions during class, if at all possible.

**Before contacting us**, please check to see if your question has already been answered elsewhere, e.g. [StackOverflow](https://stackoverflow.com/).

If you cannot find the answer, please make sure to ask your question thoughtfully (https://stackoverflow.com/help/how-to-ask) and provide everything needed to answer e.g. code, error message, dataset, etc.

In general, please use the [course gitter channel](https://gitter.im/biof309/community) to communicate with classmates and instructors. In case of personal/private question/concerns, please use the private chat functionality of gitter.

In case of an emergency, please use [gitter](https://gitter.im/biof309) *and* an email.

Logistics
---------

This is a one-semester course starting on the 6th of February 2020.

Unless otherwise notified classes will be held at:

** Building 10, Room B1C209-211, NIH Bethesda campus**

Attendance in class is strongly recommended; however, we realize other commitments may occasionally prevent attendance. If you miss a class, please review the materials available at the course [GitHub repository](https://github.com/biof309/fall2019) and keep up with activities and homework.

Forming groups to complete the final project is highly encouraged! 

Required Materials
------------------

**Each student is encouraged to bring their own laptop to each class.**

*Programing without a computer would be an exceptional feat.*

Laptops are available to borrow for class on an as needed basis. There are also Data Processing Stations available to use in the library. 

Required software installation
------------------

With a successful install of the required software, you should be able to open the application "Anaconda Navigator", launch a notebook, and execute a cell (Ctrl + Enter) containing the command `!git status`. The indication of success will most likely be an error telling you that your current directory is not a git repository (unless of course you are currently in a git repository):

`fatal: not a git repostory (or any of the parent directories): .git`

If this is not the case you should follow the instructions below (including instructions specific to your operating system).

Please install the following programs **BEFORE** the first class, you do **not** need admin privileges to do this:
1. The [Anaconda Scientific Python Distribution](https://www.anaconda.com/download/).

    The Anaconda installer will automatically install most of the software we will use during the course, including [Jupyter Notebooks](http://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/What%20is%20the%20Jupyter%20Notebook.html).


## OSX (Apple) specific requirements:

1. A working installation of git is required on OSX. Note, this should be available by default on OSX but if it is not, this step will need admin privileges. The most frequent cause of git not being available on OSX can be fixed by the following: opening the terminal application on OSX and running the command `xcode-select --install` as described [here](https://stackoverflow.com/questions/52522565/git-is-not-working-after-macos-mojave-update-xcrun-error-invalid-active-devel) and selecting "Install". 
2. Open a terminal and type `echo $0`. This should report /bin/bash. If this is not the case you may wish to ask your system administrator to set /bin/bash as your login shell. Alternatively, for the classes you can set the terminal to use a login shell by adding `/bin/bash -l` as a run command (in `Terminal > Preferences > Shell > Run command`).


## Windows

If you use Windows 10, please try to set up the [Windows subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10). This will make things easier.

If this is not possible you can try the following alternative:
1. When installing [gitforwindows](gitforwindows.org) be sure to select the option "Use git and other UNIX tools from the command prompt" when provided options to "Adjust your PATH environment", and take a note of the installation directory. Otherwise install the application with all the default settings.

2. In order to use the software you installed in step 1. within jupyter you need to make a small change to a text file (and you may have to create the text file in the first place). The first option should just work (note though that it assumes that the gitforwindows installed the program "C:\Program Files\Git\bin\bash.exe". If the command below doesn't work you may have to use the second approach and substitute the installation location noted in step 1.)

    + The easiest way to do this is by executing the following command in the "gitbash" application (this will erase pre-existing setup if you have it). Right-click on your mouse is often the way to paste in gitbash. We do not advise attempting to manually type the command below:
       
       ```if [ ! -d ~/.jupyter ]; then mkdir ~/.jupyter;fi ; curl https://afni.nimh.nih.gov/pub/dist/john/jupyter_notebook.py -o ~/.jupyter/jupyter_notebook_config.py```

    + Another way to configure your installation is to open the file ~/.jupyter/jupyter_notebook_config.py in a text editor and add the line described [here](https://medium.com/@konpat/using-git-bash-in-jupyter-noteobok-on-windows-c88d2c3c7b07)



Optional extras
------------------

We recommend that you avail of the following tools as they will help you in your path towards Pythonic stardom:

1. The [PyCharm Integrated Development Environment (IDE)](https://www.jetbrains.com/pycharm/)

    The very nice folks at [JetBrains](https://www.jetbrains.com) have given us free licenses for the Professional Edition of [PyCharm Integrated Development Environment (IDE)](https://www.jetbrains.com/pycharm/), the best (in my humble opinion) Python Integrated Development Environment (IDE).

    If you have a .edu email address, please install [PyCharm Integrated Development Environment (IDE)](https://www.jetbrains.com/pycharm/) Professional using [this link](https://www.jetbrains.com/student/).

    If not, a installation link will be distributed to you by email and made available on [Slack](https://biof309.slack.com/).
    
    Before the first class, please watch the [Getting Started with PyCharm](https://www.youtube.com/watch?v=BPC-bGdBSM8&list=PLQ176FUIyIUZ1mwB-uImQE-gmkwzjNLjP) video series.
    
    Before the second class, please watch the [PyCharm In-Depth VCS](https://www.youtube.com/watch?v=jFnYQbUZQlA) video series.


2. [DataCamp](https://www.datacamp.com)

    Since Fall 2017, the very nice folks at [DataCamp](https://www.datacamp.com) have been generously supporting our class via their [DataCamp for the Classroom](https://www.datacamp.com/groups/education) initiative.
    
    This program give us free 6 month access to DataCamp's awesome Data Visualization📊, Machine Learning🤖, and Data Science learning materials.
    
    We will discuss the most interesting examples from DataCamp during class and point out others to be reviewed outside of class.

3. [GitHub](https://github.com/)

    All of the course materials are available on [GitHub](https://github.com/).
    Before accessing the [course materials repo](https://github.com/biof309/fall2019), you should know that
    * it is likely to be under constant development throughout the semester and
    * you are not expected to work through _everything_ contained therein!




2. [GitHub student pack](https://education.github.com/pack)

    [GitHub](https://github.com) is offering some free awesome resources to students, that might be of interest to you, depending on your background:

Approximate Schedule (subject to substantial revision)
--------

| #  |Date| Title                                   | Lead|
|----|----|-----------------------------------------|---------|
|1 |2020-02-06|Introduction                                   |John|
|2 |2020-02-13|Jupyter, python, and bash                      |John|
|3 |2020-02-20|A python whirlwind (Part 1)                    |John|
|4 |2020-02-27|A python whirlwind (Part 2)                    |John|
|5 |2020-03-05|Git                                            |John|
|6 |2020-03-12|Using what we have learned                     |John|
|7 |2020-03-19|More advance git usage                         |John|
|8 |2020-03-26|Private methods, and structuring our own code. |John|
|9 |2020-04-02|A python whirlwind (Part 3)                    |John|
|10|2020-04-09|A python whirlwind (Part 4)                    |John|
|11|2020-04-16|Packaging python code                          |John|
|12|2020-04-23|Final Project Clinic                           |All Instructors|
|13|2020-04-30|Final Project Clinic                           |All Instructors|
|14|2020-05-04|Final Project Clinic                           |All Instructors|


Homework
--------

The due dates below are guidelines.
By the end of the semester, you must complete at least one career track or at least two skills tracks on [DataCamp](https://www.datacamp.com/tracks/career).

This will take 28-67 hours total to complete, depending on which you choose to do.

*[DataCamp](https://www.datacamp.com) Career Tracks* (complete at least 1):
- [DataCamp Python Programmer](https://www.datacamp.com/tracks/python-programmer), 36 hours, 10 courses
- [DataCamp Data Analyst with Python](https://www.datacamp.com/tracks/data-analyst-with-python), 47 hours, 13 Courses
- [DataCamp Data Scientist with Python](https://www.datacamp.com/tracks/data-scientist-with-python), 67 hours, 20 Courses

*DataCamp Skills Tracks* (complete at least 2):
- [Python Programming](https://www.datacamp.com/tracks/python-programming), 15 hours, 4 courses
- [Importing & Cleaning Data with Python](https://www.datacamp.com/tracks/importing-cleaning-data-with-python), 13 hours, 4 courses
- [Data Manipulation with Python](https://www.datacamp.com/tracks/data-manipulation-with-python), 16 hours, 4 courses
- [Machine Learning](https://www.datacamp.com/tracks/machine-learning-with-python), 16 hours, 4 courses

**Please start on your chosen track(s) on [DataCamp](https://www.datacamp.com)  as soon as possible and work towards the certificate(s) throughout the semester. This will require substantial work! Do not wait until the end of the semester!**

Please use the schedule below as a guide to which [DataCamp](https://www.datacamp.com)chapters/lessons correspond to what is covered in class.

01. 2020-02-13 (BEFORE Class)
    - Install [Anaconda Scientific Python Distribution](https://www.continuum.io/downloads)
    - Install [PyCharm](https://www.jetbrains.com/student)

02. 2020-02-20 (BEFORE Class)
    - [Python Basics](https://campus.datacamp.com/courses/intro-to-python-for-data-science/chapter-1-python-basics)
    - Chapters 01-05 in [Whirlwind Tour of Python](https://github.com/jakevdp/WhirlwindTourOfPython)
    - Chapter 02 in [Python for Data Analysis](https://github.com/wesm/pydata-book)

03. 2020-02-27 (BEFORE Class)
    - [Python Lists](https://campus.datacamp.com/courses/intro-to-python-for-data-science/chapter-2-python-lists)
    - [Functions and Packages](https://campus.datacamp.com/courses/intro-to-python-for-data-science/chapter-3-functions-and-packages)
    - Chapter 08 & 13 in [Whirlwind Tour of Python](https://github.com/jakevdp/WhirlwindTourOfPython)
    - Chapter 03 in [Python for Data Analysis](https://github.com/wesm/pydata-book)

04. 2020-03-05 (BEFORE Class)
    - [Loops](https://campus.datacamp.com/courses/intermediate-python-for-data-science/loops)
    - [Logic, Control Flow and Filtering](https://campus.datacamp.com/courses/intermediate-python-for-data-science/logic-control-flow-and-filtering)
    - Chapter 06, 07, & 09 in [Whirlwind Tour of Python](https://github.com/jakevdp/WhirlwindTourOfPython)

05. 2020-03-12 (BEFORE Class)
    - Biopython TBD
    - Chapter 00-02 in [Biopython-Notebook](https://github.com/tiagoantao/biopython-notebook/tree/master/notebooks)

06. 2020-03-19 (BEFORE Class)
    - [NumPy](https://campus.datacamp.com/courses/intro-to-python-for-data-science/chapter-4-numpy)
    - Chapter 02 in [Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook/tree/master/notebooks)
    - Chapter 04 in [Python for Data Analysis](https://github.com/wesm/pydata-book)

07. 2020-03-26 (BEFORE Class)
	- [Dictionaries & Pandas](https://campus.datacamp.com/courses/intermediate-python-for-data-science/dictionaries-pandas)
	- Chapter 03 in [Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook/tree/master/notebooks)
	- Chapter 05-12 in [Python for Data Analysis](https://github.com/wesm/pydata-book)

08. 2020-04-02 (BEFORE Class)
    - [Getting Started with Machine Learning in Python](https://campus.datacamp.com/courses/kaggle-python-tutorial-on-machine-learning/getting-started-with-python)
    - [Predicting with Decision Trees](https://campus.datacamp.com/courses/kaggle-python-tutorial-on-machine-learning/predicting-with-decision-trees)
    - [Improving your Predictions through Random Forests](https://campus.datacamp.com/courses/kaggle-python-tutorial-on-machine-learning/improving-your-predictions-through-random-forests)
    - Chapter 05 in [Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook/tree/master/notebooks)

09. 2020-04-09 (BEFORE Class)
    - [Introduction to Data Visualization with Python](https://www.datacamp.com/courses/introduction-to-data-visualization-with-python)
    - [Data Visualization with Seaborn](https://www.datacamp.com/courses/data-visualization-with-seaborn)
    - Chapter 04 in [Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook/tree/master/notebooks)

Recommended Books
-----------------
**There is no required textbook for this course.**

We do, however, highly recommend [Python for Data Science](https://github.com/jakevdp/PythonDataScienceHandbook) and its companion text [A Whirlwind Tour of Python](https://github.com/jakevdp/WhirlwindTourOfPython) by Jake Vanderplas. Both of these books are available free on [GitHub](https://github.com/) in Jupyter Notebook form. The code for [Python for Data Analysis](https://github.com/wesm/pydata-book) by Wes McKinney is also on [GitHub](https://github.com/) but the text is only available in the printed copy of the book. For maximum enjoyment, consider working through the relevant chapters before coming to class.

We will link to relevant online resources throughout the course.

If you would like additional material on the basics, the following resources may be useful:

* [Python for Biologists](http://pythonforbiologists.com/) by Martin Jones.
* [Learn Python the Hard Way (ebook freely available from the author)](http://learnpythonthehardway.org/book/) by Zed A. Shaw; a [video course](http://learnpythonthehardway.org/) is also available.
* [Think Python (ebook freely available from the author)](http://www.greenteapress.com/thinkpython/thinkpython.html) by Allen B. Downey.
* [Python for Everybody: Exploring Data in Python 3 (ebook freely available from the author)](https://www.pythonlearn.com/book.php) by Charles Severance.
* [The Hitchhiker’s Guide to Python](http://docs.python-guide.org/en/latest/) by Kenneth Reitz and Tanya Schlusser.
* [Automate the Boring Stuff with Python](www.automatetheboringstuff.com) by Al Sweigart.
* [Introduction to Machine Learning with Python](https://github.com/amueller/introduction_to_ml_with_python) by Andreas Mueller and Sarah Guido.

For more information about Python, please see the official [Python Software Foundation website](https://www.python.org/).

Grading
-------

The emphasis of the course is on learning and mastering the skills covered. The grade for the course will be divided into 3 components:

+ Online course work. Completion of the suggested courses on Datacamp will provide 15% of the grade
+ A simple assignment during the course, submitted using github will provide up to 10% of the grade
+ The remaining 75% of the grade is based on the final project submitted via github

If some of the material appears unclear, please ask for clarification.

Some details regarding the final project:

+ Pick a project that is interesting to you. You’ll find it easier to work on if you think it is fun or solves a problem that you have encountered in your daily work. Regarding content the sky is the limit.
+ The project should be setup as a fork of (and pull request to) the [project template](https://github.com/biof309/spring2020_template_project)
+ Record your plans on github as you go
+ Pay attention to what your minimally viable product is so that if you only achieve that you will at least have something to show for your efforts.
+ Pay attention to the rubric listed below
+ Not creating a formal python package is acceptable but must be justified.
+ Joint projects are looked upon favorably.
+ Breadth of python skills will be noted.
+ Having commits from instructors is fine (though you don't get points for such beautiful code).
+ Try to show weekly improvement (on github) during the final weeks

Grading the __final project__ will be done using the following rubric:

### Project description / Specification
  - Goals for the project are discussed and placed in the context of pre-existing work. This could take the form of other python projects or indeed software in any  language. Not reinventing the wheel is an important result of good planning   (0-5)

### Documentation
  - Comments  are embedded in the code or Objects/functions have docstrings (0-5)
  - Comments and docstrings are used (6-10)
  - Documentation is thorough both in the readme and in the code itself aiding interpretation of the project (11-15)
  
### Readability and reusability
  - The code is poorly organized and difficult to interpret (1-10)
  - Basic organization and modularity of the code is present (11-20)
  - Careful organization of the code (commented, well-named variables in well-named functions in well-named modules, in a package if appropriate), coupled with attention to style guides for python. (21-30)

### Testing
   Marks will not necessarily be lost for failing tests.
  - Tests should cover a significant fraction of the python code used. (0-10)
  - Tests have aided development and have helped discover bugs in the code (11-20)

### "The product"
   - The code technically works but does not show evidence of engagement (1-5)
  - The project checks the boxes in the rubric effectively and is nicely implemented (6-10)
  - The code attempts to solve a real-life problem, shows great progress both inside and outside class over the weeks of the project (11-20)
  - The project is a roaring success. It's amazing to see what you can now do with python! You have earned the title of pythonista (21-30)


Course Materials
----------------

Course materials are available in the course [GitHub repository](https://github.com/biof309/fall2019).
