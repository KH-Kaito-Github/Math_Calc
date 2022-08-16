
import re
#文字式掛け算 引数(式A,式B) 戻り値(AとBの積)
def LiCalc_Malti(A,B):
    if(str(A)=="" or str(B)==""):
        return "0"
    elif(str(A)[0]=="-" or str(B)[0]=="-"):
        A_sub = 0
        B_sub = 0
        if(str(A)[0] == "-"):
            A = str(A).replace("-","")
            A_sub = 1
        if(str(B)[0] == "-"):
            B = str(B).replace("-","")
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
            return  str(C)+"".join(sorted(C_literal))
        else:
            multiple_ret = str(C)+"".join(sorted(C_literal))
            return "-"+str(multiple_ret)
    else:
        pattern = '[0-9]*'
        if(isinstance(A, int)==True):
            A_coefficient = A
            A_literal = ""
        else:
            A_coefficient = re.search(pattern,A).group()
            A_literal = A.replace(A_coefficient,"")
        if(isinstance(B, int)==True):
            B_coefficient = B
            B_literal = ""
        else:
            B_coefficient = re.search(pattern,B).group()
            B_literal = B.replace(B_coefficient,"")
        Empty_Frag = 0
        if(str(A_coefficient) == ""):
            Empty_Frag = 1
        elif(str(B_coefficient) == ""):
            Empty_Frag = 1

        if(Empty_Frag==1):
            C = str(A_coefficient)+str(B_coefficient)
        else:
            C = int(A_coefficient) * int(B_coefficient)
        C_literal = A_literal+B_literal
        return  str(C)+"".join(sorted(C_literal))
#文字式足し算 引数(式A,式B) 戻り値(AとBの和)
def LiCalc_Add(A,B):
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
                return  str(C)+A_literal
            if(B_sub == 1):
                C = int(A_coefficient) - int(B_coefficient)
                return  str(C)+A_literal
            C = int(A_coefficient)+int(B_coefficient)
            return str(C)+A_literal
    else:
        if(A_sub==1 and B_sub==1):
            return "-"+A+"-"+B
        else:
            if(A_sub==1):
                return "-"+A+"+"+B
            elif(B_sub==1):
                return A+"-"+B
            else:
                return A+"+"+B          
#指数になっていない式を指数表記に直す 引数(式) 戻り値(指数表記になってる式)
def LiCalc_SerLitToExp(A):
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
#指数表記に直せるか確認 引数(式) 戻り値(0できない,1できる)
def LiCalc_SerLitToExpCheck(A):
    pattern = "[0-9]*"
    A_coeficcient = re.search(pattern,A).group()
    A_literal = A.replace(A_coeficcient,"")
    pattern1 = r"(.)\1+"
    A_contliteral = re.search(pattern1,A_literal).group()
    if(A_contliteral==None):
        return 0
    else:
        return 1
#符号を消す 引数(式,+か-) 戻り値(符号が消えてる式)
def LiCalc_RmSign(A,Sign):
    if(A[0]=="-" and Sign == "-"):
        return A.replace("-","")
    if(A[0]=="+" and Sign == "+"):
        return A.replace("+","")
#符号を付けます 引数(式,+か-) 戻り値(符号がついた式)
def LiCalc_MkSign(A,Sign):
    if(A[0]!="-" and A[0]!="+" and Sign == "+"):
        return "+"+A
    if(A[0]!="-" and A[0]!="+" and Sign == "-"):
        return "-"+A
#符号を調べます 引数(式) 戻り値(+か-か空白)
def LiCalc_ChSign(A):
    if(A.isdecimal()==True):
        return ""
    if(A==""):
        return ""
    if(A[0]=="-"):
        return "-"
    elif(A[0]=="+"):
        return "+"


print(LiCalc_Malti("2","-1"))



