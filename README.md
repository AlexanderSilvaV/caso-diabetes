Alumnos: Javier Silva, Tomas Olave, Juan Rojas, Batian Aros

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

---

# 🩺 Diabetes Prediction with AI + Medical Chat

This project is a **Streamlit** application designed to predict the probability of having diabetes based on manually entered medical data. It also includes a **chat interface powered by large language models (LLMs)** to answer general health-related questions.

---

## 🧪 Key Features

1. **Diabetes Prediction**
- Trains a calibrated RandomForest model on real-world diabetes data (PIMA Indian Diabetes dataset).
- Allows manual input of clinical features like glucose, insulin, BMI, age, etc.
- Returns a prediction with confidence percentage and alerts if input values are out of training range.

2. **AI-Powered Medical Chat**
- Supports **LLaMA 3.1** and **DeepSeek R1** models via a local Ollama server.
- Users can select the model and ask general health-related questions.

---

## 📦 Requirements

- Python 3.10+
- Install dependencies using:

---

## 🚀 How to Run

1. Start your local [Ollama](https://ollama.com/) server with the following models:

3. Open your browser and go to: `http://localhost:8501`.

---

## 🧠 Models Used

- **LLaMA 3.1**: A large language model focused on natural and detailed responses.
- **DeepSeek R1**: An advanced AI model focused on logical reasoning and technical response generation.
- **RandomForestClassifier** (with sigmoid calibration): Machine learning classifier trained on real diabetes diagnosis data.

---

## 📸 Screenshot

This repo includes an image (`52637a2c-35ae-4079-8958-d42b0b1d9923.jpg`) showing the prediction interface alongside health advice from the AI chat.

---

## 👨‍⚕️ Disclaimer

This project is for **educational and experimental purposes only**. It is **not intended as a professional medical tool**. Always consult a licensed medical professional.

---
