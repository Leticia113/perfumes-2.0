import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="Perfume Finder 2026",
    page_icon="✨",
    layout="wide"
)

# Estilização global para melhorar o visual
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    h1 { color: #f8f9fa; font-family: 'Helvetica Neue', sans-serif; font-weight: 700; }
    h3 { color: #ced4da; }
    .perfume-card {
        border: 1px solid #2d3748;
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 20px;
        background-color: #1a202c;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s;
    }
    .perfume-card:hover {
        transform: translateY(-4px);
        border-color: #4a5568;
    }
    .tag {
        background-color: #2b6cb0;
        color: white;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Dados dos perfumes com links de imagens (Substitua as URLs pelas suas imagens se quiser)
@st.cache_data
def carregar_dados():
    perfumes = [
        {
            "Nome": "Bleu de Chanel", "Marca": "Chanel", "Familia": "Amadeirado", "Ocasiao": "Noite / Formal", "Preco": 890, "Nota": "Citros, Incenso, Cedro",
            "Imagem": "https://unsplash.com"
        },
        {
            "Nome": "Sauvage", "Marca": "Dior", "Familia": "Fougère / Aromático", "Ocasiao": "Versátil", "Preco": 750, "Nota": "Bergamota, Pimenta, Ambroxan",
            "Imagem": "https://unsplash.com"
        },
        {
            "Nome": "La Vie Est Belle", "Marca": "Lancôme", "Familia": "Floral / Doces", "Ocasiao": "Casual / Noite", "Preco": 680, "Nota": "Íris, Jasmim, Baunilha",
            "Imagem": "https://unsplash.com"
        },
        {
            "Nome": "Acqua di Giò", "Marca": "Giorgio Armani", "Familia": "Cítrico / Aquático", "Ocasiao": "Dia / Verão", "Preco": 620, "Nota": "Notas Marinhas, Limão, Alecrim",
            "Imagem": "https://unsplash.com"
        },
        {
            "Nome": "Good Girl", "Marca": "Carolina Herrera", "Familia": "Oriental", "Ocasiao": "Noite / Balada", "Preco": 720, "Nota": "Amêndoa, Café, Jasmim, Cacau",
            "Imagem": "https://unsplash.com"
        },
        {
            "Nome": "Light Blue", "Marca": "Dolce & Gabbana", "Familia": "Cítrico / Floral", "Ocasiao": "Dia / Verão", "Preco": 550, "Nota": "Maçã Verde, Bambu, Limão Siciliano",
            "Imagem": "https://unsplash.com"
        }
    ]
    return pd.DataFrame(perfumes)

df = carregar_dados()

# Cabeçalho principal
st.title("✨ Perfume Finder 2026")
st.subheader("Encontre a fragrância perfeita para a sua assinatura olfativa")
st.markdown("---")

# Barra lateral para filtros
st.sidebar.header("🔍 Filtre Suas Preferências")

familias = ["Todas"] + list(df["Familia"].unique())
familia_selecionada = st.sidebar.selectbox("Família Olfativa", familias)

ocasioes = ["Todas"] + ["Dia / Verão", "Versátil", "Noite / Formal", "Noite / Balada", "Casual / Noite"]
ocasiao_selecionada = st.sidebar.selectbox("Ocasião de Uso", ocasioes)

preco_max = st.sidebar.slider("Preço Máximo (R$)", min_value=500, max_value=1000, value=1000, step=50)

# Aplicar filtros
df_filtrado = df[df["Preco"] <= preco_max]

if familia_selecionada != "Todas":
    df_filtrado = df_filtrado[df_filtrado["Familia"] == familia_selecionada]

if ocasiao_selecionada != "Todas":
    df_filtrado = df_filtrado[df_filtrado["Ocasiao"].str.contains(ocasiao_selecionada, na=False)]

# Exibição dos cards
st.write(f"### 🛍️ Fragrâncias Recomendadas ({len(df_filtrado)})")

if df_filtrado.empty:
    st.warning("Nenhum perfume encontrado com os filtros selecionados. Tente ajustar suas preferências na barra lateral!")
else:
    cols = st.columns(3)
    
    for index, row in df_filtrado.reset_index().iterrows():
        with cols[index % 3]:
            # Container estilizado para modo escuro
            st.markdown(
                f"""
                <div class="perfume-card">
                    <h3 style="margin-top:0; color:#fff;">{row['Nome']}</h3>
                    <p style="color:#a0aec0; margin-bottom:15px;"><strong>Marca:</strong> {row['Marca']}</p>
                    <p style="margin-bottom:10px;"><span class="tag">{row['Familia']}</span></p>
                    <p style="color:#e2e8f0; font-size:14px;"><strong>Ocasião:</strong> {row['Ocasiao']}</p>
                    <p style="color:#cbd5e0; font-size:14px; min-height:40px;"><strong>Notas:</strong> <em>{row['Nota']}</em></p>
                    <h2 style="color:#48bb78; margin-top:15px; margin-bottom:15px;">R$ {row['Preco']},00</h2>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            # Exibe a imagem logo abaixo do card (com largura ajustada à coluna)
            st.image(row['Imagem'], use_container_width=True)
            
            if st.button(f"Ver Detalhes", key=f"btn_{row['Nome']}"):
                st.info(f"Você selecionou o {row['Nome']} ({row['Marca']}). Perfeito para {row['Ocasiao']}!")
            st.markdown("<br>", unsafe_allow_html=True)

st.markdown("---")
st.write("### 🧠 Não sabe o que escolher?")
if st.button("✨ Fazer o Quiz de Assinatura Olfativa"):
    st.balloons()
    st.success("Quiz em desenvolvimento! Em breve você poderá descobrir o perfume ideal para o seu perfil.")
