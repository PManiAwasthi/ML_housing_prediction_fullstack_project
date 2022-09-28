# House Price Prediction using Machine Learning

### Software and account Requirement.

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documention](https://git-scm.com/gittutorial)
6. [Anaconda](https://www.anaconda.com/)


### Creating conda environment
```
conda create -p venv python==3.7 -y
```

```
conda activate venv/
```
OR
```
conda activate venv
```

### Now we install the packages and libraries
```
pip install -r requirements.txt
```

### Git commands
1. To add Files
```
git add .
```
> Note: To ignore a file or folder from getting tracked or uploaded to git we can write name of file/folder in .gitignore file

2. To check status of the files being tracked
```
git status
```

3. To commit the changes in the local git
```
git commit -m "message"
```

4. To push the final changes to the github repository branch
```
git push origin master
```

5. To view the logged information of git activities
```
git log
```

6. To check the remote url
```
git remote -v
```

### Build docker image
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name should be in lowercase

To list docker image
```
docker images
```

Run Docker image
```
docker run -p 5000:5000 -e PORT=5000 6f771ff2395a
```

To check if a image is running
```
docker ps
```


To stop a docker image
```
docker stop <container_id>
```