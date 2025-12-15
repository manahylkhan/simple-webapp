pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "manahyl/simple-webapp"
        MONITORING_NS = "monitoring"
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
                echo "Deploying application to Kubernetes..."
                sh '''
                    sudo -u ubuntu kubectl apply -f k8s/pvc.yaml
                    sudo -u ubuntu kubectl apply -f k8s/mysql-deployment.yaml
                    sudo -u ubuntu kubectl apply -f k8s/mysql-service.yaml
                    sudo -u ubuntu kubectl apply -f k8s/deployment.yaml
                    sudo -u ubuntu kubectl apply -f k8s/service.yaml
                '''
            }
        }

        /* ===================== MONITORING ===================== */

        stage('Prometheus Status') {
            steps {
                echo "Checking Prometheus pods & service..."
                sh '''
                    sudo -u ubuntu kubectl -n $MONITORING_NS get pods
                    sudo -u ubuntu kubectl -n $MONITORING_NS get svc
                '''
            }
        }

        stage('Grafana Status') {
            steps {
                echo "Checking Grafana pods & service..."
                sh '''
                    sudo -u ubuntu kubectl -n $MONITORING_NS get pods | grep grafana
                    sudo -u ubuntu kubectl -n $MONITORING_NS get svc | grep grafana
                '''
            }
        }

        stage('Expose Prometheus & Grafana') {
            steps {
                echo "Access Prometheus & Grafana via Port Forwarding"
                echo "Prometheus → http://<EC2-IP>:9090"
                echo "Grafana → http://<EC2-IP>:3000 (admin/admin)"
                sh '''
                    sudo -u ubuntu kubectl -n $MONITORING_NS port-forward svc/prometheus-kube-prometheus-prometheus 9090:9090 --address=0.0.0.0 &
                    sudo -u ubuntu kubectl -n $MONITORING_NS port-forward svc/prometheus-grafana 3000:80 --address=0.0.0.0 &
                '''
            }
        }
    }

    post {
        success {
            echo "CI/CD + Monitoring pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed. Please check logs."
        }
    }
}
