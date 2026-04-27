---
description: "Stage, commit, and push repository changes"
argument-hint: "Commit message"
agent: "agent"
---

Run these Git commands in order:

1. `git add .`
2. `git commit -m "${input:commitMessage}"`
3. `git push`
