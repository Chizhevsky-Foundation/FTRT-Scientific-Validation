# 🤝 Guía de Contribución

**Cómo contribuir al Sistema FTRT**

Gracias por tu interés en contribuir a este proyecto científico. Toda contribución es valiosa, desde reportar bugs hasta proponer nuevas características.

---

## 📜 Código de Conducta

Este proyecto honra el legado de Alexander Leonidovich Chizhevsky, quien defendió la verdad científica bajo circunstancias extremas. Esperamos que todos los contribuyentes:

✅ **Sean respetuosos** con otros colaboradores  
✅ **Sean honestos** sobre limitaciones y resultados  
✅ **Sean constructivos** en críticas y sugerencias  
✅ **Sean inclusivos** - la ciencia es para todos  
✅ **Prioricen la verdad** sobre narrativas convenientes  

❌ **No toleramos**: Acoso, discriminación, pseudociencia sin base, o deshonestidad científica.

---

## 🎯 Tipos de Contribuciones

### 1. 🐛 Reportar Bugs

**Antes de reportar:**
- Busca si ya existe un issue similar
- Verifica que sea reproducible
- Prepara información del error

**Cómo reportar:**
```markdown
**Descripción del bug:**
[Descripción clara y concisa]

**Pasos para reproducir:**
1. Ejecuta '...'
2. Con estos datos '...'
3. Ver error

**Comportamiento esperado:**
[Qué debería pasar]

**Comportamiento actual:**
[Qué pasa realmente]

**Entorno:**
- OS: [Windows 10 / Ubuntu 20.04 / macOS 12]
- Python: [3.9.5]
- Versión FTRT: [commit hash o tag]

**Logs/Errores:**
```
[Pegar traceback completo]
```
```

### 2. 💡 Sugerir Mejoras

**Tipos de mejoras bienvenidas:**
- Nuevas funcionalidades
- Mejoras de rendimiento
- Mejor documentación
- Nuevos análisis estadísticos
- Visualizaciones adicionales

**Template para sugerencias:**
```markdown
**Propuesta:**
[Descripción clara de la mejora]

**Motivación:**
[Por qué esto sería útil]

**Implementación propuesta:**
[Si tienes ideas de cómo implementarlo]

**Alternativas consideradas:**
[Otros enfoques posibles]
```

### 3. 📊 Contribuir Datos

**Datos útiles:**
- Nuevos eventos solares verificados
- Mejoras a datos históricos existentes
- Correcciones de errores en datos

**Requisitos:**
- Fuente verificable (NOAA, NASA, publicación científica)
- Fecha exacta (±1 día mínimo)
- Magnitud X-ray o índice Kp
- Documentación clara

### 4. 📝 Mejorar Documentación

**Áreas que siempre necesitan mejora:**
- Correcciones de typos
- Clarificación de conceptos
- Traducción a otros idiomas
- Ejemplos adicionales
- Tutoriales

### 5. 💻 Contribuir Código

Ver sección detallada abajo.

---

## 🛠️ Proceso de Contribución de Código

### Paso 1: Fork y Clone

```bash
# Hacer fork en GitHub (botón "Fork")

# Clonar tu fork
git clone https://github.com/TU-USUARIO/FTRT-Scientific-Validation.git
cd FTRT-Scientific-Validation

# Añadir upstream
git remote add upstream https://github.com/Chizhevsky-Foundation/FTRT-Scientific-Validation.git
```

### Paso 2: Crear Rama

```bash
# Actualizar desde upstream
git fetch upstream
git checkout main
git merge upstream/main

# Crear rama para tu feature
git checkout -b feature/nombre-descriptivo
# o para bugfix:
git checkout -b fix/descripcion-bug
```

**Convenciones de nombres de rama:**
- `feature/nueva-funcionalidad` - Nueva característica
- `fix/corregir-bug` - Corrección de bug
- `docs/mejorar-readme` - Documentación
- `refactor/optimizar-codigo` - Refactorización
- `test/añadir-tests` - Tests

### Paso 3: Configurar Entorno de Desarrollo

```bash
# Instalar dependencias de desarrollo
pip install -r requirements.txt
pip install pytest black flake8 mypy

# Instalar pre-commit hooks (opcional pero recomendado)
pip install pre-commit
pre-commit install
```

### Paso 4: Hacer Cambios

