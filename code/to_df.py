import sys                      # The sys module provides functions and variables used to manipulate different parts of the Python runtime environment.
import json                     # The System Codes from BridgeDb are linked to their full database name in a .json file.
filepath = sys.argv[1]      # Specifify the filepath (where Matlab saved the response.txt file).
with open(filepath, 'r') as handle:                                         # Read the response file.
    res = handle.read()
with open('code/system_codes.json', 'r') as handle:                     # Read the System Codes file.
    system_codes = json.loads(handle.read())

inverted_codes = {v:k for k,v in system_codes.items()}      # Create a Python Dictionary to store the System Code - Database name as key,value pairs.

records = []                                                                            # Open a List to store the split response data in.
for identifier in res.split('\n'):                                                 # Start loop to go over all new lines (\n)
    if len(identifier) > 0:                                                           # Only initiate split when data is present.
        mappings = identifier.split()
        for mapping in mappings[2].split(','):                             # Split all xRef responses (separated by comma).
            target = mapping.split(':', 1)                                        # Each ID is connected to the corresponding System Code by a colon).
            records.append((mappings[0], mappings[1], system_codes[mappings[1]], target[1], inverted_codes[target[0]], target[0])) # Add all information as defined above to the list.
            # Note that the above line creates 6 columns (Python counts from 0): [0] Original ID, [1] Source Database, [2] Source System Code,
            # [3] Mapping ID, [4] Target Database, [5] Target System Code .

csv = 'original, source, source_code, mapping, target, target_code \n' # Create headers for csv file
for line in records:                                                                   # Add all response from list.
    csv += (', '.join(line)+'\n')
with open('mappings.csv', 'w') as handle:                               # Open CSV file and write responses to file (file is closed after writing operation).
    handle.write(csv)
