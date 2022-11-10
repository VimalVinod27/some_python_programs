
def removeText(text,remove):
    rem_list=remove.split(',')
    text_list=text.split()
    for i in rem_list:
        for j in range(len(text_list[:])):
            if i in text_list:
                text_list.remove(i)
    newText=" ".join(text_list)
    print("New Text",newText)






print("Enter a text")
text=input()
print("enter the sub strings to remove seperated by comma")
remove=input()
removeText(text,remove)