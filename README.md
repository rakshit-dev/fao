Data Scrapping API
=======

## Installation Instructions

1. Clone the project.
    ```shell
    $ git clone https://github.com/rakshit-dev/fao.git
    ```
1. `cd` intro the project directory
    ```shell
    $ cd fao
    ```
1. Create a new virtual environment using Python 3.7 and activate it.
    ```shell
    $ python3 -m venv env
    $ source env/bin/activate
    ```2
1. Install dependencies from requirements.txt:
    ```shell
    (env)$ pip install -r requirements.txt
    ```
1. Migrate the database.
    ```shell
    (env)$ python manage.py migrate
    ```

1. Run the local server via:
    ```shell
    (env)$ python manage.py runserver
    ```

### Done!
The local application will be available at <a href="http://localhost:8000" target="_blank">http://localhost:8000</a>