# Day 23 – Git Branching & Working with GitHub

## Task 1: Understanding Branches

### What is a branch in Git?

A branch is a separate path where you can work on changes without affecting the main code.

You copy the project, work freely, and later decide whether to add it back.

Command to see branches

- git branch

Command to create a new branch

- git branch feature-login

Command to switch to that branch
- git checkout feature-login

(or modern way)

- git switch feature-login


### Why do we use branches instead of committing everything to main?

We don’t commit everything to main because:

main should always be stable

New features may break things

Bugs should not affect working code

Branches allow:

Safe experimentation

Clean and organized work

Easy collaboration

### What is HEAD in Git?

HEAD is a pointer that tells Git:

“This is where you are right now.”

It points to:

The current branch

The latest commit on that branch

### What happens to your files when you switch branches?

When you switch branches:

- Git updates your files automatically

- Files change to match the selected branch

  * Uncommitted changes may stop the switch

