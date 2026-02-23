
## Day 25 – Git Reset vs Revert & Branching Strategies

## Challenge Tasks

### Task 1: Git Reset — Hands-On

1. Make 3 commits in your practice repo (commit A, B, C)

<img width="1000" height="687" alt="Task1-ques1" src="https://github.com/user-attachments/assets/dc4613a4-abbf-45c4-8224-949f065d1e95" />

<img width="554" height="87" alt="task1-ques1-part2" src="https://github.com/user-attachments/assets/f752bd72-558f-41eb-813c-53a718a08977" />

2. Use git reset --soft to go back one commit — what happens to the changes?

<img width="592" height="179" alt="task1-ques2-part1" src="https://github.com/user-attachments/assets/554ceba6-1fb4-491f-bc29-936a6d9f0184" />

<img width="561" height="359" alt="task1-ques2-part2" src="https://github.com/user-attachments/assets/0f2a8756-4392-4a4a-88d9-bf63ef4e6f5e" />

Before running git reset command repository contains three commits in sequence:

Commit A → Commit B → Commit C (HEAD, main)

#### What Happens when git reset --soft HEAD~1 is executed:

Commits        : A → B (HEAD)

* HEAD moves from Commit C → Commit B

* Branch main also points to Commit B

* Commit C is removed from commit history

* Changes from Commit C are:

    - Preserved

    - Kept in the staging area

#### Reset command moves only the commit pointer

      Does NOT modify:

    - Working directory files

    - Staging area contents


#### Use Cases

*  Editing or fixing the last commit message

*  Squashing commits before pushing

*  Cleaning up commit history before opening a PR

*  Recommitting changes in a better logical structure

