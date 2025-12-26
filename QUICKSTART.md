# ⚡ Guía de Inicio Rápido - Sistema FTRT

**Empieza a usar el Sistema FTRT en 5 minutos**

---

## 🚀 Instalación Ultra-Rápida

### Linux / macOS

```bash
# Descargar e instalar automáticamente
git clone https://github.com/Chizhevsky-Foundation/FTRT-Scientific-Validation.git
cd FTRT-Scientific-Validation
chmod +x install.sh
./install.sh
```

### Windows

```batch
# Descargar e instalar automáticamente
git clone https://github.com/Chizhevsky-Foundation/FTRT-Scientific-Validation.git
cd FTRT-Scientific-Validation
install.bat
```

**¿Sin Git?** Descarga el ZIP desde GitHub y descomprime.

---

## 📊 Primer Uso: Calcular FTRT

### Opción 1: Script Rápido (Recomendado)

**Linux/macOS:**
```bash
source activate_ftrt.sh
python src/ftrt_calculator.py
```

**Windows:**
```batch
run_calculator.bat
```

### Opción 2: Manual

```bash
# Activar entorno
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Ejecutar
python src/ftrt_calculator.py
```

**Salida esperada:**
```
==============================================================
SISTEMA FTRT - VALIDACIÓN CIENTÍFICA COMPLETA
En honor a Alexander Leonidovich Chizhevsky (1897-1964)
==============================================================

[1/3] Calculando FTRT para eventos históricos...
...
✓ Correlación de Pearson: r = 0.6342
✓ P-value: 0.008200
```

---

## 🧪 Usar el Sistema Interactivamente

### En Python

```python
# Activar entorno primero
from src.ftrt_calculator import FTRTCalculator
from datetime import datetime

# Crear calculadora
calc = FTRTCalculator()

# Calcular FTRT para una fecha específica
result = calc.calculate_ftrt('2024-05-10')

print(f"FTRT: {result['ftrt_total']:.2f}")
print(f"Nivel: {result['alert_level']}")
print(f"Baricentro: {result['barycenter_distance_rsun']:.2f} R☉")
```

**Salida:**
```
FTRT: 1.34
Nivel: ELEVADO
Baricentro: 0.68 R☉
```

### Calcular para Cualquier Fecha

```python
from src.ftrt_calculator import FTRTCalculator

calc = FTRTCalculator()

# Tu fecha de interés
fecha = '2026-09-15'
result = calc.calculate_ftrt_offline(fecha)

print(f"FTRT para {fecha}: {result['ftrt_total']:.2f}")
```

---

## 📓 Usar Jupyter Notebook

### Método 1: Script Rápido

**Windows:**
```batch
run_jupyter.bat
```

**Linux/macOS:**
```bash
source activate_ftrt.sh
jupyter notebook notebooks/FTRT_Exploratory_Analysis.ipynb
```

### Método 2: Abrir desde navegador

1. Activa el entorno virtual
2. Ejecuta: `jupyter notebook`
3. Navega a: `notebooks/FTRT_Exploratory_Analysis.ipynb`
4. Click en: **Cell → Run All**

---

## 🔍 Casos de Uso Comunes

### 1. Calcular FTRT para Hoy

```python
from datetime import datetime
from src.ftrt_calculator import FTRTCalculator

calc = FTRTCalculator()
hoy = datetime.now().strftime('%Y-%m-%d')
result = calc.calculate_ftrt_offline(hoy)

print(f"FTRT hoy ({hoy}): {result['ftrt_total']:.2f}")
print(f"Nivel de alerta: {result['alert_level']}")
```

### 2. Analizar Eventos Históricos

```python
from src.ftrt_calculator import HistoricalValidator

validator = HistoricalValidator()

# Calcular FTRT para todos los eventos históricos
results = validator.calculate_all_historical(use_offline=True)

# Ver resultados
for r in results:
    print(f"{r['date']} | {r['name']:20s} | FTRT: {r['ftrt']:.2f}")
```

### 3. Análisis Estadístico Completo

```python
from src.ftrt_advanced_analysis import run_complete_analysis
import pandas as pd

# Cargar datos
df = pd.read_csv('data/ftrt_results.csv')

# Análisis completo (bootstrap, permutación, visualizaciones)
analysis = run_complete_analysis(df)

# Ver correlación con IC
print(f"Correlación: {analysis['bootstrap']['mean']:.3f}")
print(f"IC 95%: [{analysis['bootstrap']['ci_lower']:.3f}, {analysis['bootstrap']['ci_upper']:.3f}]")
```

### 4. Predecir Próximos Días

```python
from datetime import datetime, timedelta
from src.ftrt_calculator import FTRTCalculator

calc = FTRTCalculator()

# Calcular para los próximos 7 días
for i in range(7):
    fecha = (datetime.now() + timedelta(days=i)).strftime('%Y-%m-%d')
    result = calc.calculate_ftrt_offline(fecha)
    print(f"{fecha}: FTRT = {result['ftrt_total']:.2f} ({result['alert_level']})")
```

---

## 📁 Archivos Importantes

| Archivo | Descripción |
|---------|-------------|
| `README.md` | Documentación completa del proyecto |
| `INSTALL.md` | Guía de instalación detallada |
| `src/ftrt_calculator.py` | Calculadora FTRT principal |
| `src/utils.py` | Funciones auxiliares |
| `data/historical_events.csv` | 16 eventos solares verificados |
| `data/ftrt_results.csv` | Resultados calculados |
| `notebooks/FTRT_Exploratory_Analysis.ipynb` | Análisis interactivo |
| `docs/methodology.md` | Metodología científica detallada |

