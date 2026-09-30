import threading
import time

def walk_dog(first,last):
    time.sleep(8)
    print(f"You finish Walking the dog {first} {last}")
def walk_up(name):
    time.sleep(2)
    print(f"You finished {name} walking up")
def walk_down():
    time.sleep(4)
    print("You finished walking down")

chore1=threading.Thread(target=walk_dog,args=("Scoby","Doo"))
chore1.start()
chore2=threading.Thread(target=walk_up,args=("Booby",))
chore2.start()
chore3=threading.Thread(target=walk_down,args=())
chore3.start()
chore1.join()
chore2.join()
chore3.join()
print("You Finished All The works")