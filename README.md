# IJustWorkHere

## League Of Legends Stat Tracker 

Commercial:https://www.youtube.com/watch?v=6zvKBPHoauM

Website/Runtime link: http://leagueofstats.cf:8080

The website to track your progress in League of Legends! Find your game stats for your last few games! 

Summary: a Stat tracking website (tracks the statistics that are unique to the gameplay) which involves the use of databases, json, flask, html, and css. Users must interact with the website's sign up and login systems to access the main stat tracking function. When in the main page, users are able to interact with the search bar to find any player's performace in the game, allowing you to be able to view your own, and other people's stats! 

Scrum board: https://github.com/largecodeman1/IJustWorkHere/projects/1

![image](https://user-images.githubusercontent.com/72989414/110561461-91227300-80fc-11eb-9c9f-48f9cfcfec26.png)

## How to use
* Enter the website through http://leagueofstats.cf:8080
* Sign up and Login in!
* You're in! now find your username from League of Legends. This should be the name that is displayed when playing LoL (league of legends). If you don't have a League account and want to test, use the username "psy6"
* Enter the username into the search bar and search!
* Want to find your stats, and how you can improve? enter the analysis page!
* Compare your stats to pros, and watch the Proguides videos on how to improve.         
* You're done! observe your stats from the last few games played, improve, and repeat!

![image](https://user-images.githubusercontent.com/70777993/110672519-8f03f700-8184-11eb-981b-540f86affaff.png)

# Major Technicals 

Here are the technicals we made use of throughout tri 2 of CSP. (Tech talks and individual research)

### Signup/Login page

![image](https://user-images.githubusercontent.com/72989414/110564324-77375f00-8101-11eb-8dca-67273f3b2c41.png)

The login and signup code (excluding html) are all located in the views.py file. **Wesley** worked on this by using WTforms and SQLAlchemy. By creating a simple database, in which user inputed data is able to be stored and withdrawn from the database, and the helpful use of wtform logic, the login and signup pages were formed. Along with the login, a logout and login required authethication was integrated to make the site navigatable anywhere. Databases were a huge part of this trimester's goals which were accomplished through this technical.  

### Riot API/data
![image](https://user-images.githubusercontent.com/70777993/110669705-70503100-8181-11eb-97b4-bb0f702001f6.png)

![image](https://user-images.githubusercontent.com/70777993/110670982-db4e3780-8182-11eb-94de-de33408c00be.png)


The rest API code (excluding html) are located in riot_api.py, views.py, and create_riot_db.py. **Zach** worked on this using json and SQLAlchemy. The rest API used to extract information was the RIOT league of legends api. The database created is able to store the json values extracted from the RIOT game api and sort them until the right type of information can be displayed. The search bar was created by **Aiden** and **Zach** to search through the database and display the right stats on the website.

### Frontend/HTML/CSS

![image](https://user-images.githubusercontent.com/72989414/110570793-5b38bb00-810b-11eb-918f-43c3a7a27bbe.png)

![image](https://user-images.githubusercontent.com/72989414/110570850-7277a880-810b-11eb-8cd2-756d7f5d4737.png)

All the HTML and CSS can be found in the static and templates folder. **Brandon** and **Aiden** were the ones who worked on this part of the project. From the embeding of videos and images, to the navigation bar, Brandon and Aiden worked together to get the backend and frontend linked together. They helped design the buttons and pages to display certain stats and pieces of information to help guide users into the website.

## Dependencies
pip install each of the following to run the program in intellij
- In the IntelliJ terminal type in "pip3 install "___"

* Flask
* flask_bootstrap
* flask_wtf
* wtforms
* wtforms.validators
* flask_sqlalchemy
* werkzeug.security
* flask_login
* json

__________________________________________________________________________________________________________________________________________
## Scrum Board Cards/Tickets and Deployment Focus
# https://github.com/largecodeman1/IJustWorkHere/projects/1
* Successfully integrated new login page into repository, working on adding a linking button to get from the login page to the website - Aiden

* Imported and deployed login system into main website - Wesley
(NOTE) We have yet to link a button onto the login and signup system, so type in /login or /signup into the url. The process is being worked on.

* Create a get to recieve and pull - Zach
- - match Ids
- - Encrypted summoner names
- - Match Lists

Print to web page 

* Research how to implement analysis for the program - Brandon

Check scrum board for more details
## Runtime Link:http://leagueofstats.cf:8080/ or Runtime Link:http://24.255.211.218:8080/

## Grading

Past

* Aiden - 18/20
* Zach - 20/20
* Wesley - 20/20
* Brandon - 19/20

2/5/21

* Aiden - 25
* Zach - 25
* Wesley - 25
* Brandon - 25

2/18/21


1. Link to scrumboard and tickets at the top and here: https://github.com/largecodeman1/IJustWorkHere/projects/1 
2. https://docs.google.com/document/d/13E1IAy700dugCS4vYhOEkxepcT8rbkOxReJ65N6snI4/edit to show our collegeboard requirements, we are currently working on crossover report issues. We are currently meeting all of the collegeboard requirements at this point in time, we are working on polishing and making our code more efficent by removing dead code and using more efficent code in our program
3. Mini code Review focus on tickets and project. See below


Define database schema

## Crossover Report:  2/12/21

Link to report: https://docs.google.com/document/d/1SqaIoVOVPu1tSyZY4-8suobg2gzMQInMlo7zBMJdOOg/edit?usp=sharing

Total Score: 24/25
- Were working on making the login and registration more aesthetically pleasing by adding backgrounds, images, weve extended the background of the base to the other pages, makingthem uniform and more aesthetically pleasing
- weve made it more obvious that the search bar is there for searching up player names, and we moved it to the main page
- The images not working during the runtime was the fault of the API were taking data from, not our program, although we will still look into this issue to see if there is any way to pull images from the API in a faster or more efficent way so that we can display the updated images

## Tickets 

Past 12/14/20 - 1/11/21

* Aiden - https://github.com/largecodeman1/IJustWorkHere/projects/1#card-52772395
          https://github.com/largecodeman1/IJustWorkHere/projects/1#card-51612766
        
* Zach - Error checking for RIOT API - https://github.com/largecodeman1/IJustWorkHere/projects/1#card-52930789
         https://github.com/largecodeman1/IJustWorkHere/projects/1#card-52709625
         https://github.com/largecodeman1/IJustWorkHere/projects/1#card-52930817

* Wesley - https://github.com/largecodeman1/IJustWorkHere/projects/1#card-52772343
           https://github.com/largecodeman1/IJustWorkHere/projects/1#card-51612798
         
* Brandon - https://github.com/largecodeman1/IJustWorkHere/projects/1#card-52607939
            https://github.com/largecodeman1/IJustWorkHere/projects/1#card-51612834
          
Present 1/25 - Now

* Aiden - https://github.com/largecodeman1/IJustWorkHere/projects/1#card-53782757 

* Zach - https://github.com/largecodeman1/IJustWorkHere/projects/1#card-53870553
         https://github.com/largecodeman1/IJustWorkHere/projects/1#card-53870542
       
* Wesley - https://github.com/largecodeman1/IJustWorkHere/projects/1#card-53782311
          https://github.com/largecodeman1/IJustWorkHere/projects/1#card-54357741

* Brandon - https://github.com/largecodeman1/IJustWorkHere/projects/1#card-53869792



## Instructions
* To use our program, first fill out the signup sheet where you will then be taken to the main page, and will be able to access the analysis program, which will be implemented in the future

* For Test Riot Data, utilize the Url and paste in either psy6 or PsychicMaster6 after the initial / to get an example call
ie. http://24.255.211.218:8080/riot_api_query/psy6
* Note: Riot API key needs to be updated every 24 hours
