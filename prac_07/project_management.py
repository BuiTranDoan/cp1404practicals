"""
Prac 07 Project Management Program
Estimate time: 2 Hour
Actual time: 2 and a half hour
"""
import datetime
from project import Project

def main():
    projects = Project.load_projects("projects.txt")
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from projects.txt")
    menu = "\n- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"
    while True:
        print(menu)
        choice = input(">>> ").upper()

        if choice == 'L':
            filename = input("Enter filename to load: ")
            projects = Project.load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")

        elif choice == 'S':
            filename = input("Enter filename to save: ")
            Project.save_projects(filename, projects)
            print(f"Projects saved to {filename}")

        elif choice == 'D':
            display_projects(projects)

        elif choice == 'F':
            date_str = input("Show projects that start after date (dd/mm/yy): ")
            filter_projects_by_date(projects, date_str)

        elif choice == 'A':
            add_new_project(projects)

        elif choice == 'U':
            update_project(projects)

        elif choice == 'Q':
            save_choice = input("Would you like to save to projects.txt? (yes/no): ").lower()
            if save_choice == 'yes':
                save_projects(projects, "projects.txt")
            print("Thank you for using custom-built project management software")
            break

def display_projects(projects):
    incomplete_projects = [project for project in projects if not project.is_completed()]
    completed_projects = [project for project in projects if project.is_completed()]

    incomplete_projects.sort(key=priority_sort_key)
    completed_projects.sort(key=priority_sort_key)

    print("Incomplete projects: ")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects: ")
    for project in completed_projects:
        print(f"  {project}")

def priority_sort_key(project):
    return project.priority

def filter_projects_by_date(projects, date):
    filter_date = datetime.datetime.strptime(date, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.start_date >= filter_date]

    filtered_projects.sort(key=project_start_date_key)
    for project in filtered_projects:
        print(f"{project}")

def project_start_date_key(project):
    return project.start_date

def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    completion_percentage = input("Percent complete: ")

    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)

def update_project(projects):
    """Prompt the user to choose a project and update its completion percentage and/or priority.
    The completion percentage must not be lower than the current percentage."""
    print("Which project would you like to update?")
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    project_choice = int(input("Project choice: "))
    project = projects[project_choice]

    # Display the selected project details
    print(f"{project.name}, start: {project.start_date.strftime('%d/%m/%Y')}, "
          f"priority: {project.priority}, estimate: ${project.cost_estimate:.2f}, "
          f"completion: {project.completion_percentage}%")

    # Get new percentage and validate it
    new_percentage = input(f"New Percentage (current: {project.completion_percentage}): ")
    if new_percentage:
        new_percentage = int(new_percentage)
        if new_percentage < project.completion_percentage:
            print("Error: New completion percentage cannot be lower than the current one.")
            return  # Return to main menu if invalid input
        else:
            project.completion_percentage = new_percentage

    new_priority = input(f"New Priority (current: {project.priority}): ")
    if new_priority:  # If the user enters a new priority
        project.priority = int(new_priority)
    else:
        return

def save_projects(projects, filename):
    """Save the list of Project objects to a specified file."""
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")

if __name__ == "__main__":
    main()