pipeline {
    agent any
    stages {
        stage('version'){
            steps {
                sh 'python3 --version'
            }
        }
        stage ('read'){
            steps {
                sh 'python3 get_cvname.py'
            }
        }
    }
}
