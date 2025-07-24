Git is an open-sourced version control system (VCS) used for tracking changes in files, allowing teams to work collaboratively while also maintaining the integrity of the source code.

# What is Git?

|                                                                                                                |                                                                 |
| -------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| **Definition**                                                                                                 | **Characteristics**                                             |
| - Free open source Version Control System (VCS)<br>- Tracks changes in source code during software development | - Distributive<br>- Adaptive<br>- Fast & Reliable<br>- Flexible |
Git is a **free and open source version control system (VCS)** designed to handle everything from small to large projects.
Git records all of the changes made to a file in a repository (a database), enabling the collaboration between software developers.

**Git Benefits:**
 - Free and open source
 - Supports non-linear development
 - Tracks history of files
 - Creates backups
 - Supports collaboration - Git can be command line or GUI driven, allowing everyone to contribute easily.
 - Scalable - Git's branching model can adapt to fit the workflow of almost any team.
 - It's a distributed environment - does not require a constant connection to a central server.

Why is Git so popular:
 ![[Pasted image 20250723124558.png]]

# Git is a Version Control System. But what _is_ a Version Control System?
A version control system (VCS) tracks changes to a file or set of files over time.
Developers can check out a file from the server, make changes, and check the file back in. 
The server then stores the new version of the file

There are three types of Version Control Systems:
- Local Version Control Systems
- [Centralized Version Control Systems (CVCS)](https://about.gitlab.com/topics/version-control/what-is-centralized-version-control-system/)
- [Distributed Version Control Systems (DVCS)](https://about.gitlab.com/topics/version-control/benefits-distributed-version-control-system/)

## Centralised vs Distributed Version Control Systems
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Centralised Version Control Systems (CVCS)**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | ****Distributed Version Control Systems (**DVCS)**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ![](https://d36ai2hkxl16us.cloudfront.net/course-uploads/bf663a54-0bb6-4726-bd83-1e76668129cf/v0pafkvn099r-Screenshot2023-05-16at14.36.29.png)<br><br>- Developers have access to the entire code base<br>- Operations are performed on a single repository (a server)<br>- Since changes are made to a central repository, other developers are not aware of code changes a developer makes until they merge it to the central repository.<br>- Developers work using local copy of the repo (_pulling_ the piece of code they need into their local machines), then commit their changes (_merging_ the changes into the repository) and resolve any possible conflicts<br>    <br>- Easy to learn and setup for Git beginners<br>    <br>- Difficult and time consuming to work on branches than in DVCS | ![](https://d36ai2hkxl16us.cloudfront.net/course-uploads/bf663a54-0bb6-4726-bd83-1e76668129cf/sfydhtclrtm8-Screenshot2023-05-16at14.46.46.png)<br><br>- Operations are performed on local servers or machines, instead of one single repository<br>- Offers more flexibility than CVCS and the possibility to work offline<br>- No need to depend upon the central server. The users can copy _(clone)_ the entire history of a project on their local machines and work independently<br>- Merge conflicts are less common than in CVCS, as  every developer work on their own piece of code. <br>- Getting the new change from a repository is called _pulling_; merging the local repository’s changes is called _pushing_<br>- Harder to start with for Git beginners<br>- It can take longer times to copy the entire repo into local machines if the project is big<br>- Developers tend to work in silos longer periods than when using CVCS |

**Benefits of version control**:

**1. Quality**
- Teams can review, comment, and improve each other's code and assets.
**2. Acceleration**
- Branch code, make changes, and merge commits faster.
**3. Visibility**
- Understand and spark team collaboration to foster greater release build and release patterns. Better visibility improves everything from project management to code quality.

# Common Git Terms and definitions

Branch:
A branch is an independent line of development.
- Used to develop features separate and isolated from your team
- Share and work on the same source code
- The main branch is the main (default) branch
- $ git branch *[branch_name]*

Tag:
Marks a specific point in time on a branch.
- Used to mark a code version release
- $ git tag

Checkout:
Get a specific branch to start making your changes.
- Create and navigate or switch between branches
- “Checking out” is the execution of the command $ git checkout

Commit:
Add changes you've made to the repository.
- Mechanism for saving changes to your local repository
- Point-in-Time Snapshot
- Commit snapshots are "safe" versions of a project - Git will never change them unless you explicitly ask it to.
- $ git commit

Push:
Send changes to a remote directory.
- Transfer or upload content from your local repository to the remote repository
- “Pushing” transfers commits from local -> remote repositories
    - Pushing exports commits $ git push
    - Fetching imports commits $ git fetch


![[Pasted image 20250723131045.png]]
![[Pasted image 20250723131034.png]]

[Download a Git Cheat Sheet!](https://about.gitlab.com/images/press/git-cheat-sheet.pdf?_gl=1*16x0kok*_ga*ODg3MzU2MDMxLjE2ODQzNTMxMjQ.*_ga_ENFH3X7M5Y*MTY4ODYwMjQxNy45Mi4wLjE2ODg2MDI0MTcuMC4wLjA.)

# Basic Git Workflow

The basic git workflow (agnostic of software used) involves isolating the work into different types of Git branches. Basically, the Git flow is a branching strategy - knowing when to use different types of branches during the development process, in order to organize and speed up the releases. In the usual Git flow, there are five different branch types: 

- **Main (or Master)** - created at the start of a project and is maintained throughout the development process. The main branch in the Git flow should contain production-ready code that can be released.
- **Develop** - Created at the start of a project; contains pre-production code with newly developed features that are in the process of being tested.
- **Feature** - the most common type of branch in the Git flow. It is used when adding new features to the code, basically the working branch which will be merged back into the development branch when the feature is ready
- **Release** - used when preparing new production releases
- **Hotfix** - used to quickly address necessary changes in the main branch

Each time you push a change, Git records it as a unique commit. These commits make up the history of when and how a file changed, and who changed it.

![](https://d36ai2hkxl16us.cloudfront.net/course-uploads/bf663a54-0bb6-4726-bd83-1e76668129cf/oqkyh06m81xj-Screenshot2023-05-16at15.04.19.png)

By default, the contents of a repository are in a default branch. To make changes, you need to work in your own branch.

> _Access the plus signs to learn more about each step._
![[Pasted image 20250723132246.png]]