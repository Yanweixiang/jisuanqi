while True:
    print("选择运算：")
    print("1、相加")
    print("2、相减")
    print("3、相乘")
    print("4、相除")
    choice=input("输入你的选择\n")
    if choice!="1" and choice!="2" and choice!="3" and choice!="4":
        print("没有此选项")
        break
    num1=float(input("输入第一个数字\n"))
    num2=float(input("输入第二个数字\n"))
    if choice=='1':
        print("计算结果",num1,"+",num2,"=", num1+num2)
    if choice=='2':
        print("计算结果",num1,"-",num2,"=", num1-num2)
    if choice=='3':
        print("计算结果",num1,"*",num2,"=", num1*num2)
    if choice=='4':
        print("计算结果",num1,"/",num2,"=", num1/num2)