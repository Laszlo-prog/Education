import request
import json
from urllib.parse import urlparse

def download_json(url, params=None, headers=None, output_file=None):
    """
    Download JSON data from a given URL.
    
    Args:
        url (str): The URL to fetch JSON data from
        params (dict, optional): Query parameters to send with the request
        headers (dict, optional): Headers to send with the request
        output_file (str, optional): File path to save the JSON data. If None, data is returned but not saved.
    
    Returns:
        dict: The parsed JSON data if successful, None otherwise
    """
    try:
        # Make the HTTP request
        response = request.get(url, params=params, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse the JSON data
        json_data = response.json()
        
        # Save to file if output_file is specified
        if output_file:
            with open(output_file, 'w') as f:
                json.dump(json_data, f, indent=4)
            print(f"JSON data successfully saved to {output_file}")
        
        return json_data
    
    except request.exceptions.RequestException as e:
        print(f"Error making HTTP request: {e}")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    return None

def get_valid_url():
    """Prompt user for a valid URL"""
    while True:
        url = input("Enter the URL to download JSON data from: ").strip()
        
        # Basic URL validation
        parsed = urlparse(url)
        if not all([parsed.scheme, parsed.netloc]):
            print("Invalid URL. Please include http:// or https://")
            continue
        
        return url

def main():
    print("JSON Data Downloader")
    print("-------------------")
    
    # Get user input
    url = get_valid_url()
    save_file = input("Enter output filename (leave blank to not save): ").strip()
    
    # Optional parameters
    params = {}
    headers = {}
    
    # Add common headers for API requests
    headers['User-Agent'] = 'Mozilla/5.0 (JSON Data Downloader)'
    headers['Accept'] = 'application/json'
    
    # Download the JSON data
    json_data = download_json(url, params=params, headers=headers, output_file=save_file if save_file else None)
    
    if json_data is not None:
        print("\nDownload successful! Here's a preview of the data:")
        print(json.dumps(json_data, indent=4)[:500] + ("..." if len(str(json_data)) > 500 else ""))
    else:
        print("\nFailed to download JSON data.")

if __name__ == "__main__":
    main()