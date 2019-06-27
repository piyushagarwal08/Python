class A:
    
    def add(self,x,y):
        A.sub(self.x,self.y)
        return x+3
    def sub(x,y):
        return x-y
a=A
print(a.add(5,3))
