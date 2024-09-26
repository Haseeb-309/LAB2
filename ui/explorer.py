# explorer.py
import db.database as database

def add_post(username):
    print("=== Add Post ===")
    post_content = input("Enter your post: ")

    database.add_post(username, post_content)
    print("Post added successfully.")

def view_posts():
    print("=== Posts ===")
    
    posts = database.get_posts()
    if not posts:
        print("No posts available.")
    else:
        for post in posts:
            print(f"{post['user']}: {post['content']}")

 
# main.py
import ui.login as login
import ui.explorer as explorer

def main():
    while True:
        print("\n1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            user = login.login()
            if user:
                while True:
                    print("\n1. Add Post")
                    print("2. View Posts")
                    print("3. Logout")
                    explorer_choice = input("Choose an option: ")

                    if explorer_choice == "1":
                        explorer.add_post(user)
                    elif explorer_choice == "2":
                        explorer.view_posts()
                    elif explorer_choice == "3":
                        break
                    else:
                        print("Invalid option.")
            else:
                print("Login failed.")
        elif choice == "2":
            login.register()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    # Application entry point
    main()
