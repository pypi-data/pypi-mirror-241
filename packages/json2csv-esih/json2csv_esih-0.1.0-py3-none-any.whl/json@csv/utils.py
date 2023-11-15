def json_to_csv(json_path, csv_path):
    try:
        with open(json_path, 'r') as json_file:
            data = eval(json_file.read())

        if isinstance(data, list) and all(isinstance(item, dict) for item in data):
            with open(csv_path, 'w') as csv_file:
                # Write header
                header = ','.join(data[0].keys())
                csv_file.write(f"{header}\n")

                # Write data
                for row in data:
                    values = ','.join(str(val) for val in row.values())
                    csv_file.write(f"{values}\n")

            print(f"JSON to CSV conversion successful. CSV file is at: {csv_path}")
        else:
            print("Incorrect JSON format. JSON should be a list of dictionaries.")
    except FileNotFoundError:
        print(f"Error: File not found. Check the path of the JSON file: {json_path}")
    except PermissionError:
        print(f"Error: Permission denied. Close the CSV file: {csv_path}")
    except Exception as e:
        print(f"An error occurred: {e}")



def csv_to_json(csv_path, json_path, separator=','):
    try:
        with open(csv_path, 'r') as csv_file:
            lines = csv_file.readlines()

            # Extract header and data
            header = lines[0].strip().split(separator)
            data = [line.strip().split(separator) for line in lines[1:]]

            # Create list of dictionaries
            json_data = []
            for row in data:
                json_row = {}
                for i, value in enumerate(row):
                    json_row[header[i]] = value
                json_data.append(json_row)

            # Write to JSON file manually
            with open(json_path, 'w') as json_file:
                json_file.write("[\n")
                for i, row in enumerate(json_data):
                    json_file.write("  {\n")

                    for j, (key, value) in enumerate(row.items()):
                        json_file.write(f'    "{key}": "{value}"')
                        if j < len(row) - 1:
                            json_file.write(",\n")
                        else:
                            json_file.write("\n")

                    json_file.write("  }")
                    if i < len(json_data) - 1:
                        json_file.write(",\n")
                    else:
                        json_file.write("\n")

                json_file.write("]\n")

            print(f"CSV to JSON conversion successful. JSON file is at: {json_path}")
    except FileNotFoundError:
        print(f"Error: File not found. Check the path of the CSV file: {csv_path}")
    except PermissionError:
        print(f"Error: Permission denied. Close the CSV file: {csv_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

