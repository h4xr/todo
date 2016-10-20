# **To-Do Application**
### How to Run the example

1. Get the codebase in your development machine by executing `git clone https://github.com/h4xr/todo todo`
2. Now, get into the todo directory that was created due to the above step by executing `cd <path_to_directory>`
3. The next step is to setup a virtual environment for the project since it will help us in keeping our dependencies isolated from the rest of the system. To create virtual environment, we can execute the following command `virtualenv venv`. This will create a virtual environment named *venv* inside the project folder.
4. The next step is to activate the virtual environment. For this, execute, `source venv/bin/activate`
5. Next, we need to get the required dependencies in our system for running the example. The dependencies are listed inside *requirements.txt*. The pip tool can help you setup the required dependencies for the same. Execute the following command to setup the dependencies: `pip install -r requirements.txt`
6. At this point of time, we have all the required dependencies setup in the system. Its time to run our microservices. It can be achieved by executing `python run.py`
7. You can verify whether the services are running properly or not by visiting `http://localhost:5000`