**Mejores prácticas:**

✅ **Hacer commits pequeños y frecuentes**
```bash
git add archivo_modificado.py
git commit -m "feat: añadir cálculo de baricentro exacto"
```

✅ **Seguir estilo de código:**
```bash
# Formatear con black
black src/

# Verificar con flake8
flake8 src/
```

✅ **Escribir tests:**
```python
# En tests/test_nueva_funcionalidad.py
def test_calcular_baricentro():
    """Test para cálculo de baricentro exacto."""
    result = calcular_baricentro_exacto(fecha='2024-01-01')
    assert 0 < result < 3.0  # Rango válido
```

✅ **Actualizar documentación** si cambias funcionalidad

### Paso 5: Ejecutar Tests

```bash
# Tests unitarios
pytest tests/

# Verificar estilo
black --check src/
flake8 src/

# Type checking (opcional)
mypy src/
```

### Paso 6: Commit

**Formato de commits (Conventional Commits):**

```
tipo(scope): descripción corta

Descripción más detallada si es necesario.

Fixes #123
```

**Tipos:**
- `feat`: Nueva funcionalidad
- `fix`: Corrección de bug
- `docs`: Solo documentación
- `style`: Formateo, sin cambios de código
- `refactor`: Refactorización
- `test`: Añadir tests
- `chore`: Mantenimiento

**Ejemplos:**
```bash
git commit -m "feat(calculator): añadir integración JPL Horizons real"
git commit -m "fix(utils): corregir cálculo de baricentro para Urano"
git commit -m "docs(readme): añadir sección de FAQ"
git commit -m "test(ftrt): añadir tests para casos edge"
```

### Paso 7: Push y Pull Request

```bash
# Push a tu fork
git push origin feature/nombre-descriptivo

# Ir a GitHub y crear Pull Request
```

**Template de Pull Request:**

```markdown
## Descripción
[Descripción clara de qué cambia este PR]

## Tipo de cambio
- [ ] Bug fix
- [ ] Nueva funcionalidad
- [ ] Breaking change
- [ ] Documentación

## ¿Cómo se ha probado?
[Describe los tests que ejecutaste]

## Checklist
- [ ] Mi código sigue el estilo del proyecto
- [ ] He añadido tests que prueban mi funcionalidad
- [ ] He actualizado la documentación
- [ ] Todos los tests pasan
- [ ] He verificado que no rompo funcionalidad existente

## Issues relacionados
Closes #123
Related to #456
```

---

## 📐 Estándares de Código

### Estilo Python (PEP 8)

**Usar black para formateo automático:**
```bash
black src/
```

**Convenciones:**
- Indentación: 4 espacios
- Líneas: max 100 caracteres (flexible para legibilidad)
- Nombres de funciones: `snake_case`
- Nombres de clases: `PascalCase`
- Constantes: `UPPER_CASE`

### Documentación de Código

**Docstrings (Google Style):**

```python
def calculate_ftrt(date: str, planets: List[str] = None) -> Dict:
    """
    Calcula FTRT para una fecha específica.
    
    Args:
        date: Fecha en formato 'YYYY-MM-DD'
        planets: Lista de planetas a incluir (default: todos)
        
    Returns:
        Dict con:
            - ftrt_total: Valor FTRT calculado
            - alert_level: Nivel de alerta
            - planets: Desglose por planeta
            
    Raises:
        ValueError: Si la fecha es inválida
        
    Example:
        >>> result = calculate_ftrt('2024-05-10')
        >>> print(result['ftrt_total'])
        1.34
    """
    # Implementación...
```

### Type Hints

**Usar type hints siempre que sea posible:**

```python
from typing import List, Dict, Optional, Tuple

def process_events(events: List[Dict[str, any]], 
                  min_magnitude: float = 1.0) -> Tuple[int, float]:
    """Process solar events."""
    # ...
```

---

## 🧪 Tests

### Estructura de Tests

```
tests/
├── __init__.py
├── test_ftrt_calculator.py
├── test_utils.py
├── test_advanced_analysis.py
└── test_integration.py
```

### Escribir Tests

**Test unitario simple:**

