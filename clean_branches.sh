echo "remove all branches but main"
git branch | grep -v "main" | xargs git branch -D 