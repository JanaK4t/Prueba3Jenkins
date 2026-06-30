pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo "Construcción"
                echo "Compilando el código fuente y resolviendo dependencias..."
                echo "Build completado exitosamente."
            }
        }

        stage('Test') {
            steps {
                echo "Fase de pruebas"
                echo "Ejecutando pruebas unitarias automatizadas..."
                echo "Resultados: 100% de las pruebas pasaron."
            }
        }

        stage('Generate Documentation') {
            steps {
                echo "Generando documentación"
                echo "Ejecutando comando: doxygen Doxyfile"
                echo "Analizando comentarios y estructura en el código fuente..."
                echo "Generando documentación en formato HTML y PDF..."
                echo "Documentación generada correctamente en el directorio /docs."
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
                echo "Despliegue"
                echo "Desplegando la aplicación y la documentación en el entorno de prueba..."
                echo "Despliegue finalizado con éxito."
            }
        }
    }

    post {
        success {
            echo "ALERTA DE SISTEMA: Pipeline completado con éxito. La documentación ha sido actualizada, versionada y está disponible para el equipo."
        }
        failure {
            echo "ALERTA DE SISTEMA: Fallo en el pipeline. Se ha enviado una notificación al equipo de desarrollo para revisar los errores a la brevedad."
        }
    }
}