```python
# tests/test_utils.py
import pytest
from src.utils import calculate_ftrt_single_planet

def test_ftrt_jupiter():
    """Test FTRT calculation for Jupiter."""
    ftrt = calculate_ftrt_single_planet(mass_jupiter=1.0, distance_au=5.2)
    assert ftrt > 0
    assert isinstance(ftrt, float)

def test_ftrt_invalid_distance():
    """Test that invalid distance raises error."""
    with pytest.raises(ValueError):
        calculate_ftrt_single_planet(1.0, distance_au=-1)
```

**Test con fixtures:**

```python
import pytest
import pandas as pd

@pytest.fixture
def sample_events():
    """Sample solar events for testing."""
    return pd.DataFrame({
        'date': ['2024-01-01', '2024-06-15'],
        'magnitude': [5.0, 10.0],
        'kp': [7, 9]
    })

def test_correlation_analysis(sample_events):
    """Test correlation analysis with sample data."""
    # Use fixture
    result = analyze_correlation(sample_events)
    assert 'r' in result
    assert 'p_value' in result
```

### Ejecutar Tests

```bash
# Todos los tests
pytest

# Con coverage
pytest --cov=src tests/

# Tests específicos
pytest tests/test_utils.py

# Test específico
pytest tests/test_utils.py::test_ftrt_jupiter

# Verbose
pytest -v

# Stop en primer fallo
pytest -x
```

---

## 📊 Contribuir Análisis Científico

### Proponer Nuevo Análisis

Si quieres añadir un nuevo método de análisis estadístico:

1. **Abre un Issue** describiendo el análisis propuesto
2. **Justifica** por qué sería útil
3. **Proporciona referencias** (papers que lo usen)
4. **Espera feedback** antes de implementar

### Requisitos para Análisis

- Método estadístico bien establecido
- Referencias a literatura científica
- Código bien documentado
- Tests que validen correctitud
- Interpretación clara de resultados

---

## 🌍 Traducción

**Idiomas bienvenidos:**
- Inglés (priority)
- Español
- Ruso (en honor a Chizhevsky)
- Otros

**Archivos para traducir:**
- README.md → README_[lang].md
- INSTALL.md → INSTALL_[lang].md
- docs/methodology.md → docs/methodology_[lang].md

---

## 📦 Versionado

Seguimos [Semantic Versioning](https://semver.org/):

- **MAJOR** (1.0.0): Cambios incompatibles
- **MINOR** (0.1.0): Nueva funcionalidad compatible
- **PATCH** (0.0.1): Bug fixes

---

## ✅ Checklist de Pull Request

Antes de enviar tu PR, verifica:

- [ ] Código sigue el estilo del proyecto (black, flake8)
- [ ] Añadí tests para mi código
- [ ] Todos los tests pasan
- [ ] Actualicé documentación relevante
- [ ] Actualicé CHANGELOG.md si aplica
- [ ] Mi commit messages son descriptivos
- [ ] Resolví conflictos con main
- [ ] PR tiene título y descripción claros

---

## 🎓 Recursos para Contribuyentes

### Git y GitHub
- [Git Tutorial](https://git-scm.com/docs/gittutorial)
- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [Conventional Commits](https://www.conventionalcommits.org/)

### Python
- [PEP 8 Style Guide](https://pep8.org/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)

### Testing
- [Pytest Documentation](https://docs.pytest.org/)
- [Testing Best Practices](https://testdriven.io/blog/testing-best-practices/)

### Ciencia
- [Good Enough Practices in Scientific Computing](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510)

---

## 🏆 Reconocimiento

Todos los contribuyentes serán:
- Listados en CONTRIBUTORS.md
- Mencionados en releases
- Agradecidos eternamente por la comunidad

**Top contribuyentes** pueden ser invitados como maintainers.

---

## 📧 Contacto

**¿Preguntas sobre cómo contribuir?**

- **GitHub Discussions**: Para preguntas generales
- **GitHub Issues**: Para bugs y features
- **Email**: ia.mechmind@gmail.com

---

## 🙏 Agradecimiento

Gracias por considerar contribuir a este proyecto. Cada línea de código, cada corrección de typo, cada sugerencia nos acerca más a comprender las conexiones cósmicas que Chizhevsky intuyó hace un siglo.

**Tu contribución honra su legado.**

---

**En memoria de Alexander Leonidovich Chizhevsky (1897-1964)**

*"La ciencia avanza no solo por el genio individual, sino por la colaboración de mentes curiosas."*

---

**Última actualización**: Diciembre 2025
