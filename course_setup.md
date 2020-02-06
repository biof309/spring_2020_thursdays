# BIOF-309, Spring 2020 Pre-class installation requirements

Please consider [editing this document](https://github.com/biof309/spring_2020_thursdays/edit/master/course_setup.md) (submit a "Pull request" for your changes) if you feel anything is unclear or if you wish to document a peculiarity that you encountered during your own attempts at setting up your computer...

With a successful install of the required software, you should be able to open the application "Anaconda Navigator" or terminal application ("Terminal" on OSX, "gitbash" on Windows), launch a notebook, and execute a cell (Ctrl + Enter) containing the command `!git status`. The indication of success will most likely be an error telling you that your current directory is not a git repository (unless of course you are currently in a git repository):

`fatal: not a git repostory (or any of the parent directories): .git`

If this is not the case you should follow the instructions below (including instructions specific to your operating system).

Please install the following programs **BEFORE** the first class, you do **not** need admin privileges to do this:
1. The [Anaconda Scientific Python Distribution](https://www.anaconda.com/download/) (the python3 version).

    The Anaconda installer will automatically install most of the software we will use during the course, including Jupyterlab.

1. On Windows you are required to also install [gitforwindows](https://gitforwindows.org).

###### OSX (Apple) specific details:

1. A working installation of git is required on OSX. Note, this should be available by default on OSX but if it is not, this step will need admin privileges. The most frequent cause of git not being available on OSX is due to a licencing issue relating to Xcode. This can be fixed (as described [here](https://stackoverflow.com/questions/52522565/git-is-not-working-after-macos-mojave-update-xcrun-error-invalid-active-devel) ) by the following: opening the terminal application on OSX and running the command `xcode-select --install` and selecting "Install". 
2. Open a terminal and type `echo $0`. This should report /bin/bash. If this is not the case you may wish to ask your system administrator to set /bin/bash as your login shell. Alternatively, for the classes you can set the terminal to use a login shell by adding `/bin/bash -l` as a run command (in `Terminal > Preferences > Shell > Run command`).
3. Please pay attention to what is in your bash configuration files (~/.bashrc and ~/.bash_profile). Students often have other pre-existing installations of other software that modify system settings in various ways using these files. At the very least, if you need help let the helper know if there are any entries in these files that you don't understand.


###### Windows

If you use Windows 10, please try to set up the [Windows subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10). This will make things easier.

If this is not possible you can try the following alternative:
1. When installing gitforwindows be sure to select the option "Use git and other UNIX tools from the command prompt" when provided options to "Adjust your PATH environment", and take a note of the installation directory. Otherwise install the application with all the default settings.

2. In order to use the software you installed in step 1. within jupyter you need to make a small change to a text file (and you may have to create the text file in the first place). The first option should just work (note though that it assumes that the gitforwindows installed the program "C:\Program Files\Git\bin\bash.exe". If the command below doesn't work you may have to use the second approach and substitute the installation location noted in step 1.)

    + The easiest way to do this is by executing the following command in the "gitbash" application (this will erase pre-existing setup if you have it). Right-click on your mouse is often the way to paste in gitbash. We do not advise attempting to manually type the command below:
       
       ```if [ ! -d ~/.jupyter ]; then mkdir ~/.jupyter;fi ; curl https://afni.nimh.nih.gov/pub/dist/john/jupyter_notebook.py -o ~/.jupyter/jupyter_notebook_config.py```

    + Another way to configure your installation is to open the file ~/.jupyter/jupyter_notebook_config.py in a text editor and add the line described [here](https://medium.com/@konpat/using-git-bash-in-jupyter-noteobok-on-windows-c88d2c3c7b07)


###### Linux

Use of Linux operating systems for the class is welcomed. We assume you can adapt the OSX instructions for your purposes. We are more than happy to help if you are struggling.

# Further installation troubleshooting

Pay attention to what you use to edit the text files mentioned in the below steps. If you do not have a favourite text editor already there are lots to choose from. Depending on your preferences vim, sublimetext, and atom are all good choices. Quick and easy solutions are notepad on Windows and TextEdit on OSX because they are already installed. **If you use something like microsoft word it will corrupt the file and will break things...**

## OSX

#### Anaconda was installed but none of the conda commands work from the terminal

The command `conda` is set up when a conda.sh script is sourced  (meaning run or executed) in a terminal (by set up... when you type the text `conda` and hit enter you will see something sensible other than "command not found..."). In the anaconda directory that you installed on your computer this conda.sh file is contained in "etc/profile.d". This means that executing the command `source /Users/$USER/opt/anaconda3/etc/profile.d/conda.sh` should make things work... with some caveats... read on. Now execute the command `conda init`. This will modify your ".bash_profile" file to contain code that initializes conda for you each time you open a new terminal. There is a big gotcha for some people:

If you used the command line installer for anaconda, the **equivalent** of the above command will likely have already been executed during installation. With that said, removing all mentions of conda in both .bash_profile and .bashrc and running this should get conda working on your system once more if it has been broken since installation. **Note equivalent** command: if you used the command line installer for Anaconda, it installs Anaconda into a slightly different location: you will need to instead type `source /Users/$USER/anaconda3/etc/profile.d/conda.sh; conda init` for similar effect.
