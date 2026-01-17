from user import User
from post import Post

# Object Creation

user1 = User("John Doe", 30, "john@example.com", "secure123", "Software Engineer")
user1.display_user_info()

user1.update_job_title("DevOps Engineer")
user1.display_user_info()

user2 = User("Jane Smith", 28, "jane@example.com", "secure456", "Data Scientist")
user2.display_user_info()

Post1 = Post("Learning Python is fun!", user1.name)
Post1.get_post_info()