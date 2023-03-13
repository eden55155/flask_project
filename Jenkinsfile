    agent { label "slave1" }
    
    stages {
        stage('Clone repository') {
            steps {
                git 'https://github.com/eden55155/flask_project.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    def build = currentBuild.rawBuild
                    def cause = build.getCause(hudson.model.Cause.UserIdCause.class)
                    def name = cause.getUserName()
                    def now = new Date()
                    sh "docker build -t projectflask ."
                    sh "docker run --name testimage -p 80:80 -d -it projectflask"
                    sh "sleep 5"
                    sh "${name} >> successlog.csv"
                    sh "Date: ${now} >> successlog.csv"
                    sh "Result: ${currentBuild.result} >> successlog.csv"
                    
//                     sh "/var/jenkins_home/jobs/Project/builds/${buildNumber}/log >> log"
//                     sh "python3 log.py >> successlog.csv"
                }
            }
        }
        
        stage('Upload to AWS') {
            steps {
                withAWS(region:'us-east-1', credentials:'awscred') {
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
