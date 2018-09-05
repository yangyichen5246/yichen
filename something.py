name = input("please input your name :  ")
print("hello,"+name+"!")

height = input("please input your height:")
height = int(height)

# while height <100 :
if height > 10:
       print("ok")
else:
       print("fuck")

class Dog():
    """简单测试"""



    def __init__(self,name,age):
        """初始化属性"""
        self.name = name
        self.age = age
    def sit(self):
        """sit"""
        print(self.name.title()+"is now sitting")
    def roll_over(self):
        print(self.name.title()+"rolled over")


