class Factor:
    def GCD(self,a,b):
        if a==0:
            return b
        if b==0:
            return a
        if a==b:
            return a
        return self.GCD(b%a,a)
obj=Factor()
print(obj.GCD(625,25)) # 4
# Time complexity: O(log(min(a,b))) where a and b are the two numbers