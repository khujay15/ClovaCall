import re
import json
data = []

with open('dev.trn', 'r') as f:

    while True:
        line = f.readline()
        if not line: break
        fileAndAnswer = line.split("::")
        filename = fileAndAnswer[0].split('/')[-1].rstrip()
        answer = fileAndAnswer[1].lstrip()

        if re.findall('[0-9a-zA-Z+*]', answer): continue

        data.append({
            'wav': filename,
            'text': answer.replace('/', '').rstrip()
        })

with open('test.json', 'w') as js:
    json.dump(data, js, ensure_ascii=False, indent=4)
