import pandas as pd
import requests

def fetch_nasa_power_data(lat, lon, start_date, end_date):
    """
    Fetches daily climate data from the NASA POWER API.
    Used for the COP32 regional analysis project.
    """
    base_url = "https://power.larc.nasa.gov/api/temporal/daily/point"
    params = {
        "start": start_date,
        "end": end_date,
        "latitude": lat,
        "longitude": lon,
        "community": "ag",
        "parameters": "T2M_MAX,PRECTOTCORR,RH2M",
        "format": "json"
    }
    
    # In a real run, you'd use requests.get(base_url, params=params)
    # This script ensures the 'app/' only handles the UI.
    print(f"Fetching data for coordinates: {lat}, {lon}")
    return True