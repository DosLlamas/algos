def expressions(seq):
    res = 0 # 33
    num = "" # 
    num2 = "" # 33
    op = "" # *
    operators = {"+", "-", "*"}
    for i in range(seq):
        if seq[i] == "+":
            op = seq[i]
        elif seq[i] == "*":
            op = seq[i]
        elif seq[i] == "-":
            op = seq[i]
        else:
            if i < len(seq) - 1:
                if not op:
                    num+= seq[i]
                else:
                    if seq[i+1] in operators:
                        if num: 
                            num2 += seq[i]
                            if op == "+":
                                res = int(num) + int(num2)
                            elif op == "*":
                                res = int(num) * int(num2)
                            elif op == "-":
                                res = int(num) - int(num2)
                            num = ""
                            num2 = ""
                            op = ""
                        else:
                            num2 += seq[i]
                            if op == "+":
                                res += int(num2)
                            elif op == "*":
                                res *= int(num2)
                            elif op == "-":
                                res -= int(num2)
                            num = ""
                            num2 = ""
                            op = ""
                    else:
                        num2 += seq[i]
                    
            else:
                num2 += seq[i]
                if op == "+":
                    res = res + (int(num) + int(num2))
                elif op == "*":
                    res = res + (int(num) * int(num2))
                elif op == "-":
                    res = res + (int(num) - int(num2))



    return res

print(expressions("11+22*33-44*55*66"))