import pandas as pd     # type: ignore # Import Pandas for data manipulation
import json             # type: ignore # For handling JSON data
import time             # type: ignore # For adding timestamps

def json_to_csv(json_file, csv_file):
    
    """
    Converts a JSON file to a CSV file using Pandas.
    
    Args:
        json_file (str): Path to the input JSON file
        csv_file (str): Path to the output CSV file
    """

    try:
       
        # Record the start time of the function execution
        start_time = time.time()
        print(f"Starting conversion at: {time.strftime('%Y-%m-%d %H:%M:%S')}")

        # Read the JSON file
        print(f"Input file picked up : {json_file}")
        with open(json_file, 'r') as f:
            data = json.load(f)
        
        # Print basic information about the data structure
        print(f"Data type after loading: {type(data)}")
        print(f"First element of data: {data[0]}")

        # Normalize the JSON data into a Pandas DataFrame
        df = pd.json_normalize(data)

        # Print the preview of the JSON data as in the DataFrame
        print("\nPreview of the DataFrame:")
        print(df.head())

        # Clean column names by replacing spaces with underscores
        df.columns = [col.replace(' ', '_') for col in df.columns]

        # Export the DataFrame to CSV
        df.to_csv(csv_file, index=False)

        # Record the end time and calculate duration
        end_time = time.time()
        duration = end_time - start_time

        print(f"\nConversion completed successfully.")
        print(f"Duration: {duration:.3f} seconds")
        print(f"Output file saved as: {csv_file}")

    except Exception as e:
        # Handle any exceptions that occur during the process
        print(f"Error occurred during JSON to CSV conversion: {str(e)}")

# Example usage:
if __name__ == "__main__":
    input_json = 'input.json'  # Replace with your input JSON file path
    output_csv = 'output.csv'  # Replace with desired output CSV file path

    json_to_csv(input_json, output_csv)
