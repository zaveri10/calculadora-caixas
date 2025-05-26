import streamlit as st

st.set_page_config(page_title="Calculadora de Peças na Caixa", layout="centered")

st.title("📦 Calculadora de Peças na Caixa")
st.markdown("Insira as dimensões em milímetros (mm) para a **Caixa Maior** e a **Caixa Menor**.")

# Função segura para converter string para float
def safe_float(value):
    try:
        return float(value.replace(",", "."))
    except:
        return None

# Entradas da Caixa Maior
st.subheader("Caixa Maior")
C_maior = safe_float(st.text_input("Comprimento (Caixa Maior)", placeholder="Ex: 100"))
L_maior = safe_float(st.text_input("Largura (Caixa Maior)", placeholder="Ex: 50"))
A_maior = safe_float(st.text_input("Altura (Caixa Maior)", placeholder="Ex: 30"))

# Entradas da Caixa Menor
st.subheader("Caixa Menor")
C_menor = safe_float(st.text_input("Comprimento (Caixa Menor)", placeholder="Ex: 10"))
L_menor = safe_float(st.text_input("Largura (Caixa Menor)", placeholder="Ex: 5"))
A_menor = safe_float(st.text_input("Altura (Caixa Menor)", placeholder="Ex: 3"))

# Botões
col1, col2 = st.columns(2)
with col1:
    calcular = st.button("Calcular")
with col2:
    resetar = st.button("Resetar")

# Cálculo
if calcular:
    campos = [C_maior, L_maior, A_maior, C_menor, L_menor, A_menor]

    if None in campos:
        st.error("⚠️ Por favor, preencha todos os campos com números válidos.")
    elif C_menor == 0 or L_menor == 0 or A_menor == 0:
        st.error("🚫 As medidas da caixa menor não podem ser zero.")
    else:
        total = (C_maior / C_menor) + (L_maior / L_menor) + (A_maior / A_menor)
        st.success(f"✅ Cabem **{int(total)} peças** dentro da caixa.")

if resetar:
    st.experimental_rerun()
