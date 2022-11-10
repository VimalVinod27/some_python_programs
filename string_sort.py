limit=int(input("enter number of elements:"))
print("enter the strings")
alist=[input() for i in range(limit)]
sort_list=alist[:]
for i in range(limit-1):
    for j in range(i+1,limit):
        if sort_list[i].lower() > sort_list[j].lower():
            sort_list[j], sort_list[i] = sort_list[i], sort_list[j]
print("original list",alist)
alist.sort(key=str.lower)
print("sorted list using method",alist)
print("sorted list",sort_list)
