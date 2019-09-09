# Advanced Data Journalism software requirements

Below is a list of the key software you'll need for class, along with some resources offering tips about how to get it installed.

### Text editor

A good programming text editor will help you organize your code, catch typos and generally make your life a lot easier. We recommend [Sublime Text 2](http://www.sublimetext.com/2), which you can easily download and install from their website.

### Terminal client

We'll be doing most of our work from the command line, which means you'll need access to a terminal client. On a Mac, you can either type the word "Terminal" into your Spotlight Search to access the default client:

<img width="675" alt="screen shot 2016-08-29 at 8 26 30 am" src="https://cloud.githubusercontent.com/assets/947791/18051798/c348bccc-6dc4-11e6-9f1c-09375f87fb0d.png">

Or you can download [iTerm2](https://www.iterm2.com/) (recommended). Either way, you might want to add the tool to your Dock for easy access.

If you use Windows, this setup is going to be a bit more complicated. Your first step should be trying to install and run [Cygwin](https://cygwin.com/install.html), which is software that emulates the Unix-style terminal that runs on Macs. There's a good guide [here](https://www.physionet.org/physiotools/cygwin/) as well.

### Python

The main programming language we'll be using is Python. If you're using a Mac, you should already have it installed. If you're using a PC, you can install it using the self-installer found [here.](https://www.python.org/downloads/release/python-374/)

To test whether it works, go to your terminal and type the word `python`. You should see something that looks like this:

<img width="503" alt="Screen Shot 2019-09-09 at 6 58 04 AM" src="https://user-images.githubusercontent.com/947791/64528912-3c1b5c00-d2cf-11e9-93ef-65330e60ceaf.png">

To test Python 3, go to your terminal and type `python3`. You should see similar output.

### easy_install and pip

To make our lives easier, Python comes with two package management tools, which allow us to install new packages that extend Python's core functionality. You'll probably need some help getting these up and running, but here are some basic instructions:

**On Windows**: http://stackoverflow.com/questions/4750806/how-to-install-pip-on-windows

**On OSX**: easy_install should already be included. To install pip, simply type ```sudo easy_install pip``` and enter your administrative password.

### Virtualenv and virtualenvwrapper

These are Python tools that make it easier to install external packages and libraries. They're standard tools in most newsrooms for reasons we'll discuss in class.

We can install them both by following a slightly modified version of the [virtualenvwrapper installation instructions](http://virtualenvwrapper.readthedocs.org/en/latest/install.html):

```
sudo pip install virtualenvwrapper --ignore-installed six
echo 'export WORKON_HOME=$HOME/.virtualenvs; source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bash_profile
source ~/.bash_profile
```

To see if it works, try creating a new virtual environment like so:

```
mkvirtualenv dataj
```

That will create a new virtual environment, which will be reflected in your command line setup like so (notice the "dataj" piece at the left of the prompt):

<img width="503" alt="Screen Shot 2019-09-09 at 6 58 04 AM" src="https://user-images.githubusercontent.com/947791/64528912-3c1b5c00-d2cf-11e9-93ef-65330e60ceaf.png">

Subsequently you will be able to access that environment by typing `workon dataj` into your terminal. You can exit the environment by typing `deactivate`.

### Various Python packages

Once your virtual environments are set up, you'll easily be able to install the various Python packages we'll use in class using the command ```pip install LIBRARY-NAME```. You'll want to install these within your virtual environment (we'll talk about this), but you can get started with that like so:

```
workon dataj
pip install bs4
pip install requests
pip install mechanize
pip install jupyter
```

There will be others as well, which we'll get to later this semester.

### Homebrew (OSX only)

[Homebrew](http://brew.sh/) is a package manager, like pip, but designed to install command-line utilities rather than Python packages. We'll use it to install git (and possibly some other things later):

Install it by copying and pasting this line into the terminal:

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

### Git and Github

Git is the version control system of choice for modern development teams. It allows you to continually save and back up your code to the web, via [Github](https://github.com/).

First you're going to need to install git itself, which (if you installed Homebrew above) should be as simple as:

```
brew install git
```

On Windows, you can install it by following the directions [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git#Installing-on-Windows).

Second, you'll need to set up a Github account, which you can do by following [these instructions](https://github.com/join).
