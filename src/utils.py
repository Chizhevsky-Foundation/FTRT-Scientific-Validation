"""
Funciones auxiliares para el Sistema FTRT
En honor a Alexander Leonidovich Chizhevsky (1897-1964)
"""

import numpy as np
from datetime import datetime, timedelta
from typing import List, Dict, Tuple, Optional
import pandas as pd


# ============================================================================
# CONSTANTES ASTRONÓMICAS
# ============================================================================

# Masas planetarias (en masas de Júpiter)
PLANET_MASSES = {
    'Mercury': 0.000174,
    'Venus': 0.00257,
    'Earth': 0.00315,
    'Mars': 0.000339,
    'Jupiter': 1.0,
    'Saturn': 0.299,
    'Uranus': 0.0457,
    'Neptune': 0.0537
}

# Distancias medias orbitales (semi-major axis en AU)
PLANET_ORBITS = {
    'Mercury': 0.387,
    'Venus': 0.723,
    'Earth': 1.000,
    'Mars': 1.524,
    'Jupiter': 5.203,
    'Saturn': 9.537,
    'Uranus': 19.191,
    'Neptune': 30.069
}

# Períodos orbitales (en años terrestres)
PLANET_PERIODS = {
    'Mercury': 0.241,
    'Venus': 0.615,
    'Earth': 1.000,
    'Mars': 1.881,
    'Jupiter': 11.862,
    'Saturn': 29.457,
    'Uranus': 84.011,
    'Neptune': 164.79
}

# Radio del Sol (km)
SUN_RADIUS_KM = 696000

# 1 Unidad Astronómica (km)
AU_TO_KM = 149597870.7

# Códigos NAIF para JPL Horizons
NAIF_CODES = {
    'Sun': '10',
    'Mercury': '199',
    'Venus': '299',
    'Earth': '399',
    'Mars': '499',
    'Jupiter': '599',
    'Saturn': '699',
    'Uranus': '799',
    'Neptune': '899'
}


# ============================================================================
# CÁLCULOS ORBITALES
# ============================================================================

def calculate_planet_position(planet: str, date: datetime, 
                              use_simple: bool = True) -> Dict:
    """
    Calcula posición aproximada de un planeta para una fecha dada.
    
    Args:
        planet: Nombre del planeta
        date: Fecha de cálculo
        use_simple: Si True, usa órbitas circulares (más rápido, menos preciso)
        
    Returns:
        Dict con 'distance_au', 'angle_deg', y otros parámetros
    """
    if planet not in PLANET_ORBITS:
        raise ValueError(f"Planeta desconocido: {planet}")
    
    if use_simple:
        # Método simplificado: órbita circular
        a = PLANET_ORBITS[planet]  # Semi-major axis
        period = PLANET_PERIODS[planet]  # Período orbital
        
        # Época de referencia: J2000 (2000-01-01)
        epoch = datetime(2000, 1, 1)
        days_since_epoch = (date - epoch).days
        years_since_epoch = days_since_epoch / 365.25
        
        # Ángulo orbital (simplificado)
        mean_anomaly = (years_since_epoch / period) * 360.0
        mean_anomaly = mean_anomaly % 360.0
        
        # Para órbitas circulares: r ≈ a
        distance_au = a
        
        return {
            'distance_au': distance_au,
            'angle_deg': mean_anomaly,
            'semi_major_axis': a,
            'period_years': period,
            'method': 'simple_circular'
        }
    else:
        # Método más preciso requeriría elementos orbitales completos
        # y cálculo de anomalía verdadera
        # Por ahora, usar método simple
        return calculate_planet_position(planet, date, use_simple=True)


def calculate_barycenter_distance(planet_positions: Dict[str, Dict]) -> float:
    """
    Calcula distancia aproximada del baricentro solar.
    
    Args:
        planet_positions: Dict con posiciones de planetas
        
    Returns:
        Distancia del baricentro en radios solares
    """
    # Simplificación: el baricentro está dominado por Júpiter y Saturno
    jupiter_dist = planet_positions.get('Jupiter', {}).get('distance_au', 5.2)
    saturn_dist = planet_positions.get('Saturn', {}).get('distance_au', 9.5)
    
    jupiter_mass = PLANET_MASSES['Jupiter']
    saturn_mass = PLANET_MASSES['Saturn']
    
    # Cálculo simplificado del centro de masa
    # (ignorando Sol para aproximación de primer orden)
    total_mass = jupiter_mass + saturn_mass
    
    # Contribución de Júpiter (dominante)
    jupiter_contribution = (jupiter_mass / total_mass) * (jupiter_dist - 1.0)
    
    # Convertir a radios solares (1 AU ≈ 215 R☉)
    barycenter_rsun = abs(jupiter_contribution * 215 * 0.005)
    
    # Limitar a rango realista (0-3 R☉)
    barycenter_rsun = max(0.01, min(barycenter_rsun, 3.0))
    
    return barycenter_rsun


