#!/bin/bash
# -------------------------------------------------------------------
# SCRIPT DE DESPLIEGUE AUTOMÁTICO - ANTIGRAVITY PIPELINE
# -------------------------------------------------------------------

echo "🚀 [Antigravity] Iniciando entorno local y configuración de Git..."

# 1. Inicializar repositorio Git si no existe
if [ ! -d ".git" ]; then
    git init
    echo "✅ Repositorio Git inicializado."
fi

# 2. Configurar entorno virtual aislado
if [ ! -d ".venv" ]; then
    PYTHON_CMD="python3"
    if ! command -v python3 &>/dev/null; then
        PYTHON_CMD="python"
    fi
    $PYTHON_CMD -m venv .venv
    echo "✅ Entorno virtual (.venv) creado con éxito usando: $PYTHON_CMD"
fi

# 3. Forzar la creación del archivo .gitignore seguro
cat << 'EOF' > .gitignore
.venv/
*.pyc
__pycache__/
.DS_Store
EOF
echo "✅ Archivo .gitignore configurado."

# 4. Confirmación de preparación
echo "-------------------------------------------------------------------"
echo "🔥 Entorno listo. Asegúrate de que 'main.py' y 'README.md' estén guardados."
echo "-------------------------------------------------------------------"

# 5. Automatización de carga a GitHub
git add .
git commit -m "🚀 Feat: Implementación final del patrón MVC y documentación interactiva Mermaid"
git branch -M main

# Reemplaza la URL de abajo con la de tu repositorio real asignado
URL_REPOSITORIO="https://github.com/lorddark2358-max/Juego-del-Ahorcado-by-Juan-Diego-Sarmiento-Esparza.git"

git remote remove origin 2>/dev/null || git remote remove origin 2>/nul || true
git remote add origin "$URL_REPOSITORIO"

echo "📦 Subiendo los entregables del Paso 1 y Paso 2 a GitHub..."
git push -u origin main --force

echo "🎉 [Antigravity] ¡Despliegue completado con éxito absoluto!"
