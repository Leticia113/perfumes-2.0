import streamlit as st
import pandas as pd

# Configuração da página - Tema bem garota
st.set_page_config(
    page_title="Garota Perfumada 2026",
    page_icon="🌸",
    layout="wide"
)

# Estilização global - Estética Pink, Pastel, Dreamy e Coquette
st.markdown("""
    <style>
    /* Importando fontes delicadas e divertidas do Google Fonts */
    @import url('https://googleapis.com');
    
    /* Fundo degradê rosa pastel mágico e romântico */
    .stApp {
        background: linear-gradient(135deg, #ffe5ec 0%, #ffc2d1 50%, #fbc4ab 100%);
    }
    
    /* Títulos e textos com fontes fofas e arredondadas */
    h1 {
        color: #ff4d6d; 
        font-family: 'Fredoka', sans-serif; 
        font-weight: 700;
        text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.6);
        text-align: center;
        font-size: 3rem !important;
        margin-bottom: 5px !important;
    }
    h2, h3, h4, p, span, label {
        font-family: 'Quicksand', sans-serif !important;
        font-weight: 600 !important;
        color: #4a3b42 !important;
    }
    
    /* Cards dos Perfumes - Estilo Vidro Rosa Translúcido (Soft Coquette) */
    .perfume-card {
        border: 2px solid rgba(255, 255, 255, 0.6);
        border-radius: 20px;
        padding: 20px;
        margin-bottom: 15px;
        background: rgba(255, 255, 255, 0.55);
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 24px rgba(255, 182, 193, 0.3);
        transition: all 0.3s ease-in-out;
        display: flex;
        flex-direction: column;
    }
    .perfume-card:hover {
        transform: translateY(-8px);
        background: rgba(255, 255, 255, 0.75);
        border-color: #ff758f;
        box-shadow: 0 12px 30px rgba(255, 117, 143, 0.4);
    }
    
    /* Container para a imagem dentro do HTML com proporção bonita */
    .card-img-container {
        width: 100%;
        height: 200px;
        border-radius: 12px;
        overflow: hidden;
        margin-bottom: 15px;
    }
    .card-img-container img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    
    /* Tags de Família Olfativa em formato de pílula rosa chiclete */
    .tag {
        background: #ff758f;
        color: white !important;
        padding: 4px 12px;
        border-radius: 25px;
        font-size: 11px;
        font-weight: bold !important;
        letter-spacing: 0.5px;
        display: inline-block;
        box-shadow: 0 2px 8px rgba(255, 117, 143, 0.2);
    }
    
    /* Customizando os botões para ficarem super fofos e arredondados */
    div.stButton > button {
        background: linear-gradient(135deg, #ff758f 0%, #ff4d6d 100%) !important;
        color: white !important;
        font-family: 'Fredoka', sans-serif !important;
        font-size: 14px !important;
        border: none !important;
        border-radius: 50px !important;
        padding: 10px 24px !important;
        box-shadow: 0 4px 15px rgba(255, 77, 109, 0.3) !important;
        transition: all 0.2s ease;
    }
    div.stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0px 6px 20px rgba(255, 77, 109, 0.5) !important;
        background: linear-gradient(135deg, #ff8da1 0%, #ff5c7a 100%) !important;
    }
    
    /* Estilização da sidebar (Menu de Filtros) */
    [data-testid="stSidebar"] {
        background-color: rgba(255, 240, 245, 0.9) !important;
        border-right: 2px solid rgba(255, 182, 193, 0.4);
    }
    </style>
""", unsafe_allow_html=True)

