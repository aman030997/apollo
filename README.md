# Apollo Back-End Engineering Challenge

This challenge is designed to evaluate three things:
 - How well you know Python
 - How effectively you can work with the Django framework
 - How well you understand different data serialization formats, which is important for working with the diverse APIs Apollo integrates with
 
## Setting Up

Install Python 3.7 or later if it is not already installed. Then, use `pip install -r requirements.txt` to install `django` and other necessary packages. You should then be able to run the project from the `exercise` directory by running `python manage.py runserver`.

To verify that the server is running correctly, visit `http:127.0.0.1:8000` in your browser.

## How to use Xml-Json converter
Once you have opened `http:127.0.0.1:8000` in your browser, click on upload button to upload your `.xml` file.
Click on `convert` and you will be able to see Json converted response on your browser.

###Note
- Make sure file upload is a xml file else you will receive invalid choice response
similar to the one below:

    `"invalid choice" : "file should be xml"`