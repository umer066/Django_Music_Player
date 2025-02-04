import re
import json
import syncedlyrics 

try:
    query=input("Enter Song Name").strip()
    lrc = syncedlyrics.search(query)


# Input data
    data = lrc

    if not data:
        raise ValueError("No lyrics found for the given song.")
    
    # Split the data into linesf
    lines = data.split('\n')


    # Initialize a list to store the JSON entries
    json_data = []

    # Define a regular expression pattern to extract timestamps and text
    pattern = r'\[(\d+:\d+\.\d+)\] (.+)'

    for line in lines:
        match = re.match(pattern, line)
        if match:
            timestamp, text = match.groups()
            json_entry = {
                "time": timestamp,
                "lyrics": text
            }
            json_data.append(json_entry)

    # Convert the list of JSON entries to a JSON-formatted string
    json_string = json.dumps(json_data, indent=4)

    # Print the JSON string
    print(json_string)

except syncedlyrics.SyncedLyricsError as e:
    print (f"Error with the lyrics service: {e}")

except ValueError as e:
    print(f"Error: {e}")

except re.error as e:
    print(f"Error in regex  processing: {e}")

except Exception as e:
    print( f"An unexcepted error occurred: {e}")