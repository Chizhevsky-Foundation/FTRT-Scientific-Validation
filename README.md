# 🌌 Sistema FTRT - Validación Científica

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Status: Research](https://img.shields.io/badge/status-research-orange.svg)]()

**Fuerzas de Marea Relativas Totales (FTRT) - Análisis de Correlación con Actividad Solar**

---

## 🎯 Objetivo del Proyecto

Este proyecto investiga científicamente si las configuraciones planetarias, medidas mediante el índice FTRT (Fuerzas de Marea Relativas Totales), correlacionan con eventos de tormentas solares mayores.

**En honor a Alexander Leonidovich Chizhevsky (1897-1964)**, pionero de la heliobiología quien documentó correlaciones entre ciclos solares y eventos históricos terrestres, y quien sufrió 16 años de Gulag por defender sus ideas científicas.

---

## 📚 Marco Teórico

### Hipótesis Central

Las fuerzas de marea gravitacionales ejercidas por los planetas sobre el Sol, cuando alcanzan configuraciones específicas (conjunciones, oposiciones, cuadraturas), pueden correlacionar con incrementos en la actividad solar.

### Fórmula FTRT

```
FTRT = Σ (M_planeta × R_☉) / d_planeta³
```

Donde:
- `M_planeta` = Masa del planeta (en masas de Júpiter)
- `R_☉` = Radio del Sol (696,000 km)
- `d_planeta` = Distancia planeta-Sol (en AU)

### Niveles de Alerta

| Nivel | Rango FTRT | Interpretación |
|-------|------------|----------------|
| 🟢 **NORMAL** | < 1.5 | Actividad solar típica |
| 🟡 **ELEVADO** | 1.5 - 2.5 | Posible actividad incrementada |
| 🟠 **CRÍTICO** | 2.5 - 4.0 | Alta probabilidad de tormentas |
| 🔴 **EXTREMO** | > 4.0 | Evento excepcional esperado |

---

## 🔬 Metodología Científica

### Fuentes de Datos

1. **Posiciones Planetarias**: NASA JPL Horizons System
2. **Eventos Solares**: NOAA Space Weather Prediction Center
3. **Índice Geomagnético**: GFZ German Research Centre for Geosciences

### Eventos Históricos Analizados (n=13)

| Fecha | Evento | Magnitud | Kp | FTRT Calculado |
|-------|--------|----------|----|----|
| 1859-09-01 | Carrington Event | X45+ | 9 | 3.21* |
| 1989-03-13 | Quebec Blackout | X15 | 9 | 2.80* |
| 2003-10-28 | Halloween Storm | X17.2 | 9 | 4.87* |
| 2003-11-04 | Halloween 2 | X28 | 9 | 4.65* |
| 2024-05-10 | May 2024 Storm | X5.8 | 9 | 1.34* |

*Valores calculados con el sistema. Ver resultados completos en `/results/`

### Análisis Estadísticos Realizados

- ✅ Correlación de Pearson con test de significancia
- ✅ Bootstrap (10,000 iteraciones) para intervalos de confianza
- ✅ Test de permutación para validación de p-value
- ✅ Análisis de outliers (residuales y z-scores)
- ✅ Validación cruzada (k-fold) para poder predictivo
- ✅ Análisis de regresión lineal

---

## 📁 Estructura del Proyecto

```
FTRT-Scientific-Validation/
│
├── README.md                          # Este archivo
├── LICENSE                            # Licencia MIT
├── requirements.txt                   # Dependencias Python
│
├── src/
│   ├── ftrt_calculator.py            # Calculadora FTRT con JPL Horizons
│   ├── ftrt_advanced_analysis.py     # Análisis estadístico avanzado
│   └── utils.py                       # Funciones auxiliares
│
├── data/
│   ├── historical_events.csv         # Eventos solares verificados
│   └── ftrt_results.csv               # Resultados calculados
│
├── results/
│   ├── ftrt_validation_results.csv   # Dataset completo con FTRT
│   ├── ftrt_statistical_report.txt   # Reporte estadístico
│   └── ftrt_analysis.png              # Visualizaciones
│
├── notebooks/
│   └── FTRT_Exploratory_Analysis.ipynb  # Jupyter notebook interactivo
│
└── docs/
    ├── methodology.md                 # Metodología detallada
    ├── chizhevsky_legacy.md          # Sobre A.L. Chizhevsky
    └── references.md                  # Referencias científicas
```

---

## 🚀 Instalación y Uso

### Requisitos

- Python 3.8+
- pip

### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/tuusuario/FTRT-Scientific-Validation.git
cd FTRT-Scientific-Validation

# Crear entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

### Uso Básico

#### 1. Calcular FTRT para una fecha específica

```python
from src.ftrt_calculator import FTRTCalculator

calculator = FTRTCalculator()
result = calculator.calculate_ftrt('2024-05-10')

print(f"FTRT: {result['ftrt_total']:.2f}")
print(f"Nivel: {result['alert_level']}")
```

#### 2. Validar contra eventos históricos

```bash
python src/ftrt_calculator.py
```

Esto calculará FTRT para todos los eventos históricos y generará:
- `results/ftrt_validation_results.csv`
- Estadísticas de correlación en consola

#### 3. Análisis estadístico completo

```bash
python src/ftrt_advanced_analysis.py
```

Genera:
- Bootstrap de correlación
- Test de permutación
- Análisis de outliers
- Visualizaciones (`results/ftrt_analysis.png`)
- Reporte completo (`results/ftrt_statistical_report.txt`)

---

## 📊 Resultados Preliminares

### ⚠️ IMPORTANTE: Resultados en Desarrollo

Los resultados actuales son **preliminares** y están siendo validados. Los valores FTRT mostrados fueron calculados con aproximaciones iniciales.

**Estado Actual del Análisis:**

- ✅ Metodología definida y documentada
- ✅ Sistema de cálculo implementado
- 🔄 Integración con JPL Horizons en progreso
- 🔄 Validación con dataset completo pendiente
- ⏳ Resultados estadísticos finales: En desarrollo

### Compromiso con la Transparencia

Siguiendo el ejemplo de Chizhevsky, este proyecto se compromete a:

1. **Reportar resultados honestos** sean favorables o desfavorables
2. **Documentar todas las limitaciones** del análisis
3. **Publicar código abierto** para reproducibilidad
4. **Aceptar refutación** si los datos no apoyan la hipótesis

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas, especialmente:

- 🔍 Revisión de metodología estadística
- 📊 Expansión del dataset histórico
- 🔬 Validación independiente de cálculos
- 📝 Mejoras en documentación
- 🐛 Reporte de bugs

### Cómo Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📖 Limitaciones Conocidas

Este estudio reconoce las siguientes limitaciones:

1. **Muestra pequeña**: n=13 eventos (ideal: n≥30)
2. **Mecanismo físico**: No se ha demostrado el mecanismo causal
3. **Factores confundentes**: Ciclo solar de 11 años, manchas solares
4. **Precisión de cálculo**: Dependiente de la calidad de datos de efemérides
5. **Correlación ≠ Causalidad**: Una correlación no prueba causa-efecto

---

## 🎓 Referencias

### Trabajos de A.L. Chizhevsky

- Chizhevsky, A.L. (1976). *Physical Factors of the Historical Process*. Cycles Research Institute.
- Chizhevsky, A.L. (1973). *The Terrestrial Echo of Solar Storms*. USSR Academy of Sciences.

### Literatura Científica Relevante

- Landscheidt, T. (2003). *New Little Ice Age Instead of Global Warming?* Energy & Environment, 14(2-3).
- Wolff, C.L. & Patrone, P.N. (2010). *A new way that planets can affect the sun*. Solar Physics, 266(1).
- Scafetta, N. (2012). *Does the Sun work as a nuclear fusion amplifier of planetary tidal forcing?* Journal of Atmospheric and Solar-Terrestrial Physics, 81-82.

### Fuentes de Datos

- JPL Horizons System: https://ssd.jpl.nasa.gov/horizons/
- NOAA Space Weather: https://www.swpc.noaa.gov/
- SILSO Sunspot Data: https://www.sidc.be/silso/

---

## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

La Licencia MIT permite:
- ✅ Uso comercial
- ✅ Modificación
- ✅ Distribución
- ✅ Uso privado

Con la condición de:
- 📝 Incluir el aviso de copyright
- 📝 Incluir la licencia MIT

---

## 🌟 Reconocimientos

### Alexander Leonidovich Chizhevsky (1897-1964)

Este proyecto honra la memoria de Chizhevsky, quien:

- Fundó la heliobiología como disciplina científica
- Documentó correlaciones entre ciclos solares y eventos terrestres
- Fue encarcelado 8 años y enviado al Gulag otros 8 años (1942-1958)
- Mantuvo su integridad científica pese a la persecución
- Fue rehabilitado parcialmente antes de su muerte en 1964

> *"La sinceridad en la ciencia es más importante que cualquier descubrimiento conveniente."*  
> — Espíritu de A.L. Chizhevsky

### Agradecimientos

- NASA JPL por los datos de efemérides
- NOAA por los datos de actividad solar
- La comunidad científica de código abierto
- Todos los contribuidores a este proyecto

---

## 📧 Contacto

**Proyecto Lead**: Benjamin Cabeza Duran  
**Email**: ia.mechmind@gmail.com  
**GitHub**: [@mechmind-dwv](https://github.com/mechmind-dwv)

**Issues y Discusiones**: [GitHub Issues](https://github.com/tuusuario/FTRT-Scientific-Validation/issues)

---

## 📈 Estado del Proyecto

- [x] Definición de hipótesis
- [x] Implementación de cálculo FTRT
- [x] Sistema de análisis estadístico
- [x] Documentación inicial
- [ ] Integración completa con JPL Horizons
- [ ] Validación con n≥30 eventos
- [ ] Análisis de días sin tormenta (control negativo)
- [ ] Comparación con modelos NOAA existentes
- [ ] Peer review informal
- [ ] Pre-print en arXiv (si resultados significativos)
- [ ] Publicación en revista arbitrada (objetivo final)

---

## 🔮 Roadmap Futuro

### Corto Plazo (3 meses)
- Completar integración JPL Horizons
- Expandir dataset a 50+ eventos
- Validación estadística completa

### Mediano Plazo (6 meses)
- Análisis de falsos positivos/negativos
- Comparación con modelos predictivos existentes
- Dashboard interactivo web

### Largo Plazo (1 año)
- Sistema de predicción en tiempo real
- API pública
- Colaboración con instituciones científicas

---

<div align="center">

### ⭐ Si este proyecto te parece valioso, considera darle una estrella

### 🌍 La ciencia avanza cuando compartimos conocimiento abiertamente

**"La verdad es más valiosa que cualquier teoría conveniente."**

*En memoria de Alexander Leonidovich Chizhevsky*  
*1897 - 1964*

</div>

---

**Última actualización**: Diciembre 2025  
**Versión**: 0.1.0 (Alpha - Investigación en Curso)
