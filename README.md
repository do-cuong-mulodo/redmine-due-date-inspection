# Setup environment for MAC

### Installing python (skip this if already done)
- brew install python3

### create a new virtual environment called myvenv (skip this if already done)
- python3 -m venv ~/.virtualenvs/myvenv

### activate this virtual environment
- source ~/.virtualenvs/myvenv/bin/activate

### Installing flask (skip this if already done)
- pip install Flask

### Installing Redmine Library (skip this if already done)
- pip install python-redmine

### Run app
- cd src && python app.py

### Test
- Open browser and enter the URL:
- http://localhost:5000/api/issues/without-due-date

### Setup Sonarqube Server (skip this if already done)
- Setup Sonarqube Server runing on localhost:19000 (You can clone the source code from this link https://github.com/mulodo-vietnam/vcs-inspection and startup docker sonaqube server)

### analyze with SonarQube
- sonar-scanner -Dsonar.projectKey=xxx -Dsonar.sources=.

### Check source code with SonarQube
- Go to http://localhost:19000/ and login as admin
- Navigate Projects tab and Select project "Using Sonar Scanner to scan python project"