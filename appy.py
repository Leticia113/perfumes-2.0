import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="Perfume Finder 2026",
    page_icon="✨",
    layout="wide"
)

# Dados simulados de perfumes
@st.cache_data
def carregar_dados():
    perfumes = [
        {"Nome": "Bleu de Chanel", "Marca": "Chanel", "Familia": "Amadeirado", "Ocasiao": "Noite / Formal", "Preco": 890, "Nota": "Citros, Incenso, Cedro"},
        {"Nome": "Sauvage", "Marca": "Dior", "Familia": "Fougère / Aromático", "Ocasiao": "Versátil", "Preco": 750, "Nota": "Bergamota, Pimenta, Ambroxan"},
        {"Nome": "La Vie Est Belle", "Marca": "Lancôme", "Familia": "Floral / Doces", "Ocasiao": "Casual / Noite", "Preco": 680, "Nota": "Íris, Jasmim, Baunilha"},
        {"Nome": "Acqua di Giò", "Marca": "Giorgio Armani", "Familia": "Cítrico / Aquático", "Ocasiao": "Dia / Verão", "Preco": 620, "Nota": "Notas Marinhas, Limão, Alecrim"},
        {"Nome": "Good Girl", "Marca": "Carolina Herrera", "Familia": "Oriental", "Ocasiao": "Noite / Balada", "Preco": 720, "Nota": "Amêndoa, Café, Jasmim, Cacau"},
        {"Nome": "Light Blue", "Marca": "Dolce & Gabbana", "Familia": "Cítrico / Floral", "Ocasiao": "Dia / Verão", "Preco": 550, "Nota": "Maçã Verde, Bambu, Limão Siciliano"}
    ]
    return pd.DataFrame(perfumes)

df = carregar_dados()

# Cabeçalho principal
st.title("✨ Perfume Finder 2026")
st.subheader("Encontre a fragrância perfeita para a sua assinatura olfativa")
st.markdown("---")

# Barra lateral para filtros (Sidebar)
st.sidebar.header("🔍 Filtre Suas Preferências")

# 1. Filtro por Família Olfativa
familias = ["Todas"] + list(df["Familia"].unique())
familia_selecionada = st.sidebar.selectbox("Família Olfativa", familias)

# 2. Filtro por Ocasião
ocasioes = ["Todas"] + ["Dia / Verão", "Versátil", "Noite / Formal", "Noite / Balada", "Casual / Noite"]
ocasiao_selecionada = st.sidebar.selectbox("Ocasião de Uso", ocasioes)

# 3. Filtro por Preço Máximo
preco_max = st.sidebar.slider("Preço Máximo (R$)", min_value=500, max_value=1000, value=1000, step=50)

# Aplicar os filtros ao DataFrame
df_filtrado = df[df["Preco"] <= preco_max]

if familia_selecionada != "Todas":
    df_filtrado = df_filtrado[df_filtrado["Familia"] == familia_selecionada]

if ocasiao_selecionada != "Todas":
    df_filtrado = df_filtrado[df_filtrado["Ocasiao"].str.contains(ocasiao_selecionada, na=False)]

# Área de Exibição dos Perfumes Recomendados
st.write(f"### 🛍️ Fragrâncias Recomendadas ({len(df_filtrado)})")

if df_filtrado.empty:
    st.warning("Nenhum perfume encontrado com os filtros selecionados. Tente ajustar suas preferências na barra lateral!")
else:
    # Criar um grid de colunas para os cards de perfumes
    cols = st.columns(3)
    
    for index, row in df_filtrado.iterrows():
        # Distribui os perfumes entre as colunas do grid
        with cols[index % 3]:
                        st.markdown(
                f"""
                <div style="border:1px solid #e6e6e6; border-radius:10px; padding:20px; margin-bottom:20px; background-color:#fafafa;">
                    <h4>{row['Nome']}</h4>
                    <p><strong>Marca:</strong> {row['Marca']}</p>
                    <p><strong>Família:</strong> <span style="background-color:#e1f5fe; padding:2px 8px; border-radius:5px;">{row['Familia']}</span></p>
                    <p><strong>Ocasião:</strong> {row['Ocasiao']}</p>
                    <p><strong>Notas principais:</strong> <em>{row['Nota']}</em></p>
                    <h3 style="color:#2e7d32;">R$ {row['Preco']},00</h3>
                </div>
                """,
                unsafe_allow_html=True
            )

            
            # Botão interativo do Streamlit para cada perfume
            if st.button(f"Ver Detalhes de {row['Nome']}", key=row['Nome']):
                st.info(f"Você selecionou {row['Nome']}. Adicione aqui redirecionamentos ou mais detalhes sobre as notas de coração e fundo!")

# Rodapé ou seção de Quiz
st.markdown("---")
st.write("### 🧠 Não sabe o que escolher?")
if st.button("✨ Fazer o Quiz de Assinatura Olfativa"):
    st.balloons()
    st.success("Quiz em desenvolvimento! Em breve você responderá a perguntas sobre sua personalidade para encontrar seu perfume ideal.")
