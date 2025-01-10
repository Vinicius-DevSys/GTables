import csv, random

class TableMaker():
    def __init__(self, columns):
        self.table = [columns]

    def add_row(self, row):
       self.table.append(row)
    
    def columns(self):
        return self.table[0]
       
    def check_table(self):
        return self.table
    
    def build(self):
        with open("Table.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for row in self.table:
                writer.writerow(row)

class DataMaker():
    def __init__(self, substantive, adjective, last_number=0):
        self.substantive = substantive
        self.adjective = adjective
        self.last_number = last_number
        
    def create_name_data(self):
        return f"{random.choice(self.substantive)} {random.choice(self.adjective)}"

    def create_progress_data(self, minmax=[0, 10]):
        send_number = self.last_number
        self.last_number += random.randint(minmax[0], minmax[1])
        return send_number
