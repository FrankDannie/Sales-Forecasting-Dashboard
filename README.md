# Sales Forecasting Dashboard

## Overview

This project provides a Streamlit dashboard for forecasting sales using historical data. Users can upload CSV files containing sales data, visualize the data, and run forecasts using the Prophet model.

## Project Structure

- `app.py`: The main entry point for the Streamlit application.
- `components/`:
  - `data_uploader.py`: Handles file upload and data loading.
  - `data_visualization.py`: Handles data visualization.
  - `forecasting.py`: Handles forecasting and plotting.
  - `utils.py`: Contains utility functions (if any).
- `src/services/forecasting_service.py`: Contains the forecasting logic using Prophet.
- `README.md`: This file.

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
