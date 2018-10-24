# Welcome to Git Feature Branching!
The goal here is to provide a series of training steps and an environment in which to practice the principles and processes associated with feature branching and how they can speed up and improve your development lifecycle.

## Some Things to Remember:
In Git, branches are cheap. You should use them whenever you're making changes to your repository.  
Commit early and often. Git only takes full responsibility for your data when you commit. If you fail to commit and then do something poorly thought out, you can run into trouble. Additionally, having periodic checkpoints means that you can understand how you broke something. 


## Let's Get Started
Follow these steps to walk through a basic feature implementation process using both TFS work items and Git Feature Branches. This document is designed to cover the git bash command line, the sourcetree GUI tool, or the Git tools for Visual Studio. There are dozens of other options and the choice is yours as to which you use in the end. Visual studio 2013+ comes with the Git tools installed, you can find SourceTree and the commandline tools here:  
https://git-scm.com/downloads  
https://www.sourcetreeapp.com/

We will also be using the TFS web UI to access work items, pull requests and to explore some of the options to link work items with your work.

## Step 1: Clone your repository and take a look at the existing code and branches
**The first thing we need is a copy of the existing code from the server. Cloning a repository will make a local copy using the repo on the server. This includes history and individual commits, as well as the details of what existing branches are available.**

#### Command line
1. Use the 'cd' command to change to the directory in which you would like to create a folder for our training repository.
   * **mkdir C:/_TFS**
   *  **cd C:/_TFS**
2. use the 'clone' command to make a copy of the server repository. You can specify a folder name in which to put the code
   * **git clone http://temptfs:8080/tfs/migration/DevOpsTraining/_git/Feature%20Branching FeatureBranching**
3. If you are prompted for credentials, use your Aptean provided single sign-on creds.
4. Once the clone finishes, open the FeatureBranching folder in file explorer. Here we have the readme file, as well as a folder for a visual studio solution, and a number of text files as this training project rolls on.
5. use the 'cd' command to change to this new folder.
   * **cd FeatureBranching**
6. Let's take a look at what branches we have. use the 'branch' command to list the branches, either locally, remote or both
   * **git branch** <-- this will show your local branches. Since we just started, this should only show 'master'
   * **git branch -r** <-- this will show the remote branches. There should be a number of feature branches already prefixed with 'feat/'
   * **git branch -a** <-- this will show all the branches, local and remote. The branches are color coded according to local/remote  
   * ![alt text](/Readme-Images/CLI_branches.PNG "A list of the branches in this repository")  
7. use the 'checkout' command to change branches, adding it to your local list of branches, and update your local repository directory to reflect the state of the code on that branch.
   * **git checkout feat/1-SomeNewFeature**
8. You can see that on the feat/1-SomeNewFeature branch, a number of the text files in the root folder don't exist like they do on master. Also, a number of the .cs files in the FB-Project directory have different contents between this branch and master. You can change back and forth between the branches and view the changes between these 2 versions of the code base.  
   * ![alt text](/Readme-Images/CLI_master_file_state.PNG "The state of the files on master") ![alt text](/Readme-Images/CLI_feature_file_state.PNG "The state of the files on feat/1-SomeNewFeature")  
9. use the checkout command again to change back to the master branch once you are done looking around.
   * **git checkout master**

#### SourceTree
1. If you aren't already on a 'New Tab' in source tree, click the + icon to open one.
2. Select the 'Clone' option from the top menu bar.
3. Fill in the fields related to our repository. Create the directories where required
   * **Source Path / URL:** http://temptfs:8080/tfs/migration/DevOpsTraining/_git/Feature%20Branching
   * **Destination Path:** C:/_TFS/FeatureBranching
   * **Name:** Feature Branching Training Repo  
   * ![alt text](/Readme-Images/ST_clone.PNG "Cloning a repo in SourceTree")  
