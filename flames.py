#flames = {"f":"friends","l":"love","a":"affectionate","m":"marriage","e":"enemies","s":"sister"}
print("This is the Realtion Calculator")
import sys
flames = ["friends","love","affectionate","marriage","enemies","siblings"]
boy = list(input("enter name of boy: ").lower())
girl = list(input("enter name of girl: ").lower())
try:
    common = [i for i in boy if i in girl]
    common = set(common)  
except:
    print("huh...you are just friends")
    sys.exit()
for i in common:
    boy.remove(i)
    girl.remove(i)
total_similar = len(boy)+len(girl)
while(len(flames)!=1):
    count = (total_similar%len(flames))-1
    if count>0:
        right = flames[count+1:]
        left = flames[:count]
        flames = right+left
    else:
        flames = flames[:len(flames)-1]
print(flames[0])
        
        
    
    
    
    
    
