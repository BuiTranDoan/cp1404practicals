"""
Prac 07 Project Management Program
Estimate time: 2 Hours
Actual time:
"""
import datetime

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)
