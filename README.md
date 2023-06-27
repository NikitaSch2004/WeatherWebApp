#### WeatherWebApp
#### Video Demo:  https://youtu.be/G5z0rOsItwo
#### Description:
This is a web app developed by NikitaSch.It was made with flask(a python micro web framework),html,css,sqlite3 and some javascript.
The app is hosted trough heroku and can be visited trough the https://nikitasch.herokuapp.com/ link and also i have the whole project save on my github account.
The purpose of this web app was to test my programming skills that i've learned trough all the cs50x course.This web app contains a layout page which has a nav bar that is reused in the other html pages and also some css that is helpfull to beautify the lookings of the site.Moreother the web app is mobile and tablet friendly because i implemented a responsive design. 
Overall the web app contains 6 html pages:
1.main page
2.login/logout page
3.reset page
4.register page
5.weather page
  
MAIN PAGE:
  Main page consists of a nav bar with a home button, a weather button where you can track weather in your region,a log out button and a reset button(if you are not logged in the reset and log out buttons are not available although there is a log in and a register button), a informational div that helps the user know what the web app is about and a working contact form where everyone can write me for whatever reason they have.Furthermore i put a photo of my home town to show how beautifull it is.
 
LOGIN/LOGOUT PAGE:
  This page is about loging in and out as a user of the site.With the help of python and sqlite3 i have created a complex system that stores the information of the user in a higly secured database and also uses it to know if the user is logged from another device or the same one.It consists of a nav bar a login form and two photos on each side that represent weather and its beauty
 
 RESET PAGE:
    It has the same layout as the log in page but has a different type of system where passwords are validated and if the passwords are usable they arestored in a database where you can see who and from where changed your account password
  
REGISTER PAGE:
  Same as reset and log in pages but has a register system that also registers your information in a database that is secured.

WEATHER PAGE:
  This is the page where i have worked so much on.First of all it uses a weather API that with the help of request module it gets weather data and then displays it on the page.It contains a nav bar like all the others and a section with current weather in the users area.If he is interested in a forecast for the next 2 days he can press the button below and 2 more sections will be displayed with weather information about the next 2 days like temperature, pressure,humidity,precipitations etc.(I was goig to implement a toggle switch for metric and imperial systems but it seems to be much more difficult than i have imagined).
  
CONCLUSION:
  This is project for the final project of the cs50x course.It has been a lot of fun taking this course and i would love to take it again after some time.
  
