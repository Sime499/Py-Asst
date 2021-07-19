from datetime import datetime
datetime=datetime.now()
pool_tables=[]

class PoolTable:
    def _init__(self,table_num):
        self.table_num=table.table_num
        self.is_occupied=False 
        self.start_time=None
        self.end_time=None
        self.played_time=None
        self.total_cost=0



    def checkout() :
        self.is_occupied=False
        self.start_time=datetime.now()
        print(f"You checkedout Table {table_num} Status: { is_occupied} Start time {start_time.strftime('%m/%d/%Y %H:%M:%S')}")

    def checkin ():
        self.is_occupied=True
        self.start_time=datetime.now()('%m/%d/%Y %H:%M:%S')
        self.end_time=datetime.now()('%m/%d/%Y %H:%M:%S')
        self.time_played=(self.end_time-self.start_time)('%m/%d/%Y %H:%M:%S')
        self.total_cost=self.played_time*30
def display_tables():
    for  pool_table in pool_tables:
        if is_occupied==True:
            status=="occupied"
            print("f Table {table_num} Status: { pooltable.is_occupied} Start time {start_time} Played time {current_time -start_time}")
            
        else: 
            status=="Available"
            print("f Table {table_num} Status: { is_occupied} Start time {start_time.strftime('%m/%d/%Y %H:%M:%S)}")

def To_add_file():
    date=str(datetime.now())
    file_ext= ".txt"
    file_name=date + file_ext
    with open (file_name,"w") as file:
        array=[]
        for pool_table in pool_tables:
            table_info=f"\n Table {pool_table.table.num} start time:{pool_table.start_time} End time: {pooltable.end_time} Time played: {pool_table.time_played} cost:{pool_table.total_cost}"
            file.write(table_info)

 
for i in range(1-13):
    pool_tables=PoolTable(i)
    pool_tables.append(pool_tables)
    
print("***************Universit of Texas Pool Table Managment System***************\n")
print("*********************************USER MENU**********************************\n")
print("Enter 1.To Checkout Table:\n")
print("Enter 2.To Checkin Table:\n")
print("Enter 3.To View All Table:\n")
print("Enter 4.To Quit or any key to Exit:\n")
print("****************************************************************************\n")

while True:
    choice=input("Please select your choice from the menu:")
    print("*************POOLTABLE LIST********************")
    try:

        if choice =="1":
            for pool_table in pool_tables:
                
                    display_tables()
                    table_number=int(input("Enter table Number to checkout"))
                    pool_table=pool_tables[table_number-1]
                    pool_table.time_start=datetime.now()
                    pool_table.checkout()

        else:
            To_add_file()
            break


    except Error:
         print("please selct the correct option")








