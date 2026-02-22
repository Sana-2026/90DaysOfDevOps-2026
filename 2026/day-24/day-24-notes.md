





 ## 🔀 Merge vs Squash
| Feature | Normal Merge (`git merge`) | Squash Merge (`git merge --squash`) |
|-------|----------------------------|-------------------------------------|
| Keeps all commits | ✅ Yes | ❌ No |
| Creates merge commit | ✅ Yes | ❌ No |
| Preserves branch history | ✅ Yes | ❌ No |
| Commit history | Detailed | Clean & compact |
| Easy to understand history | ❌ Can be messy | ✅ Very clean |
| Rollback changes | ❌ Hard (many commits) | ✅ Easy (single commit) |
| Common usage | Long-running branches, open-source | Feature branches, PRs |
| Used in GitHub PRs | ⚠️ Sometimes | ✅ Very common |


## 🔀 Rebase vs Merge

| Feature | `git merge` | `git rebase` |
|-------|-------------|--------------|
| What it does | Combines two branches | Replays commits on top of another branch |
| Commit history | Preserved | Rewritten |
| Merge commit | ✅ Yes (for non fast-forward) | ❌ No |
| Commit hashes | Remain the same | Change |
| History shape | Branching graph | Linear / straight line |
| Conflict handling | Once per merge | Possibly once per commit |
| Safe for shared branches | ✅ Yes | ❌ No |
| Common usage | Merging feature → main | Updating feature branch with main |
| Industry preference | Safer, more explicit | Cleaner, more readable history |
| Risk level | Low | Medium (if misused) |
