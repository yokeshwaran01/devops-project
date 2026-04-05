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
        sshagent(['ssh-key']) {
            sh '''
            ssh -o StrictHostKeyChecking=no ubuntu@<DEPLOY_SERVER_IP> << EOF
            docker pull yokeshwaran01/devops-project:latest
            docker stop app || true
            docker rm app || true
            docker run -d -p 5000:5000 --name app yokeshwaran01/devops-project:latest
            EOF
            '''
        		}
    		}
	}

    }
}
