






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
