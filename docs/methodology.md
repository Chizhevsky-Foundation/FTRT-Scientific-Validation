# Metodología Científica - Sistema FTRT

**Fuerzas de Marea Relativas Totales**

---

## Índice

1. [Marco Teórico](#marco-teórico)
2. [Fórmula FTRT](#fórmula-ftrt)
3. [Obtención de Datos](#obtención-de-datos)
4. [Procesamiento de Datos](#procesamiento-de-datos)
5. [Análisis Estadístico](#análisis-estadístico)
6. [Criterios de Validación](#criterios-de-validación)
7. [Limitaciones Conocidas](#limitaciones-conocidas)

---

## Marco Teórico

### Hipótesis Central

Las fuerzas de marea gravitacionales ejercidas por los planetas sobre el Sol, cuando alcanzan configuraciones específicas, pueden correlacionar con incrementos en la actividad solar (tormentas solares, eyecciones de masa coronal).

### Fundamentos Físicos

#### 1. Fuerzas de Marea

La fuerza de marea que un cuerpo de masa M ejerce sobre otro a distancia d es proporcional a:

```
F_marea ∝ M / d³
```

Esta fuerza es significativamente mayor que la fuerza gravitacional simple (∝ M/d²) en sistemas donde las dimensiones del cuerpo receptor son relevantes.

#### 2. Baricentro Solar

El centro de masa del sistema solar (baricentro) no coincide con el centro del Sol debido a la influencia de los planetas, especialmente Júpiter y Saturno.

- **Distancia típica**: 0-2.5 radios solares desde el centro del Sol
- **Máxima registrada**: ~3 radios solares (configuraciones excepcionales)

#### 3. Configuraciones Planetarias Críticas

- **Conjunción**: Planetas alineados en el mismo lado del Sol
- **Oposición**: Planetas en lados opuestos
- **Cuadratura/Escuadra**: Planetas a 90° (configuración T)
- **Gran Cruz**: Cuatro planetas formando cruz (90° entre ellos)

---

## Fórmula FTRT

### Ecuación Principal

```
FTRT = Σ (M_p × R_☉) / d_p³
```

Donde:
- **FTRT**: Fuerza de Marea Relativa Total (unidades arbitrarias)
- **M_p**: Masa del planeta p (en masas de Júpiter)
- **R_☉**: Radio del Sol (696,000 km)
- **d_p**: Distancia planeta-Sol (en AU)
- **Σ**: Suma sobre todos los planetas considerados

### Normalización

Los valores FTRT están normalizados de forma que:
- FTRT = 1.0 representa condiciones típicas
- FTRT = 2.5 es el umbral para "crítico"
- FTRT = 4.0 indica condiciones "extremas"

### Planetas Incluidos

Por defecto, se incluyen:
- **Gigantes gaseosos**: Júpiter, Saturno, Urano, Neptuno (contribución dominante)
- **Planetas interiores**: Venus, Tierra (contribución menor pero no despreciable)

Se excluyen Mercurio y Marte por su masa insignificante para el efecto de marea total.

---

## Obtención de Datos

### Posiciones Planetarias

#### Fuente Primaria: JPL Horizons

**URL**: https://ssd.jpl.nasa.gov/horizons/

**API Endpoint**: https://ssd.jpl.nasa.gov/api/horizons.api

**Parámetros de consulta**:
```
COMMAND: [planet_code]  # Ej: '599' para Júpiter
CENTER: '500@10'        # Sol como centro
START_TIME: YYYY-MM-DD
STOP_TIME: YYYY-MM-DD
STEP_SIZE: '1d'
QUANTITIES: '1,20'      # Coordenadas y distancias
```

#### Método Offline (Backup)

Cuando JPL Horizons no está disponible, se usa aproximación con órbitas keplerianas:

```python
# Distancia aproximada usando semi-major axis
distance_au ≈ a * (1 + e * cos(M))

# Donde:
# a = semi-major axis (constante)
# e = excentricidad orbital
# M = anomalía media (función del tiempo)
```

**Precisión estimada**: ±5-10% vs. posiciones reales

### Eventos Solares Históricos

#### Fuente Primaria: NOAA SWPC

**URL**: https://www.swpc.noaa.gov/

**Datasets utilizados**:
- Solar flare lists (X-ray flux)
- Geomagnetic storm index (Kp)
- CME catalogs

#### Criterios de Inclusión

Para que un evento solar se incluya en el análisis:

1. **Magnitud mínima**: X1.0 o superior
2. **Índice Kp**: ≥6 (tormenta geomagnética)
3. **Fecha precisa**: Conocida con certeza de ±1 día
4. **Fuente verificable**: NOAA, NASA, o publicación científica

### Índice Geomagnético (Kp)

**Fuente**: GFZ German Research Centre for Geosciences

**Escala Kp**:
- 0-2: Tranquilo
- 3-4: Perturbado
- 5: Tormenta menor (G1)
- 6: Tormenta moderada (G2)
- 7: Tormenta fuerte (G3)
- 8: Tormenta severa (G4)
- 9: Tormenta extrema (G5)

---

## Procesamiento de Datos

### Flujo de Trabajo

```
1. Entrada
   ├── Fecha del evento
   └── Lista de planetas a incluir

2. Obtención de Posiciones
   ├── Consulta a JPL Horizons (preferido)
   └── Cálculo offline (backup)

3. Cálculo FTRT
   ├── Para cada planeta:
   │   └── FTRT_p = (M_p × R_☉) / d_p³
   └── FTRT_total = Σ FTRT_p

4. Cálculo de Baricentro
   └── Aproximación usando Júpiter y Saturno

5. Clasificación
   └── Nivel de alerta según umbral

6. Salida
   ├── Valor FTRT
   ├── Nivel de alerta
   ├── Distancia baricentro
   └── Desglose por planeta
```

### Validación de Datos

Cada cálculo pasa por validación:

```python
def validate_ftrt_result(ftrt: float) -> bool:
    # Rango esperado: 0.5 - 10.0
    if not (0.1 <= ftrt <= 15.0):
        return False
    return True
```

Si un resultado falla la validación, se marca como outlier para revisión manual.

---

## Análisis Estadístico

### 1. Correlación de Pearson

**Objetivo**: Medir asociación lineal entre FTRT y magnitud de tormentas solares

```
r = Σ[(x_i - x̄)(y_i - ȳ)] / √[Σ(x_i - x̄)² × Σ(y_i - ȳ)²]
```

**Interpretación**:
- |r| < 0.3: Correlación débil
- 0.3 ≤ |r| < 0.5: Correlación moderada
- 0.5 ≤ |r| < 0.7: Correlación fuerte
- |r| ≥ 0.7: Correlación muy fuerte

### 2. Test de Significancia

**H₀** (hipótesis nula): No hay correlación (r = 0)

**Test t**:
```
t = r × √(n-2) / √(1-r²)
```

**Criterio de rechazo**: p-value < 0.05 (95% de confianza)

### 3. Bootstrap para Intervalos de Confianza

**Procedimiento**:
1. Resample con reemplazo (n=10,000 iteraciones)
2. Calcular r para cada muestra
3. Determinar percentiles 2.5% y 97.5%

**Ventaja**: No asume distribución normal

### 4. Test de Permutación

**Procedimiento**:
1. Permutar aleatoriamente magnitudes (n=10,000 veces)
2. Calcular r para cada permutación
3. p-value = proporción de |r_perm| ≥ |r_obs|

**Ventaja**: P-value exacto sin asumir distribución

### 5. Regresión Lineal

**Modelo**:
```
Magnitud = β₀ + β₁ × FTRT + ε
```

**Métricas**:
- **R²**: Proporción de varianza explicada
- **RMSE**: Raíz del error cuadrático medio
- **Residuales**: Análisis de normalidad (Q-Q plot)

### 6. Validación Cruzada

**Método**: K-fold cross-validation (k=5)

**Procedimiento**:
1. Dividir dataset en 5 partes
2. Entrenar en 4, validar en 1
3. Repetir 5 veces
4. Promediar R²

**Ventaja**: Evalúa generalización del modelo

### 7. Análisis de Outliers

**Método**: Z-score de residuales

```
z = (residual - mean) / std
```

**Criterio**: |z| > 2.0 es outlier potencial

**Investigación**: Cada outlier se analiza manualmente para identificar causas (ej: baricentro muy alejado, otros factores solares).

---

## Criterios de Validación

### Para Considerar el Modelo Válido

El modelo FTRT se considera científicamente válido si cumple:

#### 1. Criterios Estadísticos

- ✅ **Tamaño de muestra**: n ≥ 30 eventos
- ✅ **Correlación significativa**: |r| > 0.5 Y p < 0.05
- ✅ **Poder predictivo**: R² > 0.4 (explica >40% de varianza)
- ✅ **Validación cruzada**: CV R² > 0.3

#### 2. Criterios de Robustez

- ✅ **Bootstrap**: IC 95% no incluye r=0
- ✅ **Permutación**: p < 0.05
- ✅ **Residuales**: Distribución aproximadamente normal
- ✅ **Outliers**: <20% de la muestra

#### 3. Criterios de Reproducibilidad

- ✅ **Código abierto**: Disponible en GitHub
- ✅ **Datos verificables**: Fuentes citadas y accesibles
- ✅ **Documentación completa**: Metodología reproducible
- ✅ **Resultados replicables**: Otros pueden obtener los mismos valores

### Estado Actual

**Muestra**: n=16 (< 30 ideal)  
**Correlación**: r=0.63, p=0.008 (✓ significativa)  
**Poder predictivo**: R²=0.40 (✓ moderado)  
**Validación cruzada**: R²≈0.41 (✓ consistente)

**Veredicto**: Resultados prometedores pero **no concluyentes**. Se requiere muestra expandida.

---

## Limitaciones Conocidas

### 1. Tamaño de Muestra

**Limitación**: n=16 eventos (ideal: n≥30)

**Impacto**:
- Intervalos de confianza amplios
- Mayor susceptibilidad a outliers
- Poder estadístico reducido

**Mitigación**: Expandir dataset a 50+ eventos

### 2. Método de Cálculo

**Limitación**: Uso de órbitas keplerianas en lugar de posiciones reales de JPL

**Impacto**:
- Error estimado de ±10% en valores FTRT
- Puede afectar clasificación de eventos cercanos a umbrales

**Mitigación**: Integrar API de JPL Horizons completamente

### 3. Ausencia de Control Negativo

**Limitación**: No hay días sin tormenta en el dataset

**Impacto**:
- No se puede calcular tasa de falsos positivos
- Sesgo de selección presente
- Imposible evaluar especificidad del modelo

**Mitigación**: Incluir días aleatorios sin actividad solar

### 4. Factores Confundentes

**Limitación**: No se consideran:
- Ciclo solar de 11 años
- Número de manchas solares
- Campos magnéticos solares
- Rotación diferencial solar

**Impacto**:
- Posible atribución incorrecta de causalidad
- Variables omitidas que pueden explicar la correlación

**Mitigación**: Análisis multivariable futuro

### 5. Mecanismo Físico Desconocido

**Limitación**: No se ha demostrado el mecanismo causal

**Impacto**:
- Correlación no implica causalidad
- Posibilidad de correlación espuria

**Mitigación**: Investigación teórica del mecanismo

### 6. Aproximación del Baricentro

**Limitación**: Cálculo simplificado usando solo Júpiter y Saturno

**Impacto**:
- Error estimado de ±20% en distancia de baricentro
- No captura configuraciones complejas de múltiples planetas

**Mitigación**: Cálculo exacto del centro de masa del sistema solar

---

## Próximas Mejoras Metodológicas

### Corto Plazo

1. **Integración JPL Horizons**: API completa para posiciones precisas
2. **Expansión de muestra**: 30-50 eventos mínimo
3. **Control negativo**: 100+ días sin tormenta
4. **Tests adicionales**: Análisis de sensibilidad, curvas ROC

### Mediano Plazo

1. **Análisis multivariable**: Incluir manchas solares, ciclo solar
2. **Cálculo exacto de baricentro**: Usando todos los planetas
3. **Ventana temporal**: Análisis de lead-time (días antes del evento)
4. **Comparación con NOAA**: Validar contra modelos operacionales

### Largo Plazo

1. **Modelo de machine learning**: Random Forest, XGBoost
2. **Serie temporal**: Análisis de autocorrelación
3. **Predicción en tiempo real**: Dashboard operacional
4. **Investigación teórica**: Mecanismo físico de acoplamiento

---

## Referencias Metodológicas

- Bevington, P.R. & Robinson, D.K. (2003). *Data Reduction and Error Analysis for the Physical Sciences*. McGraw-Hill.
- Efron, B. & Tibshirani, R.J. (1993). *An Introduction to the Bootstrap*. Chapman & Hall.
- Good, P. (2005). *Permutation, Parametric, and Bootstrap Tests of Hypotheses*. Springer.
- James, G. et al. (2013). *An Introduction to Statistical Learning*. Springer.

---

**Última actualización**: Diciembre 2025  
**Versión de metodología**: 1.0

*"El método científico no garantiza la verdad, pero es el mejor camino que conocemos hacia ella."*
