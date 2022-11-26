email1= str(input("enter your email= "))
email2=str(input("enter your email= "))
index1=email1.index("@")
index2=email2.index("@")
#start:end
username1=email1[:index1]
username2=email2[:index2]
#strt:end
domain1=email1[index1:]
domain2=email2[index2:]
print(f"username: {username1} and domain: {domain1}")
print(f"username: {username2} and domain: {domain2}")





