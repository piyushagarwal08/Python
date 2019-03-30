friends = {"harshita":"13/11/1999","kush":"24/03/1999","vaishali":"6-06-1998","raju":"6/04/1999"}
name = input("Enter a name: ")

if(friends.get(name)):
    print(friends[name])
else:
    DOB = input("Enter your Date of birth(dd/mm/yyyy): ")
    friends[name] = DOB
    print(friends)
