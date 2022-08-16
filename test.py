
import re

def Main():
    literal_A = "-2a"
    literal_B = "3a"
    print("文字式の掛け算>> "+literal_A+"・"+literal_B+"="+CalcSerLitToExp_LiteralEx(CalcMalti_LiteralEx(literal_A,literal_B)))
    print("文字式の足し算>> "+literal_A+"+"+literal_B+"="+CalcAdd_LiteralEx(literal_A,literal_B))

def CalcMalti_LiteralEx(A,B):
    if(A[0]=="-" or B[0]=="-"):
        A_sub = 0
        B_sub = 0
        if(A[0] == "-"):
            A = A.replace("-","")
            A_sub = 1
        if(B[0] == "-"):
            B = B.replace("-","")
            B_sub = 1
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
        if(A_sub == 1 and B_sub == 1):
            return  "".join(sorted(str(C)+C_literal))
        else:
            multiple_ret = "".join(sorted(str(C)+C_literal))
            return "-"+str(multiple_ret)
    else:
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
        return  "".join(sorted(str(C)+C_literal))
def CalcAdd_LiteralEx(A,B):
    A_sub = 0
    B_sub = 0
    if(A[0]=="-"):
        A = A.replace("-","")
        A_sub = 1
    if(B[0]=="-"):
        B = B.replace("-","")
        B_sub = 1
    pattern = '[0-9]*'
    A_coefficient = re.search(pattern,A).group()
    B_coefficient = re.search(pattern,B).group()
    A_literal = A.replace(A_coefficient,"")
    B_literal = B.replace(B_coefficient,"")
    if(A_coefficient=="" and A_literal != ""):
        A_coefficient = 1
    if(B_coefficient=="" and B_literal != ""):
        B_coefficient = 1
    if(A_literal == B_literal):
        if(A_sub == 1 and B_sub == 1):
            C =  -1*(int(B_coefficient) + int(A_coefficient))
        else:
            if(A_sub == 1):
                C = int(B_coefficient) - int(A_coefficient)
            if(B_sub == 1):
                C = int(A_coefficient) - int(B_coefficient)
        return  str(C)+A_literal
    else:
        return  A+"+"+B
def CalcSerLitToExp_LiteralEx(A):
    A_sub = 0
    if(A[0]=="-"):
        A = A.replace("-","")
        A_sub = 1
    pattern = "[0-9]*"
    A_coeficcient = re.search(pattern,A).group()
    A_literal = A.replace(A_coeficcient,"")
    pattern1 = r"(.)\1+"
    A_contliteral = re.search(pattern1,A_literal)
    if(A_contliteral == None):
        return A
    pattern2 = "["+A_contliteral.string+"]+"
    A_contliteral_len = len(re.search(pattern2,A_literal).group())
    
    A_literal_n2 = A_literal.replace(A_contliteral.string,"")
    A_exponential = A_contliteral.string[0]+"^"+str(A_contliteral_len)
    if(A_sub==1):
        return "-"+A_coeficcient + A_exponential + A_literal_n2
    else:
        return A_coeficcient + A_exponential + A_literal_n2
def CalkSerLitToExpCheck_LiteralEx(A):
    pattern = "[0-9]*"
    A_coeficcient = re.search(pattern,A).group()
    A_literal = A.replace(A_coeficcient,"")
    pattern1 = r"(.)\1+"
    A_contliteral = re.search(pattern1,A_literal).group()
    if(A_contliteral==None):
        return 0
    else:
        return 1

if __name__ == "__main__":
    Main()