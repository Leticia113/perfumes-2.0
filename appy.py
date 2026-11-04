import streamlit as st
import pandas as pd

# Configuração da página - Identidade Visual de Luxo Neutra
st.set_page_config(
    page_title="Essence Studio 2026",
    page_icon="✨",
    layout="wide"
)

# Estilização global - Luxuosa, sofisticada e Unissex
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    /* Fundo degradê sutil em Champagne Rose e Off-White */
    .stApp {
        background: linear-gradient(135deg, #f7ebe6 0%, #f0dfd5 50%, #e3cebf 100%);
    }
    
    /* Tipografia de Alta Perfumaria */
    h1 {
        color: #2c2523; 
        font-family: 'Playfair Display', serif; 
        font-weight: 700;
        text-align: center;
        font-size: 2.8rem !important;
        letter-spacing: 1px;
        margin-bottom: 5px !important;
    }
    h2, h3, h4, p, span, label {
        font-family: 'Montserrat', sans-serif !important;
        color: #3a312e !important;
    }
    
    /* Cards Unissex Premium - Vidro Minimalista Acetinado */
    .perfume-card {
        border: 1px solid rgba(255, 255, 255, 0.7);
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 15px;
        background: rgba(255, 255, 255, 0.45);
        backdrop-filter: blur(12px);
        box-shadow: 0 10px 30px rgba(58, 49, 46, 0.06);
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    }
    .perfume-card:hover {
        transform: translateY(-6px);
        background: rgba(255, 255, 255, 0.75);
        border-color: #ba9d8e;
        box-shadow: 0 15px 35px rgba(58, 49, 46, 0.12);
    }
    
    /* Container interno para preservar a proporção exata da foto */
    .card-img-container {
        width: 100%;
        height: 240px;
        border-radius: 8px;
        overflow: hidden;
        margin-bottom: 18px;
        background-color: #ffffff;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .card-img-container img {
        max-width: 100%;
        max-height: 100%;
        object-fit: contain;
        padding: 5px;
    }
    
    /* Tags de Categorias Elegantes e Neutras */
    .tag {
        background: #4a3f3b;
        color: #f7ebe6 !important;
        padding: 4px 12px;
        border-radius: 4px;
        font-size: 10px;
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        display: inline-block;
    }
    
    /* Customização dos Botões de Ação do Streamlit */
    div.stButton > button {
        background: #2c2523 !important;
        color: #f7ebe6 !important;
        font-family: 'Montserrat', sans-serif !important;
        font-size: 13px !important;
        font-weight: 600 !important;
        border: none !important;
        border-radius: 4px !important;
        padding: 12px 24px !important;
        letter-spacing: 1px;
        text-transform: uppercase;
        box-shadow: 0 4px 12px rgba(44, 37, 35, 0.15) !important;
        transition: all 0.2s ease;
    }
    div.stButton > button:hover {
        background: #4a3f3b !important;
        transform: scale(1.02);
        box-shadow: 0px 6px 18px rgba(44, 37, 35, 0.25) !important;
    }
    
    /* Ajustes na Barra Lateral */
    [data-testid="stSidebar"] {
        background-color: rgba(247, 235, 230, 0.95) !important;
        border-right: 1px solid rgba(44, 37, 35, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Dados com o La Vie Est Belle na primeira posição e links das fotos atribuídos corretamente
@st.cache_data
def carregar_dados():
    perfumes = [
        {
            "Nome": "La Vie Est Belle", "Marca": "Lancôme", "Familia": "Floral / Doces", "Ocasiao": "Casual / Noite", "Preco": 680, "Nota": "Íris, Jasmim, Baunilha",
            "Imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRSsZJESmU0dngud1Wj2kxDZzQrMJoP9FEUnbb0jDwSFw&s=10"
        },
        {
            "Nome": "Bleu de Chanel", "Marca": "Chanel", "Familia": "Amadeirado", "Ocasiao": "Noite / Formal", "Preco": 890, "Nota": "Citros, Incenso, Cedro",
            "Imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRl-aShQSkoM-tREHi5kEkGDw8AhqYXl7LsS4gdOhqqqA&s=10"
        },
        {
            "Nome": "Sauvage", "Marca": "Dior", "Familia": "Fougère / Aromático", "Ocasiao": "Versátil", "Preco": 750, "Nota": "Bergamota, Pimenta, Ambroxan",
            "Imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSUEERz5U8b5mD7FO61pEJlp4ux6sZa1p7ugh0ozeyT3g&s=10"
        },
        {
            "Nome": "Acqua di Giò", "Marca": "Giorgio Armani", "Familia": "Cítrico / Aquático", "Ocasiao": "Dia / Verão", "Preco": 620, "Nota": "Notas Marinhas, Limão, Alecrim",
            "Imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTqtmErVmfqb7purM28OAIgmnLjHUnnE2btwsPOZNljog&s=10"
        },
        {
            "Nome": "Good Girl", "Marca": "Carolina Herrera", "Familia": "Oriental", "Ocasiao": "Noite / Balada", "Preco": 720, "Nota": "Amêndoa, Café, Jasmim, Cacau",
            "Imagem": "https://img.lojasrenner.com.br/item/551652881/original/3.jpg"
        },
        {
            "Nome": "Light Blue", "Marca": "Dolce & Gabbana", "Familia": "Cítrico / Floral", "Ocasiao": "Dia / Verão", "Preco": 550, "Nota": "Maçã Verde, Bambu, Limão Siciliano",
            "Imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6KGhiyrVMT0iuhBvNm3VkZuNZPFIpTRojsvI1FCqMTg&s=10"
        }
    ]
    return pd.DataFrame(perfumes)

df = carregar_dados()

# Título Principal do App
st.markdown("<h1>✨ ESSENCE STUDIO PREMIUM</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #5e514c; font-size: 15px; font-weight: 500; letter-spacing: 0.5px; margin-top:0;'>Encontre a fragrância ideal para a sua assinatura e rastro olfativo</p>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Barra lateral para os filtros refinados
st.sidebar.markdown("<h3 style='color: #2c2523; font-weight: 700; margin-top: 20px; font-size: 18px;'>🔍 Filtrar Catálogo</h3>", unsafe_allow_html=True)

familias = ["Todas"] + list(df["Familia"].unique())
familia_selecionada = st.sidebar.selectbox("Família Olfativa", familias)

ocasioes = ["Todas"] + ["Dia / Verão", "Versátil", "Noite / Formal", "Noite / Balada", "Casual / Noite"]
ocasiao_selecionada = st.sidebar.selectbox("Ocasião de Uso", ocasioes)

preco_max = st.sidebar.slider("Preço Máximo (R$)", min_value=500, max_value=1000, value=1000, step=50)

# Processamento de Filtros do DataFrame
df_filtrado = df[df["Preco"] <= preco_max]

if familia_selecionada != "Todas":
    df_filtrado = df_filtrado[df_filtrado["Familia"] == familia_selecionada]

if ocasiao_selecionada != "Todas":
    df_filtrado = df_filtrado[df_filtrado["Ocasiao"].str.contains(ocasiao_selecionada, na=False)]

# Grid de Exibição
st.markdown(f"<h4 style='font-weight: 600; margin-bottom: 20px;'>✨ Curadoria Exclusiva ({len(df_filtrado)})</h4>", unsafe_allow_html=True)

if df_filtrado.empty:
    st.warning("Nenhuma fragrância corresponde aos critérios selecionados. Ajuste os filtros na barra lateral.")
else:
    cols = st.columns(3)
    
    # Renderização unificada mantendo as imagens perfeitamente alinhadas dentro de cada bloco
    for index, row in df_filtrado.reset_index().iterrows():
        with cols[index % 3]:
            st.markdown(
                f"""
                <div class="perfume-card">
                    <div class="card-img-container">
                        <img src="{row['Imagem']}" alt="{row['Nome']}">
                    </div>
                    <h3 style="margin-top:0; color:#2c2523; font-family:'Playfair Display', serif; font-size:22px; margin-bottom:4px;">{row['Nome']}</h3>
                    <p style="color:#70605a; margin-bottom:12px; font-size: 12px; letter-spacing: 0.5px;"><strong>CASA:</strong> {row['Marca'].upper()}</p>
                    <p style="margin-bottom:14px;"><span class="tag">{row['Familia']}</span></p>
                    <p style="font-size:13.5px; margin-bottom:6px; color:#4e413c;"><strong>Uso Recomendado:</strong> {row['Ocasiao']}</p>
                    <p style="font-size:13.5px; color:#5c4f4a; min-height: 40px;"><strong>Acorde de Notas:</strong> <em>{row['Nota']}</em></p>
                    <h3 style="color:#2c2523; margin-top:14px; margin-bottom:5px; font-family:'Montserrat', sans-serif; font-weight:700!important;">R$ {row['Preco']},00</h3>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            # Botão de interação elegante e unificado
            if st.button(f"Detalhes da Fragrância", key=f"btn_{row['Nome']}", use_container_width=True):
                st.info(f"Experiência Olfativa: {row['Nome']} de {row['Marca']} entrega uma evolução perfeita de notas de topo focadas em {row['Nota']}.")
            st.markdown("<br>", unsafe_allow_html=True)

st.markdown("<hr style='border-color: rgba(44, 37, 35, 0.15);'>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #2c2523; font-family:\"Playfair Display\", serif;'>✨ Consultoria Privada</h3>", unsafe_allow_html=True)

if st.button("Iniciar Análise de Assinatura Olfativa", use_container_width=True):
    st.balloons()
    st.success("O mapeamento de perfil olfativo está ativo. Descubra as notas que mais se alinham à sua pele em breve!")
