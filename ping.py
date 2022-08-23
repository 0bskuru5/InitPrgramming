import os
import time
a = input("Enter your target: ")

while True:
    def pingit(target):
        response = os.system("ping -c 1 " + target)
    
        if response == 0:
            return True
        else:
            return False
        time.sleep(120)
    
print(pingit(a))

pingit()
    

