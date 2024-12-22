import requests
import pandas as pd

def get_data(output_file="data/raw/raw_data.csv"):
    """
    Fetch data from the Données Québec API and save it to a CSV file.
    """
    
    # Define API URL
    url = "https://www.donneesquebec.ca/recherche/api/3/action/datastore_search"
    
    # Parameters as found in CKAN API documentation
    params = {
        "resource_id": "841b69a5-d420-42d5-b127-c2850b88f63b",  # Dataset ID
        "limit": 1000
    }
    
    try:
        # Send request
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception if the request fails
        
        # Get records from the response JSON
        data = response.json()
        records = data["result"]["records"]
        
        # Convert records to a pandas DataFrame
        df = pd.DataFrame(records)
        
        # Save the DataFrame to CSV
        df.to_csv(output_file, index=False)
        print(f"Data successfully saved to {output_file}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    get_data()
