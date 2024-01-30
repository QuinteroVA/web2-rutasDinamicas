node {
    stage('Checkout') {
        checkout scm
    }

    stage('Instalar Dependencias') {
        'npm install'
    }

    stage('Construir') {
        'npm run build'
    }
  
    stage('Enviar correo') {
        'C:\\Users\Nino\AppData\Local\Programs\Python\Python311\python.exe correo.py'
    }

}
