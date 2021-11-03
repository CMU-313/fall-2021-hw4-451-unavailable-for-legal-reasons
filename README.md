# Software Engineering for Machine Learning Assignment

## Documentation of API
- Follow Deployment Instructions to get the API running.
- The API expects input from the client in the form of a JSON string, which includes the features selected for the ML model, consisting of `G1`, `G2`, `Studytime`, `Absences`, `Age`, and `Health`. It should be stored in a .json file under the same directory as the `client.py` file. 
- To obtain the prediction of whether the student will succeed from the ML mode, compile and run the `client.py` file.
- The output will be in the form of a json object the key "prediction". If the value field is 0, the student is likely to fail. If the value field is 1 the student is expected to succeed.

## Information on ML model
The baseline model had 3 features, Health, Age and Absences. In our new model, we trained using the existing 3 features and 3 additional features, Studytime, G1 score and G2 score. The retrained model shows a large improvement in F1 score, from 52.2% to 95.8%.

This can be attributed to the fact that the additional features provided more information, allowing for more accurate predictions. In particular, it is important to note that our target performance metric is G3 score, which represents the final year grade. Given that the grade that a student is expected to get is typically influenced by the amount of time the student spends studying for the test and their performance on previous tests, Studytime as well as the G1 and G2 scores, which represents the first and second period grades respectively would serve as effective features to predict G3 score.

We also attempted cross validation to optimize the hyperparameters of the random model. We specifically optimized 4 hyperparameters and found that the optimal values are as follows:
```
n_estimators : 2000
max_features: 'auto'
max_depth: 10
bootstrap: True
 ```

However, the results obtained from cross validation were comparable to that obtained from the model without cross validation. This is likely because the optimal values obtained from cross validation are very similar to the default values for the Random Forest model, which were used for the model without cross validation. Specifically, the cross-validated model used `n_estimators = 2000` instead of `1000` and `max_depth=10` instead of `None`.

As there was no significant improvement for the model with cross validation, the model without cross validation was deployed for prediction.

The code used for the training of the model and cross validation can be found at [model_build.ipynb](https://github.com/CMU-313/fall-2021-hw4-451-unavailable-for-legal-reasons/blob/master/model_build.ipynb).

## Deployment Instructions
To run this app, navigate to `dockerfile/` directory.

1. Build the docker container
`docker build -t ml:latest .`

2. Run the docker container
`docker run -d -p 5000:5000 ml`

Confirm that the app is running by navigating to `localhost:5000`.

## Manual and Automated Testing
For the ML model, we tested using the F1 score metric from the Scikit-learn library to obtain an accuracy score on unseen data.
For the microservice, we did both GitHub actions, which allowed for CI testing, and pytest.
