from datetime import datetime

day=datetime.today().strftime('%A')

#Making To Do Lists

def ToDoList():
    file1= input('Enter File Name: ')
    if day=='Monday':
        data="""
        To Do List:
        Workout
        School Classes
        School Notes&Homework
        Ahaguru-Science
        CS50
        Udemy-Drawing
        """
        with open(file1,'w') as a:
             a.write(data)
        print('To Do List Completed')

    if day=='Tuesday':
        data="""
        To Do List:
        Workout
        School Classes
        School Notes&Homework
        Ahaguru-Science
        Coding Class
        CS50
        Udemy-Drawing
        """
        with open(file1,'w') as a:
             a.write(data)
        print('To Do List Completed')
    
    if day=='Wednesday':
        data="""
        To Do List:
        Workout
        School Classes
        School Notes&Homework
        Ahaguru-Math
        Coding Project
        CS50
        Udemy-Drawing
        """
        with open(file1,'w') as a:
             a.write(data)
        print('To Do List Completed')

    if day=='Thursday':
        data="""
        To Do List:
        Workout
        School Classes
        School Notes&Homework
        Ahaguru-Math
        Coding Class
        CS50
        Udemy-Drawing
        """
        with open(file1,'w') as a:
             a.write(data)
        print('To Do List Completed')

    if day=='Friday':
        data="""
        To Do List:
        Workout
        School Classes
        School Notes&Homework
        Ahaguru-Science-Live Class
        Coding Project
        CS50
        Udemy-Drawing
        """
        with open(file1,'w') as a:
             a.write(data)
        print('To Do List Completed')

    if day=='Saturday':
        data="""
        To Do List:
        Workout
        School Notes&Homework
        Ahaguru-Math-Live
        CS50
        Udemy-Drawing
        """
        with open(file1,'w') as a:
             a.write(data)
        print('To Do List Completed')

ToDoList()