# Survey-Management
CS-251 Course Project
To run our project, do the following:
1. python manage.py migrate
2. python manage.py createsuperuser
3. In the survey management directory run "python3 manage.py runserver"
4. open browser and visit this address http://127.0.0.1:8000

## Making a survey

1. Using the admin interface you can create surveys, add questions, give questions
categories, and mark them as required or not. You can define choices for answers
using comma separated words.
2. The front-end survey view then automatically populates based on the questions
that have been defined and published in the admin interface. We use bootstrap3
to render them.
3. Submitted responses can be viewed via the admin backend, in an exported csv
the terminal command "python3 manage.py exportresult --survey-all --csv" can be used to download csv format recorded responses of all surveys.
4. to extract a specific csv of responses from database use "python3 manage.py exportresult --survey-id SURVEY_ID --csv"
use "python3 manage.py exportresult -h " this to know more about data exportation

## accounts utilities
to reset your password do the following
1. in your linux machine open a terminal and write "python3 -m smtpd -n-c Debugging Server localhost: 1025"
2. now after clicking reset password on web app you will recieve a mail on this terminal with a link
3. visit this link and set your new password

editing your profile and viewing your profile is also available.
you can also set a new password if you wish to change your existing password
