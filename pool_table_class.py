from datetime import datetime


tables=[]

class Table:
    def __init__(self, number):
       self.number = number
       self.occupied = False
       self.start_time = None
       self.end_time = None
       self.time_played = None
       self.current_time = None

    def checkout(self):
      self.occupied=True
      self.start_time=datetime.now()
      print(f"You checkout Table {self.number} {self.occupied} {self.start_time.strftime('%m/%d/%Y %H:%M%:%S')}")


    def checkin(self):
        self.occupied=False
        self.start_time=None
        self.end_time=None
        self.time_played=self.end_time-self.start_time
        print(f"Table Closed  Table {self.number} {self.occupied} {self.start_time.strftime('%M/%d/%Y %H:%M%:%S')}")

        
      
def display_tables():
    
    for table in tables:

        if self.occupied==True:
            status="Occupied"

        else:
            status= "Available"

        print(f"Table No1--{table.number}-- current_time--{table.current_time}--status--{table.occupied}")
        

    
for i in range (1,13):
  table=Table(i)
  tables.append(table)

print("************************Pool Table Managment*****************************\n")
print("To Checkout: Enter 1: ")
print("To Checkin: Enter 2: ")
print("View All Table: Enter 3: ")
print("To quit, Enter 'q'  ")
print("************************P*****************************\n")


def Display_tables(self):
    current_time = datetime.now()
    Print(f"************************Pool Table Managment*****************************\n")   
    print("******* TABLE LIST***************")

    for table in tables:
            if table.occupied == True:
                status = "Occupied"
            else:
                status = "Available"
            if table.start_time != "":
                pretty_clock = formatter.clock_format(table.start_time,)
                elapsed_time = formatter.timer_format(
                current_time, table.start_time)
                print( f"Table-{table.number} - {status} -  Start: {pretty_clock} - Play time: {elapsed_time}")
            else:
                print(
                    f"Table-{table.number} - {status}")


while True:

    choice = input("MAIN MENU: Please Select Your Choice From The Menu ")
        
    if choice == "1":
        print("*************************************")
        
        confirmatation = input("Check pooltable Availablity?\n 'Enter Yes or No (y/n)':")
        if confirmatation == "No":
            print("No table available now please comeback later, THANKYOU!!")
        else confirmatation=="Yes"
            Display_tables()
            table_number=int(input("Enter table Number to check-out:"))
            table=tables[table_number-1]
            table.time_start=None
            table.checkout()
            print(f"Table {table.number} has been checked out at: {self.start_time.strftime('%M/%d/%Y %H:%M%:%S')}")


    




