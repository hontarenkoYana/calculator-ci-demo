pipeline {
    agent { docker { image 'python:3.7.2' } }
    stages {
        stage('build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('test') {
            steps {
                sh 'python -m unittest test_calculator.py'
	        sh 'python -m unittest test_app.py'
            } 
        }
    }
}
