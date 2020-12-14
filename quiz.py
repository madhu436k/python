'''make quiz that has 4 optonsadd
    1.point if the answer is correct,delet 1 point if answeris worrng
    itshouldhave an option to skip and quit the quiz'''
from test import *
val()

name=input("enter your name:")
print(30*'❓')
print('hi',name,'welcome to quiz' )
print(30*'❓')
q1='''1> what is the capital of india
                            1.delhi
                            2.hyd
                            3.bangalore
                            4.channai'''
q2='''2>what is the capital of andraparadesh
                            1.hyd   
                            2.amaravathi
                            3.tirupati
                            4.kadapa'''
q3='''3>what is the capital of karnataka
                        1.bangalore
                        2.mysure
                        3.ballari
                        4.all above'''
quations={q1:1,q2:2,q3:1}
score=0
for i in quations:
    print(i)
    print(50*'*')
  
    flag=input("do you want skip quation..?")
    l=len(quations)
    if flag=='yes' :
        continue
   

    answer=int(input("enter ur answer 1/2/3/4:"))
    if answer==quations[i]:
        print("your answer is correct ✔✅ ")
        print(50*'*')
        score+=1
        
    else:
        print("your answer is worng ❌,correcr answer is:",quations[i])
 
        print(50*'*')
while True:
    submit=input("press 's' to  submit :")
   
    if submit=='s':
        #submit=input("press 's' to  submit:")
        print(20*'=','RSULT IS',20*'=')
        print(name,"your total score is:",score,"out of",len(quations))
        print(50*'=')
        str='👍'
        print(str.center(40))
        break
    else:
        print("plz submit to see ur result")  