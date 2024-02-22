import json
with open('data/values.json', 'r') as file_v:
    data_v = json.load(file_v)
with open('data/tests.json', 'r') as file_t:
     data_t = json.load(file_t)
for item_t in data_t:
    test_id = item_t['id']
for item_v in data_v:
    item_t['value'] = item_v['value']
    break
with open('report.json', 'w') as file:
    json.dump(data_t, file, indent=4)