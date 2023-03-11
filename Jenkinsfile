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
        sh "curl -v http://52.3.252.159:5000 > successlog.csv"
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
     }
}
