import re
file1=open("Myfile.txt","a")
if re.match("\A(?P<name>[\w\-_]+)@(?P<domain>[\w\-_]+).(?P<toplevel>[\w]+)\Z",file1,re.IGNORECASE):
   print("Email is valid")
   delimiters="@","."
   repattern='|'.join(map(re.escape,delimiters))
   name=re.spilt(repattern,file1)
   print("[Name is:,Domain is:,Extenion is]=",name)
else:
    print("email is invalid")