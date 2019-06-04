# rpg_hero_creator
An updated version of my Warhammer Hero Creator made in 2018. It's still a Django project but this time made in a Docker container, hosted on Heroku with static files served on AWS.
Here's a link to the Django project used as a Docker template: https://github.com/ccurvey/heroku-django-docker-example

# Installation:
1 - Download and install Docker
2 - Copy temp.env and rename the copy to to .env and change the variables inside it to your project needs. To do so you'll need:
    a - Create a Gmail account from which application will send user registration emails.
    b - Create a AWS account to store static and media files. Particularly you'll need IAM and S3 services. 
        Here's the link explaining how to do it: https://simpleisbetterthancomplex.com/tutorial/2017/08/01/how-to-setup-amazon-s3-in-a-django-project.html (note, that the parts that require code change are already done).
3 - To run the project locally:
    a - Open the project folder in a console and type: "docker build --tag test --file Dockerfile ." in order to create docker image
    b - Once to process is done type: "docker-compose up" to start docker containers, one with database and the other with web app.
    c - Open http://localhost:8000 address in your browser to enter the site.
    d - To execute Django-specific commands, like makemigrations or collectstatic write: "docker exec -it <container-name> python manage.py <command>" for example "docker exec -it rpg-hero-creator python manage.py collectstatic"
4 - To upload project to AWS:
    a - Enter EC2 service in AWS and launch an instance. Choose Amazon Linux AMI 2018.03.0 (HVM) machine image (free tier, as for june 2019).
	b - While launching you'll need to create or use an existing key pair. Save this file as it will be required to access the virtual machine with SSH.
    c - Download and launch Putty ( https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html ).
	d - Follow this tutorial to connect to your EC2 instance: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html .
	e - Update pip in your virtual machine (pip install --upgrade pip),
	  -	git (sudo yum install git),
	  - docker ( sudo yum -y install docker , sudo service docker start)
	  - docker-compose (pip install docker-compose --user)
	f - Clone the repository to your AWS machine.
	g - Copy previously made .env file to the project folder.
	
	
- installation of git, docker and running pip commands in virtual machine, apt-get: command not found, pip sometimes works with sudo, sometimes doesnt - use "sudo yum install"

# Installation(AWS):