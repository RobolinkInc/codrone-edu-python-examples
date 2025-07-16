#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()

x = int(input("Enter a number:"))

if x > 5:
  drone.controller_buzzer_sequence("success") # controller's buzzer creates 'success' sound sequence
else:
  drone.controller_buzzer_sequence("error") # controller's buzzer creates 'error' sound sequence

drone.close()