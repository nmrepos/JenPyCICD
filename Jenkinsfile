pipeline {
  agent any
  
  options {
    skipStagesAfterUnstable()
  }
  
  environment {
    PYTHONPATH = "${WORKSPACE}"
    PIP_CACHE_DIR = "${WORKSPACE}/.pip-cache"
  }

  stages {
    stage('Build') {
      steps {
        sh '''
          echo "=== Building Application ==="
          echo "Running in: $(hostname)"
          echo "Kubernetes Pod: ${HOSTNAME:-unknown}"
          python3 --version
          python3 -m pip install --user --upgrade pip
          python3 -m pip install --user -r requirements.txt
        '''
        sh '''
          echo "=== Compiling Python Files ==="
          python3 -m py_compile sources/add2vals.py sources/calc.py
          ls -la sources/
        '''
        stash(name: 'compiled-results', includes: 'sources/*.py*')
      }
    }

    stage('Test') {
      steps {
        sh '''
          echo "=== Running Tests ==="
          python3 -m pytest --junit-xml test-reports/results.xml sources/test_calc.py -v
        '''
      }
      post {
        always {
          junit 'test-reports/results.xml'
        }
      }
    }

    stage('Deliver') {
      steps {
        sh '''
          echo "=== Creating Standalone Executable ==="
          python3 -m PyInstaller --onefile sources/add2vals.py
          echo "=== Build Artifacts ==="
          ls -la dist/
        '''
      }
      post {
        success {
          archiveArtifacts 'dist/add2vals'
        }
      }
    }
  }

  post {
    always {
      echo "=== Pipeline Cleanup ==="
      cleanWs()
    }
    success {
      echo "✅ Pipeline completed successfully!"
      echo "📦 Standalone executable available in artifacts"
    }
    failure {
      echo "❌ Pipeline failed!"
    }
  }
}