4. Click 'Clone'
5. Once the clone finishes, open the FeatureBranching folder in file explorer. Here we have the readme file, as well as a folder for a visual studio solution, and a number of text files as this training project rolls on.
6. Back in SourceTree, in the left hand tree view, we can see the only local branch is 'master'. Expanding the 'remotes' section will show us a number of branches that exist only on the remote currently. There should be a number of feature branches already prefixed with 'feat/'
7. The central window shows the graph of existing branches and helps provide a visual representaion of the states of various branches.  
   * ![alt text](/Readme-Images/ST_branches.PNG "The main SourceTree window")   
8. In the left hand tree view, expand Remotes >> origin >> feat. Right click the '1-SomeNewFeature' branch, select 'checkout origin/feat/1-SomeNewFeature...' and click ok on the proceeding window. This will change your working branch to this feature branch, adding it to your local list of branches and update your directory to reflect the state of the code on that branch.
9. You can see that on the feat/1-SomeNewFeature branch, a number of the text files in the root folder don't exist like they do on master. Also, a number of the .cs files in the FB-Project directory have different contents between this branch and master. You can change back and forth between the branches and view the changes between these 2 versions of the code base.
10. Again in the left hand tree view, under 'Branches', right click 'master' and select 'checkout master...' to change back to the master branch once you are done looking around.

#### Visual Studio
1. Open Team Explorer and click the green 'Manage Connections' button.
2. Once you are on the 'Connect' view, expand manage connections and select 'Connect to Team Project'.
   * ![alt text](/Readme-Images/VS_connect.PNG "Connect to Team Project")
3. Click the 'Servers' button and 'Add' to add the server connection details.
   * **Name of Team Foundation Server:** temptfs
   * **Path:** tfs
   * **Port Number:** 8080
   * **Protocol:** http
   * ![alt text](/Readme-Images/VS_add_server.PNG "Adding a server to connect to")
4. Select this new server from the server drop down and check the box next to 'DevOpsTraining' and click 'Connect'
   * ![alt text](/Readme-Images/VS_connect2.PNG "Connect to Server")
5. Go back to the manage connections view and expand our newly added server and project. Right click the 'Feature Branching' repository and select 'Clone'.
6. Enter a file path in which to clone the repository, creating the directories where required
   * **C:\_TFS\Feature_Branching**
7. Click 'Clone'
   * ![alt text](/Readme-Images/VS_clone.PNG "Cloning a repo in Visual Studio")
8. Once the clone finishes, open the FeatureBranching folder in file explorer. Here we have the readme file, as well as a folder for a visual studio solution, and a number of text files as this training project rolls on.
9. Back in Visual Studio, double click the repository under the server and project name to go to the home page for this repository.
10. Click the 'Branches' button to view all of the available branches.
11. Expand remotes/origin >> feat. Right click the '1-SomeNewFeature' branch, select 'Checkout'. This will change your working branch to this feature branch, adding it to your local list of branches and update your directory to reflect the state of the code on that branch.
   * ![alt text](/Readme-Images/VS_checkout_branches.PNG "Moving between branches")
12. You can see that on the feat/1-SomeNewFeature branch, a number of the text files in the root folder don't exist like they do on master. Also, a number of the .cs files in the FB-Project directory have different contents between this branch and master. You can change back and forth between the branches and view the changes between these 2 versions of the code base.
13. Right click 'master' and select 'Checkout' to change back to the master branch once you are done looking around.

## Step 2: Set up your work item  
**We will use the TFS web UI to create a work item that will represent some new feature or task that we have been assigned.**

#### TFS Web UI
1. Go to the TFS Use Case board for this training project: http://temptfs:8080/tfs/migration/DevOpsTraining/_backlogs/board/Use%20Cases
2. In the 'Backlog' column, select 'New Item' and choose 'Use Case'.
3. Create a title for the work item, starting with your name
   * **Drew Grubb: Training Feature**
4. Fill out any required fields (their values are not important) and select 'save and close'
5. We have the option to create a branch from within the TFS work item UI. There is nothing wrong with this approach, but we are going to create the branch externally to TFS. This approach is agnostic to what tool is hosting your git repository and will carry over to GitHub or any other tool also. You can find a few more details on ways to link work items to Git code here: 
   * https://blogs.msdn.microsoft.com/devops/2016/03/02/linking-work-items-to-git-branches-commits-and-pull-requests/
