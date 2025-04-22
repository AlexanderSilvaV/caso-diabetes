Alumnos:
JAVIER SILVA
TOMAS OLAVES
JUAN ROJAS
NICOLAS AROS

# caso-diabetes

# Predicción de Diabetes con IA + Chat Médico

Este proyecto es una aplicación desarrollada en **Streamlit** que permite predecir la probabilidad de tener diabetes a partir de datos médicos ingresados manualmente. Además, incorpora un **chat asistido por modelos de lenguaje grandes (LLMs)** para resolver dudas médicas generales.

---

## 🧪 Funcionalidades Principales

1. **Predicción de Diabetes**
   - Entrenamiento de modelo RandomForest calibrado con un dataset real de diabetes (PIMA Indian Diabetes).
   - Entrada manual de variables clínicas como glucosa, insulina, IMC, edad, etc.
   - Resultado con porcentaje de confianza y alertas si los valores ingresados están fuera del rango de entrenamiento.

2. **Chat IA Médico**
   - Utiliza los modelos **LLaMA 3.1** y **DeepSeek R1** desde un servidor Ollama local.
   - Puedes seleccionar el modelo y consultar sobre temas de salud generales.

---

## 📦 Requisitos

- Python 3.10+
- `pip install -r requirements.txt` (debes crear este archivo con las siguientes librerías clave):




---

## 🚀 Cómo Ejecutar

1. Asegúrate de tener corriendo un servidor local de [Ollama](https://ollama.com/) con los modelos:



2. Ejecuta la app:



3. Accede en tu navegador a `http://localhost:8501`.

---

## 🧠 Modelos Utilizados

- **LLaMA 3.1**: Modelo de lenguaje grande orientado a respuestas naturales y detalladas.
- **DeepSeek R1**: Modelo IA avanzado con foco en razonamiento lógico y generación de respuestas técnicas.
- **RandomForestClassifier** (con calibración sigmoid): Clasificador de machine learning entrenado sobre datos reales de diagnóstico de diabetes.

---

## 📸 Captura de Pantalla

Se incluye una imagen (`52637a2c-35ae-4079-8958-d42b0b1d9923.jpg`) que muestra la interfaz de predicción junto con consejos de salud generados por el chat.

---

## 👨‍⚕️ Disclaimer

Este proyecto es solo para fines educativos y experimentales. **No debe usarse como herramienta médica profesional. Consulta siempre con un especialista.**

---

