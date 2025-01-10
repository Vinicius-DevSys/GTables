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
        with open("Table.csv", "w", newline="") as file:
            writer = csv.writer(file)
            for row in self.table:
                writer.writerow(row)

class DataMaker():
    def __init__(self, substantive, adjective):
        self.substantive = substantive
        self.adjective = adjective
        
    def build_data(self):
        return f"{random.choice(self.substantive)} {random.choice(self.adjective)}"

