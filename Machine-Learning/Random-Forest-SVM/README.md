## End to End Project Life Cycle

Steps:

1. Do EDA
2. Then Do Feature Engineering
3. Then Do Feature Selection
4. Then Create a model.


- Model is a file that gives us some output after giving some input.

After model is created, we need to use this model in the production environment.

**Steps:**

1. Convert this model into pickle file format.
There are different ways to convert the model. we can save it as .sav file, .pkl file.

2. In a real world application, once model is created, with the help of flask framework, we can create front end side. 

3. With in this flask, we create an API. Inside the API, we load the pickle file, give the inputs and do the prediction.

**Example**: let's say the api is */predict*.

4. We give the inputs to this API which inturn give us the outputs as prediction.

5. We can use this flask api everywhere to use this model.

Example:

- In netflix, there is a recommendation module. - If netflix wants to use the recommendation, it will hit the recommendation module.
- In response we get the output.


**Summary:**

- First of all, Convert the model into a pickle file. 
- Then start creating the flask application.
- In that flask application, create prediction API.
- Inside the API, load the model and do the prediction.






