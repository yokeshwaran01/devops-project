pipeline {
    agent any

    environment {
        IMAGE = "yokeshwaran01/devops-project"
        TAG = "latest"
        SERVER = "172.31.71.47"  // app server IP
    }

    stages {

        stage('Build Image') {
            steps {
                sh "docker build -t ${IMAGE}:${TAG} ."
            }
        }

        stage('Push Image') {
            steps {
                sh "docker push ${IMAGE}:${TAG}"
            }
        }

        stage('Deploy') {
            steps {
                sshagent(['ssh-key']) {
                    sh """
                    ssh -o StrictHostKeyChecking=no ubuntu@172.31.72.208 '
                        echo "Pulling latest image..."
                        docker pull ${IMAGE}:${TAG}
                        
                        echo "Stopping existing container (if any)..."
                        docker stop app || true
                        docker rm app || true
                        
                        echo "Running new container..."
                        docker run -d -p 5000:5000 --name app ${IMAGE}:${TAG}
                        
                        echo "Deployment complete!"
                    '
                    """
                }
            }
        }
    }

    post {
        failure {
            echo "Pipeline failed. Check logs for errors."
        }
        success {
            echo "Pipeline succeeded! Application deployed."
        }
    }
}
