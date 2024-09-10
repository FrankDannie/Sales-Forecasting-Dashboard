from prophet import Prophet
import pandas as pd

def forecast_sales(data: pd.DataFrame, periods: int = 30):
    # Check for required columns
    if 'Date' not in data.columns or 'Sales' not in data.columns:
        raise ValueError("The DataFrame must contain 'Date' and 'Sales' columns.")

    # Prepare the data for Prophet (Prophet requires columns: ds (Date), y (value))
    df = data.rename(columns={'Date': 'ds', 'Sales': 'y'})
    
    # Convert 'ds' to datetime format for Prophet
    df['ds'] = pd.to_datetime(df['ds'], format='%d-%m-%Y', errors='coerce')
    df = df.dropna(subset=['ds'])
    
    # Initialize and fit the Prophet model
    model = Prophet()
    model.fit(df)
    
    # Make future predictions
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    
    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
