from os import system
with open("test.zc","r") as f:
    data = f.read()
code = []
code_letters = []
for i in data:
    code_letters.append(i)
xg = data.find("/")
if xg != -1 and xg+1 < len(data):
    if code_letters[xg+1] == "/":
        while code_letters[xg]!= "\n":
            code_letters.remove(code_letters[xg])
            print(code_letters[xg])
            xg = xg +1




    
print(code_letters)

        
