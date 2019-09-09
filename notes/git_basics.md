# Git basics

There are a number of [useful](http://rogerdudler.github.io/git-guide/) [guides](https://try.github.io/levels/1/challenges/1) for [learning](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics) [git](http://blog.udacity.com/2015/06/a-beginners-git-github-tutorial.html), but in this class we're going to focus (mostly) on just a few simple tasks, and the commands that go with them.

## Creating a repository

If you're working with Github, it's generally easiest to create a repository by following [these instructions](https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/). It requires you to first create a repository on Github, then create a corresponding folder on your local machine, then run a couple commands to link them up.

**Useful commands:**

  - `git init`: Turns a normal folder into a git repository
  - `git remote add origin (your remote repository URL)`: Links up your local git repository with Github (or another remote git location).

## Cloning and updating a repository

Often you'll want to get a copy of someone else's repository, either so you can play around with the code or collaborate by submitting your own. This requires knowing the URL for the repository, which can be found on its [Github page](https://github.com/cjdd3b/advanced-data-journalism) and generally looks something like this: `https://github.com/cjdd3b/advanced-data-journalism.git`.

**Useful commands:**

  - `git clone (remote repository URL)`: Grabs a copy of that repository from Github
  - `git pull`: If you run this command from inside your local copy of a remote repository, it will pull down any updates that have been made to the code since you cloned it.

## Updating and commiting to a repository

If you want to push code from your local repository to its home on Github, you will have to follow a three-step process. First get your code ready to push, then write a commit message describing what you did, then finally push it to the remote repository.

**Useful commands:**

  - `git add .`: Run this command from within the directory where the local code you changed lives. Note the dot. This will get your changes ready to be pushed.
  - `git commit -m "Your commit message here"`: Write a short commit message describing what you did.
  - `git push` or `git push origin master`: Connect to your remote repository and push your code changes to it.

## Github accounts to explore

Most major news organizations maintain a presence on Github. Here are a few worth checking out:

  - [The New York Times](https://github.com/newsdev)
  - [NPR Visuals](https://github.com/nprapps)
  - [ProPublica](https://github.com/propublica)
  - [The Los Angeles Times](https://github.com/datadesk)
  - [The Washington Post](https://github.com/datanews)
  - [The Texas Tribune](https://github.com/texastribune)
  - [WNYC](https://github.com/datanews)
  - [FiveThirtyEight](https://github.com/fivethirtyeight)
  - [St. Louis Post-Dispatch](https://github.com/PostDispatchInteractive)
  - [Chicago Tribune](https://github.com/newsapps)
  - [Vox](https://github.com/voxmedia)
  - [Politico](https://github.com/The-Politico)
