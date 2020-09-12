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
                sh 'docker build'
            }
        }
    }
}
