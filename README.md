# Software Engineering for Machine Learning Assignment

## Documentation of API

Running the app:
- To run this app, in the `dockerfile` directory, run `docker build -t ml:latest .`
- After building your code, run `docker run -d -p 5000:5000 ml` to create a docker container.
- See the app in `localhost:5000`
- The input from the client is expected to be a JSON file, which includes the features selected for the ML model, consisting of Studytime, Absences, Age, and Health. It should be stored under the same directory with the client file. 
- To obtain the prediction of whether the student will succeed from the ML mode, compile the client.py file.
- The output of value 0 of the prediction indicates that the student is likely to fail, and the model predicting 0 means that the student is expected to succeed.

## Information on ML model
The baseline model had 3 features, Health, Age and Absences. In our new model, we trained using the existing 3 features and 3 additional features, Studytime, G1 score and G2 score. The retrained model shows a large improvement in F1 score, from 52.2% to 95.8%.

This can be attributed to the fact that the additional features provided more information, allowing for more accurate predictions. In particular, it is important to note that our target performance metric is G3 score, which represents the final year grade. Given that the grade that a student is expected to get is typically influenced by the amount of time the student spends studying for the test and their performance on previous tests, Studytime as well as the G1 and G2 scores, which represents the first and second period grades respectively would serve as effective features to predict G3 score.

We also attempted cross validation to optimize the hyperparameters of the random model. We specifically optimized 4 hyperparameters and found that the optimal values are as follows:
```
“n_estimators' : 2000
 'max_features': 'auto'
 'max_depth': 10
 'bootstrap': True
 ```

However, the results obtained from cross validation were comparable to that obtained from the model without cross validation. This is likely because the optimal values obtained from cross validation are very similar to the default values for the Random Forest model, which were used for the model without cross validation. Specifically, the cross-validated model used `n_estimators = 2000` instead of `1000` and `max_depth=10` instead of `None`.

As there was no significant improvement for the model with cross validation, the model without cross validation was deployed for prediction.

The code used for the training of the model and cross validation can be found at [model_build.ipynb](https://github.com/CMU-313/fall-2021-hw4-451-unavailable-for-legal-reasons/blob/master/model_build.ipynb).
