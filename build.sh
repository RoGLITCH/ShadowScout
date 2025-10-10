eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
git add .
git commit -m "$1"
git push
