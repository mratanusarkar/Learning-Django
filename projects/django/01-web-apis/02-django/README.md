# Setup
1. Install django and pillow 
   > (or use requirements.txt in parent directory by using `pip install -r requirements.txt`)
2. Create a new django project using `django-admin startproject <project-name>`
3. Go ahead and run the routine operations as below:
4. Navigate inside the project folder where you will find `manage.py` and main app with same name as the project name.
4. Run migrations: `python manage.py migrate`
5. Create superuser: `python manage.py createsuperuser`
   > give a username, email and password. (use strong password for prod, and if dev, you can choose to bypass password validation)
6. Setup VSCode to run `manage.py runserver` command. (you can choose to launch your app in other ways too)
   - If you choose to go with the above, then 
   - go to debug tab
   - select setting to config `launch.json` for .vscode
   - select python as environment and existing config setup template as django
   - set value for program in configurations pointing to `manage.py` as:
    `"program": "${workspaceFolder}/projects/django/01-web-apis/02-django/techmart/manage.py"`
   - go to debug menu, select "Python: Django" and press run (green triangle).
7. Move inside `<project-name>` directory
8. Go ahead a create a new app using: `python manage.py startapp <app-name>`
9. Register/Install the new app inside the `<project-name>/<project-name>/settings.py` inside `INSTALLED_APPS` list
10. Start creating the models, views, templates and other business logics! Happy coding!

# Run
1. `cd projects/django/01-web-apis/02-django/techmart/`
2. ensure in launch.json, configurations, the value for program is:
   `"program": "${workspaceFolder}/projects/django/01-web-apis/02-django/techmart/manage.py"`
3. In debug tab, select "Python: Django" and press run.