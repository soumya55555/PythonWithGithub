# demo=open("Demo.txt","r")
# print(demo.read())
# demo.close()

# with open("Demo.txt","r") as dm:
#     content=dm.read()
#     print(content)
#
# dm.close()
# print("file has been closed")

#########Write in to file#############
filename="my_first_file"
with open(filename,"w") as fn:
    fn.write("hello world\n")
    fn.write("you are great\n")
print("***************************blow is the code for append to a file********************************")
with open(filename,"a") as fn:
    fn.write("hello python,you are rocking\n")


