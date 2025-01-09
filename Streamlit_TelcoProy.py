import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import RobustScaler

'''
This code was made in sustitution of the presentation, because the presentation depends on how do you present your results, there is no just one correct way to present, just be creative.
But instead this code was made to present a quick deployment of the model created.
Streamlit is open-source app framework. You can know more about in this link https://streamlit.io/#install
There is some thinks that you need to know to be able to develop the streamlit proyect:
1) Create an account on streamlit.
2) Install it in your environment (in my case i am using Visual Studio Code).
3) Read the documentation of streamlit.
In this case I created this code just to prove and to show one of the many things that can be done in this amazing app.
The page consist in two principal screens, first is "feature importante" and second "Predict Churn". This is just an hypotetical case because, the bottons of selection to insert a new customer was made quickly.
'''

st.title("Churn Prediction")

def main():
    #Load data and model, you need to save the data and model used in Code to just import these variables. Data is a parquet file and model an pkl file.
    data=pd.read_parquet("**here put your directory**\\data.parquet")
    model=pickle.load(open("**same**\\best_model.pkl","rb"))

    # Separate features and labels
    X = data.drop('Churn_Yes', axis=1)
    Y = data['Churn_Yes']

    # Radio buttons for options
    election = st.radio("Make Your Choice:", ("Feature Importance", "Calculate the probability of CHURN"))

    if election == "Feature Importance":
        st.write("Model coefficients:\n")
        df=pd.DataFrame(model.coef_.T, index=X.columns.drop(["customerID"]), columns=['coef'])
        #Sort df
        df=df.sort_values(by='coef',ascending=True)
        #Plot
        st.bar_chart(df,horizontal=True)
        
    elif election == "Calculate the probability of CHURN":
        st.write("Calculate the probability of CHURN")
        #Create a data frame to store user-entered data
        columns = []
        for col in range(0,3):
            columns.append(st.number_input(f"Enter the value for {X.columns[col]}",-1.0,1.0,step=0.01))
        for col in range(3,30):
            columns.append(st.selectbox(f"Enter the value for {X.columns[col]}",X[X.columns[col]].unique()))
        # Confirmation button
        confirmation_button = st.button("Confirm")

        #When the confirmation button is clicked
        if confirmation_button:
            #Convert user-entered data into a data frame
            new_customer_data = pd.DataFrame(columns).T

            # Predict churn probability using the model
            churn_probability = model.predict_proba(new_customer_data)[:, 1]

            # Format churn probability
            formatted_churn_probability = "{:.2%}".format(churn_probability.item())

            big_text = f"<h1>Churn Probability: {formatted_churn_probability}</h1>"
            st.markdown(big_text, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
