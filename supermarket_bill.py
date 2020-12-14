import math
from datetime import datetime

  

name=input("enter ur name::")
print('hi, mr/miss.',name,"welocome to market🙏")


def bill_call():
    a=True
    total_price=0
    list_item_price=[]
    while a:
        print("available optins")
        print('''
        1.list of items
        2.choosi items
        3.exit
        '''  )


        choice=int(input("enter your choice::"))
        choices=[1,2,3]
        if choice in choices:
            d={'dal':50,'oil':80,'mirchi':30,'past':20}
            if choice == 1:  # it is used to see items for user
               # c=1
                print("thids is availablelist:")
                print(20*"+")
                for i,j in d.items():
                    #print("thids is availablelist:")         # it s for to ittrate items in dictionary
                    print('\t','-',i,'$',j) #\t is for to get tab space in o/p and i represents keys and j represents values in dict and c represent ittration count
                   # c+=1                      #c increments each ittration
#here while a is not falls so it will ittarate again and it will ask again while loop print statement
                print(20*"+")
            if choice == 2:                     #for selecting items
                q=True
                while q:
                    print("press q to c main menu:")
                       
                    item=input("enter ur item::")
                    if item in d. keys():
                        qnt=int(input("enter item quantity:"))
                       # if qnt . isdigit() :

                           # qnt =int(qnt)
                        price=float(d[item]*qnt)#here d[items]means values in dict ,it will multiples the qnt and price in dict
                        list_item_price.append((item,qnt,price))
                        total_price +=price# here the totoal price is always incremented by price,
                            #after these the controler will go while q it will ask presss q to c main menu
                        #else:
                        #    print("invaild input")
                    elif item=='q':#if here user enters q 
                        q=False # here the while loop becomes break bcz q= false it will come out from the loop 
                                #it will go while a loop
                    else:
                        print("item not present")
            if choice == 3:
                a = False #here choice is 3 we said a=false so when a=flase the while a loop gets break it will come out 
        else:
            print("invaild input")
    return total_price,'Thank u Visit again.urs madu store',list_item_price

total,msg,item_price=bill_call()#method calll from top
if total !=0:
    print('/n')
    print('''
                madhu stores
        marathahalli,bangalore.
                560037
                ''')
    print('Custtomer Name:',name,'\t','Date:',datetime.now())
    print(60*'=')
    #print('/n')


    for j in item_price:
        print('Items:',j[0],'\tQuntity:',j[1],'price',j[2])


    gst=total*0.010
    gst=math.ceil(gst)# ceil() is used to round figure the next value,flolre() is for figure back value
    print(60*'=')
    print('GST:rs',float(gst))
    print('Total payble amount: Rs.',float(gst+total))
    print(20*'=')
    print(msg)
else:
    print("hey you not bought any item.......plz buy somthing")
    bill_call()

