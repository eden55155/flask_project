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
        sh "cp -r /home/ubuntu/workspace/test successlog.csv"
      }
    }
        
        stage('Upload to S3') {
      steps {
        withCredentials([[
          $class: 'AmazonWebServicesCredentialsBinding',
          accessKeyVariable: 'AKIAXHSZ337B6LYYH4NN',
          secretKeyVariable: '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'
        ]]) {
          sh 'aws s3 cp successlog.csv s3://sqlabs-devops-edeni/Project/successlog.csv --acl public-read'
        }
      }
    }
}
}
