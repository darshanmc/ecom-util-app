pipeline {
    agent any

    stages {
        stage('Notify') {
            steps {
                echo 'Building..'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build --tag=util-app .'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker run -p 8000:8000 util-app'
            }
        }
    }
}
