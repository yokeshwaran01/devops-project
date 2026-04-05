stage('Deploy') {
    steps {
        sshagent(['deploy-server-key']) {
            sh '''
            ssh -o StrictHostKeyChecking=no ubuntu@172.31.72.208 << EOF

            echo "Pull latest image"
            docker pull yokeshwaran01/devops-project:latest

            echo "Stop old container"
            docker stop flask-app || true
            docker rm flask-app || true

            echo "Run new container"
            docker run -d -p 5000:5000 --name flask-app yokeshwaran01/devops-project:latest

            echo "Deployment done"
            EOF
            '''
        }
    }
}
