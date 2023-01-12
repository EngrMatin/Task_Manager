import datetime
import uuid  

class Task_Manager:
    task_list = []
    task_id = ''
    task_name = ''
    created_time = 'NA'
    update_status = False
    updated_time = 'NA'
    completion_status = False
    completed_time = 'NA'
    task_done = False
    

    def add_new_task(self):
        task_id = str(uuid.uuid4())
        task_name = input("Enter Task: ")
        created_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        update_status = False
        updated_time = 'NA'
        completion_status = False
        completed_time = 'NA'
        new_task = {'ID': task_id, 'Task': task_name, 'Created Time': created_time, 'Update Status': update_status, 'Updated Time': updated_time, 'Completion Status': completion_status, 'Completed Time': completed_time}
        self.task_list.append(new_task) 
        print('\nTask Created Successfully\n')
        

    def update_task(self):
        not_updated_task_list = []
        for i in range(len(self.task_list)):
            if self.task_list[i]['Update Status'] == False:
                not_updated_task_list.append(self.task_list[i])

        if len(not_updated_task_list) == 0:
            print("\nNo Task to Update\n")
        else:
            print("\nSelect which Task to Update\n")

            for i in range(len(not_updated_task_list)):
                print(f"Task No - {i+1}")
                print(f"ID - {not_updated_task_list[i]['ID']}")
                print(f"Task - {not_updated_task_list[i]['Task']}")
                print(f"Created Time - {not_updated_task_list[i]['Created Time']}")
                print(f"Updated Time - {not_updated_task_list[i]['Updated Time']}")
                print(f"Completed - {not_updated_task_list[i]['Completion Status']}")
                print(f"Completed Time - {not_updated_task_list[i]['Completed Time']}")
                print()

            try:
                n = int(input("Enter Task No: "))
            except:
                print('\nEnter a Valid Task Number\n')
                return False

            if n<1 or n>len(not_updated_task_list):
                print('\nEnter a Valid Task Number\n')
                return False


            new_task_name = input("Enter new Task: ")
            not_updated_task_list[n-1]['Task'] = new_task_name
            not_updated_task_list[n-1]['Update Status'] = True
            not_updated_task_list[n-1]['Updated Time'] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            print('\nTask Updated Successfully\n')


    def complete_task(self):
        incomplete_task_list = []
        for i in range(len(self.task_list)):
            if self.task_list[i]['Completion Status'] == False:
                incomplete_task_list.append(self.task_list[i])
        if len(incomplete_task_list) == 0:
            print("\nNo Task to Complete\n")
        else:
            print("\nSelect which Task to Complete\n")

            for i in range(len(incomplete_task_list)):
                print(f"Task No - {i+1}")
                print(f"ID - {incomplete_task_list[i]['ID']}")
                print(f"Task - {incomplete_task_list[i]['Task']}")
                print(f"Created Time - {incomplete_task_list[i]['Created Time']}")
                print(f"Updated Time - {incomplete_task_list[i]['Updated Time']}")
                print(f"Completed - {incomplete_task_list[i]['Completion Status']}")
                print(f"Completed Time - {incomplete_task_list[i]['Completed Time']}")
                print()

            try:
                n = int(input("Enter Task No: "))
            except:
                print('\nEnter a Valid Task Number\n')
                return False

            if n<1 or n>len(incomplete_task_list):
                print('\nEnter a Valid Task Number\n')
                return False

            incomplete_task_list[n-1]['Completion Status'] = True
            incomplete_task_list[n-1]['Completed Time'] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            print('\nTask Completed Successfully\n')
            


    def view_all_task(self):
        if len(self.task_list) == 0:
            print("\nNo Task to Show\n")
        else:
            print()
            for i in range(len(self.task_list)):
                print(f"ID - {self.task_list[i]['ID']}")
                print(f"Task - {self.task_list[i]['Task']}")
                print(f"Created Time - {self.task_list[i]['Created Time']}")
                print(f"Updated Time - {self.task_list[i]['Updated Time']}")
                print(f"Completed - {self.task_list[i]['Completion Status']}")
                print(f"Completed Time - {self.task_list[i]['Completed Time']}")
                print()
        
        

    def view_incomplete_task(self):
        incomplete_task_list = []
        for i in range(len(self.task_list)):
            if self.task_list[i]['Completion Status'] == False:
                incomplete_task_list.append(self.task_list[i])

        if len(incomplete_task_list) == 0:
            print("\nNo Incomplete Task to Show\n")
        else:
            print()
            for i in range(len(incomplete_task_list)):
                print(f"ID - {incomplete_task_list[i]['ID']}")
                print(f"Task - {incomplete_task_list[i]['Task']}")
                print(f"Created Time - {incomplete_task_list[i]['Created Time']}")
                print(f"Updated Time - {incomplete_task_list[i]['Updated Time']}")
                print(f"Completed - {incomplete_task_list[i]['Completion Status']}")
                print(f"Completed Time - {incomplete_task_list[i]['Completed Time']}")
                print()
        

    def view_completed_task(self):
        completed_task_list = []
        for i in range(len(self.task_list)):
            if self.task_list[i]['Completion Status'] == True:
                completed_task_list.append(self.task_list[i])

        if len(completed_task_list) == 0:
            print("\nNo Completed Task to Show\n")
        else:
            print()
            for i in range(len(completed_task_list)):
                print(f"ID - {completed_task_list[i]['ID']}")
                print(f"Task - {completed_task_list[i]['Task']}")
                print(f"Created Time - {completed_task_list[i]['Created Time']}")
                print(f"Updated Time - {completed_task_list[i]['Updated Time']}")
                print(f"Completed - {completed_task_list[i]['Completion Status']}")
                print(f"Completed Time - {completed_task_list[i]['Completed Time']}")
                print()
            


if __name__ == "__main__":

    my_task = Task_Manager()

    error = False
    choice = ''
    while True:
        print("1. Add New Task \n2. Show All Task \n3. Show Incomplete Task \n4. Show Completed Task \n5. Update Task \n6. Mark a Task Completed \n0. EXIT")
        try:
            if error == False:
                choice = int(input("ENTER OPTION: "))
            else:
                error = False
                choice = int(input("PLEASE PROVIDE A VALID OPTION (1-6): "))  
            if choice == 1:
                my_task.add_new_task()
            elif choice == 2:
                my_task.view_all_task()
            elif choice == 3:
                my_task.view_incomplete_task()
            elif choice == 4:
                my_task.view_completed_task()
            elif choice == 5:
                my_task.update_task()
            elif choice == 6:
                my_task.complete_task()
            elif choice == 0:
                break
            else:
                error = True

        except:
            error = True