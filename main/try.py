#Messing around with python code

print("stuffsdfsdfs")

req = 2

message = "Thank you for ordering with us!\n"
message += "You ordered: \n"
if req > 0:
  message += "Eggroll (3 cnt): " + str(req) + '\n'
  message += "  Cost of item: " + str(req * 5)

print(message)