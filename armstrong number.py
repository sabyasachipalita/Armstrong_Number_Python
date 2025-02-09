
#armstrong number code:
n=int(input("enter  number:")) 
num=n 
arm=0 
while n > 0:  
    r=n%10
    arm=arm+(r*r*r)
    n=n//10
if(num==arm):
    print("armstrong number",arm)
else:
    print("not armstrong number",arm)



#dry run of this code is
# lets suppose n=153 which is a armstrong number
# n=153 (1*1*1+5*5*5+3*3*3)=153
# num=153(153 will assign to num variable)
# while always check condition then execute
# then i think you should understand easyly  because all valuee given you just put and check

       #THANKS






















#fibocaccic series using python

def fibonnaic_series(n):
    if(n==0): 
        return 0
    elif(n==1):
        return 1
    else:
        return fibonnaic_series(n-1)+(n-2)
          















    