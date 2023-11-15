import argparse
import os
from shutil import copytree, rmtree
import inquirer
import re
from art import *
from pathlib import Path
import platform
import subprocess
import time


def create_django_app(app_name):
    # Use os.path.join to join paths in a platform-independent way
    app_path = os.path.join(os.getcwd(), app_name)
    venv_path = os.path.join(app_path, "venv")

    # Create the app directory if it doesn't exist
    os.makedirs(app_path, exist_ok=True)

    # Move to the app directory
    os.chdir(app_path)

    # Use subprocess.run for running commands to capture the output and handle errors
    subprocess.run(["python", "-m", "venv", "venv"], shell=True, check=True)

    # Use os.path.join to create the path to the activate script
    activate_script = os.path.join(
        venv_path, "Scripts" if platform.system() == "Windows" else "bin", "activate"
    )

    # Use the "source" command on Linux/Mac or "call" on Windows to activate the virtual environment
    activate_command = (
        f"call {activate_script}"
        if platform.system() == "Windows"
        else f"source {activate_script}"
    )
    subprocess.run(activate_command, shell=True, check=True)

    manage_script = os.path.join(app_path, "manage.py")

    subprocess.run(["pip", "install", "django"], shell=True, check=True)
    subprocess.run(
        ["python", "manage.py", "startapp", "authentication"], shell=True, check=True
    )

    # Install Django Rest Framework (DRF)
    subprocess.run(
        [
            "pip",
            "install",
            "djangorestframework",
            "djangorestframework-simplejwt",
            "python-dotenv",
        ],
        shell=True,
        check=True,
    )

    # Update settings.py with DRF in INSTALLED_APPS
    with open(os.path.join(app_path, app_name, "settings.py"), "a") as settings_file:
        settings_file.write(
            "\nINSTALLED_APPS += ['rest_framework', 'rest_framework_simplejwt', 'authentication']"
        )

    with open(os.path.join(app_path, app_name, "settings.py"), "a") as settings_file:
        settings_file.write("\nAUTH_USER_MODEL = 'authentication.CustomUser'")

    # Update urls.py with DRF
    with open(os.path.join(app_path, app_name, "urls.py"), "a") as urls_file:
        urls_file.write(
            "\nfrom django.urls import include\nfrom rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)\n\nurlpatterns += [path('api-auth/', include('rest_framework.urls')),\
                        path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),                            \
                        path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), \
                        path('api/', include('authentication.urls')),]"
        )

    # Update requirements.txt
    subprocess.run(["pip", "freeze", ">", "requirements.txt"], shell=True, check=True)

    current_directory = os.getcwd()
    parent_directory = os.path.join(current_directory, os.pardir)
    api_folder_path = os.path.join(app_path, "authentication", "api")
    os.makedirs(api_folder_path)

    # models.py
    script_dir = os.path.dirname(os.path.realpath(__file__))
    print(script_dir)
    views_path = os.path.join(script_dir, "authentication", "api", "views.py")
    with open(views_path, "r") as models_file:
        models_file_content = models_file.read()
        with open(os.path.join(app_path, "authentication", "models.py"), "a+") as new_models_file:
            new_models_file.write(models_file_content)



    #subprocess.run(["python", "manage.py", "makemigrations", "--noinput"], check=True)
    #subprocess.run(["python", "manage.py", "migrate"], shell=True, check=True)





def configure_django_app(app_name, use_drf, database):
    print(f"Configuring Django app with the following options:")
    print(f"App Name: {app_name}")
    print(f"Use DRF: {use_drf}")
    print(f"Database: {database}\n\n")

    # Create a new Django project
    os.system(f"django-admin startproject {app_name}")

    # Modify settings.py based on user choices
    settings_path = os.path.join(app_name, app_name, "settings.py")

    with open(settings_path, "r") as settings_file:
        content = settings_file.read()

    if use_drf == "Yes (Recommended)":
        create_django_app(app_name)
        return True


    if database == "Sqlite3":
        return True

    elif database == "Postgres":
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': app_name,
                'USER': app_name,
                'PASSWORD': '123cls4',
                'HOST': 'localhost',
                'PORT': '5432',
            }
        }

    elif database == "MySQL":
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': app_name,
                'USER': app_name,
                'PASSWORD': '1234',
                'HOST': 'localhost',
                'PORT': '3306',
            }
        }

    # Use regular expressions to find and replace the DATABASES block
    pattern = re.compile(r'DATABASES\s*=\s*{[^}]+}\s*}', re.DOTALL)
    content = pattern.sub(f"DATABASES = {DATABASES}", content)

    with open(settings_path, "w") as settings_file:
        settings_file.write(content)



def main():
    Art=text2art("CEDRIC")
    print(Art)
    print(
        "🚀 Welcome to CEDRIC Django Template – because even coding wizards need a magic wand! 🧙\n\n"
        "#############################################################################################################################################\n"
        "# Your Django development journey is about to get as smooth as a salsa dancer on roller skates!                                             \n"
        "# Developed by: Abhishek Choudhury (Got so annoyed, decided to create his own helper library, but cool enough to share it with you! 😎)    \n"
        "# Get ready to soar through your coding adventure with a sprinkle of Python magic!\n#\n"
        "# Remember, bugs are just undocumented features waiting to be discovered! 🐞✨\n"
        "#############################################################################################################################################\n\n"
    )

    questions = [
        inquirer.Text(
            "app_name", message="What shall we call your magical application?"
        ),
        #inquirer.List(
        #    "use_docker",
        #    message="Are you ready to embark on a 🚢 Docker adventure?",
        #    choices=["Yes", "No"],
        #    default="Yes",
        #),
        inquirer.List(
            "use_drf",
            message="Shall we add Django DRF with JWT based APIs for authentication?\n (Note: This action will create a new app authentication in the django app, with a custom user model along with required fields like email, name, password)",
            choices=["Yes (Recommended)", "No"],
            default="Yes (Recommended)",
        ),
        #inquirer.List(
        #    "use_jwt",
        #    message="Shall we add JWT based authentication?",
        #    choices=["Yes (Recommended)", "No"],
        #    default="Yes (Recommended)",
        #),
        inquirer.List(
            "database",
            message="Select a Database for your coding kingdom",
            choices=["Postgres", "MySQL", "Sqlite3"],
            default="Sqlite3",
        ),
    ]

    answers = inquirer.prompt(questions)

    # Validate app name
    app_name = answers["app_name"]
    if not app_name or not app_name.isidentifier() or app_name[0].isdigit():
        print(
            "Error: Please provide a valid app name. It should be a valid Python identifier."
        )
        return

    # Confirm overwrite if the app directory already exists
    app_directory = os.path.join(os.getcwd(), app_name)
    if os.path.exists(app_directory):
        response = inquirer.confirm(
            f"The directory {app_name} already exists. Do you want to overwrite it?",
            default=True,
        )
        if not response:
            print("Aborting setup.")
            return
        else:
            rmtree(app_directory)

    configure_django_app(
        app_name,
        answers["use_drf"],
        answers["database"],
    )

    print("\n\nTa-da! Your Django app has been summoned successfully. 🚀✨ Now go forth and conjure some code magic!")


if __name__ == "__main__":
    main()
