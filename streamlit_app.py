import streamlit as st
import requests
import json

st.title("Credit Card Fraud Detection Web App")

st.write("""
## About
Credit card fraud is a form of identity theft that involves an unauthorized taking of another's credit card information 
for the purpose of charging purchases to the account or removing funds from it.

**This Streamlit App utilizes a Machine Learning model served as an API in order to detect fraudulent credit card 
transactions based on the following criteria: hours, type of transaction, amount, balance before and after transaction etc.**
""")

# Sidebar inputs
st.sidebar.header('Input Features of The Transaction')

sender_name = st.sidebar.text_input("Input Sender ID")
receiver_name = st.sidebar.text_input("Input Receiver ID")

step = st.sidebar.slider("Number of Hours it took the Transaction to complete: ", 
                        min_value=0, max_value=744)  # 31 days max

st.sidebar.subheader("Type of Transfer Made:")
transaction_types = {
    0: 'Cash In',
    1: 'Cash Out',
    2: 'Debit',
    3: 'Payment',
    4: 'Transfer'
}
types = st.sidebar.selectbox("Select transaction type:", 
                           options=list(transaction_types.keys()),
                           format_func=lambda x: transaction_types[x])

amount = st.sidebar.number_input("Amount in $", min_value=0.0, max_value=110000.0)
oldbalanceorg = st.sidebar.number_input("Sender Balance Before Transaction ($)", min_value=0.0, max_value=110000.0)
newbalanceorg = st.sidebar.number_input("Sender Balance After Transaction ($)", min_value=0.0, max_value=110000.0)
oldbalancedest = st.sidebar.number_input("Recipient Balance Before Transaction ($)", min_value=0.0, max_value=110000.0)
newbalancedest = st.sidebar.number_input("Recipient Balance After Transaction ($)", min_value=0.0, max_value=110000.0)

# Calculate isflaggedfraud
isflaggedfraud = 1 if amount >= 200000 else 0

if st.button("Detection Result"):
    # Input validation
    if not sender_name or not receiver_name:
        st.error("Please input Transaction ID or Names of Sender and Receiver!")
    else:
        # Display transaction details
        st.write("""### Transaction Details:""")
        details = f"""
        - Sender ID: {sender_name}
        - Receiver ID: {receiver_name}
        - Hours to complete: {step}
        - Type of Transaction: {transaction_types[types]}
        - Amount Sent: ${amount:,.2f}
        - Sender Balance Before: ${oldbalanceorg:,.2f}
        - Sender Balance After: ${newbalanceorg:,.2f}
        - Recipient Balance Before: ${oldbalancedest:,.2f}
        - Recipient Balance After: ${newbalancedest:,.2f}
        - System Fraud Flag: {isflaggedfraud}
        """
        st.markdown(details)

        # Prepare API request
        values = {
            "step": step,
            "types": types,
            "amount": amount,
            "oldbalanceorig": oldbalanceorg,
            "newbalanceorig": newbalanceorg,
            "oldbalancedest": oldbalancedest,
            "newbalancedest": newbalancedest,
            "isflaggedfraud": isflaggedfraud
        }

        try:
            # Make API request
            response = requests.post(
                "https://credit-card-fraud-detection-123.streamlit.app/predict",  # Update this URL to match your FastAPI deployment
                json=values,
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 200:
                result = response.json()
                prediction = result.get("prediction", "Error in prediction")
                st.write(f"""### Result: The '{transaction_types[types]}' transaction between {sender_name} and {receiver_name} is {prediction}.""")
            else:
                st.error(f"API Error: Status code {response.status_code}")
                st.error(f"Response: {response.text}")
                
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to the API: {str(e)}")
        except json.JSONDecodeError as e:
            st.error(f"Error decoding API response: {str(e)}")
            st.error(f"Raw response: {response.text}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