# Dados com as imagens corrigidas e lindas que combinam com o tema rosa/pastel
@st.cache_data
def carregar_dados():
    perfumes = [
        {
            "Nome": "Bleu de Chanel", "Marca": "Chanel", "Familia": "Amadeirado", "Ocasiao": "Noite / Formal", "Preco": 890, "Nota": "Citros, Incenso, Cedro",
            "Imagem": "https://ftcdn.net"
        },
        {
            "Nome": "Sauvage", "Marca": "Dior", "Familia": "Fougère / Aromático", "Ocasiao": "Versátil", "Preco": 750, "Nota": "Bergamota, Pimenta, Ambroxan",
            "Imagem": "https://pngtree.com"
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
st.markdown("<h1>🌸 CLUBE DAS GAROTAS PERFUMADAS 🌸</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #6c5862; font-size: 16px; font-weight: bold; margin-top:0;'>Encontre o cheirinho perfeito que combina com o seu mood de hoje! ✨</p>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Barra lateral para filtros
st.sidebar.markdown("<h2 style='color: #ff4d6d; text-align: center; margin-top: 20px;'>💖 Filtros Fofos</h2>", unsafe_allow_html=True)

familias = ["Todas"] + list(df["Familia"].unique())
familia_selecionada = st.sidebar.selectbox("Escolha a vibe olfativa:", familias)

ocasioes = ["Todas"] + ["Dia / Verão", "Versátil", "Noite / Formal", "Noite / Balada", "Casual / Noite"]
ocasiao_selecionada = st.sidebar.selectbox("Onde você vai usar?", ocasioes)

preco_max = st.sidebar.slider("Preço Máximo (R$)", min_value=500, max_value=1000, value=1000, step=50)

# Aplicar filtros
df_filtrado = df[df["Preco"] <= preco_max]

if familia_selecionada != "Todas":
    df_filtrado = df_filtrado[df_filtrado["Familia"] == familia_selecionada]

if ocasiao_selecionada != "Todas":
    df_filtrado = df_filtrado[df_filtrado["Ocasiao"].str.contains(ocasiao_selecionada, na=False)]

# Grid principal de cards
st.markdown(f"<h3>🎀 Seus Combinados Perfeitos ({len(df_filtrado)})</h3>", unsafe_allow_html=True)

if df_filtrado.empty:
    st.warning("Poxa, nenhum cheirinho achado com esses filtros. Tente mudar as opções na barra lateral! 💕")
else:
    cols = st.columns(3)
    
    for index, row in df_filtrado.reset_index().iterrows():
        with cols[index % 3]:
            # Imagem e informações unificadas dentro do mesmo HTML para alinhar tudo
            st.markdown(
                f"""
                <div class="perfume-card">
                    <div class="card-img-container">
                        <img src="{row['Imagem']}" alt="{row['Nome']}">
                    </div>
                    <h3 style="margin-top:0; color:#ff4d6d; font-family:'Fredoka', sans-serif; font-size:20px; margin-bottom:5px;">{row['Nome']}</h3>
                    <p style="color:#8a737f; margin-bottom:12px; font-size: 13px;"><strong>MARCA:</strong> {row['Marca']}</p>
                    <p style="margin-bottom:12px;"><span class="tag">✨ {row['Familia']}</span></p>
                    <p style="font-size:14px; margin-bottom:6px;"><strong>Ideal para:</strong> {row['Ocasiao']}</p>
                    <p style="font-size:14px; color:#5c4d55; min-height: 40px;"><strong>Notas:</strong> <em>{row['Nota']}</em></p>
                    <h3 style="color:#ff4d6d; margin-top:10px; margin-bottom:10px; font-family: 'Fredoka', sans-serif;">R$ {row['Preco']},00</h3>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            # Botão de interação fofo posicionado perfeitamente abaixo de cada card
            if st.button(f"Quero esse! 💕", key=f"btn_{row['Nome']}", use_container_width=True):
                st.balloons()
                st.success(f"Arrasou! O {row['Nome']} é perfeito para exalar a sua energia icônica!")
            st.markdown("<br>", unsafe_allow_html=True)

st.markdown("<hr style='border-color: rgba(255, 117, 143, 0.3);'>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #ff4d6d;'>✨ Ainda na dúvida, amiga?</h3>", unsafe_allow_html=True)

if st.button("✨ Descobrir minha Assinatura Olfativa Secreta 💖", use_container_width=True):
    st.balloons()
    st.snow()
    st.success("Yay! Nosso teste de personalidade de garota está quase pronto para você descobrir seu aroma secreto!")
