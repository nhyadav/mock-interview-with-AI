# AI Recruter
Today many applicants apply for a specific job. But recruiter will hire only a small number of people. Before hiring the big problem is how to identify the applicant resumes, manually it will consume more time and money that why recruiters used an applicant tracking system that will perform screening on all resumes in a short time. But it totally depends upon the recruiter, which type of resume content will prefer more for opening jobs. Every recruiter has its own keywords for hiring applicants, it is not simple for applicants they can create a resume that got shortlisted in any specific jobs. It's a complex job for the applicant, and every recruiter has its own applicant tracking system.  That's why this web project will provide a platform where the applicant can test themselves resume for shortlisted and participate in a mock interview with an AI bot. The project will return the scoreboard of applicants with proper reports.


> ## Application of AI Recruter:
- Applicants can scan their resumes. 
- Applicants can generate a report for creating an attractive resume for jobs. 
- Applicants can attend a mock interview with an AI bot before attending the interview with a recruiter.


> ## Technology
- Python
- django 3.2
- PostgrsQL
- HTML
- CSS
- Bootsrap
- Machine Learning
- Natural Language Processing
- Deep Learning
- Angular (optional)

> ## Cloud
- GCP

> ## Ops Pipeline
- Mlflow and DVC

> ## Deployment
- Heroku

> ## Installation
- get ready with Anaconda3.
- create a conda environment.
    ```git
    conda create -n env_name python=version -y
    ```
- clone the repository.
    ```git
    git clone git@github.com:nhyadav/mock-interview-with-AI.git
    ```
- install all dependencies.
    ```git
    pip install -r requirements.txt
    ```
- start the application.
    ```bash
    cd AIrecruter
    python manage.py runserver
    ```
- to stop the server press ctrl+c.

> ## Contribution
To Contribute in this project follow below command.
- fork the current repository.
- after fork this repository, it will be created one more repository in your github accout with `username/mock-interview-with-AI`. and click on `username/mock-interview-with-AI` repository.
- go to code button, and copy the repository url.
- create a isolated `folder` for this project in your `local computer`.
- open particular folder with `vs code` or any other editor.
- open the terminal at created new folder location, and run below command.
    ```git
    git clone git@github.com:username/mock-interview-with-AI.git
    #copy above link from your github account repository.
    ```
- after cloning this repository, lets check out that repository is up to date or not.
    ```git
    git remote -v
    # there will be two name 1 is upstream and 2 is origin. if upstream is not visible then create upstream with below command.
    
    git remote add upstream git@github.com:nhyadav/mock-interview-with-AI.git
    #copy above link from source repository page. that is already mention above.

    git pull upstream 
    ```
- create a new branch for editing code.
    ```git
    git checkout -b branch_name
    ```
    above command ceate a new branch and set it for running current branch state. after this any editing in code will be save in new created branch. to check running branch run the below command output will be list of the branch, running branch represent with `*branch_name`.
    ```git
    git branch
    ```
- after editing the code part, you need to save your changes and pull that changes to master repository wwith below command.
    ```git
    git add . 
    # we can use "git add -A" or "git add --a"
    git commit -m "message what you have maked changes in repository"
    git push -u origin branch_name
    #we can use "git push origin branch_name" also without -u flag.
    ```


> ## Contibutor
- Narayan Hari Yadav

### *- Note -*: if you like this repository helpful, please star it.


# * Thank You! *

