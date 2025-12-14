pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')
        IMAGE_NAME = 'manahyl/simple-webapp:latest'
    }
    stages {
        stage('Code Fetch') {
            steps {
                git branch: 'main', url: 'https://github.com/manahylkhan/simple-webapp.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}")
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-creds') {
                        docker.image("${IMAGE_NAME}").push()
                    }
                }
            }
        }
       stage('Deploy to Kubernetes') {
            steps {
                sh '''
                export KUBECONFIG=/var/lib/jenkins/.kube/config
                kubectl apply -f k8s/
                '''
    }
}
        stage('Prometheus / Grafana') {
            steps {
                echo 'Metrics exposed for Prometheus at http://<EC2-IP>:8080/prometheus'
            }
        }
    }
}