# ============================================================================
# CÁLCULOS FTRT
# ============================================================================

def calculate_ftrt_single_planet(mass_jupiter: float, distance_au: float) -> float:
    """
    Calcula contribución FTRT de un solo planeta.
    
    Formula: FTRT = (M_p × R_☉) / d³
    
    Args:
        mass_jupiter: Masa del planeta en masas de Júpiter
        distance_au: Distancia al Sol en AU
        
    Returns:
        Contribución FTRT del planeta
    """
    return (mass_jupiter * SUN_RADIUS_KM) / (distance_au ** 3)


def calculate_ftrt_total(planet_positions: Dict[str, Dict], 
                        planets_included: Optional[List[str]] = None) -> float:
    """
    Calcula FTRT total para un conjunto de planetas.
    
    Args:
        planet_positions: Dict con posiciones de planetas
        planets_included: Lista de planetas a incluir (None = todos)
        
    Returns:
        FTRT total
    """
    if planets_included is None:
        planets_included = ['Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Venus', 'Earth']
    
    ftrt_total = 0.0
    
    for planet in planets_included:
        if planet in planet_positions and planet in PLANET_MASSES:
            distance = planet_positions[planet]['distance_au']
            mass = PLANET_MASSES[planet]
            ftrt_total += calculate_ftrt_single_planet(mass, distance)
    
    return ftrt_total


def get_alert_level(ftrt: float) -> str:
    """
    Determina nivel de alerta basado en valor FTRT.
    
    Args:
        ftrt: Valor FTRT calculado
        
    Returns:
        Nivel de alerta ('NORMAL', 'ELEVADO', 'CRÍTICO', 'EXTREMO')
    """
    if ftrt >= 4.0:
        return 'EXTREMO'
    elif ftrt >= 2.5:
        return 'CRÍTICO'
    elif ftrt >= 1.5:
        return 'ELEVADO'
    else:
        return 'NORMAL'


# ============================================================================
# FUNCIONES ESTADÍSTICAS
# ============================================================================

def calculate_correlation_with_ci(x: np.ndarray, y: np.ndarray, 
                                  n_bootstrap: int = 1000) -> Dict:
    """
    Calcula correlación con intervalo de confianza por bootstrap.
    
    Args:
        x: Array de valores X
        y: Array de valores Y
        n_bootstrap: Número de iteraciones bootstrap
        
    Returns:
        Dict con 'r', 'p_value', 'ci_lower', 'ci_upper'
    """
    from scipy import stats
    
    # Correlación observada
    r_observed, p_value = stats.pearsonr(x, y)
    
    # Bootstrap
    correlations = []
    n = len(x)
    
    for _ in range(n_bootstrap):
        indices = np.random.choice(n, n, replace=True)
        x_sample = x[indices]
        y_sample = y[indices]
        r_boot, _ = stats.pearsonr(x_sample, y_sample)
        correlations.append(r_boot)
    
    correlations = np.array(correlations)
    
    # Intervalos de confianza al 95%
    ci_lower = np.percentile(correlations, 2.5)
    ci_upper = np.percentile(correlations, 97.5)
    
    return {
        'r': r_observed,
        'p_value': p_value,
        'ci_lower': ci_lower,
        'ci_upper': ci_upper,
        'mean_bootstrap': np.mean(correlations)
    }


def permutation_test(x: np.ndarray, y: np.ndarray, 
                    n_permutations: int = 10000) -> Dict:
    """
    Test de permutación para correlación.
    
    Args:
        x: Array de valores X
        y: Array de valores Y
        n_permutations: Número de permutaciones
        
    Returns:
        Dict con 'r_observed', 'p_value', 'r_permuted'
    """
    from scipy import stats
    
    # Correlación observada
    r_observed, _ = stats.pearsonr(x, y)
    
    # Permutaciones
    r_permuted = []
    for _ in range(n_permutations):
        y_shuffled = np.random.permutation(y)
        r_perm, _ = stats.pearsonr(x, y_shuffled)
        r_permuted.append(r_perm)
    
    r_permuted = np.array(r_permuted)
    
    # p-value: proporción de permutaciones con |r| >= |r_observed|
    p_value = np.mean(np.abs(r_permuted) >= np.abs(r_observed))
    
    return {
        'r_observed': r_observed,
        'p_value': p_value,
        'r_permuted': r_permuted
    }


# ============================================================================
# FORMATEO Y UTILIDADES
# ============================================================================

def format_date(date: datetime, format: str = '%Y-%m-%d') -> str:
    """Formatea fecha de forma consistente."""
    return date.strftime(format)


