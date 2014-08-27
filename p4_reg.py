import re

data=open('3.txt').read()

matches=re.findall(r'[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]',data)

print ''.join(matches)

# str=open('3.txt','r')
# c_list=[]
# for char in str.read():
    # c_list.append(char)

    
    
# str.close()    
    
    
