import re
P="2{1,4}"
if re.match(P,"2"):
    print("matched")
if re.match(P,"222"):
    print("match")
