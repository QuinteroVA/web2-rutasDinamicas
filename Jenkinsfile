node {
    stage('Checkout') {
        checkout scm
    }

    stage('Instalar Dependencias') {
        sh 'npm install'
    }

    stage('Construir') {
        sh 'npm run build'
    }

    
}
