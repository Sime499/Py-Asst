from datetime import datetime
time = datetime.now()


class Table:
    def __init__(self, number):
        self.number = number
        self.occupied = False
        self.start_time = None
        self.end_time = None
        self.time_played = None
        self.current_time = None


    def checkout(self):
        if self.occupied == True:
            
            input(f" Table {self.number} is currently occupied! ")
        else:
            self.occupied = True
            self.start_time = datetime.now
            self.end_time = datetime.now
            self.time_played = self.end_time - self.start_time


    def checkin(self):
        if self.occupied == False:
    
            input( " This table is currently available!! Please select another table")
            
        else:
            self.occupied = False
            self.end_time = datetime.now()
            self.time_played = self.end_time - self.start_time

    class ActivityLog():
    def __init__(self, date):
        self.date = date
        self.entry_list = []

    def create_entry(self, table, start, end, total_time):
        start_start = formatter.date_format(start)
        end_time = formatter.date_format(end)
        played_time = formatter.timer_format(end, start)
        cost = formatter.cost_calc(end, start)
        entry = {"Table Number": table, "Start Time": start_time,
            "End Time": end_time, "Total Time Played": f_total_time, "Cost": cost
        }
        self.entry_list.append(entry)
        return self.entry_list

    def cost_calc(self, end, start):
        delta_time = end - start
        delta_min = delta_time.now()
        cost = f"${(hours * 30.00) + (minutes * 0.50)}"
        return cost
