Syllabus
========

**Introduction to Python Programming - BIOF309 - FAES**

**Fall 2019**

**Time: Thursday 6:00PM - 8:00PM**

*This document is subject to revision!*

Changes are tracked using the [git version control system](https://git-scm.com/).

To interact with the materials in the repo online you may use [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) (via [Binder](https://mybinder.org/)), by clicking the link below.

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/marskar/biof309_fall2019/master?urlpath=lab)

Instructors
-----------

* John Lee 
* Ryan Patterson
* Sydney Hertafeld

Course Description
------------------

This course is designed for non-programmers, biologists, or those without specific knowledge of Python to learn how to program.
Week by week, we will slowly build up your skills and understanding of computer programming and the Python programming language.
There will be in-class demonstrations, using [JupyterLab](http://jupyterlab.readthedocs.io), and activities to be completed outside of class, using [DataCamp](https://www.datacamp.com), for you to practice and learn at your own pace.

Learning Objectives
-------------------

By the end of this course you should be able to:
1. Look at a task and determine if you can or should automate it
2. Create working Python programs
3. Understand the difference between Python object types (e.g. lists, dicts)
4. Perform data analysis and visualization with Python
5. Use [git](https://git-scm.com/) for version control and collaboration
6. Demonstrate your Python skills with a project

Communication
------------

Please try to ask your questions during class, if at all possible.

**Before contacting us**, please check to see if your question has already been answered elsewhere, e.g. [StackOverflow](https://stackoverflow.com/).

If you cannot find the answer, please make sure to ask your question thoughtfully (https://stackoverflow.com/help/how-to-ask) and provide everything needed to answer e.g. code, error message, dataset, etc.

In general, please use the [course gitter channel](https://gitter.im/biof309/community) to communicate with classmates and instructors. In case of personal/private question/concerns, please use the private chat functionality of gitter.

In case of an emergency, please use [gitter](https://biof309.slack.com) *and* an email.

Logistics
---------

This is a one-semester course starting on the 12th of September 2019 and finishing in December 2019.

Unless otherwise notified classes will be held at:

** Building 10, Room B1C209-211, NIH Bethesda campus**

Attendance in class is strongly recommended; however, we realize other commitments may occasionally prevent attendance. If you miss a class, please review the materials available at the course [GitHub repository](https://github.com/biof309/fall2019) and keep up with activities and homework.

Forming groups to complete the final project is highly encouraged! 

Required Materials
------------------

**Each student is encouraged to bring their own laptop to each class.**

*Programing without a computer would be an exceptional feat.*



Required software installation
------------------

With a successful install of the required software, you should be able to open the application "Anaconda Navigator", launch a notebook, and execute a cell (Ctrl + Enter) containing the command `!git status`. The indication of success will most likely be an error telling you that your current directory is not a git repository:

`fatal: not a git repostory (or any of the parent directories): .git`

If this is not the case you should follow the instructions below (including instructions specific to your operating system).

Please install the following programs **BEFORE** the first class, you do **not** need admin privileges to do this:
1. The [Anaconda Scientific Python Distribution](https://www.anaconda.com/download/).

    The Anaconda installer will automatically install most of the software we will use during the course, including [Jupyter Notebooks](http://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/What%20is%20the%20Jupyter%20Notebook.html).


## OSX (Apple) specific requirements:

1. A working installation of git is required on OSX. Sometimes there is an error on Mac computers where git does not work. This can be resolved by opening the terminal application on OSX and running the command `xcode-select --install` as described [here](https://stackoverflow.com/questions/52522565/git-is-not-working-after-macos-mojave-update-xcrun-error-invalid-active-devel) and selecting "Install".


## Windows

If you use Windows 10, please try to set up the [Windows subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10). This will make things easier.

If this is not possible you can try the following alternative:
1. When installing [gitforwindows](gitforwindows.org) be sure to select the option "Use git and other UNIX tools from the command prompt" when provided options to "Adjust your PATH environment", and take a note of the installation directory. Otherwise install the application with all the default settings.

2. In order to use the software you installed in step 1. within jupyter you need to make a small change to a text file (and you may have to create the text file in the first place). The first option should just work (note though that it assumes that the gitforwindows installed the program "C:\Program Files\Git\bin\bash.exe". If the command below doesn't work you may have to use the second approach and substitute the installation location noted in step 1.)

    + The easiest way to do this is by executing the following command in the "gitbash" application (this will erase pre-existing setup if you have it). Right-click on your mouse is often the way to paste in gitbash. We do not advise attempting to type the command below:
       
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

Schedule
--------

| #  | Date       | Title                                   | Lead              |
|----|------------|-----------------------------------------|-------------------|
| 1  | 2019-09-12 | Introduction        | Martin            |
| 2  | 2019-09-17 | Github, binder, jupyter | Martin        |
| 3  | 2019-10-01 | A python whirlwind        | John            |
| 4  | 2019-10-04 | Git                          | John            |
| 5  | 2019-10-11 | A python whirlwind (Part 2)   | John            |
| 6  | 2019-10-18 | Booleans and Conditionals               | TBD |
| 7  | 2019-10-25 | NumPy and Arrays                        | TBD            |
| 8  | 2019-11-01 | Pandas and DataFrames                   | TBD |
| 9  | 2019-11-19 | Machine Learning                        | TBD            |
| 10 | 2019-11-27 | Data Visualization                      | TBD |
| 11 | 2019-11-29 | Requested Topics/Final Project Clinic   | All Instructors   |
| 13 | TBD | Student Presentations                   |                   |
| 12 | TBD | Student Presentations                   |                   |
| 14 | TBD | Student Presentations                   |                   |


Homework
--------

This semester we are continuing our free-form approach to homework assignments. The due dates below are guidelines.
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

01. DUE September 13, 2019 (BEFORE Class)
    - Install [Anaconda Scientific Python Distribution](https://www.continuum.io/downloads)
    - Install [PyCharm](https://www.jetbrains.com/student)

02. DUE September 20, 2019 (BEFORE Class)
    - [Python Basics](https://campus.datacamp.com/courses/intro-to-python-for-data-science/chapter-1-python-basics)
    - [Python: Getting Started](https://www.pluralsight.com/courses/python-getting-started)
    - [Python Fundamentals](https://www.pluralsight.com/courses/python-fundamentals)
    - Chapters 01-05 in [Whirlwind Tour of Python](https://github.com/jakevdp/WhirlwindTourOfPython)
    - Chapter 02 in [Python for Data Analysis](https://github.com/wesm/pydata-book)

03. DUE September 27, 2019 (BEFORE Class)
    - [Python Lists](https://campus.datacamp.com/courses/intro-to-python-for-data-science/chapter-2-python-lists)
    - [Functions and Packages](https://campus.datacamp.com/courses/intro-to-python-for-data-science/chapter-3-functions-and-packages)
    - [Python – Beyond the Basics](https://www.pluralsight.com/courses/python-beyond-basics)
    - Chapter 08 & 13 in [Whirlwind Tour of Python](https://github.com/jakevdp/WhirlwindTourOfPython)
    - Chapter 03 in [Python for Data Analysis](https://github.com/wesm/pydata-book)

04. DUE October 4, 2019 (BEFORE Class)
    - [Loops](https://campus.datacamp.com/courses/intermediate-python-for-data-science/loops)
    - [Logic, Control Flow and Filtering](https://campus.datacamp.com/courses/intermediate-python-for-data-science/logic-control-flow-and-filtering)
    - [The Python Developer's Toolkit](https://www.pluralsight.com/courses/python-developers-toolkit)
    - Chapter 06, 07, & 09 in [Whirlwind Tour of Python](https://github.com/jakevdp/WhirlwindTourOfPython)

05. DUE October 11, 2019 (BEFORE Class)
    - Biopython TBD
    - Chapter 00-02 in [Biopython-Notebook](https://github.com/tiagoantao/biopython-notebook/tree/master/notebooks)
    - [Unit Testing with Python](https://www.pluralsight.com/courses/unit-testing-python)

06. DUE October 18, 2019 (BEFORE Class)
    - [NumPy](https://campus.datacamp.com/courses/intro-to-python-for-data-science/chapter-4-numpy)
    - Chapter 02 in [Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook/tree/master/notebooks)
    - Chapter 04 in [Python for Data Analysis](https://github.com/wesm/pydata-book)
    - [Full Stack Web Development with Python (WEB2PY)](https://www.pluralsight.com/courses/full-stack-web-development-python-web2py)
    - [Advanced Python](https://www.pluralsight.com/courses/advanced-python)

07. DUE October 25, 2019 (BEFORE Class)
	- [Dictionaries & Pandas](https://campus.datacamp.com/courses/intermediate-python-for-data-science/dictionaries-pandas)
	- Chapter 03 in [Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook/tree/master/notebooks)
	- Chapter 05-12 in [Python for Data Analysis](https://github.com/wesm/pydata-book)
	- [Django Fundamentals](https://www.pluralsight.com/courses/django-fundamentals-update)

08. DUE November 1, 2019 (BEFORE Class)
    - [Getting Started with Machine Learning in Python](https://campus.datacamp.com/courses/kaggle-python-tutorial-on-machine-learning/getting-started-with-python)
    - [Predicting with Decision Trees](https://campus.datacamp.com/courses/kaggle-python-tutorial-on-machine-learning/predicting-with-decision-trees)
    - [Improving your Predictions through Random Forests](https://campus.datacamp.com/courses/kaggle-python-tutorial-on-machine-learning/improving-your-predictions-through-random-forests)
    - Chapter 05 in [Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook/tree/master/notebooks)
    - [Testing Django Applications](https://www.pluralsight.com/courses/testing-django-applications)

09. DUE November 8, 2019 (BEFORE Class)
    - [Introduction to Data Visualization with Python](https://www.datacamp.com/courses/introduction-to-data-visualization-with-python)
    - [Data Visualization with Seaborn](https://www.datacamp.com/courses/data-visualization-with-seaborn)
    - Chapter 04 in [Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook/tree/master/notebooks)

10. WORK ON FINAL PROJECTS
Depending on your final project, you might find the following topics useful:
	- [Error handling](https://github.com/jakevdp/WhirlwindTourOfPython/blob/master/09-Errors-and-Exceptions.ipynb)
	- [Comprehensions](https://github.com/jakevdp/WhirlwindTourOfPython/blob/master/10-Iterators.ipynb)
	- [Iterators](https://github.com/jakevdp/WhirlwindTourOfPython/blob/master/10-Iterators.ipynb) and [Generators](https://github.com/jakevdp/WhirlwindTourOfPython/blob/master/12-Generators.ipynb)
	- [Regular Expressions](https://github.com/jakevdp/WhirlwindTourOfPython/blob/master/14-Strings-and-Regular-Expressions.ipynb)


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

The emphasis of the course is on learning and mastering the skills covered. We hope that everyone will be able to complete one of the Python tracks on [DataCamp](https://www.datacamp.com) and submit a final project via [GitHub](https://github.com/). If some of the material appears unclear, please ask for clarification.

Completion of the Python tracks on [DataCamp](https://www.datacamp.com) will be graded in a binary manner (completed/incomplete).

Grading the __final project__ will be done using the following rubric:

* Project description / Specification

  - Goals unclear, difficulty demonstrating functionality (1-3)
  - Goals for the project and functionality are discussed but difficult to follow (4-6)
  - Goals for the project and functionality are discussed (7-9)
  - Goals for the project and functionality are logically presented and clearly communicated (10-12)

* Documentation

  - Only comments embedded in the code (1-3)
  - Objects and methods have docstrings (4-6)
  - Objects and methods have docstrings, additional standalone documentation (7-9)
  - Objects and methods have docstrings, extensive standalone documentation with example usage (10-12)

* Readability
  - The code is poorly organized and very difficult to read (1-3)
  - The code is readable, but challenging to understand (4-6)
  - The code is fairly easy to read (7-9)
  - The code is well organized and very easy to read (10-12)

* Reusability

  - The code is not organized for reusability (1-3)
  - Some parts of the code could be reused (4-6)
  - Most of the code could be reused (7-9)
  - Each part of the code, and the whole, could be reused (10-12)

* Performance

  - Program does not run (1-6)
  - Program runs, but does not produce correct output (7-12)
  - Program runs, produces correct output under most conditions (13-18)
  - Program runs, produces correct output with robust error checking (19-24)

Course Materials
----------------

Course materials are available in the course [GitHub repository](https://github.com/biof309/fall2019).
