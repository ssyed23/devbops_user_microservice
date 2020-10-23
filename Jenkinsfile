pipeline {
     agent { docker { image 'python:3.7.2' } }
     environment {
        AWS_DEFAULT_REGION = 'us-east-1'
     }
     stages {
         stage('Build') {
             steps {
                    withEnv(["HOME=${env.WORKSPACE}"]) {
                         sh 'pip install flask --user'
                         sh 'pip install boto3 --user'
                         sh 'pip install requests --user'
                         sh 'pip install bcrypt --user'

                     }
                 }
         }
         stage('Test') {
             steps {
                 withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'python3 Test.py'
                 }
             }
         
         stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    
    }
     }
}
