responses=["Welcome to smart calculator","My name is Smart_Calculator","Ok  Thank you \n Good Bye","Sorry,this is beyond my ability","Hi User"]
def extract_no_from_text(text):
    l=[]
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return(l)
def lcm(a,b):
    L= a if a>b else b
    while L<=a*b:
        if L%a==0 and L%b==0:
            return L
        L+=1
def hcf(a,b):
    H=a if a<b else b
    while H>=1:
        if a%H==0 and b%H==0:
            return H
        H-=1
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b
def end():
    print(responses[2])
    input("Press entre to exit ")
    exit()
def myname():
    print(responses[1])
def sorry():
    print(responses[3])
def hi():
    print(responses[4])
operations={"PLUS":add,"ADD":add,"ADDITION":add,"SUM":add,"MINUS":sub,"SUBTRACT":sub,"SUBTRACTION":sub,"DIFFEREBCE":sub,"LCM":lcm,"HCF":hcf,"PRODUCT":multiply,"MULTIPLY":multiply,"MULTIPLICATION":multiply,"DIVISION":division,"DIVIDE":division}
commands={"NAME":myname,"END":end,"STOP":end,"EXIT":end,"HI":hi}

print(responses[0])
print(responses[1])
while True:
    print()
    text=input("How may I help you?  ")
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l=extract_no_from_text(text)
                r=operations[word.upper()](l[0],l[1])
                print("Ans = ",r)
            except:
                print("Something is wrong please retry")
            finally:
                break
        elif word.upper() in commands.keys():
            commands[word.upper()]()
            break
    else:
        sorry()