import streamlit as st
import pandas as pd

# Configuração da página com tema de luxo
st.set_page_config(
    page_title="Perfume Premium Finder",
    page_icon="✨",
    layout="wide"
)

# Estilização global - Identidade visual baseada em Ouro, Champagne e Brilho Estúdio
st.markdown("""
    <style>
    /* Fundo da aplicação num tom escuro arroxeado/luxuoso */
    .stApp {
        background: radial-gradient(circle at 50% 50%, #1e152a 0%, #0b0711 100%);
    }
    
    /* Títulos e Subtítulos em tons de Ouro e Champagne */
    h1 {
        color: #f3e5ab; 
        font-family: 'Playfair Display', 'Georgia', serif; 
        font-weight: 700;
        text-shadow: 0px 0px 12px rgba(243, 229, 171, 0.4);
        text-align: center;
    }
    h3, p, span {
        font-family: 'Montserrat', sans-serif;
    }
    
    /* Cards dos Perfumes - Efeito Glassmorphism Dourado/Champagne */
    .perfume-card {
        border: 1px solid rgba(212, 175, 55, 0.3);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 10px;
        background: rgba(30, 21, 42, 0.6);
        backdrop-filter: blur(8px);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        transition: all 0.3s ease-in-out;
    }
    .perfume-card:hover {
        transform: translateY(-6px);
        border-color: rgba(212, 175, 55, 0.8);
        box-shadow: 0 12px 40px 0 rgba(212, 175, 55, 0.2);
    }
    
    /* Tags de Família Olfativa em Rosa Champagne */
    .tag {
        background: linear-gradient(135deg, #ffb7b2 0%, #e8a598 100%);
        color: #1e152a;
        padding: 4px 12px;
        border-radius: 30px;
        font-size: 11px;
        font-weight: bold;
        letter-spacing: 0.5px;
    }
    
    /* Customizando os botões padrão do Streamlit para combinar com o tema */
    div.stButton > button {
        background: linear-gradient(135deg, #e8a598 0%, #d4af37 100%) !important;
        color: #1e152a !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 8px !important;
        transition: all 0.2s ease;
    }
    div.stButton > button:hover {
        transform: scale(1.03);
        box-shadow: 0px 0px 15px rgba(232, 165, 152, 0.6) !important;
    }
    </style>
""", unsafe_allow_html=True)

# Dados dos perfumes com links de imagens placeholder (substitua pelas suas imagens reais se quiser)
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

# Cabeçalho principal estilizado
st.markdown("<h1>✨ PERFUME STUDIO PREMIUM</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #dfd5c6; font-size: 16px;'>Descubra o aroma que traduz o seu luxo e personalidade</p>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Barra lateral para filtros
st.sidebar.header("👑 Seletor de Luxo")

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

# Grid principal
st.markdown(f"<h3 style='color: #f3e5ab;'>🛍️ Coleção Selecionada ({len(df_filtrado)})</h3>", unsafe_allow_html=True)

if df_filtrado.empty:
    st.warning("Nenhum perfume encontrado com os filtros selecionados. Tente ajustar suas preferências!")
else:
    cols = st.columns(3)
    
    for index, row in df_filtrado.reset_index().iterrows():
        with cols[index % 3]:
            # Container com design elegante de estúdio de fotografia
            st.markdown(
                f"""
                <div class="perfume-card">
                    <h3 style="margin-top:0; color:#f3e5ab; font-family:'Playfair Display', serif;">{row['Nome']}</h3>
                    <p style="color:#d0c4b4; margin-bottom:15px; font-size: 13px;"><strong>MARCA:</strong> {row['Marca'].upper()}</p>
                    <p style="margin-bottom:15px;"><span class="tag">{row['Familia'].upper()}</span></p>
                    <p style="color:#e2e8f0; font-size:14px;"><strong>Ocasião:</strong> {row['Ocasiao']}</p>
                    <p style="color:#cbd5e0; font-size:14px; min-height:45px;"><strong>Notas de topo:</strong> <em>{row['Nota']}</em></p>
                    <h2 style="color:#d4af37; margin-top:15px; margin-bottom:0px; font-family: 'Playfair Display', serif;">R$ {row['Preco']},00</h2>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            # Imagem do perfume perfeitamente integrada
            st.image(row['Imagem'], use_container_width=True)
            
            if st.button(f"Explorar Fragrância", key=f"btn_{row['Nome']}"):
                st.info(f"Notas exclusivas de {row['Nome']}. Ideal para destacar sua presença em momentos como {row['Ocasiao']}.")
            st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("<hr style='border-color: rgba(212, 175, 55, 0.2);'>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #f3e5ab; text-align: center;'>✨ Deseja uma consultoria sob medida?</h3>", unsafe_allow_html=True)
c_button = st.columns([1,2,1])
with c_button[1]:
    if st.button("Iniciar Quiz da Assinatura Olfativa", use_container_width=True):
        st.balloons()
        st.success("Perfeito! Em breve liberaremos o questionário personalizado de alta perfumaria.")
