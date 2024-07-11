import threading
import random

entrace = 568/4
time_trip = [0]
speed_baj1 = [0]
speed_baj2 = [0]
thread1 = []
thread2 = []

def harkat(entrace,time_trip,speed_baj1,speed_baj2):
    speed_baj1[0] = random.randint(70,120)
    speed_baj2 [0]= random.randint(70,120)
    print("speed1 {}".format(speed_baj1[0]),"\n")
    print("speed2 {}".format(speed_baj2[0]),'\n')
    if speed_baj1[0] <= speed_baj2[0]:
        time_trip[0] = time_trip[0] + (entrace / speed_baj1[0])
    else:
        time_trip[0] = time_trip[0] + (entrace / speed_baj2[0])

if __name__ == "__main__":
    thred_baj1 = threading.Thread(target=harkat,args=(entrace,time_trip,speed_baj1,speed_baj2,))
    thred_baj2 = threading.Thread(target=harkat,args=(entrace,time_trip,speed_baj1,speed_baj2))
    j = 0
    k = 0
    for i in range(4):
        thred_baj1 = threading.Thread(target=harkat,args=(entrace,time_trip,speed_baj1,speed_baj2,))
        thred_baj2 = threading.Thread(target=harkat,args=(entrace,time_trip,speed_baj1,speed_baj2))
        thread1.append(thred_baj1)
        thread2.append(thred_baj2)
        
        if speed_baj1 >= speed_baj2:
            print("speed baj1 wins!\n")
            thread1[j].start()
            thread1[j].join()
            thread2[k].start()
          #  thread1[j].join()
            print("bajenagh 1 arrived\n")
            
            thread2[k].join()
            print("bajenagh 2 arrived\n")
            print(f"entrace {i} finished\n")           
            j += 1
            k += 1
        else:
            print("speed baj2 wins!\n")
            thread2[k].start()
            thread2[k].join()
            thread1[j].start()
            #thread2[k].join()
            print("bajenagh 2 arrived\n")
            
            thread1[j].join()
            print("bajenagh 1 arrived\n")
            print(f"entrace {i} finished\n")
            
            k += 1
            j += 1
