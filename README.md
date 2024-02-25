# Login-and-Admin-Pages-using-Flask

## This project consists of a Login and Administration Page. HTML5 and CSS were used in the frontend, and Python in the backend. Additionally, the Flask framework was essential to create the logic behind the screens.

![login](https://github.com/eduardo-de-bastiani/Login-and-Admin-Pages-using-Flask/assets/94228732/1cd45b5a-1ea5-4259-b896-7b3edf4d43b1)


### The Login page requires a Name and Password. After filling in the gaps, IF the user is registered, they will be redirected to a merely illustrative page.

![logged](https://github.com/eduardo-de-bastiani/Login-and-Admin-Pages-using-Flask/assets/94228732/d70d8e4c-6752-4152-855f-523361c2f954)

### If the user is not registered and tries to login, a flash message will appear at the top of the screen saying "Invalid User."


![usuario invalido](https://github.com/eduardo-de-bastiani/Login-and-Admin-Pages-using-Flask/assets/94228732/31dc2de1-57f3-454d-83df-0aae6b49c99d)

### If the name and password correspond to "adm" and "000" respectively, it will redirect to the administrator page, where new users can be added. Not only that, all the registered users are displayed, along with their passwords.


![adm page](https://github.com/eduardo-de-bastiani/Login-and-Admin-Pages-using-Flask/assets/94228732/a342c7f9-e5b6-4382-ae12-6d5f45095ea7)

### Thinking about security, a lock was installed. When an intruder tries to change the website's URL, adding "/admin" to access the administrator page, a flash message appears at the top of the screen saying "Unauthorized Access."

![access denied](https://github.com/eduardo-de-bastiani/Login-and-Admin-Pages-using-Flask/assets/94228732/5b451a81-b652-490e-b597-eb204849ab37)

### It is worth highlighting that the website can only be accessed if the Flask framework is installed on the user's computer. To execute the Python source code, the framework needs to have access to "port 5000." Personally, I executed the code in Gitbash with the command "python main.py."
