pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                   withEnv(["HOME=${env.WORKSPACE}"]) {
                        sh "pip install flask"
                        
                    }
                }
        }
        stage('test') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'python3 test.py'
                }
            }
    
        }
    }
}