pipeline {
    agent { 
        node {
            label 'docker-python'
            }
      }
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh '''
                python3 math_help.py
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                python3 tests.py
                echo "doing test stuff.."
                '''
            }
        }
    }
}