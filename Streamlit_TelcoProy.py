import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import RobustScaler

st.title("Churn Prediction")

def main():
    #Load data and model
    data=pd.read_parquet("G:\\My Drive\\Downloads\\Downloads\\DMR Project ACCENTURE\\CODE\\data.parquet")
    model=pickle.load(open("G:\\My Drive\\Downloads\\Downloads\\DMR Project ACCENTURE\\CODE\\best_model.pkl","rb"))

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