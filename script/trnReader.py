import re
import json
data = []

COUNT = 5000
cnt = 0
with open('train.trn', 'r') as f:
    while cnt < COUNT:
        cnt = cnt + 1
        line = f.readline()
        print(line)
        if not line: break
        fileAndAnswer = line.split("::")
        filename = fileAndAnswer[0].split('/')[-1].rstrip()
        answer = fileAndAnswer[1].lstrip()

        if re.findall('[0-9a-zA-Z+*]', answer): continue

        data.append({
            'wav': filename,
            'text': answer.replace('/', '').rstrip()
        })

with open('model_train.json', 'w') as js:
    json.dump(data, js, ensure_ascii=False, indent=4)
