pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                echo "Code pulled from GitHub"
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devops-project .'
            }
        }
    }
}
