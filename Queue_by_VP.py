#queue is built in module in python 3.7 therefore Available in College pc for sure.

import queue as a
def dis(q):
    s=q.qsize()
    while s>0:
        a=q.get()
        print(a)
        q.put(a)   #puting the element again which has been removed for printing earlier.                         
        s-=1

q=a.Queue()
print("MENU:\n1.EnQueue\n2.DeQueue\n3.LengthOfQueue\n4.Check Queue Emptiness\n5.Display Queue\n6.EXIT")
ch=int(input("Enter Your Choise=  "))
while ch<=5:
    if (ch==1):
        val=int(input("Enter Element To Be Inserted Into  Queue=  "))
        q.put(val)
        print("Value ",val,"  Inserted")
       
        
    elif (ch==2):
          
          
         
          if q.qsize()==0:
              print("Queue Is Empty, Cannot Delete Element  !!! ")
              
          else:
              print("Removed Element=  ",q.get())
             
          
              
            
    elif (ch==3):
        l=q.qsize()
        print("Number Of Elements In The Queue Are =  ",l)
    elif (ch==4):
         if (q.qsize()==0):
            print("Queue Is Empty")
         else:
            print("Queue Is Not Empty")
           
    elif (ch==5):
            dis(q)
            print("End")
    
            
            
            
    ch=int(input("Enter Your Next Choise=  "))
print("INVALID INPUT ,Execution Stopped\nYOU HAVE TO RUN AGAIN!!!!!!")
        