---

## 🔧 Comandos Útiles

### Activar/Desactivar Entorno

**Activar:**
```bash
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

**Desactivar:**
```bash
deactivate
```

### Actualizar el Sistema

```bash
# Activar entorno primero
git pull origin main
pip install --upgrade -r requirements.txt
```

### Ver Resultados Guardados

```bash
# Ver reporte estadístico
cat results/ftrt_statistical_report.txt

# Ver datos
head -20 data/ftrt_results.csv
```

---

## 🎓 Ejemplos de Código Útil

### Crear Gráfica Rápida

```python
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_csv('data/ftrt_results.csv')

# Gráfica simple
plt.figure(figsize=(10, 6))
plt.scatter(df['ftrt_calculated'], df['magnitude'], s=100, alpha=0.6)
plt.xlabel('FTRT')
plt.ylabel('Magnitud X-Class')
plt.title('Correlación FTRT vs Magnitud')
plt.grid(True, alpha=0.3)
plt.show()
```

### Filtrar Eventos Críticos

```python
import pandas as pd

df = pd.read_csv('data/ftrt_results.csv')

# Solo eventos con FTRT crítico o extremo
criticos = df[df['ftrt_calculated'] >= 2.5]

print(f"Eventos críticos encontrados: {len(criticos)}")
print(criticos[['date', 'name', 'ftrt_calculated', 'alert_level']])
```

### Exportar Resultados Personalizados

```python
from src.ftrt_calculator import FTRTCalculator
import pandas as pd

calc = FTRTCalculator()

# Tus fechas de interés
fechas = ['2025-01-01', '2025-06-15', '2025-12-31']

resultados = []
for fecha in fechas:
    r = calc.calculate_ftrt_offline(fecha)
    resultados.append({
        'fecha': fecha,
        'ftrt': r['ftrt_total'],
        'nivel': r['alert_level']
    })

# Guardar en CSV
df = pd.DataFrame(resultados)
df.to_csv('mis_resultados.csv', index=False)
print("Resultados guardados en: mis_resultados.csv")
```

---

## ❓ Preguntas Frecuentes (FAQ)

### ¿Qué significa el valor FTRT?

FTRT mide la fuerza de marea gravitacional total que los planetas ejercen sobre el Sol. Valores más altos indican configuraciones planetarias que *potencialmente* correlacionan con mayor actividad solar.

**Escala:**
- < 1.5: Normal
- 1.5-2.5: Elevado
- 2.5-4.0: Crítico
- \> 4.0: Extremo

### ¿Puedo predecir tormentas solares con esto?

**No directamente.** El sistema FTRT muestra *correlaciones estadísticas*, no causalidad probada. Es una herramienta de investigación, no un sistema operacional de predicción.

### ¿Los datos son reales?

Sí. Los eventos solares provienen de NOAA/NASA. Los cálculos FTRT usan posiciones planetarias aproximadas (órbitas keplerianas). Para máxima precisión, se necesitaría integración completa con JPL Horizons.

### ¿Puedo contribuir al proyecto?

¡Absolutamente! Ve a:
- GitHub Issues: Reportar bugs o sugerir mejoras
- Pull Requests: Contribuir código
- Discussions: Compartir ideas

### ¿Por qué Chizhevsky?

Alexander Leonidovich Chizhevsky (1897-1964) fue pionero en estudiar la influencia del Sol en procesos terrestres. Pasó 16 años encarcelado por Stalin por sus ideas científicas, pero nunca renunció a la verdad. Este proyecto honra su legado.

---

## 🆘 ¿Problemas?

**Error común: "Module not found"**
```bash
# Asegúrate de estar en el directorio correcto
pwd  # Debes ver: /ruta/a/FTRT-Scientific-Validation

# Y que el entorno esté activado
which python  # Debería mostrar: .../venv/bin/python
```

**Error: "pip not found"**
```bash
python -m pip install --upgrade pip
```

**Más ayuda:**
1. Ver `INSTALL.md` para solución de problemas detallada
2. Buscar en [GitHub Issues](https://github.com/Chizhevsky-Foundation/FTRT-Scientific-Validation/issues)
3. Contacto: ia.mechmind@gmail.com

---

## 📚 Siguiente Nivel

Una vez que domines lo básico:

1. **Lee la metodología completa**: `docs/methodology.md`
2. **Explora el código fuente**: `src/`
3. **Modifica y experimenta**: Es open source
4. **Contribuye mejoras**: Pull requests bienvenidos

---

## 🌟 Recursos Adicionales

- **NASA JPL Horizons**: https://ssd.jpl.nasa.gov/horizons/
- **NOAA Space Weather**: https://www.swpc.noaa.gov/
- **Python Tutorial**: https://docs.python.org/3/tutorial/
- **Pandas Cheat Sheet**: https://pandas.pydata.org/docs/

---

**En honor a Alexander Leonidovich Chizhevsky (1897-1964)**

*"El primer paso en la ciencia es observar. El segundo es dudar. El tercero es verificar."*

---

**¿Todo listo?** ¡Empieza a calcular FTRT! 🚀

```bash
python src/ftrt_calculator.py
```
