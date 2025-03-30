"""
Prac 07 Project Management Program
Estimate time: 2 Hour
Actual time: 2 and a half hour
"""
import datetime

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialize a new Project instance with the given attributes."""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        """Return a string representation of the project, showing relevant details."""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"

    def update(self, completion_percentage=None, priority=None):
        """Update the completion percentage and/or priority of the project."""
        if completion_percentage is not None:
            self.completion_percentage = int(completion_percentage)
        if priority is not None:
            self.priority = int(priority)

    @classmethod
    def from_line(cls, line):
        """Convert a line from the projects file into a Project instance."""
        fields = line.strip().split("\t")
        return cls(fields[0], fields[1], fields[2], fields[3], fields[4])

    def is_completed(self):
        """Check if the project is completed."""
        return self.completion_percentage == 100

    @staticmethod
    def load_projects(filename):
        """Load projects from a specified file and return them as a list of Project objects."""
        projects = []
        try:
            with open(filename, "r") as file:
                file.readline()  # Skip header
                for line in file:
                    projects.append(Project.from_line(line))
        except FileNotFoundError:
            print(f"File {filename} not found.")
        return projects
