# Contact Book with Login - Django Mini Project
A simple contact book web application using Django where users can securely log in and manage their own contacts (add, view, update, delete). Each user has isolated access to their own contacts only.

## Features
- User authentication (Login/Logout/Register).  
- Contact Management (Create, Read, Update, Delete).  
- Search contacts by name or email.  
- User-specific contact isolation (each user sees only their contacts).


### Getting Started
# 1. Clone the Repository
```bash
https://github.com/Farzana3274/django-mini-project.git
cd contactbook
```
(git clone https://github.com/Farzana3274/django-mini-project.git)


# 2. Create and Activate Virtual Environment
```bash   
python -m venv env
env\Scripts\activate
```

# 3. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

# 4. Create a Superuser (Admin Access)
```bash
python manage.py createsuperuser
```
Follow the prompts to set a username, email, and password.

# 5. Run the Development Server
```bash
python manage.py runserver
```
Visit http://127.0.0.1:8000/ in your browser.

#### Login / Register
- Users can register via /accounts/register/
- Admins can log in at /admin/ using the superuser credentials.
