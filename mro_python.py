"""
We are trying to learn how MRO workes in the Python Method Resolution Order

Method Resolution Order(MRO) it denotes the way a programming language resolves a method or attribute.
Python supports classes inheriting from other classes. 
"""


class sample_1:
    def __init__(self,):
        print(f"Sample_1 : {self.__str__}")
    

class sample_2:
    def __init__(self,):
        print(f"Sample_2 : {self.__str__}")

class sample_3(sample_2, sample_1):
    def print_s3(self,):
        print("Hello - s3")


s3 = sample_3()
s3.print_s3()

