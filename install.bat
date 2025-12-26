@echo off
REM ==============================================================================
REM Sistema FTRT - Script de Instalación Automática para Windows
REM En honor a Alexander Leonidovich Chizhevsky (1897-1964)
REM ==============================================================================

setlocal enabledelayedexpansion

REM Configuración de colores (limitado en CMD, pero funcional)
color 0A

cls
echo ================================================================
echo.
echo              SISTEMA FTRT - INSTALADOR
echo.
echo   Fuerzas de Marea Relativas Totales
echo   En honor a A.L. Chizhevsky (1897-1964)
echo.
echo ================================================================
echo.

REM Verificar que estamos en el directorio correcto
if not exist "README.md" (
    echo [ERROR] Este script debe ejecutarse desde la raiz del repositorio
    echo         FTRT-Scientific-Validation
    pause
    exit /b 1
)

echo [INFO] Verificando Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python no encontrado
    echo.
    echo Por favor instala Python 3.8 o superior desde:
    echo https://www.python.org/downloads/
    echo.
    echo IMPORTANTE: Marca la opcion "Add Python to PATH" durante la instalacion
    pause
    exit /b 1
)

REM Obtener versión de Python
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo [OK] Python %PYTHON_VERSION% encontrado

echo.
echo [INFO] Verificando pip...
python -m pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [WARN] pip no encontrado, instalando...
    python -m ensurepip --upgrade
    echo [OK] pip instalado
) else (
    echo [OK] pip encontrado
)

echo.
echo [INFO] Verificando Git...
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [WARN] Git no encontrado
    echo.
    echo Git es opcional pero recomendado. Puedes instalarlo desde:
    echo https://git-scm.com/download/win
    echo.
) else (
    for /f "tokens=3" %%i in ('git --version') do set GIT_VERSION=%%i
    echo [OK] Git !GIT_VERSION! encontrado
)

echo.
echo ================================================================
echo   CREANDO ENTORNO VIRTUAL
echo ================================================================
echo.

if exist "venv" (
    echo [WARN] El entorno virtual ya existe
    choice /C SN /M "Deseas recrearlo?"
    if errorlevel 2 (
        echo [INFO] Usando entorno virtual existente
    ) else (
        echo [INFO] Eliminando entorno virtual anterior...
        rmdir /s /q venv
        echo [INFO] Creando nuevo entorno virtual...
        python -m venv venv
        echo [OK] Entorno virtual recreado
    )
) else (
    echo [INFO] Creando entorno virtual...
    python -m venv venv
    echo [OK] Entorno virtual creado
)

echo.
echo [INFO] Activando entorno virtual...
call venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo [ERROR] No se pudo activar el entorno virtual
    pause
    exit /b 1
)
echo [OK] Entorno virtual activado

echo.
echo [INFO] Actualizando pip...
python -m pip install --upgrade pip --quiet
echo [OK] pip actualizado

echo.
echo ================================================================
echo   INSTALANDO DEPENDENCIAS
echo ================================================================
echo.

if not exist "requirements.txt" (
    echo [ERROR] requirements.txt no encontrado
    pause
    exit /b 1
)

echo [INFO] Instalando dependencias desde requirements.txt...
echo        (Esto puede tomar varios minutos...)
echo.

python -m pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Fallo la instalacion de dependencias
    echo.
    echo Posibles soluciones:
    echo 1. Verifica tu conexion a internet
    echo 2. Ejecuta este script como Administrador
    echo 3. Instala Microsoft Visual C++ Build Tools si el error menciona compilacion
    pause
    exit /b 1
)

echo.
echo [OK] Dependencias instaladas correctamente

echo.
echo ================================================================
echo   COMPONENTES OPCIONALES
echo ================================================================
echo.

