A friendly reminder
---------------------------------------------------------

* START DB SERVER:
	* mysqladmin -u root -p; status	    # check server
	* if server is not running:
	* sudo mysql -u root -p		        # start server

* ACTIVATE VIRTUALENV
  Command categories which should be run from the project virtualenv are marked with -V
	* cd PROJECT_DIR                    # ie navigate to project directory where manage.py is
	* source devenv/bin/activate

* START APP SERVER -V
	* python manage.py check
	* python manage.py makemigrations
	* python manage.py migrate
	* python manage.py runserver

# PREPARE FOR ADMIN -V
    * if not able to access to admin page or authentication system has changed:
    # python manage.py check

