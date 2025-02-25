# canvas_bulk_pages
Add pages to your Canvas LMS courses in bulk

![first version screenshot](/git_assets/sgrab_1.png)

# Introduction
This is a pretty small quality-of-life tool that I built to fast-track adding template pages to a large number of Canavs LMS courses. 

Given a group of SIS course ids (which can be typed in or uploaded from a CSV containing the SIS ids in a column named "subject_code"), the tool makes use of the Canvas API to bulk-add pages based on the "Title" and "Content" provided. 

## How to run
1. Install the latest version of Python from [https://www.python.org/downloads](https://www.python.org/downloads/), ensuring that you've added Python to your `PATH` (more on this here: [https://realpython.com/add-python-to-path](https://realpython.com/add-python-to-path/)). 

2. Clone this repository in your machine or download the project files via `Code > Download ZIP`. It is recommended to use a Python virtual environment (like [venv](https://docs.python.org/3/library/venv.html)) so that all modules and dependencies can be housed neatly in one place.

3. Create a `.env` file to store your Canvas API URL and token. An `.env.example` file has been provided in this repo.

4. Open your terminal and `cd` to the repository directory and run the following command:

    ```
    pip install -r requirements.txt
    ```

    This will install all necessary modules. 

5. To run the application, open a terminal, `cd` to the correct directory and run the following command:

    ```
    python3 app.py
    ```

    Depending on your system, you may need to use `python` or `python3` in the above command. 

6. The command in step 5 will launch a Flask development server (usally on http://127.0.0.1:5000), but check the command line as it might be running on a different localhost ip address. 

