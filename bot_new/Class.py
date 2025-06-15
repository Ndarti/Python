class Example:
    def __init__(self):
        self.Num1 = 0
        self.Num2 = '-'
        self.Count=0
    def set_Num1(self, new_Num):
        self.Num1 = new_Num
    def set_Num2(self, new_Num):
        self.Num2 = new_Num
    def set_Count(self, new_Count):
        self.Count = new_Count
    def sum(self):
        if self.Count=='-':
            return self.Num1-self.Num2
        if self.Count=='+':
            return self.Num1+self.Num2
        return 0