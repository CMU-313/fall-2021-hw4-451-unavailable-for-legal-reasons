# Software Engineering for Machine Learning Assignment

Please consult the [homework assignment](https://cmu-313.github.io//assignments/hw4) for full context and instructions for this code.  

Documentation of API:

Running the app:
- To run this app, in the `dockerfile` directory, run `docker build -t ml:latest .`
- After building your code, run `docker run -d -p 5000:5000 ml` to create a docker container.
- See the app in `localhost:5000`
- The input from the client is expected to be a JSON file, which includes the features selected for the ML model, consisting of Studytime, Absences, Age, and Health. It should be stored under the same directory with the client file. 
- To obtain the prediction of whether the student will succeed from the ML mode, compile the client.py file.
- The output of value 0 of the prediction indicates that the student is likely to fail, and the model predicting 0 means that the student is expected to succeed.
