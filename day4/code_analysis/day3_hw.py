allist=[]
datetime=[]
ipadrress=[]
msisdn=[]
plan=[]
package=[]
port=[]
httpmethod=[]
httpcode=[]
logid=[]
lineno=0
flag=0
with open('apache.log', 'r') as inputfile:
    for line in inputfile:       
        for word in line.split(): 
            allist.append(word)
        lineno+=1
   
    j=0  
    for i in range(lineno):
        datetime.append(allist[j])
        j+=11
    j=1  
    for i in range(lineno):
        ipadrress.append(allist[j])
        j+=11
    j=3  
    for i in range(lineno):
        msisdn.append(allist[j])
        j+=11 
    j=4  
    for i in range(lineno):
        plan.append(allist[j])
        j+=11
    j=5  
    for i in range(lineno):
        package.append(allist[j])
        j+=11
    j=6  
    for i in range(lineno):
        port.append(allist[j])
        j+=11
    j=7  
    for i in range(lineno):
        httpmethod.append(allist[j])
        j+=11
    j=9 
    for i in range(lineno):
        httpcode.append(allist[j])
        j+=11
        
    j=10
    for i in range(lineno):
        logid.append(allist[j])
        j+=11
print(datetime)
print(ipadrress)
print(msisdn)
print(plan)
print(package)
print(port)
print(httpmethod)
print(httpcode)
print(logid)
