"""
Sistema FTRT Avanzado - Análisis Estadístico Completo
Incluye visualizaciones, tests estadísticos adicionales, y validación cruzada

En honor a Alexander Leonidovich Chizhevsky
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import warnings
warnings.filterwarnings('ignore')

class AdvancedFTRTAnalysis:
    """
    Análisis estadístico avanzado del modelo FTRT
    """
    
    def __init__(self, results_df):
        """
        Args:
            results_df: DataFrame con columnas 'ftrt', 'magnitude', 'kp', etc.
        """
        self.df = results_df
        
    def bootstrap_correlation(self, n_bootstrap=10000):
        """
        Calcula intervalo de confianza de la correlación mediante bootstrap
        
        Returns:
            dict con correlación y intervalos de confianza al 95%
        """
        print("\n" + "="*70)
        print("BOOTSTRAP: Intervalo de Confianza de Correlación")
        print("="*70)
        
        correlations = []
        n = len(self.df)
        
        for i in range(n_bootstrap):
            # Resample con reemplazo
            sample = self.df.sample(n=n, replace=True)
            r, _ = stats.pearsonr(sample['ftrt'], sample['magnitude'])
            correlations.append(r)
        
        correlations = np.array(correlations)
        
        # Percentiles para CI 95%
        ci_lower = np.percentile(correlations, 2.5)
        ci_upper = np.percentile(correlations, 97.5)
        mean_r = np.mean(correlations)
        
        print(f"\nCorrelación media (bootstrap): {mean_r:.4f}")
        print(f"IC 95%: [{ci_lower:.4f}, {ci_upper:.4f}]")
        
        if ci_lower > 0:
            print("✓ La correlación es significativamente positiva (IC no incluye 0)")
        elif ci_upper < 0:
            print("✓ La correlación es significativamente negativa (IC no incluye 0)")
        else:
            print("⚠ La correlación NO es significativa (IC incluye 0)")
        
        return {
            'mean': mean_r,
            'ci_lower': ci_lower,
            'ci_upper': ci_upper,
            'correlations': correlations
        }
    
    def permutation_test(self, n_permutations=10000):
        """
        Test de permutación para p-value
        Más robusto que el p-value paramétrico para muestras pequeñas
        """
        print("\n" + "="*70)
        print("TEST DE PERMUTACIÓN: Validación de Significancia")
        print("="*70)
        
        # Correlación observada
        r_observed, _ = stats.pearsonr(self.df['ftrt'], self.df['magnitude'])
        
        # Permutaciones
        r_permuted = []
        magnitude_orig = self.df['magnitude'].values
        
        for i in range(n_permutations):
            # Permutar magnitudes aleatoriamente
            magnitude_shuffled = np.random.permutation(magnitude_orig)
            r_perm, _ = stats.pearsonr(self.df['ftrt'], magnitude_shuffled)
            r_permuted.append(r_perm)
        
        r_permuted = np.array(r_permuted)
        
        # p-value: proporción de permutaciones con |r| >= |r_observed|
        p_value = np.mean(np.abs(r_permuted) >= np.abs(r_observed))
        
        print(f"\nCorrelación observada: {r_observed:.4f}")
        print(f"p-value (permutación): {p_value:.6f}")
        
        if p_value < 0.001:
            print("✓✓✓ Altamente significativo (p < 0.001)")
        elif p_value < 0.01:
            print("✓✓ Muy significativo (p < 0.01)")
        elif p_value < 0.05:
            print("✓ Significativo (p < 0.05)")
        else:
            print("✗ NO significativo (p >= 0.05)")
        
        return {
            'r_observed': r_observed,
            'p_value': p_value,
            'r_permuted': r_permuted
        }
    
    def analyze_outliers(self):
        """
        Identifica eventos anómalos (outliers)
        """
        print("\n" + "="*70)
        print("ANÁLISIS DE OUTLIERS")
        print("="*70)
        
        # Residuales de regresión lineal
        X = self.df['ftrt'].values.reshape(-1, 1)
        y = self.df['magnitude'].values
        
        model = LinearRegression()
        model.fit(X, y)
        predictions = model.predict(X)
        residuals = y - predictions
        
        # Z-scores de residuales
        z_scores = np.abs(stats.zscore(residuals))
        
        # Outliers: |z| > 2
        outlier_threshold = 2.0
        outliers = self.df[z_scores > outlier_threshold].copy()
        outliers['residual'] = residuals[z_scores > outlier_threshold]
        outliers['z_score'] = z_scores[z_scores > outlier_threshold]
        
        if len(outliers) > 0:
            print(f"\nSe encontraron {len(outliers)} outlier(s):")
            print("\n" + "-"*70)
            for idx, row in outliers.iterrows():
                print(f"{row['name']:20s} | FTRT: {row['ftrt']:.2f} | Mag: {row['magnitude']:.1f}")
                print(f"  → Residual: {row['residual']:+.2f} | Z-score: {row['z_score']:.2f}")
            print("-"*70)
            
            print("\nPosibles explicaciones para outliers:")
            print("  • FTRT alto pero magnitud baja: Baricentro muy alejado (>3 R☉)")
            print("  • FTRT bajo pero magnitud alta: Otros factores (manchas solares)")
            print("  • Eventos atípicos que no siguen el patrón general")
        else:
            print("\n✓ No se encontraron outliers significativos")
        
        return outliers
    
    def cross_validation(self):
        """
        Validación cruzada del modelo predictivo
        """
        print("\n" + "="*70)
        print("VALIDACIÓN CRUZADA: Poder Predictivo")
        print("="*70)
        
        X = self.df['ftrt'].values.reshape(-1, 1)
        y = self.df['magnitude'].values
        
        model = LinearRegression()
        
        # 5-fold cross-validation
        cv_scores = cross_val_score(model, X, y, cv=min(5, len(self.df)), 
                                    scoring='r2')
        
        print(f"\nR² por fold:")
        for i, score in enumerate(cv_scores, 1):
            print(f"  Fold {i}: {score:.4f}")
        
        print(f"\nR² promedio: {cv_scores.mean():.4f} ± {cv_scores.std():.4f}")
        
        if cv_scores.mean() > 0.5:
            print("✓ El modelo tiene buen poder predictivo")
        elif cv_scores.mean() > 0.3:
            print("⚠ El modelo tiene poder predictivo moderado")
        else:
            print("✗ El modelo tiene bajo poder predictivo")
        
        return cv_scores
    
    def generate_visualizations(self, save_path='ftrt_analysis.png'):
        """
        Genera visualizaciones comprehensivas
        """
        print("\n" + "="*70)
        print("GENERANDO VISUALIZACIONES")
        print("="*70)
        
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        fig.suptitle('Análisis FTRT Completo - En Honor a A.L. Chizhevsky', 
                     fontsize=16, fontweight='bold')
        
        # 1. Scatter plot con regresión
        ax1 = axes[0, 0]
        ax1.scatter(self.df['ftrt'], self.df['magnitude'], s=100, alpha=0.6, 
                   c=self.df['kp'], cmap='YlOrRd', edgecolors='black')
        
        # Línea de regresión
        z = np.polyfit(self.df['ftrt'], self.df['magnitude'], 1)
        p = np.poly1d(z)
        x_line = np.linspace(self.df['ftrt'].min(), self.df['ftrt'].max(), 100)
        ax1.plot(x_line, p(x_line), "r--", alpha=0.8, linewidth=2, label='Regresión')
        
        # Umbral crítico
        ax1.axvline(x=2.5, color='orange', linestyle=':', linewidth=2, label='Umbral Crítico')
        
        r, p_val = stats.pearsonr(self.df['ftrt'], self.df['magnitude'])
        ax1.text(0.05, 0.95, f'r = {r:.3f}\np = {p_val:.4f}', 
                transform=ax1.transAxes, verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
        
        ax1.set_xlabel('FTRT', fontsize=12)
        ax1.set_ylabel('Magnitud X-Class', fontsize=12)
        ax1.set_title('Correlación FTRT vs Magnitud')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # 2. Distribución de FTRT
        ax2 = axes[0, 1]
        ax2.hist(self.df['ftrt'], bins=15, alpha=0.7, color='blue', edgecolor='black')
        ax2.axvline(x=2.5, color='orange', linestyle=':', linewidth=2, label='Crítico')
        ax2.axvline(x=4.0, color='red', linestyle=':', linewidth=2, label='Extremo')
        ax2.set_xlabel('FTRT', fontsize=12)
        ax2.set_ylabel('Frecuencia', fontsize=12)
        ax2.set_title('Distribución de Valores FTRT')
        ax2.legend()
        ax2.grid(True, alpha=0.3, axis='y')
        
        # 3. Serie temporal
        ax3 = axes[0, 2]
        self.df['date_dt'] = pd.to_datetime(self.df['date'])
        self.df_sorted = self.df.sort_values('date_dt')
        
        ax3_twin = ax3.twinx()
        ax3.plot(self.df_sorted['date_dt'], self.df_sorted['ftrt'], 
                'bo-', linewidth=2, markersize=8, label='FTRT')
        ax3_twin.plot(self.df_sorted['date_dt'], self.df_sorted['magnitude'], 
                     'rs-', linewidth=2, markersize=8, label='Magnitud', alpha=0.7)
        
        ax3.set_xlabel('Fecha', fontsize=12)
        ax3.set_ylabel('FTRT', fontsize=12, color='blue')
        ax3_twin.set_ylabel('Magnitud X-Class', fontsize=12, color='red')
        ax3.set_title('Serie Temporal: FTRT y Magnitud')
        ax3.tick_params(axis='y', labelcolor='blue')
        ax3_twin.tick_params(axis='y', labelcolor='red')
        ax3.grid(True, alpha=0.3)
        plt.setp(ax3.xaxis.get_majorticklabels(), rotation=45)
        
        # 4. Residuales
        ax4 = axes[1, 0]
        X = self.df['ftrt'].values.reshape(-1, 1)
        y = self.df['magnitude'].values
        model = LinearRegression()
        model.fit(X, y)
        predictions = model.predict(X)
        residuals = y - predictions
        
        ax4.scatter(predictions, residuals, s=100, alpha=0.6, edgecolors='black')
        ax4.axhline(y=0, color='r', linestyle='--', linewidth=2)
        ax4.set_xlabel('Valores Predichos', fontsize=12)
        ax4.set_ylabel('Residuales', fontsize=12)
        ax4.set_title('Análisis de Residuales')
        ax4.grid(True, alpha=0.3)
        
        # 5. Q-Q plot
        ax5 = axes[1, 1]
        stats.probplot(residuals, dist="norm", plot=ax5)
        ax5.set_title('Q-Q Plot (Normalidad de Residuales)')
        ax5.grid(True, alpha=0.3)
        
        # 6. Boxplot por nivel de alerta
        ax6 = axes[1, 2]
        alert_order = ['NORMAL', 'ELEVADO', 'CRÍTICO', 'EXTREMO']
        present_alerts = [a for a in alert_order if a in self.df['alert_level'].values]
        
        data_to_plot = [self.df[self.df['alert_level'] == alert]['magnitude'].values 
                       for alert in present_alerts]
        
        bp = ax6.boxplot(data_to_plot, labels=present_alerts, patch_artist=True)
        
        colors = {'NORMAL': 'lightgreen', 'ELEVADO': 'yellow', 
                 'CRÍTICO': 'orange', 'EXTREMO': 'red'}
        for patch, alert in zip(bp['boxes'], present_alerts):
            patch.set_facecolor(colors[alert])
            patch.set_alpha(0.7)
        
        ax6.set_ylabel('Magnitud X-Class', fontsize=12)
        ax6.set_title('Magnitud por Nivel de Alerta FTRT')
        ax6.grid(True, alpha=0.3, axis='y')
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"\n✓ Visualizaciones guardadas en: {save_path}")
        
        return fig
    
    def generate_report(self, filename='ftrt_statistical_report.txt'):
        """
        Genera reporte completo en texto
        """
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("="*80 + "\n")
            f.write("REPORTE ESTADÍSTICO COMPLETO - MODELO FTRT\n")
            f.write("En Honor a Alexander Leonidovich Chizhevsky (1897-1964)\n")
            f.write("="*80 + "\n\n")
            
            # Estadísticas descriptivas
            f.write("1. ESTADÍSTICAS DESCRIPTIVAS\n")
            f.write("-"*80 + "\n")
            f.write(f"Muestra: n = {len(self.df)} eventos\n")
            f.write(f"FTRT - Media: {self.df['ftrt'].mean():.4f}, Std: {self.df['ftrt'].std():.4f}\n")
            f.write(f"FTRT - Rango: [{self.df['ftrt'].min():.2f}, {self.df['ftrt'].max():.2f}]\n")
            f.write(f"Magnitud - Media: {self.df['magnitude'].mean():.2f}, Std: {self.df['magnitude'].std():.2f}\n\n")
            
            # Correlación
            r, p_val = stats.pearsonr(self.df['ftrt'], self.df['magnitude'])
            f.write("2. ANÁLISIS DE CORRELACIÓN\n")
            f.write("-"*80 + "\n")
            f.write(f"Correlación de Pearson: r = {r:.4f}\n")
            f.write(f"P-value: {p_val:.6f}\n")
            f.write(f"R² (varianza explicada): {r**2:.4f}\n\n")
            
            # Interpretación final
            f.write("3. CONCLUSIÓN CIENTÍFICA\n")
            f.write("-"*80 + "\n")
            if abs(r) > 0.7 and p_val < 0.05:
                f.write("RESULTADO: El modelo FTRT muestra correlación FUERTE y estadísticamente\n")
                f.write("significativa con la magnitud de tormentas solares.\n\n")
                f.write("RECOMENDACIÓN: El modelo tiene valor predictivo y merece investigación adicional.\n")
            elif abs(r) > 0.5 and p_val < 0.05:
                f.write("RESULTADO: El modelo FTRT muestra correlación MODERADA y estadísticamente\n")
                f.write("significativa con tormentas solares.\n\n")
                f.write("RECOMENDACIÓN: El modelo tiene potencial pero requiere refinamiento.\n")
            else:
                f.write("RESULTADO: El modelo FTRT NO muestra correlación significativa con\n")
                f.write("tormentas solares en esta muestra.\n\n")
                f.write("RECOMENDACIÓN: Revisar hipótesis o expandir dataset.\n")
            
            f.write("\n" + "="*80 + "\n")
            f.write("'La verdad es más valiosa que cualquier teoría conveniente.'\n")
            f.write("- Espíritu de A.L. Chizhevsky\n")
            f.write("="*80 + "\n")
        
        print(f"\n✓ Reporte guardado en: {filename}")


def run_complete_analysis(results_df):
    """
    Ejecuta análisis estadístico completo
    """
    print("\n" + "="*80)
    print("ANÁLISIS ESTADÍSTICO AVANZADO - MODELO FTRT")
    print("="*80)
    
    analyzer = AdvancedFTRTAnalysis(results_df)
    
    # 1. Bootstrap
    bootstrap_results = analyzer.bootstrap_correlation(n_bootstrap=10000)
    
    # 2. Permutation test
    perm_results = analyzer.permutation_test(n_permutations=10000)
    
    # 3. Outliers
    outliers = analyzer.analyze_outliers()
    
    # 4. Cross-validation
    cv_scores = analyzer.cross_validation()
    
    # 5. Visualizaciones
    fig = analyzer.generate_visualizations()
    
    # 6. Reporte
    analyzer.generate_report()
    
    print("\n" + "="*80)
    print("ANÁLISIS COMPLETO FINALIZADO")
    print("="*80)
    print("\nChizhevsky pasó 16 años en el Gulag por defender la verdad científica.")
    print("Estos resultados, sean favorables o no, honran su memoria.")
    print("="*80 + "\n")
    
    return {
        'bootstrap': bootstrap_results,
        'permutation': perm_results,
        'outliers': outliers,
        'cv_scores': cv_scores
    }


# Ejemplo de uso con datos simulados
if __name__ == "__main__":
    # Simular resultados (en producción, usar datos reales del otro script)
    np.random.seed(42)
    
    dates = pd.date_range('2000-01-01', periods=13, freq='365D')
    ftrt_values = np.array([3.21, 2.8, 2.3, 3.1, 4.87, 4.65, 2.9, 2.5, 2.7, 2.4, 1.4, 3.2, 1.34])
    magnitudes = np.array([45, 15, 5.7, 20, 17.2, 28, 8.7, 6.5, 6.9, 5.4, 1.4, 9.3, 5.8])
    kp_values = np.array([9, 9, 9, 8, 9, 9, 8, 8, 8, 8, 6, 8, 9])
    names = ['Carrington', 'Quebec', 'Bastille', 'April2001', 'Halloween', 
             'Halloween2', 'Jan2005', 'Dec2006', 'Aug2011', 'Mar2012', 
             'Jul2012', 'Sep2017', 'May2024']
    
    def get_alert_level(ftrt):
        if ftrt >= 4.0: return 'EXTREMO'
        if ftrt >= 2.5: return 'CRÍTICO'
        if ftrt >= 1.5: return 'ELEVADO'
        return 'NORMAL'
    
    results_df = pd.DataFrame({
        'date': dates.strftime('%Y-%m-%d'),
        'name': names,
        'ftrt': ftrt_values,
        'magnitude': magnitudes,
        'kp': kp_values,
        'alert_level': [get_alert_level(f) for f in ftrt_values],
        'x_class': [True] * len(dates)
    })
    
    # Ejecutar análisis completo
    analysis_results = run_complete_analysis(results_df)
