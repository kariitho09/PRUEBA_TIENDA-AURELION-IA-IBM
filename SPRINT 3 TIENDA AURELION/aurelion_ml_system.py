#!/usr/bin/env python3
"""
Sistema de Machine Learning para Tienda Aurelion
Implementación en Python con scikit-learn

Este archivo implementa los mismos algoritmos que el sistema TypeScript
pero utilizando las librerías estándar de Python para ML.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, accuracy_score, confusion_matrix
import json
from datetime import datetime, timedelta
import random

# Configurar estilo de gráficos
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

class AurelionMLSystem:
    def __init__(self):
        self.products_data = self.generate_products_data()
        self.sales_data = self.generate_sales_data()
        self.ml_data = None
        self.X_train = None
        self.X_test = None
        self.y_train_reg = None
        self.y_test_reg = None
        self.y_train_class = None
        self.y_test_class = None
        self.scaler = StandardScaler()
        self.label_encoder = LabelEncoder()
        
    def generate_products_data(self):
        """Generar datos sintéticos de productos"""
        products = [
            {"id": 1, "name": "Smartphone Galaxy Pro", "category": "Electrónicos", "price": 899.99, "stock": 45, "rating": 4.5, "reviews": 234, "brand": "TechCorp"},
            {"id": 2, "name": "Laptop Gaming Elite", "category": "Electrónicos", "price": 1299.99, "stock": 23, "rating": 4.8, "reviews": 156, "brand": "GameTech"},
            {"id": 3, "name": "Auriculares Bluetooth", "category": "Electrónicos", "price": 199.99, "stock": 78, "rating": 4.3, "reviews": 445, "brand": "AudioMax"},
            {"id": 4, "name": "Camiseta Deportiva", "category": "Ropa", "price": 29.99, "stock": 120, "rating": 4.2, "reviews": 89, "brand": "SportWear"},
            {"id": 5, "name": "Zapatillas Running", "category": "Ropa", "price": 129.99, "stock": 67, "rating": 4.6, "reviews": 312, "brand": "RunFast"},
            {"id": 6, "name": "Cafetera Automática", "category": "Hogar", "price": 249.99, "stock": 34, "rating": 4.4, "reviews": 178, "brand": "CoffeeMax"},
            {"id": 7, "name": "Aspiradora Robot", "category": "Hogar", "price": 399.99, "stock": 28, "rating": 4.7, "reviews": 267, "brand": "CleanBot"},
            {"id": 8, "name": "Libro de Cocina", "category": "Libros", "price": 24.99, "stock": 89, "rating": 4.1, "reviews": 56, "brand": "Editorial Gourmet"},
            {"id": 9, "name": "Novela Bestseller", "category": "Libros", "price": 19.99, "stock": 156, "rating": 4.5, "reviews": 423, "brand": "Editorial Moderna"},
            {"id": 10, "name": "Suplemento Vitamínico", "category": "Salud", "price": 34.99, "stock": 95, "rating": 4.3, "reviews": 134, "brand": "HealthPlus"}
        ]
        return pd.DataFrame(products)
    
    def generate_sales_data(self):
        """Generar datos sintéticos de ventas"""
        np.random.seed(42)  # Para reproducibilidad
        sales = []
        seasons = ['Primavera', 'Verano', 'Otoño', 'Invierno']
        days_of_week = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
        genders = ['M', 'F']
        
        for i in range(1, 1001):
            product = self.products_data.sample(1).iloc[0]
            quantity = np.random.randint(1, 6)
            discount = np.random.random() * 0.2 if np.random.random() < 0.3 else 0
            total_amount = product['price'] * quantity * (1 - discount)
            
            sale = {
                'id': i,
                'product_id': product['id'],
                'quantity': quantity,
                'date': (datetime(2024, 1, 1) + timedelta(days=np.random.randint(0, 365))).strftime('%Y-%m-%d'),
                'customer_age': np.random.randint(18, 69),
                'customer_gender': np.random.choice(genders),
                'season': np.random.choice(seasons),
                'day_of_week': np.random.choice(days_of_week),
                'total_amount': total_amount,
                'discount': discount
            }
            sales.append(sale)
        
        return pd.DataFrame(sales)
    
    def prepare_ml_data(self):
        """Preparar datos para machine learning"""
        # Unir datos de productos y ventas
        ml_data = self.sales_data.merge(self.products_data, left_on='product_id', right_on='id', suffixes=('_sale', '_product'))
        
        # Codificar variables categóricas
        season_encoder = {'Primavera': 0, 'Verano': 1, 'Otoño': 2, 'Invierno': 3}
        day_encoder = {'Lunes': 0, 'Martes': 1, 'Miércoles': 2, 'Jueves': 3, 'Viernes': 4, 'Sábado': 5, 'Domingo': 6}
        category_encoder = {'Electrónicos': 0, 'Ropa': 1, 'Hogar': 2, 'Libros': 3, 'Salud': 4}
        
        ml_data['season_encoded'] = ml_data['season'].map(season_encoder)
        ml_data['day_encoded'] = ml_data['day_of_week'].map(day_encoder)
        ml_data['category_encoded'] = ml_data['category'].map(category_encoder)
        
        # Seleccionar features
        features = ['price', 'stock', 'rating', 'reviews', 'customer_age', 'discount', 
                   'season_encoded', 'day_encoded', 'category_encoded']
        
        X = ml_data[features]
        y_regression = ml_data['total_amount']
        y_classification = ml_data['category']
        
        self.ml_data = ml_data
        return X, y_regression, y_classification
    
    def split_data(self, X, y_reg, y_class):
        """Dividir datos en entrenamiento y prueba"""
        # División para regresión
        self.X_train, self.X_test, self.y_train_reg, self.y_test_reg = train_test_split(
            X, y_reg, test_size=0.2, random_state=42
        )
        
        # División para clasificación (mismos índices)
        _, _, self.y_train_class, self.y_test_class = train_test_split(
            X, y_class, test_size=0.2, random_state=42
        )
        
        # Normalizar features
        self.X_train_scaled = self.scaler.fit_transform(self.X_train)
        self.X_test_scaled = self.scaler.transform(self.X_test)
    
    def train_regression_model(self):
        """Entrenar modelo de regresión lineal"""
        self.regression_model = LinearRegression()
        self.regression_model.fit(self.X_train_scaled, self.y_train_reg)
        
        # Predicciones
        y_pred_reg = self.regression_model.predict(self.X_test_scaled)
        
        # Métricas
        mse = mean_squared_error(self.y_test_reg, y_pred_reg)
        rmse = np.sqrt(mse)
        mae = mean_absolute_error(self.y_test_reg, y_pred_reg)
        r2 = r2_score(self.y_test_reg, y_pred_reg)
        
        return {
            'predictions': y_pred_reg,
            'actual': self.y_test_reg.values,
            'mse': mse,
            'rmse': rmse,
            'mae': mae,
            'r2': r2
        }
    
    def train_classification_model(self):
        """Entrenar modelo de clasificación KNN"""
        self.classification_model = KNeighborsClassifier(n_neighbors=5)
        self.classification_model.fit(self.X_train_scaled, self.y_train_class)
        
        # Predicciones
        y_pred_class = self.classification_model.predict(self.X_test_scaled)
        
        # Métricas
        accuracy = accuracy_score(self.y_test_class, y_pred_class)
        conf_matrix = confusion_matrix(self.y_test_class, y_pred_class)
        
        return {
            'predictions': y_pred_class,
            'actual': self.y_test_class.values,
            'accuracy': accuracy,
            'confusion_matrix': conf_matrix
        }
    
    def create_visualizations(self, reg_results, class_results):
        """Crear visualizaciones de los resultados"""
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        fig.suptitle('Tienda Aurelion - Resultados de Machine Learning', fontsize=16, fontweight='bold')
        
        # 1. Predicciones vs Valores Reales (Regresión)
        axes[0, 0].scatter(reg_results['actual'], reg_results['predictions'], alpha=0.6, color='blue')
        axes[0, 0].plot([reg_results['actual'].min(), reg_results['actual'].max()], 
                       [reg_results['actual'].min(), reg_results['actual'].max()], 'r--', lw=2)
        axes[0, 0].set_xlabel('Valores Reales')
        axes[0, 0].set_ylabel('Predicciones')
        axes[0, 0].set_title('Regresión: Predicciones vs Reales')
        axes[0, 0].grid(True, alpha=0.3)
        
        # 2. Residuos
        residuals = reg_results['actual'] - reg_results['predictions']
        axes[0, 1].scatter(reg_results['predictions'], residuals, alpha=0.6, color='green')
        axes[0, 1].axhline(y=0, color='r', linestyle='--')
        axes[0, 1].set_xlabel('Predicciones')
        axes[0, 1].set_ylabel('Residuos')
        axes[0, 1].set_title('Análisis de Residuos')
        axes[0, 1].grid(True, alpha=0.3)
        
        # 3. Distribución de errores
        axes[0, 2].hist(residuals, bins=20, alpha=0.7, color='orange', edgecolor='black')
        axes[0, 2].set_xlabel('Residuos')
        axes[0, 2].set_ylabel('Frecuencia')
        axes[0, 2].set_title('Distribución de Errores')
        axes[0, 2].grid(True, alpha=0.3)
        
        # 4. Matriz de Confusión
        sns.heatmap(class_results['confusion_matrix'], annot=True, fmt='d', 
                   xticklabels=np.unique(class_results['actual']),
                   yticklabels=np.unique(class_results['actual']),
                   ax=axes[1, 0], cmap='Blues')
        axes[1, 0].set_title('Matriz de Confusión')
        axes[1, 0].set_xlabel('Predicciones')
        axes[1, 0].set_ylabel('Valores Reales')
        
        # 5. Ventas por Categoría
        category_sales = self.ml_data.groupby('category')['total_amount'].sum().sort_values(ascending=False)
        axes[1, 1].bar(category_sales.index, category_sales.values, color='skyblue', edgecolor='navy')
        axes[1, 1].set_title('Ventas Totales por Categoría')
        axes[1, 1].set_xlabel('Categoría')
        axes[1, 1].set_ylabel('Ventas Totales ($)')
        axes[1, 1].tick_params(axis='x', rotation=45)
        
        # 6. Distribución de Ratings vs Ventas
        product_sales = self.ml_data.groupby(['name', 'rating'])['total_amount'].sum().reset_index()
        scatter = axes[1, 2].scatter(product_sales['rating'], product_sales['total_amount'], 
                                   alpha=0.6, s=60, color='purple')
        axes[1, 2].set_xlabel('Rating del Producto')
        axes[1, 2].set_ylabel('Ventas Totales ($)')
        axes[1, 2].set_title('Rating vs Ventas')
        axes[1, 2].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('aurelion_ml_results.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        return fig
    
    def generate_report(self, reg_results, class_results):
        """Generar reporte completo de resultados"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'dataset_info': {
                'total_products': len(self.products_data),
                'total_sales': len(self.sales_data),
                'training_samples': len(self.X_train),
                'test_samples': len(self.X_test)
            },
            'regression_metrics': {
                'mse': float(reg_results['mse']),
                'rmse': float(reg_results['rmse']),
                'mae': float(reg_results['mae']),
                'r2_score': float(reg_results['r2'])
            },
            'classification_metrics': {
                'accuracy': float(class_results['accuracy']),
                'confusion_matrix': class_results['confusion_matrix'].tolist()
            },
            'business_insights': {
                'top_selling_category': self.ml_data.groupby('category')['total_amount'].sum().idxmax(),
                'average_order_value': float(self.ml_data['total_amount'].mean()),
                'total_revenue': float(self.ml_data['total_amount'].sum()),
                'best_rated_products': self.products_data.nlargest(3, 'rating')[['name', 'rating']].to_dict('records')
            }
        }
        
        # Guardar reporte en JSON
        with open('aurelion_ml_report.json', 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        return report
    
    def run_complete_analysis(self):
        """Ejecutar análisis completo de ML"""
        print("🚀 Iniciando análisis de Machine Learning para Tienda Aurelion")
        print("=" * 60)
        
        # 1. Preparar datos
        print("📊 Preparando datos...")
        X, y_reg, y_class = self.prepare_ml_data()
        print(f"   ✓ Datos preparados: {len(X)} muestras, {len(X.columns)} características")
        
        # 2. Dividir datos
        print("🔄 Dividiendo datos en entrenamiento y prueba...")
        self.split_data(X, y_reg, y_class)
        print(f"   ✓ Entrenamiento: {len(self.X_train)} muestras")
        print(f"   ✓ Prueba: {len(self.X_test)} muestras")
        
        # 3. Entrenar modelo de regresión
        print("🤖 Entrenando modelo de regresión...")
        reg_results = self.train_regression_model()
        print(f"   ✓ RMSE: {reg_results['rmse']:.2f}")
        print(f"   ✓ MAE: {reg_results['mae']:.2f}")
        print(f"   ✓ R²: {reg_results['r2']:.3f}")
        
        # 4. Entrenar modelo de clasificación
        print("🎯 Entrenando modelo de clasificación...")
        class_results = self.train_classification_model()
        print(f"   ✓ Precisión: {class_results['accuracy']:.3f} ({class_results['accuracy']*100:.1f}%)")
        
        # 5. Crear visualizaciones
        print("📈 Generando visualizaciones...")
        self.create_visualizations(reg_results, class_results)
        print("   ✓ Gráficos guardados como 'aurelion_ml_results.png'")
        
        # 6. Generar reporte
        print("📋 Generando reporte completo...")
        report = self.generate_report(reg_results, class_results)
        print("   ✓ Reporte guardado como 'aurelion_ml_report.json'")
        
        print("\\n🎉 ¡Análisis completado exitosamente!")
        print("=" * 60)
        
        return reg_results, class_results, report

def main():
    """Función principal"""
    # Crear instancia del sistema ML
    ml_system = AurelionMLSystem()
    
    # Ejecutar análisis completo
    reg_results, class_results, report = ml_system.run_complete_analysis()
    
    # Mostrar resumen de resultados
    print("\\n📊 RESUMEN DE RESULTADOS:")
    print("-" * 40)
    print(f"🔢 Modelo de Regresión:")
    print(f"   • Error cuadrático medio (RMSE): {reg_results['rmse']:.2f}")
    print(f"   • Error absoluto medio (MAE): {reg_results['mae']:.2f}")
    print(f"   • Coeficiente de determinación (R²): {reg_results['r2']:.3f}")
    
    print(f"\\n🎯 Modelo de Clasificación:")
    print(f"   • Precisión: {class_results['accuracy']*100:.1f}%")
    
    print(f"\\n💼 Insights de Negocio:")
    print(f"   • Categoría más vendida: {report['business_insights']['top_selling_category']}")
    print(f"   • Valor promedio de orden: ${report['business_insights']['average_order_value']:.2f}")
    print(f"   • Ingresos totales: ${report['business_insights']['total_revenue']:,.2f}")
    
    return ml_system, reg_results, class_results, report

if __name__ == "__main__":
    # Ejecutar análisis
    ml_system, reg_results, class_results, report = main()
    
    print("\\n🔍 Para ver los gráficos, abra el archivo 'aurelion_ml_results.png'")
    print("📄 Para ver el reporte completo, abra el archivo 'aurelion_ml_report.json'")