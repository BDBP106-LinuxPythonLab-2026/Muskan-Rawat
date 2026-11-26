import re

pattern = r'^[01][0-5]{2}$'
test= ['000','100','50','300']

for i in test:
    if re.match(pattern,i):
        print(i, "valid")
    else:
        print(i,"invalid")

searc = re.search()
