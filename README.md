# Hospital-Finder
#Go through steps below to use it on your local computer after cloaning the repository

#STEP 1)Running rasa servers at port 5005 and 5055

-go in the rasa folder and open your terminal from there and type the following command without double quotes "rasa run actions"
-again open a new terminal and run this command in it without disturbing the first one "rasa run --enable-api --cors '*' --debug"

#OR

-go in the rasa folder and open your terminal from there and type the following command without double quotes "rasa run actions & rasa run --enable-api --cors '*' --debug"


#STEP 2)running django server at port 8000

-go in the RYD directory and open third terminal and run the following command "python manage.py runserver" 


##Import note
If there is an error saying that there is no model you might have to train the model again by using command "rasa train"
