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
                sh "docker run --name testimage -p 80:80 -d -it projectflask"
                sh "sleep 5"
                sh "curl -v http://54.89.59.86:5000 > successlog.csv"
            }
        }
        
        stage('Upload to AWS') {
            steps {
                withAWS(region:'us-east-1',credentials:'awscred') {
                    sh 'echo "Uploading content with AWS creds"'
                    s3Upload(pathStyleAccessEnabled: true, payloadSigningEnabled: true, file:'successlog.csv', bucket:'sqlabs-devops-eden')
                }
            }
        }
        
        stage('Delete container for new tests') {
            steps {
                sh "docker stop testimage"
                sh "docker rm testimage"
            }
        }
    }
}
