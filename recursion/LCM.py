class Factorial:
    def GCD(self,a,b):
        if a==0:
            return b
        if b==0:
            return a
        if a==b:
            return a
        return self.GCD(b%a,a)
    def LCM(self,a,b):
        return (a*b)//self.GCD(a,b)
obj=Factorial()
print(obj.LCM(14,74)) # 625
# # Time complexity: O(log(min(a,b))) where a and b are the two numbers