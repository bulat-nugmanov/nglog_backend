A friendly reminder
---------------------------------------------------------

* START DB SERVER:
	* mysqladmin -u root -p; status	    # check server
	* if server is not running:
	* sudo mysql -u root -p		        # start server

* ACTIVATE VIRTUALENV
	* cd PROJECT_DIR                    # ie navigate to project directory where manage.py is
	* source devenv/bin/activate

* START APP SERVER
	* python manage.py check
	* python manage.py makemigrations
	* python manage.py migrate
	* python manage.py runserver
