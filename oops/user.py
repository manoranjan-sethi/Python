class User :
    def __init__(self, name, age, email, password, current_job_title):   # init is a constructor method
        self.email = email
        self.name = name
        self.age = age
        self.password = password
        self.current_job_title = current_job_title


    def change_password(self, new_password):           # function belongs to a class is called method
        self.password = new_password

    def update_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def display_user_info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Email: {self.email}')
        print(f'Current Job Title: {self.current_job_title}')
        print('---------------------------')

# Object Creation

user1 = User("John Doe", 30, "john@example.com", "secure123", "Software Engineer")
user1.display_user_info()

user1.update_job_title("DevOps Engineer")
user1.display_user_info()

user2 = User("Jane Smith", 28, "jane@example.com", "secure456", "Data Scientist")
user2.display_user_info()