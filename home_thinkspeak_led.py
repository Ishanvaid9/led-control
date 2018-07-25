import RPi.GPIO as R
import time
import requests
import json
pin_list=[3,5,7,8,10,11,12,13]
R.setwarnings(False)
R.setmode(R.BOARD)
for i in pin_list:
    R.setup(i,R.OUT)


si_in=[]

#function for current status update
def checking_update():
   url1=requests.get("https://api.thingspeak.com/channels/528897/feeds.json?api_key=8K3FFOMKZ6OJWA6Q&results=1")
   response=url1.json()
   si_in.clear()
   for i in range(1,9):
       status=response['feeds'][0]['field'+str(i)]
       si_in.append(status)
       print ("Current field "+str(i)+':'+str(status))
      
       #print(si_in)
#checking_update()


#function for keeping hte fields value 0 or switch off the all LED once
def zero_value():
    x='0'
    ul="https://api.thingspeak.com/update?api_key=ZY5L5O3H8P9OPTLW&field1="+x+"&field2="+x+"&field3="+x+'&field4='+x+'&field5='+x+'&field6='+x+'&field7='+x+'&field8='+x

    url=requests.post(ul)
    print (url)    
#zero_value()

    


#function for keeping hte fields value 1 or switch ON the all LED once
def one_value():
    x='1'
    ul="https://api.thingspeak.com/update?api_key=ZY5L5O3H8P9OPTLW&field1="+x+"&field2="+x+"&field3="+x+'&field4='+x+'&field5='+x+'&field6='+x+'&field7='+x+'&field8='+x

    url=requests.post(ul)
    print (url)    
#zero_value()



#led multiple input
def multiple_input():
    checking_update()
    print("Select the led which ou want to glow\n1.Street light\n2.Street light\n3.Lobby\n4.Room\n5.Room\n6.Kitchen\n7.Bathroom\n8.Gate\n")
    led1=input("1.Street light:")
    led2=input("2.Street light:")
    led3=input("3.Lobby:")
    led4=input("4.Room:")
    led5=input("5.Room:")
    led6=input("6.Kitchen:")
    led7=input("7.Bathroom:")
    led8=input("8.Gate:")
    if((len(led1)>0 and len(led2)>0 and len(led3)>0 and len(led4)>0 and len(led5)>0 and len(led6)>0 and len(led7)>0 and len(led8)>0)):
        if((led1=='1' or led1=='0')and (led2=='1' or led2=='0')and(led3=='1' or led3=='0')and(led4=='1' or led4=='0')and(led5=='1' or led5=='0')and(led6=='1' or led6=='0')and(led7=='1' or led7=='0')and(led8=='1' or led8=='0')):
           print("DATA IS UPLOADING ON THINKSPEAK")
           ul="https://api.thingspeak.com/update?api_key=ZY5L5O3H8P9OPTLW&field1="+led1+"&field2="+led2+"&field3="+led3+'&field4='+led4+'&field5='+led5+'&field6='+led6+'&field7='+led7+'&field8='+led8
           url=requests.post(ul)

           R.output(3,int(led1))
           R.output(5,int(led2))
           R.output(7,int(led3))
           R.output(8,int(led4))
           R.output(10,int(led5))
           R.output(11,int(led6))
           R.output(12,int(led7))
           R.output(13,int(led8))
        else:
            print('THE COMMAND CAN BE ONLY 0 or 1')
            multiple_input()
    else:
         print("YOU NEED TO FILL ALL COLUMN")
         multiple_input()
        
#led single input
def single_input():
    usr_input=int(input("Select the led which ou want to glow\n1.Street light\n2.Street light\n3.Lobby\n4.Room\n5.Room\n6.Kitchen\n7.Bathroom\n8.Gate\n"))
   
    if(usr_input>0 and usr_input<9):
        checking_update()
        v = usr_input-1
        to_do=input("Enter '0' or '1':")
        if(to_do=='0' or to_do=='1'):
            if(usr_input==1):
                si_in.pop(v)
                si_in.insert(v,to_do)
            elif(usr_input==2):
                si_in.pop(v)
                si_in.insert(v,to_do)
            elif(usr_input==3):
                si_in.pop(v)
                si_in.insert(v,to_do)
            elif(usr_input==4):
                si_in.pop(v)
                si_in.insert(v,to_do)
            elif(usr_input==5):
                si_in.pop(v)
                si_in.insert(v,to_do)
            elif(usr_input==6):
                si_in.pop(v)
                si_in.insert(v,to_do)
            elif(usr_input==7):
                si_in.pop(v)
                si_in.insert(v,to_do)
            elif(usr_input==8):
                si_in.pop(v)
                si_in.insert(v,to_do)
            else:
                    single_input()
        else:
            single_input()
    else:
                single_input()
            
    
    print(si_in)
    ul="https://api.thingspeak.com/update?api_key=ZY5L5O3H8P9OPTLW&field1="+si_in[0]+"&field2="+si_in[1]+"&field3="+si_in[2]+'&field4='+si_in[3]+'&field5='+si_in[4]+'&field6='+si_in[5]+'&field7='+si_in[6]+'&field8='+si_in[7]
    url=requests.post(ul)
    out_list=[]
    out_list=si_in.copy()
    for i in range(0,len(si_in)):
        out_list[i]=int(si_in[i])
    print(out_list)    
    for i in out_list:
        R.output(pin_list[i],out_list[i])
    out_list.clear()
        
    

        
#function for controling different led

def led_control():
    print("Welcome to Home led control")
    
      
    while 1:
       option=input("SELSECT OPTION TO PERFORM\n1.MULTIPLE SELECT\n2.SINGLE SELECT\n3.Turn on all \n4.Turn off all")
       if (option=='1'):
          
           multiple_input()
           si_in.clear()
       elif(option=='2'):
           single_input()
           si_in.clear()
       elif(option=='3'):
           one_value()
       elif(option=='4'):
           zero_value()
       else:
           print ("wrong choice select again")
           
   
       
led_control()    
    
