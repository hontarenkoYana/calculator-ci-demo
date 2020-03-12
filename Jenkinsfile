pipeline {
  stages {
    stage('build') {
      agent { docker { image 'python:3.7.2' } }
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('test') {
      agent { docker { image 'python:3.7.2' } }
      steps {
        sh 'python -m unittest test_calculator.py'
	sh 'python -m unittest test_app.py'
      }   
    }
    stage('deploy') {
      agent { docker {
                      image 'hontikyana/calculator-app'
                      args '-p 5000:5000'} 
              }
      steps {
        sh 'python -m unittest test_calculator.py'
	sh 'python -m unittest test_app.py'
      }   
    }
  }
}