6. Drag the work item card into the 'In Progress' column since we are ready to do some on our new feature. Repeat the process of filling out required fields and save the changes.  
   * ![alt text](/Readme-Images/TFS_work_item.PNG "A work item in the TFS board")  

## Step 3: Make a branch and write some code
**Now that we have a unit of work to do, we need somewhere to do that work. It is time to make a branch**

#### Command line
1. Use the 'pull' command to get the latest code from the remote, and bring any changes onto your branch. This will ensure our local master is up to speed with the server before we branch off.
   * **git pull** 
2. use the 'checkout' command to create a new branch (your feature branch) off of the current branch (master). You should prefix your branch name with 'feat/' followed by your name.
   * **git checkout -b feat/DrewGrubb**
3. Lets make some conflict free changes to start. In the root of the FeatureBranching folder, create a new text file and name it with your name.
4. Use the 'status' command to check the current state of our local branch. we should see 1 new untracked file.
   * **git status**
5. Use the 'add' command to stage the changed files so that we can commit them. *note: there are 3 states in your git repository, untracked/modified >> staged >> commited*
   * **git add -A** <-- add all untracked and modified files to my staged collection  
   ![alt text](/Readme-Images/CLI_status_add.PNG "Staging our untracked work")  
6. Use the 'commit' command to create a commit of all our staged work
   * **git commit -m"added a new text file"** <-- commits the staged files and adds a message
7. Use the 'push' command to move your changed to the remote so that other developers can access it, and have it be preserved on the server.
   * **git push origin feat/DrewGrubb**
8. Now that the 'code' has been written, lets update our work item in TFS. Drag the work item into peer review, then testing (resolving any required fields in the usual way).
9. Let's assume our work meets the definition of done, and it can now be merged into the master branch. Use the 'merge' command to pull master into your feature branch. *Note: we merge into the feature branch first to ensure merge conflicts get resolved outside of the 'pristine' master code. We aren't expecting any conflicts here as we are adding a brand new file.*
   * **git merge origin/master**
10. Once master has been successfully merged into your branch, and any conflicts resolved, all this work can be merged into master. Use the checkout command to change to the master branch, and the merge command to bring your feature branch code into it.
   * **git checkout master**
   * **git merge feat/DrewGrubb**
11. Finally, we need to push the new code on master back to the remote so that other developers can consume it.
   * **git push origin master**
12. Now that the code is in master, go back to the TFS board and move the work item to 'resolved'.

#### Source Tree
1. In the top ribbon, click the 'Pull' button to get the latest code from the remote. Ensure the 'Remote branch to pull' is set to master and click ok.
2. In the top ribbon, click the 'Branch' button to create a new branch. In the 'New branch' field, enter a branch name of 'feat/' followed by your name and click 'Create Branch'.  
   * ![alt text](/Readme-Images/ST_new_branch.PNG "Make a new branch from master")  
3. Lets make some conflict free changes to start. In the root of the FeatureBranching folder, create a new text file and name it with your name.
4. At the top of the graph view, click on the 'Uncommited changes'. The lower half of the application should show the new text file in the 'Unstaged files' collection.  
   * ![alt text](/Readme-Images/ST_uncommitted_changes.PNG "We have uncommitted changes")  
5. Click the 'Stage all' button to move all the files to the staged collection so that we can commit them. *note: there are 3 states in your git repository, untracked/modified >> staged >> commited*
6. In the top ribbon, click the 'Commit' button to create a commit of all our staged work. Enter a comment like "added a new text file" in the text area at the bottom of the window and click 'Commit'.
7. In the top ribbon, click the 'Push' button to move your changes to the remote so that other developers can access it, and have it be preserved on the server. Select the checkbox next to the new branch we are working on to select it, and click 'Push'  
   * ![alt text](/Readme-Images/ST_push.PNG "Push our committed work to the server")  
