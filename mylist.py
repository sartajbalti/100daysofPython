#  list is a collection data type ordedred mutable, allows duplicates
mylist = ["aca",5,1.7]
# print(mylist)
#  access the list by indexing 
print("Index 1 : ",mylist[0])
# Duplicates 
ml2 = [1,2,2,3,1]
for a in ml2:
    print(a)
#  iteration using for loop
for i in mylist:
    print(i)

# append lish 
mylist.append("new")
print(mylist)

# insert item 
mylist.insert(1,"new2")
print(mylist)

# remove item or you can use pop 
mylist.remove("new2")
print(mylist)
# list revese 
mylist.reverse()
print(mylist)
# sort list
# mylist.sort()
print(mylist)
# list clear
mylist.clear()
print(mylist)
# list copy
mylist3 = [1,2,3,4]
mylist2 = mylist3.copy()
print(mylist2)

# list count
print(mylist2.count(1))
# list delete 
del mylist2[0]

