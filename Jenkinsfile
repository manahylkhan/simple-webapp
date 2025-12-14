pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "manahyl/simple-webapp"
        KUBE_CONFIG = credentials('kubeconfig')
    }

    stages {

        stage('Code Fetch') {
            steps {
                git 'https://github.com/manahylkhan/simple-webapp.git'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE:latest .'
            }
        }

        stage('Docker Push') {
            steps {
                withDockerRegistry([credentialsId: 'dockerhub', url: '']) {
                    sh 'docker push $DOCKER_IMAGE:latest'
                }
            }
        }

        stage('Kubernetes Deploy') {
            steps {
                sh 'kubectl apply -f k8s/'
            }
        }

        stage('Monitoring Setup') {
            steps {
                echo "Prometheus & Grafana running"
            }
        }
    }
}
