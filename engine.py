import yfinance as yf
import pandas as pd
import openmeteo_requests
import requests_cache
from retry_requests import retry
from datetime import datetime, timedelta

def get_quant_data(ticker, city_name):
    # 1. Setup Dates Automatically
    today = datetime.now().strftime('%Y-%m-%d')
    one_year_ago = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')

    # 2. GPS Coordinates
    coords = {
        "Houston (Texas)": {"lat": 29.76, "lon": -95.36},
        "Chicago (Illinois)": {"lat": 41.85, "lon": -87.65},
        "London (UK)": {"lat": 51.50, "lon": -0.12}
    }
    selected_gps = coords[city_name]

    # 3. Setup Weather API
    cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)

    # 4. Get Real Weather Data
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": selected_gps["lat"],
        "longitude": selected_gps["lon"],
        "start_date": one_year_ago,
        "end_date": today,
        "daily": "temperature_2m_max"
    }
    
    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]
    daily = response.Daily()
    
    weather_df = pd.DataFrame({
        "date": pd.date_range(
            start=pd.to_datetime(daily.Time(), unit="s", utc=True),
            end=pd.to_datetime(daily.TimeEnd(), unit="s", utc=True),
            freq=pd.Timedelta(seconds=daily.Interval()),
            inclusive='left' # Updated for modern Pandas
        ).date,
        "Temp_Max": daily.Variables(0).ValuesAsNumpy()
    })

    # 5. Get Stock Data
    stock_df = yf.download(ticker, start=one_year_ago, end=today)
    if isinstance(stock_df.columns, pd.MultiIndex):
        stock_df.columns = stock_df.columns.get_level_values(0)
    
    stock_df['Daily_Return'] = stock_df['Close'].pct_change()
    stock_df.index = stock_df.index.date
    
    # 6. Merge and Correlate
    final_df = stock_df.join(weather_df.set_index('date'), how='inner').dropna()
    correlation = final_df['Temp_Max'].corr(final_df['Daily_Return'])
    
    return final_df, correlation