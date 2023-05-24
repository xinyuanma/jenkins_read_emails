pipeline {
    agent any
    stages {
        stage('version'){
            steps {
                sh 'python3 --version'
            }
        }
        stage('install dependencies') {
            steps {
                sh 'python3 -m pip3 install -r requirements.txt'
            }
        }   
        stage ('read'){
            steps {
                sh 'python3 get_cvname.py'
            }
        }
    }
}
