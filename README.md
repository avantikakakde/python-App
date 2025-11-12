# 🚀 Automated CI/CD for a Python Flask Application with Jenkins 

This project sets up a **fully automated CI/CD pipeline** for a **Python Flask application** using **Jenkins** and **GitHub Webhooks**.  
Every time new code is pushed to the repository, Jenkins automatically triggers the **build**, **test**, and **deployment** process — ensuring smooth, consistent delivery with zero manual steps.



---

## ⚙️ Project Setup

### 1. Prerequisites

Make sure you have the following installed:

- Python 3.x  
- Flask  
- Git  
- Jenkins (on AWS EC2 or local machine)  
- GitHub repository  
- Webhook access between GitHub and Jenkins  
 
![](./images/Screenshot%202025-11-12%20132710.png)

---

### 2. Flask App Structure

python-app/
│
├── app.py
├── requirements.txt
├── Jenkinsfile
└── README.md


**Example `app.py`:**


```
from  flask  import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <title>🚀 Flask CI/CD Deployment</title>
            <style>
                body {
                    font-family: 'Poppins', sans-serif;
                    background: linear-gradient(135deg, #667eea, #764ba2);
                    color: white;
                    text-align: center;
                    padding-top: 100px;
                }
                h1 {
                    font-size: 2.8em;
                    margin-bottom: 10px;
                }
                p {
                    font-size: 1.3em;
                }
                .btn {
                    display: inline-block;
                    padding: 10px 25px;
                    margin-top: 20px;
                    font-size: 1.1em;
                    background-color: #ff9f43;
                    color: #fff;
                    text-decoration: none;
                    border-radius: 8px;
                    transition: background 0.3s ease;
                }
                .btn:hover {
                    background-color: #ff6b6b;
                }
            </style>
        </head>
        <body>
            <h1>✅ Successfully Deployed Flask App through Jenkins!</h1>
            <p>Automated with <b>CI/CD Pipeline</b> 💻 using <b>Jenkins + Docker</b> 🚀</p>
            <a href="/hi" class="btn">Say Hi 👋</a>
        </body>
    </html>
    '''

@app.route('/hi')
def hi():
    return '''
    <html>
        <head>
            <title>👋 Flask Greetings</title>
            <style>
                body {
                    font-family: 'Poppins', sans-serif;
                    background: linear-gradient(135deg, #43cea2, #185a9d);
                    color: white;
                    text-align: center;
                    padding-top: 120px;
                }
                h1 {
                    font-size: 3em;
                }
                p {
                    font-size: 1.2em;
                }
                a {
                    color: #fff;
                    text-decoration: underline;
                    font-size: 1.1em;
                }
            </style>
        </head>
        <body>
            <h1>👋 Hi There!</h1>
            <p>Welcome to your Flask + Jenkins + Docker environment 🌍</p>
            <p><a href="/">Back to Home</a></p>
        </body>
    </html>


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```


 ### 🧾 Step 2: Create GitHub Repository

Create a new repository on GitHub

Name: python-app

Branch: main


## 🔐 Step 3: Add Credentials in Jenkins

Navigate to:  
**Manage Jenkins → Credentials → System → Global**

Create a **new credential** with the following details:

| **Field**      | **Value**                     |
|----------------|-------------------------------|
| **Scope**      | Global                        |
| **ID**         | python-app-key                |
| **Description**| Python Flask app SSH key       |
| **Username**   | ubuntu                        |

---

## ⚙️ Step 4: Create a Jenkins Pipeline Job

Go to:  
**Jenkins → New Item → Pipeline**

Configure the pipeline as follows:

| **Field**        | **Value**                                                   |
|------------------|-------------------------------------------------------------|
| **Name**         | python-flask-cicd                                           |
| **Trigger**      | ✅ GitHub hook trigger for GITScm polling                   |
| **Definition**   | Pipeline script from SCM                                   |
| **SCM**          | Git                                                        |
| **Repository URL** | `https://github.com/<your-username>/python-flask-cicd.git` |
| **Branch**       | main                                                       |
| **Script Path**  | Jenkinsfile                                                |

![](./images/Screenshot%202025-11-12%20124639.png)

![](./images/Screenshot%202025-11-12%20125031.png)

### 🧠 Step 5: Jenkinsfile
```
pipeline {
    agent any

    environment {
        SSH_CRED = 'node-app-key'
        SERVER_IP = '13.234.76.204'
        REMOTE_USER = 'ubuntu'
        APP_DIR = '/home/ubuntu/pythonapp'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git url: 'https://github.com/avantikakakde/python-App.git', branch: 'main'
            }
        }

        stage('Deploy to Server') {
            steps {
                sshagent(credentials: ["${SSH_CRED}"]) {
                    sh '''
                        ssh -o StrictHostKeyChecking=no ${REMOTE_USER}@${SERVER_IP} "mkdir -p ${APP_DIR}"
                        scp -r Dockerfile README.md app.py requirements.txt test ${REMOTE_USER}@${SERVER_IP}:${APP_DIR}/
                    '''
                }
            }
        }

        stage('Install & Run App') {
            steps {
                sshagent(["${SSH_CRED}"]) {
                    sh """
                        ssh -o StrictHostKeyChecking=no ${REMOTE_USER}@${SERVER_IP} '
                            sudo apt update &&
                            sudo apt install -y python3-venv python3-pip &&
                            cd ${APP_DIR} &&
                            python3 -m venv venv &&
                            source venv/bin/activate &&
                            pip install --upgrade pip &&
                            pip install -r requirements.txt &&
                            nohup python3 app.py --host=0.0.0.0 > app.log 2>&1 &
                            exit 0
                        '
                    """
                }
            }
        }
    }
}
```

### 💾 Step 6: Push Code and Jenkinsfile to GitHub
1. git init

2. git add .
3. git commit -m "Initial commit"
4.  git push -u origin main


Once the code is pushed, the GitHub Webhook automatically triggers Jenkins.
Jenkins will:

Pull the latest code

Install dependencies

Build and deploy the Flask app on the target EC2 instance

### 🌐 Step 7: Access the Application

Open your browser and visit:

http://<TARGET-SERVER-PUBLIC-IP>:5000

![](./images/Screenshot%202025-11-12%20125552.png)

---

## 🏁 Conclusion

Deploying a Python Flask application using Jenkins CI/CD integrated with GitHub Webhooks enables a fully automated, efficient, and reliable deployment pipeline.

Every push to GitHub triggers the entire process — build → test → deploy — ensuring faster delivery, reduced manual effort, and better collaboration.

This setup enhances code quality, automation, and DevOps readiness 🚀

---

## 📘 About

This project demonstrates:

Continuous Integration and Continuous Deployment (CI/CD)

Jenkins + GitHub Webhook Integration

Python Flask Application Deployment on AWS EC2 using Gunicorn

It’s a great foundation for mastering DevOps auto