import os

#zcore代码格式
#  #include{库1;库2;...}
#  main(){代码}
#

#keywords
keywords = ["print","include"]
#keyword explain
def include(code):
    
    return code.replace("<zcstd>","\"includ/zcstd.h\"")

#get code
with open("text.zc","r") as f:
    data = f.read()
    line = ""
    code = []
    ifj = 0
    cj = 0
    ifh = 0
    for i in data:
        if i== "{":
            ifh = 1
        elif i == "}":
            line = line + i
            ifh = 0
            code.append(line.strip())
            line = ""
        if ifh == 0:
            if i == "#":
                line = line + i
                ifj = 1
                cj = cj + 1 
            elif i == "\n" and ifj == 1:
                code.append(line.strip())
                line = ""
                ifj = 0
            elif i == ";" and ifj != 1:
                line = line + i
                code.append(line.strip())
                line = ""
            elif i != "\n":
                line = line + i
        else:
            line = line + i

    print(code)

#explain
long = len(code)
for i in range(long):
    code[i] = include(code[i])
print(code)
#write code
with open("text.cpp","w") as f:
    for i in range(len(code)):
        if i == cj:
            f.write("int main(){")
        f.write(code[i])
        if i == len(code) - 1:
            f.write("return 0;}")
        f.write("\n")

os.system("g++ text.cpp -o text")