8. Now that the 'code' has been written, lets update our work item in TFS. Drag the work item into peer review, then testing (resolving any required fields in the usual way).
9. Let's assume our work meets the definition of done, and it can now be merged into the master branch. In the top ribbon, click the the 'merge' button to pull master into your feature branch. In the graph view, find and select the commit associated with origin/master, select it and click 'Ok'. *Note: we merge into the feature branch first to ensure merge conflicts get resolved outside of the 'pristine' master code. We aren't expecting any conflicts here as we are adding a brand new file.*
10. Once master has been successfully merged into your branch, and any conflicts resolved, all this work can be merged into master. Use the right click and checkout method to change back to the master branch. Click the merge button again, select the topmost commit of your feature branch and bring your feature branch code into master.  
   * ![alt text](/Readme-Images/ST_merge.PNG "Merge master into our feature branch")  
11. Finally, we need to push the new code on master back to the remote so that other developers can consume it. Click the push button again, select the correct checkbox and click push.
12. Now that the code is in master, go back to the TFS board and move the work item to 'resolved'.

#### Visual Studio 
1. In the branches view in Team Explorer, right click our 'FeatureBranching' repository and select 'New Local Branch From...' to create a new branch to do our work in.
2. In the 2 fields that appear at the top, select master as the existing branch to branch from. For the branch name, you should prefix your branch name with 'feat/' followed by your name.
   * ![alt text](/Readme-Images/VS_new_branch.PNG "Making a new branch")
3. Ensure the box for 'Checkout branch' is selected and click 'Create Branch'
4. Lets make some conflict free changes to start. In the root of the FeatureBranching folder, create a new text file and name it with your name.
5. In Team Explorer, change from the 'Branches' view to the 'Changes' view. Here you will see our new text file under the changes collection. Use the + button to stage the changed files so that we can commit them. *note: there are 3 states in your git repository, untracked/modified >> staged >> commited*
   * ![alt text](/Readme-Images/VS_uncommitted_changes.PNG "Staging the changes")
6. Enter a commit message for our unit of work and click 'Commit Staged' to preserve it in our local repository.
   * ![alt text](/Readme-Images/VS_commit.PNG "Commit the staged changes")
7. Change to the 'Sync' view in Team Explorer. Under 'Outgoing Commits', click 'Publish' to create the branch on the server and move your commits to the remote so that other developers can access it, and have it be preserved on the server. *note: subsequent commits to this same branch will be moved to the server via 'Push' rather than publish. Publish is for initial branch  creation on the server only.*
8. Now that the 'code' has been written, lets update our work item in TFS. Drag the work item into peer review, then testing (resolving any required fields in the usual way).
9. Let's assume our work meets the definition of done, and it can now be merged into the master branch. Back on the 'Branches' view, click on 'Merge'. Use the branch selectors to pull master into your feature branch. *Note: we merge into the feature branch first to ensure merge conflicts get resolved outside of the 'pristine' master code. We aren't expecting any conflicts here as we are adding a brand new file.*
10. Once master has been successfully merged into your branch, and any conflicts resolved, all this work can be merged into master. Click 'Merge' again and bring your feature branch code into master.  
11. Finally, we need to push the new code on master back to the remote so that other developers can consume it. Back to the 'Sync' view again and click 'push' under the outgoing commits.
12. Now that the code is in master, go back to the TFS board and move the work item to 'resolved'.

## Step 4: Resolve a merge conflict
**We will use our new text file to create 2 differing changes in 2 separate branches and resolve the conflict that occurs when we try to bring them together. While we will be using 2 separate feature branches of our own making to illustrate this, this process is the same when resolving merge conflicts when bringing other developer's code into your branch also.**

#### Command Line
1. Ensure you are on the master branch, use the 'checkout' command to change branches if you need to
   * **git checkout master**
2. Use the 'checkout' command again to make a new branch off of master. Prefix it with 'feat/' and your name again and add a number to the end
   * **git checkout -b feat/DrewGrubb-1**
3. Swap back to master again and make a second feature branch. Increment the number at the end
   * **git checkout master**
   * **git checkout -b feat/DrewGrubb-2**
