s="When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed, and Jem's fears of never being able to play football were assuaged, he was seldom self-conscious about his injury. His left arm was somewhat shorter than his right; when he stood or walked, the back of his hand was at right angles to his body, his thumb parallel to his thigh."

l=len(s)
letter=0
word=0
sent=0

for i in range(l):
    if (s[i]==" " or s[i]=="," or s[i]==";"):
    	word+=1
    elif (s[i]=="." or s[i]=="?" or s[i]=="!"):
        sent+=1
        word+=1
    elif(s[i]=="'" or s[i]=="-"):
    	continue
    else:
    	letter+=1
        
print("letters : ",letter)
print("words : ",word)
print("sentences : ",sent)
    
#compiled online, so didn't try file reading
#Fatematuzzohura Kareema