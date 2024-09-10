import streamlit as st
import pandas as pd
from src.services.forecasting_service import forecast_sales
import matplotlib.pyplot as plt

# Title

def data_uploader():
    st.title("Sales Forecasting Dashboard")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload your sales data (CSV)", type=["csv"])

    if uploaded_file is not None:
        # Load the file into a DataFrame
        df = pd.read_csv(uploaded_file)

        if 'Date' not in df.columns:
            st.error("The CSV does not contain a 'Date' column.")

        # Display data
        st.subheader("Uploaded Sales Data")
        st.write(df)

        # Visualize data
        st.subheader("Data Visualization")
        st.line_chart(df.set_index('Date'))

        # Forecasting section
        st.subheader("Sales Forecast")

        # Forecast button
        if st.button("Run Forecast"):
            try:
                forecast = forecast_sales(df)
                st.write("Forecast Data:")
                st.write(forecast)

                # Plot forecast results
                fig, ax = plt.subplots(figsize=(12, 6))  # Adjust size if needed
                ax.plot(forecast['ds'], forecast['yhat'], label='Predicted Sales')
                ax.fill_between(forecast['ds'], forecast['yhat_lower'], forecast['yhat_upper'], color='gray', alpha=0.2)
                ax.set_xlabel('Date')
                ax.set_ylabel('Sales')
                ax.set_title('Sales Forecast')
                ax.legend()
                
                # Rotate x-axis labels
                plt.xticks(rotation=90)

                st.pyplot(fig)
            except ValueError as e:
                st.error(f"Error in forecasting: {e}")

    else:
        st.write("Please upload a CSV file.")
