import pandas as pd
import json

def convert_csv_to_json(csv_path, json_path="output.json"):
    df = pd.read_csv(csv_path)
    json_output = df.to_json(orient="records", indent=4)

    with open(json_path, "w") as json_file:
        json_file.write(json_output)

    return json_output  # Return JSON as a string

# Example usage
if __name__ == "__main__":
    csv_file = r"C:\Users\Dhumal Sakshi\Desktop\MY_PRO\my_pro\sample_data.csv"
    json_data = convert_csv_to_json(csv_file)
    print(json_data)  # Print output for testing
