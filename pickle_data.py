import pickle

d1={"name":"vimal","age":23}
file_obj=open("data_variable.txt","wb")
pickle.dump(d1,file_obj)
file_obj.close()
file_obj=open("data_variable.txt","rb")
print(pickle.load(file_obj))
file_obj.close()