def parse_date(date_str: str, format: str = '%Y-%m-%d') -> datetime:
    """Parsea string de fecha."""
    return datetime.strptime(date_str, format)


def validate_ftrt_value(ftrt: float) -> bool:
    """
    Valida si un valor FTRT es razonable.
    
    Args:
        ftrt: Valor FTRT a validar
        
    Returns:
        True si el valor es válido
    """
    # Rango esperado: 0.5 - 10.0 (valores extremos raros pero posibles)
    return 0.1 <= ftrt <= 15.0


def create_summary_stats(data: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """
    Crea tabla de estadísticas descriptivas.
    
    Args:
        data: DataFrame con datos
        columns: Columnas a analizar
        
    Returns:
        DataFrame con estadísticas
    """
    stats_dict = {}
    
    for col in columns:
        if col in data.columns:
            stats_dict[col] = {
                'count': len(data[col].dropna()),
                'mean': data[col].mean(),
                'std': data[col].std(),
                'min': data[col].min(),
                'q25': data[col].quantile(0.25),
                'median': data[col].median(),
                'q75': data[col].quantile(0.75),
                'max': data[col].max()
            }
    
    return pd.DataFrame(stats_dict).T


# ============================================================================
# VALIDACIÓN DE DATOS
# ============================================================================

def validate_historical_event(event: Dict) -> Tuple[bool, List[str]]:
    """
    Valida que un evento histórico tenga campos requeridos.
    
    Args:
        event: Dict con datos del evento
        
    Returns:
        Tupla (es_válido, lista_de_errores)
    """
    errors = []
    required_fields = ['date', 'name', 'magnitude', 'kp']
    
    for field in required_fields:
        if field not in event:
            errors.append(f"Falta campo requerido: {field}")
    
    # Validar tipos y rangos
    if 'magnitude' in event:
        if not isinstance(event['magnitude'], (int, float)) or event['magnitude'] < 0:
            errors.append("Magnitud debe ser número positivo")
    
    if 'kp' in event:
        if not isinstance(event['kp'], int) or not (0 <= event['kp'] <= 9):
            errors.append("Kp debe ser entero entre 0 y 9")
    
    if 'date' in event:
        try:
            parse_date(event['date'])
        except ValueError:
            errors.append("Fecha en formato inválido (usar YYYY-MM-DD)")
    
    return len(errors) == 0, errors


# ============================================================================
# EXPORTACIÓN
# ============================================================================

def export_results_to_csv(results: List[Dict], filename: str) -> str:
    """
    Exporta resultados a CSV.
    
    Args:
        results: Lista de diccionarios con resultados
        filename: Nombre del archivo de salida
        
    Returns:
        Path del archivo creado
    """
    df = pd.DataFrame(results)
    df.to_csv(filename, index=False)
    return filename


def generate_report_header() -> str:
    """
    Genera encabezado estándar para reportes.
    
    Returns:
        String con encabezado formateado
    """
    return f"""
{'='*80}
SISTEMA FTRT - ANÁLISIS CIENTÍFICO
En Honor a Alexander Leonidovich Chizhevsky (1897-1964)
{'='*80}

Fecha de generación: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Versión del sistema: 0.1.0-alpha

{'='*80}
"""


# ============================================================================
# FUNCIONES DE PRUEBA
# ============================================================================

def run_self_test():
    """
    Ejecuta tests básicos del módulo de utilidades.
    """
    print("Ejecutando self-test de utils.py...")
    
    # Test 1: Cálculo de posición planetaria
    test_date = datetime(2024, 5, 10)
    jupiter_pos = calculate_planet_position('Jupiter', test_date)
    assert 4.5 <= jupiter_pos['distance_au'] <= 5.5, "Distancia de Júpiter fuera de rango"
    print("✓ Test 1: Cálculo de posición planetaria")
    
    # Test 2: Cálculo FTRT
    ftrt = calculate_ftrt_single_planet(1.0, 5.2)
    assert ftrt > 0, "FTRT debe ser positivo"
    print("✓ Test 2: Cálculo FTRT")
    
    # Test 3: Niveles de alerta
    assert get_alert_level(1.0) == 'NORMAL'
    assert get_alert_level(2.0) == 'ELEVADO'
    assert get_alert_level(3.0) == 'CRÍTICO'
    assert get_alert_level(5.0) == 'EXTREMO'
    print("✓ Test 3: Niveles de alerta")
    
    # Test 4: Validación
    test_event = {
        'date': '2024-05-10',
        'name': 'Test Event',
        'magnitude': 5.8,
        'kp': 9
    }
    is_valid, errors = validate_historical_event(test_event)
    assert is_valid, f"Evento válido marcado como inválido: {errors}"
    print("✓ Test 4: Validación de eventos")
    
    print("\n✓ Todos los tests pasados correctamente")


if __name__ == "__main__":
    run_self_test()
