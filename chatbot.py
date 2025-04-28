def greet(bot_name, birthyear):
    print("hello there...my name is : {0} ".format(bot_name))
    print("my age is {0} ".format(birthyear))

def remind_name():
    print("can u remind me ur name?" )
    name=input()
    print("nice to meet you {0} ".format(name))
    
def guess_age():
    print("let me guess your age..")
    print("please mention the remiander of your age when divided by 3,5,7")
    rem3=int(input())
    rem5=int(input())
    rem7=int(input())
    age=(rem3*70 + rem5*21 + rem7*15 )% 105
    print("your age is {0} ".format(age))

def count_num():
    print("i can count to any number u want...")
    num=int(input("please mention a number"))
    count=1
    while count<=num:
        print(count,end=" ")
        count+=1
def test():
    print("lets take a small test: ")
    print("is java an OOP language")
    print("1) true ")
    print("2) false ")
    answer=1
    guess=int(input())
    while guess!=answer:
        print("try again")
        guess= int(input())
    print("congo have a nice day")
    
def end():
    print("congratulations")
# greet('siri', '2025')
# remind_name()
# guess_age()
# count_num()
test()
end()