4. While on one of the branches, open the text file we created initially and put some text in it.
5. Stage and commit the work (pushing is optional here as this work can just live locally for the purposes of resolving with a merge conflict)
   * **git add -A**
   * **git commit -m"added some text to my text file"**
6. use the 'checkout' command to change to the other branch you created, open the text file again and put some different text in it.
7. Stage and commit your work again.
   * **git add -A**
   * **git commit -m"added some text to my text file"**
8. Use the 'merge' command to bring the changes from your other branch, into the one you are currently on.
   * **git merge feat/DrewGrubb-2** <-- Bring changes from feat/DrewGrubb-2 into the current branch (feat/DrewGrubb-1 in this case)
9. You will be informed that there are merge conflicts and asked to fix them, then commit the result. Open the text file and clean up the text, place each of your messages on its own line. *Note: There are dozens of tools to help resolve conflicts, but they are beyond the scope of this training project. For now, we will resolve them manually*  
   * ![alt text](/Readme-Images/CLI_merge_conflict.PNG "Merging branches with conflicting changes")  
10. use the add command to stage our changes (the resolution of the conflict) and make a commit.
   * **git add -A**
   * **git commit -m"resolved merge conflicts in my personal text file"**

#### Source Tree
1. Ensure you are on the master branch, use the Right click checkout approach to change branches if you need to
2. Click the 'Branch' button again to make a new branch off of master. Prefix it with 'feat/' and your name again and add a number to the end.
3. Swap back to master again and make a second feature branch. Increment the number at the end.
4. While on one of the branches, open the text file we created initially and put some text in it.
5. Stage and commit the work (pushing is optional here as this work can just live locally for the purposes of resolving with a merge conflict).
6. Right click and checkout the other branch you created, open the text file again and put some different text in it.
7. Stage and commit your work again.
8. Use the 'merge' button to bring the changes from your other branch, into the one you are currently on. You should be notified of conflicts. Open the text file and clean up the text, place each of your messages on its own line. *Note: There are dozens of tools to help resolve conflicts, including some built into SourceTree but they are beyond the scope of this training project. For now, we will resolve them manually*  
   * ![alt text](/Readme-Images/ST_merge_conflict.PNG "Merging 2 branches with conflicting changes")  
9. Stage our changes (the resolution of the conflict), enter a commit message and click commit.

#### Visual Studio
1. Ensure you are on the master branch, use the Right click checkout approach to change branches if you need to.
2. Right click the master branch and select 'New Local Branch From...' and make a new branch off of master. Prefix it with 'feat/' and your name again and add a number to the end.
3. repeat this process to make a second feature branch. Increment the number at the end.
4. While on one of the branches, open the text file we created initially and put some text in it.
5. Stage and commit the work (pushing is optional here as this work can just live locally for the purposes of resolving with a merge conflict).
6. Right click and checkout the other branch you created, open the text file again and put some different text in it.
7. Stage and commit your work again.
8. Select 'Merge' on the branches view, select our 2 feature branches as the candidates to be merged together and click 'Merge'. You should be notified of conflicts. Click the conflicts notification to see some options related to resolving merge conflicts. For this leab, you can simply choose either 'Take Source', or 'Keep Target'. *Note: There are dozens of tools to help resolve conflicts, including some built into Visual Studio but they are beyond the scope of this training project.*
   * ![alt text](/Readme-Images/VS_merge_conflict.PNG "Merge conflicts")  
9. Once the merge is resolved, click 'Commit merge'. Stage our changes (the resolution of the conflict), enter a commit message and click commit.


## What Now?
If you are planning to go the command line route long term, this cheat sheet is a great reource to help get a grip on the commands you will need.  
https://www.git-tower.com/blog/git-cheat-sheet/

There is never an end to things you can learn. Here are a couple links to additional reading if you feel like continuing beyond the scope of this training.  
https://git-scm.com/book/en/v2  
https://sethrobertson.github.io/GitBestPractices/

Now that you have a basic understanding of how to make use of Git, Feature branches and the processes that support these, think about how you can put this to work on your products.

##Happy Branching!