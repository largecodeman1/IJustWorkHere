# IJustWorkHere

## League Of Legends Stat Tracker
The website to track your progress in League of Legends! Find your game stats for your last few games! 
![image](https://user-images.githubusercontent.com/72989414/110561461-91227300-80fc-11eb-9c9f-48f9cfcfec26.png)


## How to use
* Enter the website through http://leagueofstats.cf:8080
* Sign up and Login in!
* You're in! now find your username from League of Legends. This should be the name that is displayed when playing LoL (league of legends)
* Enter the username into the search bar and search!
* Want to find your stats, and how you can improve? enter the analysis page!
* Compare your stats to pros, and watch the newest pro guide videos.           
* You're done! observe your stats from the last few games played, improve, and repeat!


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
