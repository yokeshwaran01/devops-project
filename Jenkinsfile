pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "yokeshwaran01/devops-project"
    }

    stages {
        stage('Build Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push $DOCKER_IMAGE'
            }
        }
    }
}
