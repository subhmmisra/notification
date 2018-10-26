

# Push Notification Web App

Push Notification Web App which lets admin to send push notifications to various platform (Type = "web"/"android"/"ios") in groups or to a specific user.

## Prerequisite

*   Python 3.3+ installed
*   Django 2.0+ installed
*   fcm_Django installed

## How to Use

1. Get inside project folder by using command "cd finale"
2. To make server up and going use command "python manage.py runserver"
3. Go to "http://127.0.0.1:8000/"
4. Now login as a admin by using following credentials

   USERNAME = admin PASSWORD = admin

5. Now for the registration of a new device in order to get notification from the server use following end point

   END-POINT = "http://127.0.0.1:8000/notification/create/" (POST)

   send "POST /notification/create HTTP/1.1" request to the server with following data in JSON format.  
   { registration_id = [REGISTRATION_ID], user_id = [USER_ID], type = [TYPE] }

6. This END-POINT registers the user and return the success or error message
7. Now for sending the notification use following END_POINT

   END-POINT = "http://127.0.0.1:8000/notification/send/" (POST)

   send "POST /notification/send HTTP/1.1" request to the server with following data in the JSON format.  
   { title = [TITLE] description = [DESCRIPTION] link = [IMAGE_LINK] user = [USER_ID] all = [TRUE/FALSE] }

8. Now This will send the notification to the selected user and will return success and failure message in JSON format.

## TESTING

* END_POINT = "http://127.0.0.1:8000/notification/send" (GET)

  This END_POINT will send the notification to the very first Entry in the REGISTERD_USER_TABLE which is fcm_django_fcmdevice table in the database.

