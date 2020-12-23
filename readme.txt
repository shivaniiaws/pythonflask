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

CREATE TABLE IF NOT EXISTS emp (
  `emp_id` int(11),
  `emp_name` varchar(150) ,
  `email` varchar(150) ,
  `phone` varchar(100) 
) 


INSERT INTO `emp` (`emp_id`, `emp_name`, `email`, `phone`) VALUES
(1, 'John', 'john@example.com', '2323234543'),
(2, 'Smith', 'smith@example.com', '9898577442'),
(3, 'Priska', 'priska@example.com', '9393452387'),
(4, 'Gaga', 'gaga@example.com', '8482764537');


github.com/bradtraversy/myflaskapp
