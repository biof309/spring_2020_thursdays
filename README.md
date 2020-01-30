### Introduction to Python Programming - BIOF309 - FAES

**Time: Thursday 6:00PM - 8:00PM**

Changes are tracked using the [git version control system](https://git-scm.com/). Material for this syllabus  is drawn from pre-existing courses [here](https://github.com/biof309/fall2019) and [here](https://github.com/marskar/biof309_fall2018) (This document is subject to revision)


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


Preparation before class
------------------

**Each student is encouraged to bring their own laptop to each class.**

*Programing without a computer would be an exceptional feat.*

Laptops are available to borrow for class on an as needed basis. There are also Data Processing Stations available to use in the library. 

With a successful install of the required software, you should be able to open the application "Anaconda Navigator", launch a notebook, and execute a cell (Ctrl + Enter) containing the command `!git status`. The indication of success will most likely be an error telling you that your current directory is not a git repository (unless of course you are currently in a git repository):

`fatal: not a git repostory (or any of the parent directories): .git`

If this is not the case you should follow the instructions below (including instructions specific to your operating system).

Please install the following programs **BEFORE** the first class, you do **not** need admin privileges to do this:
1. The [Anaconda Scientific Python Distribution](https://www.anaconda.com/download/).

    The Anaconda installer will automatically install most of the software we will use during the course, including [Jupyter Notebooks](http://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/What%20is%20the%20Jupyter%20Notebook.html).


###### OSX (Apple) specific requirements:

1. A working installation of git is required on OSX. Note, this should be available by default on OSX but if it is not, this step will need admin privileges. The most frequent cause of git not being available on OSX can be fixed by the following: opening the terminal application on OSX and running the command `xcode-select --install` as described [here](https://stackoverflow.com/questions/52522565/git-is-not-working-after-macos-mojave-update-xcrun-error-invalid-active-devel) and selecting "Install". 
2. Open a terminal and type `echo $0`. This should report /bin/bash. If this is not the case you may wish to ask your system administrator to set /bin/bash as your login shell. Alternatively, for the classes you can set the terminal to use a login shell by adding `/bin/bash -l` as a run command (in `Terminal > Preferences > Shell > Run command`).


###### Windows

If you use Windows 10, please try to set up the [Windows subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10). This will make things easier.

If this is not possible you can try the following alternative:
1. When installing [gitforwindows](gitforwindows.org) be sure to select the option "Use git and other UNIX tools from the command prompt" when provided options to "Adjust your PATH environment", and take a note of the installation directory. Otherwise install the application with all the default settings.

2. In order to use the software you installed in step 1. within jupyter you need to make a small change to a text file (and you may have to create the text file in the first place). The first option should just work (note though that it assumes that the gitforwindows installed the program "C:\Program Files\Git\bin\bash.exe". If the command below doesn't work you may have to use the second approach and substitute the installation location noted in step 1.)

    + The easiest way to do this is by executing the following command in the "gitbash" application (this will erase pre-existing setup if you have it). Right-click on your mouse is often the way to paste in gitbash. We do not advise attempting to manually type the command below:
       
       ```if [ ! -d ~/.jupyter ]; then mkdir ~/.jupyter;fi ; curl https://afni.nimh.nih.gov/pub/dist/john/jupyter_notebook.py -o ~/.jupyter/jupyter_notebook_config.py```

    + Another way to configure your installation is to open the file ~/.jupyter/jupyter_notebook_config.py in a text editor and add the line described [here](https://medium.com/@konpat/using-git-bash-in-jupyter-noteobok-on-windows-c88d2c3c7b07)




Approximate Schedule (subject to substantial revision)
--------

| #  |Date| Title                                   | Lead|
|----|----|-----------------------------------------|---------|
|1 |2020-02-06|Introduction                                   |John|
|2 |2020-02-13|Jupyter, python, and bash                      |*|
|3 |2020-02-20|A python whirlwind (Part 1)                    |John|
|4 |2020-02-27|A python whirlwind (Part 2)                    |John|
|5 |2020-03-05|Git                                            |John|
|6 |2020-03-12|Using what we have learned                     |John|
|7 |2020-03-19|More advance git usage                         |John|
|8 |2020-03-26|Private methods, and structuring our own code. |*|
|9 |2020-04-02|A python whirlwind (Part 3)                    |*|
|10|2020-04-09|A python whirlwind (Part 4)                    |John|
|11|2020-04-16|Packaging python code                          |John|
|12|2020-04-23|Final Project Clinic                           |All Instructors|
|13|2020-04-30|Final Project Clinic                           |All Instructors|
|14|2020-05-04|Final Project Clinic                           |All Instructors|


Grading
-------

Use the [grading](course_rubric.md) rubric for the course. Read it. Internalize it. Live by it. It is like being given the answers before the test. There are no tricks here: we grade you according to the rubric!

Communication
------------

Please try to ask your questions during class, if at all possible.

**Before contacting us**, please check to see if your question has already been answered elsewhere, e.g. [StackOverflow](https://stackoverflow.com/).

If you cannot find the answer, please make sure to ask your question thoughtfully (https://stackoverflow.com/help/how-to-ask) and provide everything needed to answer e.g. code, error message, dataset, etc.

In general, please use the [course gitter channel](https://gitter.im/biof309/community) to communicate with classmates and instructors. In case of personal/private question/concerns, please use the private chat functionality of gitter.

In case of an emergency, please use [gitter](https://gitter.im/biof309) *and* an email.


Course Materials
----------------

Course materials are available in the course [GitHub repository](https://github.com/biof309/spring_2020_thursdays.git).


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
    Before accessing the [course materials repo](https://github.com/biof309/spring_2020_thursdays.git), you should know that
    * it is likely to be under constant development throughout the semester and
    * you are not expected to work through _everything_ contained therein!




2. [GitHub student pack](https://education.github.com/pack)

    [GitHub](https://github.com) is offering some free awesome resources to students, that might be of interest to you, depending on your background:
