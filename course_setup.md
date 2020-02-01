# BIOF-309, Spring 2020 Pre-class installation requirements

With a successful install of the required software, you should be able to open the application "Anaconda Navigator" or terminal application ("Terminal" on OSX, "gitbash" on Windows), launch a notebook, and execute a cell (Ctrl + Enter) containing the command `!git status`. The indication of success will most likely be an error telling you that your current directory is not a git repository (unless of course you are currently in a git repository):

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

