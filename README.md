# 🚀 Jenkins CI/CD Pipeline with PyInstaller

A demonstration project showcasing a complete CI/CD pipeline using Jenkins to build a Python CLI application with PyInstaller. This project creates a standalone executable from Python source code and is optimized for Jenkins running in Kubernetes clusters on Linux environments.

## 📋 Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Pipeline Stages](#pipeline-stages)
- [Getting Started](#getting-started)
- [Jenkins Configuration](#jenkins-configuration)
- [Kubernetes Deployment](#kubernetes-deployment)
- [Pipeline Features](#pipeline-features)
- [Troubleshooting](#troubleshooting)

## 🎯 Overview

This project demonstrates a production-ready CI/CD pipeline that:

- ✅ **Builds** a Python CLI application (`add2vals`)
- ✅ **Tests** the application using pytest with JUnit XML reports
- ✅ **Compiles** Python source to bytecode
- ✅ **Packages** the application into a standalone executable using PyInstaller
- ✅ **Archives** build artifacts for download
- ✅ **Generates** comprehensive test reports

### The Application: `add2vals`

The `add2vals` command-line tool takes two values and adds them together:
- If both values are numbers, it performs mathematical addition
- If at least one value is a string, it concatenates them as strings
- Uses the `calc.py` library for the core addition functionality

## 📁 Project Structure

```
PROG8860A3-1/
├── Jenkinsfile              # Jenkins pipeline configuration
├── requirements.txt         # Python dependencies (pytest, pyinstaller)
├── sources/                 # Source code directory
│   ├── add2vals.py         # Main CLI application
│   ├── calc.py             # Addition/subtraction library
│   └── test_calc.py        # Unit tests for calc library
└── README.md               # This file
```

## 🔧 Prerequisites

### Jenkins Requirements
- Jenkins 2.400+ running on Linux/Kubernetes
- Required Jenkins plugins:
  - Pipeline Plugin
  - Git Plugin
  - Workspace Cleanup Plugin
  - JUnit Plugin (for test reporting)

### System Requirements
- Python 3.7+
- `zip` utility (standard on most Linux distributions)
- Git (for source code management)

### Kubernetes Environment (Recommended)
- Kubernetes cluster with Jenkins deployed
- Linux-based worker nodes
- Sufficient resources for build pods

## 🚦 Pipeline Stages

### 1. **Build Stage**
- Displays system information (hostname, Python version)
- Upgrades pip and installs dependencies (pytest, pyinstaller)
- Compiles Python source files to bytecode (.pyc files)
- Stashes compiled results for later stages

### 2. **Test Stage**
- Runs comprehensive unit tests with pytest
- Generates JUnit XML test reports
- Tests the calc library's add2 and subtract2 functions
- Publishes test results to Jenkins UI

### 3. **Deliver Stage**
- Uses PyInstaller to create a standalone executable
- Packages the add2vals application into a single binary file
- Archives the executable for download
- Only runs if previous stages succeed

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/nmrepos/PROG8860A3.git
cd PROG8860A3-1
```

### 2. Local Testing (Optional)
```bash
# Install dependencies
python3 -m pip install -r requirements.txt

# Run tests locally
python3 -m pytest sources/test_calc.py -v

# Test the calc library
python3 -c "
from sources import calc
print('Testing calc library:')
print(f'calc.add2(5, 3) = {calc.add2(5, 3)}')
print(f'calc.add2(\"hello\", \"world\") = {calc.add2(\"hello\", \"world\")}')
"

# Run the add2vals application
python3 sources/add2vals.py
```

### 3. Jenkins Pipeline Setup
1. Create a new Pipeline job in Jenkins
2. Configure the pipeline to use SCM (Git)
3. Point to your repository and specify `Jenkinsfile`
4. Save and run the pipeline

## ⚙️ Jenkins Configuration

### Environment Variables
The pipeline uses these environment variables for optimization:

```groovy
PYTHONPATH = "${WORKSPACE}"     # Ensures proper module imports
PIP_CACHE_DIR = "${WORKSPACE}/.pip-cache"  # Optimizes pip caching
```

### Required Plugins
Install these Jenkins plugins for full functionality:

```bash
# Core plugins
- pipeline-stage-view
- workflow-aggregator
- git

# Testing & Reporting
- junit
- htmlpublisher

# Utility
- ws-cleanup
- build-timestamp
```

## ☸️ Kubernetes Deployment

### Jenkins on Kubernetes Benefits
- **Pod Isolation**: Each build runs in a fresh container
- **Auto-scaling**: Automatic worker pod provisioning
- **Resource Management**: CPU/memory limits per build
- **High Availability**: Distributed Jenkins setup

### Sample Kubernetes Configuration
```yaml
# jenkins-agent-pod-template.yaml
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: python
    image: python:3.9-slim
    command:
    - cat
    tty: true
    resources:
      requests:
        memory: "256Mi"
        cpu: "250m"
      limits:
        memory: "512Mi"
        cpu: "500m"
```

## 🎨 Pipeline Features

### 🔍 **Comprehensive Logging**
Every stage includes detailed logging with clear section headers:
```bash
=== Building Application ===
=== Compiling Python Files ===
=== Running Tests ===
=== Creating Standalone Executable ===
```

### 📊 **Build Information**
Pipeline displays useful build metadata:
- Kubernetes pod hostname
- Python version information
- Compiled bytecode files (.pyc)
- Build number and timestamp

### 🧪 **Test Reporting**
- Comprehensive unit tests (6 test cases)
- JUnit XML report generation with pytest
- Test results published to Jenkins UI
- Tests cover numeric addition, string concatenation, and subtraction

### 📦 **PyInstaller Integration**
- Converts Python application to standalone executable
- Single binary file output (no Python installation required)
- Cross-platform compatibility
- Archived artifacts available for download

### 🚀 **Pipeline Resilience**
- `skipStagesAfterUnstable()` option prevents broken builds from proceeding
- Proper error handling in each stage
- Stashing/unstashing of compiled results between stages
- Clean workspace management

### 📦 **Artifact Management**
- Deployment package creation (`deploy.zip`)
- Artifact archiving for download
- Package validation and listing

### 🚀 **Deployment Simulation**
Realistic deployment process including:
- Package validation
- Deployment simulation with timing
- Health check simulation
- Deployment summary with metadata

## 🐛 Troubleshooting

### Common Issues and Solutions

#### **Python Module Import Errors**
```bash
# Issue: ModuleNotFoundError
# Solution: Ensure PYTHONPATH is set correctly
export PYTHONPATH="${WORKSPACE}"
```

#### **Permission Issues in Kubernetes**
```bash
# Issue: Permission denied for pip install
# Solution: Use --user flag (already implemented)
python3 -m pip install --user -r requirements.txt
```

#### **Missing Dependencies**
```bash
# Issue: Command not found (zip, python3, etc.)
# Solution: Ensure base image includes required tools
# For custom images, install via:
apt-get update && apt-get install -y zip python3 python3-pip
```

#### **Test Report Not Generated**
```bash
# Issue: Test results not showing in Jenkins
# Solution: Ensure pytest-xml is available
python3 -m pip install pytest-xml
python3 -m pytest --junitxml=test-results.xml
```

### **Debug Commands**
```bash
# Check Python environment
python3 --version
python3 -m pip list

# Verify compiled bytecode
ls -la sources/*.pyc

# Check PyInstaller output
ls -la dist/

# Test the calc library
python3 -c "from sources.calc import add2; print(add2(5, 3))"
```

## 📈 Pipeline Output Example

```bash
Running in: jenkins-agent-xyz123
Kubernetes Pod: jenkins-agent-xyz123
Python 3.9.2

=== Compiling Python Files ===
sources/add2vals.py
sources/calc.py

=== Running Tests ===
sources/test_calc.py::TestCalc::test_add2_integers PASSED
sources/test_calc.py::TestCalc::test_add2_floats PASSED
sources/test_calc.py::TestCalc::test_add2_strings PASSED
sources/test_calc.py::TestCalc::test_add2_string_and_integer PASSED
sources/test_calc.py::TestCalc::test_add2_integer_and_string PASSED
sources/test_calc.py::TestCalc::test_subtract2_integers PASSED

=== Creating Standalone Executable ===
Building: add2vals
-rwxr-xr-x 1 jenkins jenkins 8.2M Aug  1 12:34 dist/add2vals

✅ Pipeline completed successfully!
📦 Standalone executable available in artifacts
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally
5. Submit a pull request

## 📝 License

This project is for educational purposes and demonstration of CI/CD best practices.

## 📞 Support

For issues or questions:
- Check the [Troubleshooting](#troubleshooting) section
- Review Jenkins console logs
- Verify Kubernetes pod resources
- Check Python environment and dependencies

---

**Built with ❤️ for DevOps learning and Jenkins pipeline demonstrations**
