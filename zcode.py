from os import system
with open("test.zc","r") as f:
    data = f.read()
code = []
for i in data:
    line = ""
    ifh = 0
    if i == "{":
        ifh = 1
    elif i == "}":
        line = line + i
        ifh = 0
        code.append(line.strip())
        line = ""
    if ifh == 0:
        line = line + i
print(code)
        

