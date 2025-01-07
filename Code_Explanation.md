## 1. Clean Data
* The data doesnt have duplicate values in customerID column.
* There are two variables that is neccesary to change their type ("SeniorCitizen", "TotalCharges"), which have int64 and object type respectively, so the type was changed to object and float64, because SeniorCitizen just have two values like a boolean variable and TotalCharges is a numerical variable.
* The data have missing values in the Charges sheet, specifically in MonthlyCharges and TotalCharges columns. Those columns should be define as follows:
  * TotalCharges = MonthlyCharges * Tenure
  * MonthlyCharges = TotalCharges / Tenure

This is not exact but it gives us an approximation. That's why the missing values ​​were filled in with those formulas.

## 2. Visualize data
a) Visualizing categorical data with Churn variable (target variable) we can see that exist a balance between classes in the principal variable "Churn" and in general we can see that most of the classes have a balance when we have to compare Churn in a specific class.
![image](https://github.com/user-attachments/assets/f39b02ea-0185-4c0e-bd0a-d5b036bca761)
b) Visualizing numerical data with boxplot. We can see that when the montlhy charges trend to be higher, ther churn rate is higher. When the tenure variable is higher, the user trend to no churn. Finally the TotalCharges doesnt give us clear information about the behaviour only that exist some outlyers in the data.
![image](https://github.com/user-attachments/assets/35f57adb-fd98-4e6b-9ce9-b831234438e9)
c) Visualizing numerical data with boxplot and histograms. We can see that the two variables doesnt have a known distribution except TotalCharges that seems to have a skew distribution like a exponential dist.
![image](https://github.com/user-attachments/assets/3e91045e-0a66-470b-a825-6b09e48968b6)
## 3. Modeling
The data was split in train and testing data (70-30). I tried four popular machine learning algorithms to predict potential churners on unseen testing data. (Logistic Regression, Random Forest, XGBC, Neural Networks). The data was scale with RobustScaler (This Scaler removes the median and scales the data according to the quantile range, beeing more robust to outliers).
## 4. Results
Metrics like accuracy, recall and AUC were calculated. In this case we have two options:
  1. If Telco want to avoid False Negatives: Telco doesnt want to have cases that the model predict negative but were actually a positive churn. In this case then the best model is a Neural Network because this model has fewer cases of FN.
  2. If Telco want a balance in the results: Telco want to avoid FN but also doesnt want to missclisified True Positive and True Negative. Then, the best is Logistic Regression, because have the best AUC value.

![image](https://github.com/user-attachments/assets/02c4d2a2-dcec-48c1-bd7d-7c3423018b9d)

## 5. BOOSTING
Depending on the answer of the client, we can improve the model, in this case I used GridSearchCV to try different parameters of the best model to find the one with the best AUC value. Obtaining the following results:

![image](https://github.com/user-attachments/assets/ede3b6d7-618c-4135-bdc5-fb604f60a8c2)





