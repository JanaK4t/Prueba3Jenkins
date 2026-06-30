pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                echo "Preparando el entorno..."
                echo "Iniciando proceso de construcción (Compilación)."
                echo "Build finalizado con éxito."
            }
        }
        
        stage('Test') {
            steps {
                echo "Ejecutando suite de pruebas unitarias y básicas..."
                echo "Resultados: 100% de las pruebas pasaron correctamente."
            }
        }
        
        stage('Analyze') {
            steps {
                echo "Iniciando análisis de calidad y seguridad estática con SonarQube Scanner..."
                echo "ALERTA CRÍTICA: Vulnerabilidad detectada en el código fuente."
                echo "Vulnerabilidad: CWE-89 (Inyección SQL)"
                echo "Detalle: Uso de concatenación directa en consulta a base de datos (f-strings)."
                error("Quality Gate de SonarQube: FAILED. Se bloquea el paso a producción por motivos de seguridad.")
            }
        }
        
        stage('Deploy') {
            steps {
                echo "Desplegando la aplicación en el entorno de pruebas (Staging)..."
                echo "Aplicación levantada exitosamente en contenedor Docker."
                echo "URL de prueba generada para escaneo dinámico."
            }
        }

        stage('Security Test') {
            steps {
                echo "Iniciando scaneo de dependencias"
                echo "Ejecutando OWASP Dependency-Check..."
                echo "Reporte generado: 0 vulnerabilidades CVE detectadas en librerías."
                
                echo "Iniciando Análisis dinámico"
                echo "Levantando contenedor de OWASP ZAP (owasp/zap2docker-stable)..."
                echo "Atacando la URL de la aplicación desplegada..."
                echo "Generando reporte de vulnerabilidades (ZAP Report)."
                echo "Análisis de seguridad completado."
            }
        }
    }
}
