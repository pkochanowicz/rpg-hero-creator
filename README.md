# rpg_hero_creator
An updated version of my Warhammer Hero Creator made in 2018. It's still a Django project but this time made in a Docker container, hosted on Heroku with static files served on AWS.
Here's link to the django project i started with: https://github.com/ccurvey/heroku-django-docker-example
# Installation:
1 - Download and install Docker
2 - Change .temp_env filename to .env and chang the variables inside it to your project needs. To do so you'll need:
	a - Create a gmail account from which application will send emails.
	b - Create a AWS account to store static and media files. Particullary you'll need IAM and S3 services. 
	    Here's the link explaining how to do it: https://simpleisbetterthancomplex.com/tutorial/2017/08/01/how-to-setup-amazon-s3-in-a-django-project.html (note, that the parts that require code change are already done).
3 - To run the project locally:
	a - Comment following line in the Dockerfile: CMD python3 manage.py runserver 0.0.0.0:$PORT (if it isn't already)
	b - Open the project folder in a console and type: "docker build --tag test --file Dockerfile ." in order to create docker image
	c - Once to process is done type: "docker-compose up" to start docker containers, one with database and the other with web app.
	d - Open http://localhost:8000 address in your browser to enter the site.
	e - To execute django specific commands, like makemigrations or collectstatic write: "docker exec -it <container-name> python manage.py <command>" for example "docker exec -it rpg-hero-creator python manage.py collectstatic"
4 - To upload project to Heroku:
	a - Uncomment following line in the Dockerfile: CMD python3 manage.py runserver 0.0.0.0:$PORT
	b - Create Heroku.com account for your app.
	c - In the deploy section of the settings connect app to your GitHub. You may set the online app to automaticly update and deploy after each commit to your git repository or deploy manually when you want to.
	d - Push the code to the Git repository and wait for the deploy to finish.