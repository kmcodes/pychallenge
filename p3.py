alpha=list(map(chr, range(97,123)))

string1=open('2.txt','r')
for char in string1.read():
    if char in alpha:
        print char
       
string1.close()    
    
    
