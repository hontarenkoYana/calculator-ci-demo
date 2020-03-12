pipeline {
    agent none
    stages {
        stage('build') {
            agent {
                docker { image 'python:3.7.2' }
            }
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('test') {
            agent {
                docker { image 'python:3.7.2' }
            }
            steps {
                sh 'pip install -r requirements.txt'
                sh 'python -m unittest test_calculator.py'
	        sh 'python -m unittest test_app.py'
            } 
        }
        stage('deploy') {
            agent {
                docker { image 'hontikyana/calculator-app' } 
              }
             steps {
                sh 'docker run -p 5000:5000 hontikyana/calculator-app'
            }
        }
    }
}
