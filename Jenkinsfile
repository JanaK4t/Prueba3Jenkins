pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                echo "Preparando el entorno e Iniciando proceso de construcción..."
                echo "Build finalizado con éxito."
            }
        }
        
        stage('Test') {
            steps {
                echo "Ejecutando suite de pruebas unitarias y básicas..."
                echo "Resultados: 100% de las pruebas pasaron."
            }
        }
        
        stage('Analyze') {
            steps {
                echo "Iniciando análisis de calidad y seguridad estática con SonarQube..."
                echo " ALERTA CRÍTICA: Vulnerabilidad detectada en el código fuente."
                echo "Vulnerabilidad: CWE-89 (Inyección SQL)"
                echo "Detalle: Uso de concatenación directa en consulta a base de datos (f-strings)."
                error("Quality Gate de SonarQube: FAILED. Se bloquea el paso a producción por motivos de seguridad.")
            }
        }

        stage('Generate Documentation') {
            steps {
                echo "Generando documentación"
                echo "Ejecutando comando: doxygen Doxyfile"
                echo "Generando documentación en formato HTML y PDF en el directorio /docs."
            }
        }

        stage('Version Control') {
            steps {
                echo "Actualización de control de versiones"
                echo "Subiendo nueva documentación al repositorio Git..."
                echo "> git add docs/"
                echo "> git commit -m 'docs: Auto-generación de documentación Doxygen [skip ci]'"
                echo "> git push origin main"
                echo "Repositorio actualizado correctamente con la trazabilidad de los cambios."
            }
        }
        
        stage('Deploy') {
            steps {
                echo "Desplegando la aplicación en el entorno de pruebas (Staging)..."
                echo "URL de prueba generada para escaneo dinámico."
            }
        }

        stage('Security Test') {
            steps {
                echo "Iniciando escaneo de dependencias"
                echo "Ejecutando OWASP Dependency-Check..."
                echo "0 vulnerabilidades CVE detectadas en librerías."
                echo "Iniciando Análisis Dinámico (DAST)"
                echo "Levantando contenedor de OWASP ZAP (owasp/zap2docker-stable)..."
                echo "Atacando la URL de la aplicación desplegada... Análisis completado."
            }
        }
    }

    post {
        success {
            echo "ALERTA: Pipeline completado con éxito. Documentación actualizada y código seguro desplegado."
        }
        failure {
            echo "ALERTA: Fallo en el pipeline. Se ha notificado al equipo para revisar vulnerabilidades o fallos de documentación."
        }
    }
}
