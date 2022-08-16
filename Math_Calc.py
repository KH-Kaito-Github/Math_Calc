# 目標 二次式の平方完成

from queue import Empty
import re

def Main():
#fomula list [変数,二次項,一次項,定数項]
    formula = Create_Formula(1)
    #print(formula[1:])
    square_fomula = Complete_Square(formula)
    print(square_fomula)
    


# Create_Formula(Mode) [Mode == 0 通常入力],[Mode == 1 普通の二次式],[Mode == 2 一般の二次式],[Mode == 3 定数項なし]
def Create_Formula(Mode):
    if(Mode == 0):
        print("変数を定義してください (一文字まで)>>  ")
        formula_variable = input()
        print("変数が二次の項を入力してください()>>  ")
        formula_quadratic_term = input()
        print("変数が一次次の項を入力してください>>  ")
        formula_first_term = input()
        print("定数項を入力してください>>  ")
        formula_constant_term = input()
        formula_l = [formula_variable,CheckMk_Term(formula_quadratic_term),CheckMk_Term(formula_first_term),CheckMk_Term(formula_constant_term)]
        return formula_l
    if(Mode == 1):
        print("変数を定義してください (一文字まで)>>  ")
        formula_variable = "x"
        print("変数が二次の項を入力してください()>>  ")
        formula_quadratic_term = "2x^^2"
        print("変数が一次次の項を入力してください>>  ")
        formula_first_term = "-5x"
        print("定数項を入力してください>>  ")
        formula_constant_term = "7"
        formula_l = [formula_variable,CheckMk_Term(formula_quadratic_term),CheckMk_Term(formula_first_term),CheckMk_Term(formula_constant_term)]
        return formula_l
    if(Mode == 2):
        print("変数を定義してください (一文字まで)>>  ")
        formula_variable = "x"
        print("変数が二次の項を入力してください()>>  ")
        formula_quadratic_term = "ax^^2"
        print("変数が一次次の項を入力してください>>  ")
        formula_first_term = "bx"
        print("定数項を入力してください>>  ")
        formula_constant_term = "c"
        formula_l = [formula_variable,CheckMk_Term(formula_quadratic_term),CheckMk_Term(formula_first_term),CheckMk_Term(formula_constant_term)]
        return formula_l
    if(Mode == 3):
        print("変数を定義してください (一文字まで)>>  ")
        formula_variable = "x"
        print("変数が二次の項を入力してください()>>  ")
        formula_quadratic_term = "ax^^2"
        print("変数が一次次の項を入力してください>>  ")
        formula_first_term = "bx"
        print("定数項を入力してください>>  ")
        formula_constant_term = ""
        formula_l = [formula_variable,CheckMk_Term(formula_quadratic_term),CheckMk_Term(formula_first_term),CheckMk_Term(formula_constant_term)]
        return formula_l
def CheckRv_Term(Term):
    if(str(Term)[0] == "+"):
        return Term.replace("+","")
    if(str(Term)[0] == "-"):
        return Term.replace("-","")
    return Term
def CheckMk_Term(Term):
    if(Term == ""):
        return Term
    if(Term[0] != "+" and Term[0] != "-"):
        return "+"+Term
    return Term

def Complete_Square(formula):
    #a (x + b/2a )^^2 -b^^2/4a +c
    
def CheckSign_Formula(Term):
    if(Term[0] == "+"):
        return "+"
    if(Term[0] == "-"):
        return "-"
def CalcMalti_LiteralEx(A,B):
    pattern = '[0-9]*'
    A_coefficient = re.search(pattern,A).group()
    B_coefficient = re.search(pattern,B).group()
    A_literal = A.replace(A_coefficient,"")
    B_literal = B.replace(B_coefficient,"")
    Empty_Frag = 0
    if(A_coefficient == ""):
        Empty_Frag = 1
    elif(B_coefficient == ""):
        Empty_Frag = 1

    if(Empty_Frag==1):
        C = A_coefficient+B_coefficient
    else:
        C = int(A_coefficient) * int(B_coefficient)
    C_literal = A_literal+B_literal
    return  str(C)+C_literal



if __name__ == "__main__":
    Main()