UPDATE=$(date +%Y%m%d)

git init
git add *
git commit -m "commit${UPDATE}"
git remote add origin https://github.com/mbenedicto99/MedChaiin.git
git push -u origin master
