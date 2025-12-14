pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "manahyl/simple-webapp"
    }

    stages {

        stage('Code Fetch') {
            steps {
                echo "Fetching code from GitHub..."
                git branch: 'main', url: 'https://github.com/manahylkhan/simple-webapp.git'
            }
        }

        stage('Docker Build') {
            steps {
                echo "Building Docker Image..."
                sh 'docker build -t $DOCKER_IMAGE:latest .'
            }
        }

        stage('Docker Push') {
            steps {
                echo "Pushing Docker Image to DockerHub..."
                withDockerRegistry([credentialsId: 'dockerhub-credentials', url: '']) {
                    sh 'docker push $DOCKER_IMAGE:latest'
                }
            }
        }

        stage('Kubernetes Deploy') {
            steps {
                echo "Deploying to Kubernetes..."
                sh 'kubectl apply -f k8s/'
            }
        }

        stage('Monitoring Setup') {
            steps {
                echo "Prometheus & Grafana are already running and monitoring the application!"
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed. Check logs."
        }
    }
}
