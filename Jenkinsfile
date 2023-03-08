pipeline {
    agent {label "slave1" }
    
    stages {
        stage('Clone repository') {
            steps {
                git 'https://github.com/eden55155/flask_project.git'
            }
        }
        
    stage('Build Docker Image') {
      steps {
        sh "docker build -t projectflask ."
        sh "docker run -p 5000:5000 -d -it projectflask"
        sh "sleep 5"
        sh "curl -v http://52.3.252.159:5000 >> successlog.csv"
      }
    }
        stage('S3download'){
            steps{
                withAWS(credentials:'awscredentials', region:'us-east-1'){
                    s3Download(file: 'successlog.csv', bucket:'sqlabs-devops-edeni',path: "s3://sqlabs-devops-edeni/", force:true)
                }
            }
        }
    }
}
