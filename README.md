# HW-todo-api, Andrew's Observations

An API is short for Application Programming Interface. As the name states, you are interacting with a current program or interface and can modify it by using a computer programming language. The current interface that is being modified can also be integrated with one or many other applications through API’s.

To design an API, the following is needed:
Code: To design a website, you need to code it. In this tutorial Python will be used.

Framework - This is a special type of package that you must download within your IDE that enables the API Web Application.Once again, we will be using Python alongside a framework called Flask. 

Packages - Flask is a package and can be downloaded using “pip install flask” and before running this command, pip must be downloaded to run this command as well
Virtual Environment - A special environment must be created and then enabled to run the framework which will ultimately run the scripts 

Database - While connecting different applications, data must be queried or stored in a secure stable place. The database is responsible for this. 

Steps:
Open up IDE 

Make two py.scripts called main.py and helper.py. Be aware of the directories you place these two files in. It would be recommended to place both of these files in one folder. main.py has the main code to deploy urls with text, while helper.py includes functions to help run main.py. 

In the directory or folder where main.py and helper.py is, cd to that directory and create a virtual environment. This is done by running the command: 

Windows: py3 -m venv “name of environment”

or

Linux: python -m venv “name of environment”

The purpose of the environment is for a place for the website to deploy 

To activate the environments run this command:

Windows: “name of environment”\Scripts\activate

Linux: source “name of environment”/bin/activate

After activating the environment in the CMD you are using, you should see next to the user name (“name of environment”). This shows the environment is successfully running. 
You can install packages in the environment once you see () and those packages remain there when the environments start up. Run pip install flask to install flask in the environment
Before running the script, you need a place to store your data. Once again, a database is needed and must be implemented. This is done by installing and using the program DB Browser SQLite.

Make a file called todo.db and place it in the same directory as your main.py and helper.py

After creating the database, a popup appears to make changes. Implement the following adjustments below for a basic database:

![f](https://user-images.githubusercontent.com/65320854/131421867-ea13f4c3-249a-464a-ac5b-7086ffc43ef9.PNG)


 
Run the script main.py by either doing:

python “main.py” (need a __name__ == main in the script)

FLASK_APP=main.py flask run
Where main.py is inserted for the code for b., that can be the name for any script and it should run

After running the app, a url to deploy your website should appear. To stop the script, press CTRL + C. 

Open another terminal tab when the website is being run, use CURL commands to receive outputs from the website.  

Changes:There are no changes in my code

Notices:
@app.route(‘/.../...’) where the … is, you can add text to the url. After deploying the website, you can see the url is changed to the text you inserted in place of …
Sometimes, if a CURL command gives an error, go back to your db file and cancel the request that went through. Then re-run the curl command and it should work 

Another alternative is if a CURL command gives an error, exit out of the website for which terminal tab is running and then re-run the website again with the CURL command

The code with the dictionaries commands, you can edit the strings to change the name

There are many differences when writing code to operate in the Windows and Linux terminal to do the following commands:

cd to directories

Making environments

Activating environments

Running python scripts

After making an edit to the url through app route, you will have to include the edited urls in the CURL command as well
You can deploy a website through a VM, but it will reveal your IP regardless when a website is deployed


