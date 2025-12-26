#!/bin/bash

# ==============================================================================
# Sistema FTRT - Script de Instalación Automática
# Para Linux y macOS
# En honor a Alexander Leonidovich Chizhevsky (1897-1964)
# ==============================================================================

set -e  # Detener en caso de error

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Banner
echo -e "${BLUE}"
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                                                              ║"
echo "║              🌌 Sistema FTRT - Instalador                   ║"
echo "║                                                              ║"
echo "║   Fuerzas de Marea Relativas Totales                        ║"
echo "║   En honor a A.L. Chizhevsky (1897-1964)                    ║"
echo "║                                                              ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo ""

# Funciones auxiliares
print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ $1${NC}"
}

# Detectar sistema operativo
detect_os() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        OS="linux"
        print_info "Sistema detectado: Linux"
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        OS="macos"
        print_info "Sistema detectado: macOS"
    else
        print_error "Sistema operativo no soportado: $OSTYPE"
        exit 1
    fi
}

# Verificar Python
check_python() {
    print_info "Verificando instalación de Python..."
    
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
        PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d'.' -f1)
        PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d'.' -f2)
        
        if [ "$PYTHON_MAJOR" -ge 3 ] && [ "$PYTHON_MINOR" -ge 8 ]; then
            print_success "Python $PYTHON_VERSION encontrado"
            PYTHON_CMD="python3"
        else
            print_error "Se requiere Python 3.8 o superior. Encontrado: $PYTHON_VERSION"
            exit 1
        fi
    else
        print_error "Python 3 no encontrado"
        print_info "Por favor instala Python 3.8+ antes de continuar:"
        
        if [ "$OS" == "linux" ]; then
            echo "  sudo apt-get install python3 python3-pip python3-venv"
        elif [ "$OS" == "macos" ]; then
            echo "  brew install python3"
        fi
        exit 1
    fi
}

# Verificar pip
check_pip() {
    print_info "Verificando pip..."
    
    if $PYTHON_CMD -m pip --version &> /dev/null; then
        print_success "pip encontrado"
    else
        print_warning "pip no encontrado, instalando..."
        $PYTHON_CMD -m ensurepip --upgrade
        print_success "pip instalado"
    fi
}

# Verificar git
check_git() {
    print_info "Verificando Git..."
    
    if command -v git &> /dev/null; then
        GIT_VERSION=$(git --version | cut -d' ' -f3)
        print_success "Git $GIT_VERSION encontrado"
    else
        print_error "Git no encontrado"
        print_info "Por favor instala Git antes de continuar:"
        
        if [ "$OS" == "linux" ]; then
            echo "  sudo apt-get install git"
        elif [ "$OS" == "macos" ]; then
            echo "  brew install git"
        fi
        exit 1
    fi
}

# Crear entorno virtual
create_venv() {
    print_info "Creando entorno virtual..."
    
    if [ -d "venv" ]; then
        print_warning "El entorno virtual ya existe"
        read -p "¿Deseas recrearlo? (s/N): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Ss]$ ]]; then
            rm -rf venv
            $PYTHON_CMD -m venv venv
            print_success "Entorno virtual recreado"
        else
            print_info "Usando entorno virtual existente"
        fi
    else
        $PYTHON_CMD -m venv venv
        print_success "Entorno virtual creado"
    fi
}

# Activar entorno virtual
activate_venv() {
    print_info "Activando entorno virtual..."
    source venv/bin/activate
    print_success "Entorno virtual activado"
}

# Actualizar pip
upgrade_pip() {
    print_info "Actualizando pip..."
    pip install --upgrade pip --quiet
    print_success "pip actualizado"
}

# Instalar dependencias
install_dependencies() {
    print_info "Instalando dependencias..."
    echo ""
    
    if [ -f "requirements.txt" ]; then
        pip install -r requirements.txt
        print_success "Dependencias instaladas correctamente"
    else
        print_error "requirements.txt no encontrado"
        exit 1
    fi
}

# Instalar Jupyter (opcional)
install_jupyter() {
    echo ""
    read -p "¿Deseas instalar Jupyter Notebook? (S/n): " -n 1 -r
    echo
    
    if [[ ! $REPLY =~ ^[Nn]$ ]]; then
        print_info "Instalando Jupyter..."
        pip install jupyter notebook ipykernel --quiet
        $PYTHON_CMD -m ipykernel install --user --name=ftrt-env --display-name="Python (FTRT)"
        print_success "Jupyter Notebook instalado"
    else
        print_info "Jupyter Notebook omitido"
    fi
}

