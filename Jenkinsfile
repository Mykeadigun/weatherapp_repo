pipeline {
  agent any
  stages {
    stage('Checkcode') {
      steps {
        git(url: 'https://github.com/Mykeadigun/weatherapp_repo', branch: 'main')
      }
    }

    stage('List Directory') {
      steps {
        sh 'ls -la'
      }
    }

    stage('Build') {
      steps {
        sh 'docker build -t weather.app.'
      }
    }

  }
}