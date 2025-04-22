from langchain_community.llms import Ollama  
import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.calibration import CalibratedClassifierCV
from sklearn.metrics import classification_report
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import numpy as np

# --- 1. LLM Selector ---
model_selected = st.sidebar.selectbox(
    "Selecciona el modelo IA",
    ("llama3.1:latest", "deepseek-r1:latest")
)
llm = Ollama(model=model_selected, base_url="http://localhost:11434", verbose=True)

# --- 2. Carga y limpieza del dataset ---
df = pd.read_csv("c:/Users/rojas/Desktop/ollama/ollama-langchain-main/diabetes.csv")

# Reemplazar ceros por la mediana en columnas que NO deberían tener cero
features_to_fix = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
for feature in features_to_fix:
    df[feature] = df[feature].replace(0, df[feature].median())

X = df.drop("Outcome", axis=1)
y = df["Outcome"]

# Escalado
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Entrenamiento y calibración
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

rf_base = RandomForestClassifier(n_estimators=200, max_depth=7, random_state=42)
rf_calibrated = CalibratedClassifierCV(rf_base, method='sigmoid', cv=5)
rf_calibrated.fit(X_train, y_train)

# --- 3. Interfaz para predicción ---
st.sidebar.title("Predicción de Diabetes")

with st.sidebar.form("predict_form"):
    Pregnancies = st.number_input("Embarazos", 0, 20)
    Glucose = st.number_input("Glucosa", 0, 300)
    BloodPressure = st.number_input("Presión Sanguínea", 0, 200)
    SkinThickness = st.number_input("Grosor de piel", 0, 100)
    Insulin = st.number_input("Insulina", 0, 900)
    BMI = st.number_input("IMC (BMI)", 0.0, 70.0)
    DiabetesPedigreeFunction = st.number_input("Historial Familiar (DPF)", 0.0, 3.0)
    Age = st.number_input("Edad", 1, 120)

    submitted = st.form_submit_button("Predecir")

    if submitted:
        user_input = [[Pregnancies, Glucose, BloodPressure, SkinThickness,
                       Insulin, BMI, DiabetesPedigreeFunction, Age]]
        
        input_scaled = scaler.transform(user_input)
        prediction = rf_calibrated.predict(input_scaled)[0]
        proba = rf_calibrated.predict_proba(input_scaled)[0][1]

        # Clasificación final
        result = "✅ Positivo (diabetes)" if prediction == 1 else "❌ Negativo (sin diabetes)"
        st.sidebar.success(f"Resultado: {result} — Confianza: {round(proba * 100, 2)}%")

        # Alerta por valores fuera del rango del dataset
        X_ranges = pd.DataFrame(X).agg(["min", "max"])
        warnings = []
        for i, (val, name) in enumerate(zip(user_input[0], X.columns)):
            if val < X_ranges.loc["min", name] or val > X_ranges.loc["max", name]:
                warnings.append(f"⚠️ *{name}* está fuera del rango observado ({int(X_ranges.loc['min', name])}–{int(X_ranges.loc['max', name])})")

        if warnings:
            st.sidebar.warning("Valores fuera del rango del dataset:")
            for w in warnings:
                st.sidebar.markdown(w)

# --- 4. Chat IA ---
st.title("🩺 Uso Médico - Chat con IA")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": f"Modelo seleccionado: {model_selected}. Puedes preguntarme sobre salud o temas médicos relacionados."}
    ]

if prompt := st.chat_input("Tu pregunta"): 
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: 
    with st.chat_message(message["role"]):
        st.write(message["content"])

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            response = llm.invoke(prompt)
            st.write(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