# Instalar herramientas de desarrollo (opcional)
install_dev_tools() {
    echo ""
    read -p "¿Deseas instalar herramientas de desarrollo? (pytest, black, flake8) (s/N): " -n 1 -r
    echo
    
    if [[ $REPLY =~ ^[Ss]$ ]]; then
        print_info "Instalando herramientas de desarrollo..."
        pip install pytest black flake8 mypy --quiet
        print_success "Herramientas de desarrollo instaladas"
    else
        print_info "Herramientas de desarrollo omitidas"
    fi
}

# Verificar instalación
verify_installation() {
    print_info "Verificando instalación..."
    echo ""
    
    # Test básico
    if $PYTHON_CMD src/utils.py; then
        print_success "Tests básicos pasados correctamente"
    else
        print_error "Tests básicos fallaron"
        exit 1
    fi
    
    echo ""
    
    # Verificar importaciones
    $PYTHON_CMD -c "
import sys
sys.path.append('src')
from ftrt_calculator import FTRTCalculator
from ftrt_advanced_analysis import AdvancedFTRTAnalysis
from utils import *
print('✓ Todos los módulos importados correctamente')
"
    
    if [ $? -eq 0 ]; then
        print_success "Verificación completada"
    else
        print_error "Verificación fallida"
        exit 1
    fi
}

# Crear script de activación
create_activation_script() {
    print_info "Creando script de activación..."
    
    cat > activate_ftrt.sh << 'EOF'
#!/bin/bash
# Script de activación del entorno FTRT

# Colores
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}Activando entorno FTRT...${NC}"

# Activar entorno virtual
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
    echo -e "${GREEN}✓ Entorno activado${NC}"
    echo ""
    echo "Comandos disponibles:"
    echo "  python src/ftrt_calculator.py         - Calcular FTRT"
    echo "  python src/ftrt_advanced_analysis.py  - Análisis avanzado"
    echo "  jupyter notebook                      - Abrir notebooks"
    echo "  deactivate                            - Desactivar entorno"
    echo ""
else
    echo "Error: Entorno virtual no encontrado"
    exit 1
fi
EOF
    
    chmod +x activate_ftrt.sh
    print_success "Script de activación creado: ./activate_ftrt.sh"
}

# Mostrar resumen
show_summary() {
    echo ""
    echo -e "${GREEN}╔══════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║                                                              ║${NC}"
    echo -e "${GREEN}║        ✓ Instalación completada exitosamente                ║${NC}"
    echo -e "${GREEN}║                                                              ║${NC}"
    echo -e "${GREEN}╚══════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    
    print_info "Próximos pasos:"
    echo ""
    echo "1. Activar el entorno virtual:"
    echo "   ${BLUE}source activate_ftrt.sh${NC}"
    echo ""
    echo "2. Ejecutar análisis:"
    echo "   ${BLUE}python src/ftrt_calculator.py${NC}"
    echo ""
    echo "3. Explorar con Jupyter:"
    echo "   ${BLUE}jupyter notebook notebooks/FTRT_Exploratory_Analysis.ipynb${NC}"
    echo ""
    echo "4. Leer la documentación:"
    echo "   ${BLUE}cat README.md${NC}"
    echo ""
    
    print_info "Para desactivar el entorno virtual:"
    echo "   ${BLUE}deactivate${NC}"
    echo ""
    
    echo -e "${YELLOW}En honor a Alexander Leonidovich Chizhevsky (1897-1964)${NC}"
    echo -e "${YELLOW}'La ciencia requiere coraje, no solo inteligencia'${NC}"
    echo ""
}

# ==============================================================================
# FUNCIÓN PRINCIPAL
# ==============================================================================

main() {
    # Verificar que estamos en el directorio correcto
    if [ ! -f "README.md" ] || [ ! -f "requirements.txt" ]; then
        print_error "Este script debe ejecutarse desde la raíz del repositorio FTRT-Scientific-Validation"
        exit 1
    fi
    
    # Detectar sistema operativo
    detect_os
    
    # Verificar dependencias del sistema
    check_python
    check_pip
    check_git
    
    echo ""
    
    # Crear e instalar
    create_venv
    activate_venv
    upgrade_pip
    install_dependencies
    install_jupyter
    install_dev_tools
    
    echo ""
    
    # Verificar instalación
    verify_installation
    
    # Crear scripts auxiliares
    create_activation_script
    
    # Mostrar resumen
    show_summary
}

# Ejecutar
main
