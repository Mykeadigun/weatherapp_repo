pipeline {
  agent any
  stages {
    stage('Checkcode') {
      steps {
        git branch: 'main', url: 'https://github.com/Mykeadigun/weatherapp_repo'
      }
    } 
    stage('Check Workspace') {
      steps {
        sh 'ls -l'
      }
    }
    stages {
        stage('Check Docker Installation') {
            steps {
                sh 'docker --version || echo "Docker is not installed or not in PATH"'
            }

      stage('Build') {
        steps {
          sh 'docker build -f Dockerfile .'
          }
        }
      }
    }
  }
