# Health Registry

#### Author: [Sunguti Albright](https://github.com/sunguti-albright)


* Link to live site: [HEALTH REGISTRY](https://albrighthealthregistry.herokuapp.com/)



## Description
An application where users can sign in, post their reports and view the registry
  

| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| Login	if already have an account |if you dont have , click on the sign up link and fill the form  | If login is successful, user is navigated to home page | Signs In/ Signs Up |
| Edit profile | On the account link, click on the  update profile | Redirected to the home page |
| Click on profile | Redirects to the profile page | User adds bio and profile picture |
|Add a new report|Click on the New Profile icon to be redirected to the new report form|the report will be rendered to the home page
| Click on log Out in the accounts| Redirects to the login form | Logs out user  |

## Setup and installations
* Fork the data onto your own personal repository.
* Clone Project to your machine
* Create a virtual environment in the terminal: `python3 -m venv virtual`
* Activate a virtual environment on terminal: `source virtual/bin/activate`
* Install all the requirements found in requirements file.
* On your terminal run `python3.10 manage.py runserver`
* Access the live site using the local host provided



## Getting started

### Prerequisites
* Any python version from python3.10.4(runtime.txt version recommended)
* virtual environment
* pip


#### Clone the Repo and rename it to suit your needs.
```bash
git clone https://github.com/sunguti-albright/Instagram.git
```
#### Initialize git and add the remote repository
```bash
git init
```
```bash
git remote add origin <your-repository-url>
```

#### Create and activate the virtual environment
```bash
python3.10 -m virtualenv virtual
```

```bash
source virtual/bin/activate
```

#### Setting up environment variables
Create a `.env` file and paste paste the following filling where appropriate:
```
SECRET_KEY='<your-secret-key>'
DEBUG=True
DB_NAME='instagram'
DB_USER='<your database name>'
DB_PASSWORD='<password to your database>'
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
DISABLE_COLLECTSTATIC=1
```

#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Make and run migrations
```bash
python3 manage.py check
python manage.py makemigrations news
python3 manage.py sqlmigrate news 0001
python3 manage.py migrate
```

#### Run the app
```bash
python3 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)



## Testing the Application
`python manage.py test instaapp`
        
## Built With

* [Python3.10](https://docs.python.org/3/)
* Django 3.1.2
* Postgresql 
* Boostrap
* HTML
* CSS

## Known Issues
* Project rating functionality not properly working
* 

## Support and contact details
 Incase you come across errors, have questions, ideas ,concerns, or want to contribute to the application, feel free to reach me at :sungutialbright@gmail.com

### License

Copyright <2022> <Sunguti Albright>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.