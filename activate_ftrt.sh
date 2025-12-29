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
