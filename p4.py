str=open('3.txt','r')
c_list=[]
for char in str.read():
    c_list.append(char)
   
for i in range(0,(len(c_list))):
    if i>10:
        break
    else:        
        if i>2:
            for a in range((i-3),(i+4)):
                if c_list[a].islower:
                    if a!=i:
                        break
                else:    

    
str.close()    
    
    
