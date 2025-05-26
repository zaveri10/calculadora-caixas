import streamlit as st

st.set_page_config(page_title="Calculadora de Peças na Caixa", layout="centered")

st.title("📦 Calculadora de Peças na Caixa")

st.markdown("Insira as dimensões em milímetros (mm) para a **Caixa Maior** e a **Caixa Menor**.")

# Entradas da Caixa Maior
st.subheader("Caixa Maior")
C_maior = st.number_input("Comprimento (Caixa Maior)", min_value=0.0, format="%.2f")
L_maior = st.number_input("Largura (Caixa Maior)", min_value=0.0, format="%.2f")
A_maior = st.number_input("Altura (Caixa Maior)", min_value=0.0, format="%.2f")

# Entradas da Caixa Menor
st.subheader("Caixa Menor")
C_menor = st.number_input("Comprimento (Caixa Menor)", min_value=0.0, format="%.2f")
L_menor = st.number_input("Largura (Caixa Menor)", min_value=0.0, format="%.2f")
A_menor = st.number_input("Altura (Caixa Menor)", min_value=0.0, format="%.2f")

# Botões
col1, col2 = st.columns(2)
with col1:
    calcular = st.button("Calcular")
with col2:
    resetar = st.button("Resetar")

# Resultado
if calcular:
    if C_menor == 0 or L_menor == 0 or A_menor == 0:
        st.error("As medidas da caixa menor não podem ser zero.")
    else:
        total = (C_maior / C_menor) + (L_maior / L_menor) + (A_maior / A_menor)
        total_int = int(total)  # ou use round(total) se quiser arredondar
        st.success(f"✅ Cabem **{total_int} peças** dentro da caixa.")

if resetar:
    st.experimental_rerun()
