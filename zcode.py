from os import system
with open("test.zc","r") as f:
    data = f.read()
code = []
h = 0
for i in data:
    line = ""
    if i == "{":
        h = h+1
    elif i == "}":
        h=h-1
    line = line + i
    
print(h)
        
