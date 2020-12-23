sudo apt-get update
sudo apt-get install python-pip
pip install virtualenv
sudo apt-get install virtualenv
mkdir newproj
cd newproj
virtualenv venv
venv/bin/activate
pip install Flask
pip install mysql-connector-python

Run
python app.py
