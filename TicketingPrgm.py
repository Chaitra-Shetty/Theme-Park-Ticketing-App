# Ticketing Program
# below code to print text in color : 
#   HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKCYAN = '\033[96m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'

import datetime

def infoDesk():
    print(" \033[4m"+ "\033[1m"+ "Welcome to ABC Adventure Theme Park" + "\033[0m" + "\033[0m")
    print(" \033[92m Entrance ticket details : \033[0m")
    print(" \033[96mAdult			£20  \n Child			£12 \n Senior citizen		£11 \033[0m")
    print("\n\033[96m Parking : Free\033[0m")
   
infoDesk()

adult = int(input("How many adult tickets are required : "))
child = int(input("How many child tickets are required : "))
senior = int(input("How many senior citizen tickets are required : "))
lead = input("Lead booker surname please : ")
car_pass = input("Do you need a parking pass for the car (yes/no):  ").lower()

try:  
    if(car_pass == "yes"):
         print("\n\033[95m*****Parking Permit*****\n\033[0m")
    else:
        raise Exception("\n\033[95mThank you for Purchase!\n\033[0m")
except Exception as e:
    print(e)

def ticketPurchase(adult_tick,child_tick,senior_tick,lead_surname):
    total_tic = adult_tick + child_tick+ senior_tick
    totalcost = adult_tick * 20 + child_tick * 12 + senior_tick * 11
    return print(f"\033[94m********************************************\nTotal no. of tickets are {total_tic} which costs :{totalcost}£\nBooker Surname : {lead_surname}\nDate of Purchase : {datetime.datetime.now()}\nThank you for purchasing...\n********************************************\n\033[0m")


ticketPurchase(adult,child,senior,lead)
