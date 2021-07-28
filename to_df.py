import sys
import json
filepath = sys.argv[1]
with open(filepath, 'r') as handle:
    res = handle.read()
with open('system_codes.json', 'r') as handle:
    system_codes = json.loads(handle.read())

inverted_codes = {v:k for k,v in system_codes.items()}

records = []
for identifier in res.split('\n'):
    if len(identifier) > 0:
        mappings = identifier.split()
        for mapping in mappings[2].split(','):
            target = mapping.split(':', 1)
            records.append((mappings[0], mappings[1], system_codes[mappings[1]], target[1], inverted_codes[target[0]], target[0]))

csv = 'original, source, source_code, mapping, target, target_code \n'
for line in records:
    csv += (', '.join(line)+'\n')
with open('mappings.csv', 'w') as handle:
    handle.write(csv)