pipeline {
    agent any

    environment {
        IMAGE = "yokeshwaran01/devops-project"
        TAG = "latest"
        SERVER = "172.31.72.208"
    }

    stages {

        stage('Build Image') {
            steps {
                sh 'docker build -t $IMAGE:$TAG .'
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push $IMAGE:$TAG'
            }
        }

        stage('Deploy') {
            steps {
                sshagent(['deploy-server-key']) {
                    sh '''
                    ssh -o StrictHostKeyChecking=no ubuntu@$SERVER << EOF

                    docker pull $IMAGE:$TAG

                    docker stop flask-app || true
                    docker rm flask-app || true

                    docker run -d -p 5000:5000 --name flask-app $IMAGE:$TAG

                    EOF
                    '''
                }
            }
        }

    }
}
