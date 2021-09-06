import math_operations as m

def split_expression(expression):
          
    expr_no_brackets = ""

    counter = 0
   
    while counter < len(expression):
        if expression[counter] == "(":
            if ")" in expression[counter:]:
                exp_part = expression[counter+1:expression.index(')', counter)]
                if "(" in exp_part:
                    expr_no_brackets += str(split_expression(exp_part))
                    counter += len(exp_part)+1
                else:
                    exp_res = do_math(exp_part)
                    expr_no_brackets += str(exp_res)
                    counter += len(exp_part)+1
            else:
                exp_part = expression[counter+1:]
                        
                if "(" in exp_part:
                    expr_no_brackets += str(split_expression(exp_part))
                    counter += len(exp_part)+1
                else:
                    exp_res = do_math(exp_part)
                    expr_no_brackets += str(exp_res)
                    counter += len(exp_part)+1

        elif expression[counter] == ")":
            counter += 1

        else:
            expr_no_brackets += expression[counter]
            counter += 1

    result = do_math(expr_no_brackets)

    return result   
                         

def do_math(exp_part):

    operations = {
        '+': m.plus,
        '-': m.minus,
        '*': m.multiply,
        '/': m.divide
    }

    ops = []
    for symbol in exp_part:
        if symbol in operations:
            ops.append(symbol)

    exp = exp_part.replace('*', '+').replace('/', '+').replace('-', '+').split('+')

    while len(exp) > 1:
        if "*" in ops:
            i = ops.index('*')
            exp[i] = m.multiply(exp[i], exp[i+1])
            del exp[i+1]
            del ops[i]
        elif "/" in ops:
            i = ops.index('/')
            exp[i] = m.divide(exp[i], exp[i+1])
            del exp[i+1]
            del ops[i]
        elif "+" in ops:
            i = ops.index('+')
            exp[i] = m.plus(exp[i], exp[i+1])
            del exp[i+1]
            del ops[i]
        else:
            i = ops.index('-')
            exp[i] = m.minus(exp[i], exp[i+1])
            del exp[i+1]
            del ops[i]
    
    return exp[0]
            
expression = input('Enter your expression:\n')

print(split_expression(expression))