echo [?] Deseas instalar Jupyter Notebook?
choice /C SN /M "   (Recomendado para analisis interactivo)"
if not errorlevel 2 (
    echo.
    echo [INFO] Instalando Jupyter Notebook...
    python -m pip install jupyter notebook ipykernel --quiet
    python -m ipykernel install --user --name=ftrt-env --display-name="Python (FTRT)"
    echo [OK] Jupyter Notebook instalado
) else (
    echo [INFO] Jupyter Notebook omitido
)

echo.
echo [?] Deseas instalar herramientas de desarrollo?
choice /C SN /M "   (pytest, black, flake8 - solo para desarrolladores)"
if not errorlevel 2 (
    echo.
    echo [INFO] Instalando herramientas de desarrollo...
    python -m pip install pytest black flake8 mypy --quiet
    echo [OK] Herramientas de desarrollo instaladas
) else (
    echo [INFO] Herramientas de desarrollo omitidas
)

echo.
echo ================================================================
echo   VERIFICANDO INSTALACION
echo ================================================================
echo.

echo [INFO] Ejecutando tests basicos...
python src\utils.py
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Los tests basicos fallaron
    pause
    exit /b 1
)

echo.
echo [INFO] Verificando importaciones de modulos...
python -c "import sys; sys.path.append('src'); from ftrt_calculator import FTRTCalculator; from ftrt_advanced_analysis import AdvancedFTRTAnalysis; from utils import *; print('[OK] Todos los modulos importados correctamente')"

if %errorlevel% neq 0 (
    echo [ERROR] Fallo la verificacion de modulos
    pause
    exit /b 1
)

echo.
echo ================================================================
echo   CREANDO SCRIPTS DE ACCESO RAPIDO
echo ================================================================
echo.

echo [INFO] Creando script de activacion...

REM Crear activate_ftrt.bat
(
echo @echo off
echo echo ================================================================
echo echo   Activando entorno FTRT...
echo echo ================================================================
echo echo.
echo if exist "venv\Scripts\activate.bat" ^(
echo     call venv\Scripts\activate.bat
echo     echo [OK] Entorno activado
echo     echo.
echo     echo Comandos disponibles:
echo     echo   python src\ftrt_calculator.py         - Calcular FTRT
echo     echo   python src\ftrt_advanced_analysis.py  - Analisis avanzado
echo     echo   jupyter notebook                      - Abrir notebooks
echo     echo   deactivate                            - Desactivar entorno
echo     echo.
echo ^) else ^(
echo     echo [ERROR] Entorno virtual no encontrado
echo     pause
echo     exit /b 1
echo ^)
) > activate_ftrt.bat

echo [OK] Script de activacion creado: activate_ftrt.bat

REM Crear script para ejecutar calculadora
(
echo @echo off
echo call venv\Scripts\activate.bat
echo python src\ftrt_calculator.py
echo pause
) > run_calculator.bat

echo [OK] Script de calculadora creado: run_calculator.bat

REM Crear script para abrir Jupyter
(
echo @echo off
echo call venv\Scripts\activate.bat
echo jupyter notebook notebooks\FTRT_Exploratory_Analysis.ipynb
echo pause
) > run_jupyter.bat

echo [OK] Script de Jupyter creado: run_jupyter.bat

echo.
echo ================================================================
echo.
echo          INSTALACION COMPLETADA EXITOSAMENTE
echo.
echo ================================================================
echo.
echo PROXIMOS PASOS:
echo.
echo 1. Para activar el entorno:
echo    activate_ftrt.bat
echo.
echo 2. Para ejecutar el analisis:
echo    run_calculator.bat
echo    (o manualmente: python src\ftrt_calculator.py)
echo.
echo 3. Para explorar con Jupyter:
echo    run_jupyter.bat
echo    (o manualmente: jupyter notebook)
echo.
echo 4. Para leer la documentacion:
echo    type README.md
echo    notepad docs\methodology.md
echo.
echo ================================================================
echo.
echo En honor a Alexander Leonidovich Chizhevsky (1897-1964)
echo "La ciencia requiere coraje, no solo inteligencia"
echo.
echo ================================================================
echo.

pause
