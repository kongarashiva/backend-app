pipeline {
agent any
environment {
AWS_REGION = 'ap-south-2'
ECR_REPO = '100984277793.dkr.ecr.ap-south-2.amazonaws.com/backend-app'
}
stages {
stage('Checkout') {
steps {
git branch: 'main',
url: 'https://github.com/kongarashiva/backend-app.git'
}
}
stage('Build Docker Image') {
steps {
sh 'docker build -t backend-app .'
}
}
stage('Login ECR') {
steps {
sh '''
aws ecr get-login-password --region $AWS_REGION | \
docker login --username AWS \
--password-stdin 100984277793.dkr.ecr.ap-south-2.amazonaws.com
'''
}
}
stage('Push Image') {
steps {
sh '''
docker tag backend-app:latest $ECR_REPO:latest
docker push $ECR_REPO:latest
'''
}
}
stage('Deploy') {
steps {
sh '''
ssh -o StrictHostKeyChecking=no ec2-user@18.60.56.240 "
aws ecr get-login-password --region ap-south-2 | \
docker login --username AWS \
--password-stdin 100984277793.dkr.ecr.ap-south-2.amazonaws.com
docker pull $ECR_REPO:latest
docker stop backend-app || true
docker rm backend-app || true
docker run -d --name backend-app -p 5000:5000 \
$ECR_REPO:latest
"
'''
}
}
}
}
