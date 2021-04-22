import os, re

def get_groups(seq, group_by):
    data = []
    for line in seq:
        if line.startswith(group_by):
            if data:
                yield data
                data = []
        data.append(line)
    if data:
        yield data

reg = r'source-zone trust(.*?)destination-zone Untrust'
content = re.compile(reg, re.DOTALL)
with open(r'filedir and  filename', 'r', encoding='UTF-8') as f:
    for i, group in enumerate(get_groups(f, ' rule'), start=1):
        rule = "".join(group)
        if content.findall(rule):
            print("Group #{}".format(i))
            print(rule)
