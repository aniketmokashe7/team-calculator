# Fetch vs Pull

- `git fetch` downloads objects and refs from remote, updating remote-tracking branches (e.g., origin/master) but does NOT modify your current branch.
- `git merge origin/master
` merges the fetched changes into your current branch.
- `git pull` = `git fetch` followed by `git merge` (default), so it fetches and then merges in a single command.

Use fetch when you want to inspect updates before merging.
EOF