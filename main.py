from div import division
from add import addition
from subt import subtraction

if __name__=="__main__":
    choice = input("""
1.) Division
2.) Subtraction
3.) Addition

Enter your choice: """)
    if choice=="1":
        division()
    elif choice=="2":
        subtraction()
    elif choice=="3":
        addition()
    else:
        print("Wrong Input Provided!")
        