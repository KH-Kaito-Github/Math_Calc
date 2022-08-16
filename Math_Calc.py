# 目標 二次式の平方完成

from queue import Empty
import re
from tkinter import Variable
from wsgiref import validate
import CalcLib

def Start():
#fomula list [変数,二次項,一次項,定数項]
    print("メニューです\n-----------------------------\n1_展開\n2_因数分解\n3_平方完成\n-----------------------------")
    select = "3"#input("選択してください>> ")
    if(select == "1"):
        Tenkai()
    elif(select == "2"):
        Insuubunkai()
    elif(select == "3"):
        formula = Heihokansei()
        print(formula)
    
def Tenkai():
    test = 0
def Insuubunkai():
    test = 0
def Heihokansei():
    #a( x + b/2a ) + 4ac-b^2/4a
    variable = input("変数を入力してください>> ")
    term_2 = input("二次の項を入力してください>> ")
    term_1 = input("一次の項を入力してください>> ")
    term_c = input("定数項を入力してください>> ")

    t2_coef = term_2.split(variable)[0]
    t1_coef = term_1.split(variable)[0]
    c = term_c
    if(t2_coef==""):
        t2_coef = "1"
    if(t2_coef=="-"):
        t2_coef = "-1"
    if(t1_coef==""):
        t1_coef = "1"
    if(c==""):
        c = "0"
    square_b = CalcLib.LiCalc_Malti(t1_coef,t1_coef)

    if(CalcLib.LiCalc_ChSign(t2_coef)=="+"): 
        a = CalcLib.LiCalc_RmSign(t2_coef,CalcLib.LiCalc_ChSign(t2_coef))
    else:
        a = t2_coef

    if(CalcLib.LiCalc_ChSign(t1_coef)==""):
        squareinsign = "+"
    else:
        squareinsign = "-"

    t1_coef = t1_coef.replace("-","")
    #a( x + b/2a ) + c+(-(b^2/4a))
    if(a == "-1"):
        if(c == "0"):
            square_formula = "-({1}{2}{3}/{4})^2-{5}/{6}".format(a,variable,squareinsign,t1_coef, CalcLib.LiCalc_Malti("2",a), CalcLib.LiCalc_Malti(t1_coef,t1_coef),CalcLib.LiCalc_Malti("4",a))
        else:
            square_formula = "-({1}{2}{3}/{4})^2-{6}/{7}+{5}".format(a,variable,squareinsign,t1_coef, CalcLib.LiCalc_Malti("2",a),  c, CalcLib.LiCalc_Malti(t1_coef,t1_coef),CalcLib.LiCalc_Malti("4",a))
    elif(a == "1"):
        if(c == "0"):
            square_formula = "({1}{2}{3}/{4})^2-{5}/{6}".format(a,variable,squareinsign,t1_coef, CalcLib.LiCalc_Malti("2",a), CalcLib.LiCalc_Malti(t1_coef,t1_coef),CalcLib.LiCalc_Malti("4",a))
        else:
            square_formula = "({1}{2}{3}/{4})^2-{6}/{7}+{5}".format(a,variable,squareinsign,t1_coef, CalcLib.LiCalc_Malti("2",a),  c, CalcLib.LiCalc_Malti(t1_coef,t1_coef),CalcLib.LiCalc_Malti("4",a))
    else:
        if(c == "0"):
            square_formula = "{0}({1}{2}{3}/{4})^2-{5}/{6}".format(a,variable,squareinsign,t1_coef, CalcLib.LiCalc_Malti("2",a), CalcLib.LiCalc_Malti(t1_coef,t1_coef),CalcLib.LiCalc_Malti("4",a))
        else:
            square_formula = "{0}({1}{2}{3}/{4})^2-{6}/{7}+{5}".format(a,variable,squareinsign,t1_coef, CalcLib.LiCalc_Malti("2",a),  c, CalcLib.LiCalc_Malti(t1_coef,t1_coef),CalcLib.LiCalc_Malti("4",a))


    return square_formula

if __name__ == "__main__":
    Start()