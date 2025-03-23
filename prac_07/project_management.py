"""
Prac 07 Project Management Program
Estimate time: 2 Hours
Actual time:
"""
import datetime
from project import Project

def main():
    projects = Project.load_projects("projects.txt")
    print(f"Loaded {len(projects)} projects from projects.txt")

    while True:
        display_menu()
        choice = input(">>> ").lower()

        if choice == 'l':
            filename = input("Enter filename to load: ")
            projects = Project.load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")

        elif choice == 's':
            filename = input("Enter filename to save: ")
            Project.save_projects(filename, projects)
            print(f"Projects saved to {filename}")

        elif choice == 'd':
            display_projects(projects)

        elif choice == 'f':
            date_str = input("Show projects that start after date (dd/mm/yy): ")
            filter_projects_by_date(projects, date_str)

        elif choice == 'a':
            add_new_project(projects)

        elif choice == 'u':
            update_project(projects)

        elif choice == 'q':
            save_choice = input("Would you like to save to projects.txt? (yes/no): ").lower()
            if save_choice == 'yes':
                Project.save_projects("projects.txt", projects)
            print("Thank you for using custom-built project management software")
            break


if __name__ == "__main__":
    main()