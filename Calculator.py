#Console Calculator...
print("----------------------- CALCULATOR ------------------------\n..Print 'done' after finishing inputing in both...")
numc =0
funco =0
numlist=list()
function=list()
while True:
    while True:
        num=input("Enter your Number:- ")
        if num == "done":break
        try:
            number = float(num)
        except:
            number = 0
        if number == 0:
            print("..enter a valid number..")
        else:
            while True:
                fun = input("Enter operator(+,-,/,*):- | ")
                if fun == "done":break
                func = str(fun)

                if func in ('+','-','/','*'):
                    function.append(func)
                    break

                else:
                    print("..enter a valid operator..")
                    del func
                    continue
        numlist.append(number)
    print("..............................\n")
    #print(numlist)
    #print(function)
    numdict=dict()
    funcdict=dict()

    # This function adds two numbers
    def add(x, y):
        return x + y

    # This function subtracts two numbers
    def subtract(x, y):
        return x - y

    # This function multiplies two numbers
    def multiply(x, y):
        return x * y

    # This function divides two numbers
    def divide(x, y):
        return x / y

    n=0
    f=0
    for nu in range(len(numlist)):
        num = "num"+str(n)
        nums =numlist[nu]
        numdict[num] = nums
        n = n+1
    print(numdict)
    for fu in range(len(function)):
        fug = "fun"+str(f)
        fugn = function[fu]
        funcdict[fug] = fugn
        f =f + 1
    print(funcdict)
    v=1
    w=0
    total= numdict["num0"]
    print("\nCounting... step by step..")
    for _ in range(len(funcdict)):
        if w >= len(funcdict):
            break
        else:
            if funcdict["fun"+str(w)] == '+':
                tot = add(total, numdict["num"+str(v)])
                print(total,"+", numdict["num"+str(v)],"=",tot)
            elif funcdict["fun"+str(w)] == '-':
                tot = subtract(total, numdict["num"+str(v)])
                print(total,"-", numdict["num"+str(v)],"=",tot)
            elif funcdict["fun"+str(w)] == '*':
                tot = multiply(total, numdict["num"+str(v)])
                print(total,"*", numdict["num"+str(v)],"=",tot)
            elif funcdict["fun"+str(w)] == '/':
                tot = divide(total, numdict["num"+str(v)])
                print(total,"/", numdict["num"+str(v)],"=",tot)
            else:
                print("Can't do this")
            total = tot
        #print(total)
        v = v +1
        w =w+1
    print("..............................\nYour Answer :",total)
    ask = input("\nDo you want to continue(y/n):")
    yes = "y"
    if ask == yes:
        numlist.clear()
        function.clear()
        continue
    else:
        break

#E:\Python\Calculator.py
