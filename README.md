# CSRF-and-XSS
Vulnerable websites that simulate the attacks using Flask.

## Initial Setup
```console
pip install -r requirements.txt
```
# CSRF - Client Side Request Forgery

## Premise
The CSRF folder simualtes a basic attack on a price changing API.

# Setup
The easiest way to setup the simulation is to download the LiveServer extension in Visual Code, then start evil.html on it.   
Then start app.py using:
```console
Windows:
py app.py

Linux:
python3 app.py
```
Then open both evil.html and index.html in the browser and you are ready to demonstrate the attack.

## Explanation
The Pizza Site has an API that only supposed admins can access.   
Non admin user will get a 403 Forbidden error.   
   
When the user first enters the site, he wil be prompted to enter his name. In this demonstration, it will also be his session cookie.   
A user that will enter admin as his name will become an admin in the site (again, not secured, but also not the point of the demonstration).   
   
Now to evil.html, if the form there will be posted from the browser with the admin cookies while the anti-csrf token is not activated (for this just delete the checks from the API function in app.py and delete the field in index.html), the request will be authorized and the hacker successfully acted as an admin without actually being one.   
   
The Anti-CSRF Token solves this by adding an hidden field to the form in index.html with a randomly generated string. The hacker cannot guess the string and therefore cannot pass the request. Not including the field will Result in 400 Bad Request Error.

# XSS - Cross-Site Scripting

## Premise 
The XSS folder simulated a Reflected XSS attack with a poorly configured API.

# Setup
For this demonstration there is no need for the LiveServer, only run app.py.   
```console
Windows:
py app.py

Linux:
python3 app.py
```
Then open index.html.

## Explanation
The Snake Adoption site has an API for adoption snakes.   
The point of this site is to show how using unsanitized user input with, in this case, jinja templates can be extremely dangerous.   
The user can input any snake id he wants to adopt and will get a confirmation message.
If the user will enter the following payload he will fail to get XSS:
```html
<script>alert("Hacked")</script>
```
This is because there is one check that is happening in the backend, and it is if there is a valid id in the input. This check is very bad because of this:
```html
p1<script>alert("Hacked")</script>
```
This simply bypasses the check because it matches the validation. The user input is directly sent to the HTML file with no sanitization or validation, so the JavaScipt code just gets executed.

Note that this is just a very simple explanation to why it's extremely important to put proper validation on user input. In this case the attack can be defended by just changing the check from:
```py
if 'p1' in content or 'p2' in content or 'p3' in content:
    return content + ' Adopted!'
```
To:
```py
if content in ['p1', 'p2', 'p3']:
    return content + ' Adopted!'
```


