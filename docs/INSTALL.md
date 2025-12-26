# 🚀 Guía de Instalación - Sistema FTRT

**Instrucciones completas para configurar el Sistema FTRT en tu máquina**

---

## 📋 Tabla de Contenidos

1. [Requisitos del Sistema](#requisitos-del-sistema)
2. [Instalación Rápida](#instalación-rápida)
3. [Instalación Detallada](#instalación-detallada)
4. [Verificación de la Instalación](#verificación-de-la-instalación)
5. [Solución de Problemas](#solución-de-problemas)
6. [Instalación en Diferentes Sistemas](#instalación-en-diferentes-sistemas)

---

## Requisitos del Sistema

### Mínimos

- **Sistema Operativo**: Windows 10+, macOS 10.14+, o Linux (Ubuntu 18.04+)
- **Python**: 3.8 o superior
- **RAM**: 4 GB mínimo
- **Espacio en Disco**: 500 MB libres
- **Conexión a Internet**: Requerida para descargar dependencias

### Recomendados

- **Python**: 3.10 o superior
- **RAM**: 8 GB
- **Espacio en Disco**: 2 GB libres
- **CPU**: Multi-core para análisis más rápidos

---

## Instalación Rápida

### Para Usuarios Experimentados

```bash
# Clonar el repositorio
git clone https://github.com/Chizhevsky-Foundation/FTRT-Scientific-Validation.git
cd FTRT-Scientific-Validation

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Verificar instalación
python src/utils.py

# ¡Listo! Ejecutar análisis
python src/ftrt_calculator.py
```

---

## Instalación Detallada

### Paso 1: Verificar Python

Primero, verifica que tienes Python instalado:

```bash
python --version
```

Deberías ver algo como `Python 3.8.x` o superior.

**Si no tienes Python instalado:**

- **Windows**: Descarga desde [python.org](https://www.python.org/downloads/)
- **macOS**: `brew install python3` (requiere Homebrew)
- **Linux (Ubuntu/Debian)**: `sudo apt-get install python3 python3-pip python3-venv`

### Paso 2: Instalar Git (si no lo tienes)

```bash
git --version
```

**Si no tienes Git:**

- **Windows**: Descarga desde [git-scm.com](https://git-scm.com/download/win)
- **macOS**: `brew install git`
- **Linux**: `sudo apt-get install git`

### Paso 3: Clonar el Repositorio

```bash
# Opción 1: Usando HTTPS (recomendado)
git clone https://github.com/Chizhevsky-Foundation/FTRT-Scientific-Validation.git

# Opción 2: Usando SSH (si tienes clave SSH configurada)
git clone git@github.com:Chizhevsky-Foundation/FTRT-Scientific-Validation.git

# Entrar al directorio
cd FTRT-Scientific-Validation
```

### Paso 4: Crear Entorno Virtual

**¿Por qué un entorno virtual?**  
Mantiene las dependencias del proyecto aisladas de tu sistema Python global.

#### En Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Verás `(venv)` al inicio de tu línea de comandos.

#### En macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

**Para desactivar el entorno virtual:**
```bash
deactivate
```

### Paso 5: Actualizar pip

```bash
pip install --upgrade pip
```

### Paso 6: Instalar Dependencias

```bash
pip install -r requirements.txt
```

Esto instalará:
- numpy
- pandas
- scipy
- matplotlib
- seaborn
- scikit-learn
- requests
- jupyter
- Y más...

**Tiempo estimado**: 2-5 minutos dependiendo de tu conexión.

### Paso 7: Instalar Dependencias Opcionales

#### Para Jupyter Notebook (recomendado):

```bash
pip install jupyter notebook ipykernel
python -m ipykernel install --user --name=ftrt-env
```

#### Para desarrollo (opcional):

```bash
pip install pytest black flake8 mypy
```

---

## Verificación de la Instalación

### Test Básico

```bash
# Ejecutar tests del módulo utils
python src/utils.py
```

Deberías ver:
```
Ejecutando self-test de utils.py...
✓ Test 1: Cálculo de posición planetaria
✓ Test 2: Cálculo FTRT
✓ Test 3: Niveles de alerta
✓ Test 4: Validación de eventos

✓ Todos los tests pasados correctamente
```

### Test Completo

```bash
# Verificar que todos los módulos se pueden importar
python -c "
import sys
sys.path.append('src')
from ftrt_calculator import FTRTCalculator
from ftrt_advanced_analysis import AdvancedFTRTAnalysis
from utils import *
print('✓ Todos los módulos cargados correctamente')
"
```

### Test de Notebook

```bash
# Iniciar Jupyter
jupyter notebook

# Abrir: notebooks/FTRT_Exploratory_Analysis.ipynb
# Ejecutar: Cell > Run All
```

---

## Solución de Problemas

### Problema: "python: command not found"

**Solución**: Usa `python3` en lugar de `python`:
```bash
python3 --version
python3 -m venv venv
```

### Problema: Error al instalar numpy/scipy

**Windows**: Instala Microsoft Visual C++ Build Tools
- Descarga desde: https://visualstudio.microsoft.com/downloads/
- Selecciona "Build Tools for Visual Studio"

**Linux**: Instala dependencias del sistema:
```bash
sudo apt-get install python3-dev libopenblas-dev
```

### Problema: "pip: command not found"

**Solución**:
```bash
# Windows
python -m ensurepip --upgrade

# Linux/Mac
sudo apt-get install python3-pip  # Linux
brew install python3  # Mac
```

### Problema: Errores con matplotlib en macOS

**Solución**:
```bash
pip uninstall matplotlib
pip install matplotlib --no-cache-dir
```

### Problema: "Module not found" al ejecutar scripts

**Solución**: Asegúrate de estar en el directorio correcto:
```bash
# Debes estar en FTRT-Scientific-Validation/
pwd  # Linux/Mac
cd   # Windows

# Si no estás ahí:
cd /ruta/a/FTRT-Scientific-Validation
```

### Problema: Jupyter Kernel no encuentra módulos

**Solución**:
```bash
# Reinstalar kernel del entorno virtual
python -m ipykernel install --user --name=ftrt-env --display-name="Python (FTRT)"

# En Jupyter: Kernel > Change Kernel > Python (FTRT)
```

---

## Instalación en Diferentes Sistemas

### 🪟 Windows 10/11

#### Opción 1: Usando PowerShell

```powershell
# Abrir PowerShell como Administrador
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

# Clonar e instalar
git clone https://github.com/Chizhevsky-Foundation/FTRT-Scientific-Validation.git
cd FTRT-Scientific-Validation
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

#### Opción 2: Usando Git Bash

```bash
# Abrir Git Bash
git clone https://github.com/Chizhevsky-Foundation/FTRT-Scientific-Validation.git
cd FTRT-Scientific-Validation
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

### 🍎 macOS

#### Usando Homebrew (recomendado)

```bash
# Instalar Homebrew si no lo tienes
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instalar Python y Git
brew install python3 git

# Clonar e instalar
git clone https://github.com/Chizhevsky-Foundation/FTRT-Scientific-Validation.git
cd FTRT-Scientific-Validation
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 🐧 Linux (Ubuntu/Debian)

```bash
# Actualizar sistema
sudo apt-get update
sudo apt-get upgrade

# Instalar dependencias del sistema
sudo apt-get install -y python3 python3-pip python3-venv git

# Clonar e instalar
git clone https://github.com/Chizhevsky-Foundation/FTRT-Scientific-Validation.git
cd FTRT-Scientific-Validation
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 🐧 Linux (Fedora/CentOS/RHEL)

```bash
# Instalar dependencias
sudo dnf install python3 python3-pip git

# Clonar e instalar
git clone https://github.com/Chizhevsky-Foundation/FTRT-Scientific-Validation.git
cd FTRT-Scientific-Validation
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

---

## Instalación con Docker (Avanzado)

### Crear Dockerfile

Crea un archivo `Dockerfile` en la raíz del proyecto:

```dockerfile
FROM python:3.10-slim

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copiar archivos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Comando por defecto
CMD ["python", "src/ftrt_calculator.py"]
```

### Construir y ejecutar

```bash
# Construir imagen
docker build -t ftrt-system .

# Ejecutar
docker run -it ftrt-system

# Ejecutar con acceso a notebook
docker run -p 8888:8888 ftrt-system jupyter notebook --ip=0.0.0.0 --allow-root
```

---

## Instalación en Google Colab (Sin Instalación Local)

Si no quieres instalar nada localmente, usa Google Colab:

```python
# En una celda de Colab:
!git clone https://github.com/Chizhevsky-Foundation/FTRT-Scientific-Validation.git
%cd FTRT-Scientific-Validation
!pip install -r requirements.txt

# Importar módulos
import sys
sys.path.append('src')
from ftrt_calculator import FTRTCalculator
```

---

## Actualización del Sistema

Para actualizar a la última versión:

```bash
# Activar entorno virtual
source venv/bin/activate  # Windows: venv\Scripts\activate

# Actualizar código
git pull origin main

# Actualizar dependencias
pip install --upgrade -r requirements.txt
```

---

## Desinstalación

Para desinstalar completamente el sistema:

```bash
# Desactivar entorno virtual si está activo
deactivate

# Eliminar directorio completo
rm -rf FTRT-Scientific-Validation  # Linux/Mac
# En Windows: rmdir /s FTRT-Scientific-Validation
```

---

## Siguientes Pasos

Una vez instalado correctamente:

1. **Lee el README**: `README.md`
2. **Revisa la metodología**: `docs/methodology.md`
3. **Ejecuta el análisis**: `python src/ftrt_calculator.py`
4. **Explora el notebook**: `jupyter notebook notebooks/FTRT_Exploratory_Analysis.ipynb`

---

## Soporte

**¿Problemas con la instalación?**

1. Revisa la sección [Solución de Problemas](#solución-de-problemas)
2. Busca en [Issues existentes](https://github.com/Chizhevsky-Foundation/FTRT-Scientific-Validation/issues)
3. Abre un [nuevo Issue](https://github.com/Chizhevsky-Foundation/FTRT-Scientific-Validation/issues/new)

**Contacto**: ia.mechmind@gmail.com

---

## Recursos Adicionales

- **Python oficial**: https://www.python.org/
- **pip documentation**: https://pip.pypa.io/
- **venv guide**: https://docs.python.org/3/library/venv.html
- **Jupyter**: https://jupyter.org/

---

**En honor a Alexander Leonidovich Chizhevsky (1897-1964)**

*"La ciencia es para todos, no solo para las élites."*

---

**Última actualización**: Diciembre 2025  
**Versión**: 1.0
