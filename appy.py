import streamlit as st
import pandas as pd

# 1. CONFIGURAÇÃO PREMIUM DE PÁGINA
st.set_page_config(
    page_title="Essence Studio Premium",
    page_icon="✨",
    layout="wide"
)

# 2. ESTILIZAÇÃO GLOBAL AVANÇADA (CSS CUSTOMIZADO)
st.markdown("""
    <style>
    /* Fundo Degradê sutil Champagne Rose Acetinado */
    .stApp {
        background: linear-gradient(135deg, #f7ebe6 0%, #f0dfd5 50%, #e3cebf 100%);
    }
    
    /* Tipografia de Alta Perfumaria */
    h1 {
        color: #2c2523; 
        font-family: 'Playfair Display', serif !important; 
        font-weight: 700;
        text-align: center;
        font-size: 2.8rem !important;
        letter-spacing: 1px;
        margin-bottom: 5px !important;
    }
    h2, h3, h4, p, span, label {
        font-family: 'Montserrat', sans-serif !important;
    }
    
    /* Cards Premium Unissex */
    .perfume-card {
        border: 1px solid rgba(255, 255, 255, 0.7);
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 15px;
        background: rgba(255, 255, 255, 0.45);
        backdrop-filter: blur(12px);
        box-shadow: 0 10px 30px rgba(58, 49, 46, 0.06);
        transition: all 0.3s ease;
    }
    .perfume-card:hover {
        transform: translateY(-6px);
        background: rgba(255, 255, 255, 0.75);
        border-color: #ba9d8e;
        box-shadow: 0 15px 35px rgba(58, 49, 46, 0.12);
    }
    
    /* Container interno para as fotos */
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
    
    /* Tags de Procedência */
    .tag {
        color: #f7ebe6 !important;
        padding: 4px 12px;
        border-radius: 4px;
        font-size: 10px;
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        display: inline-block;
        margin-right: 5px;
    }
    .tag-importado { background: #2c2523; }
    .tag-nacional { background: #8c7365; }
    
    /* Customização dos Botões */
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
    }
    </style>
""", unsafe_allow_html=True)

# 3. BANCO DE DADOS COMPLETO COM SUA CURADORIA DE PRODUTOS
@st.cache_data
def carregar_dados():
    perfumes = [
        # --- IMPORTADOS ---
        {"Nome": "La Vie Est Belle", "Marca": "Lancôme", "Familia": "Floral / Doces", "Ocasiao": "Casual / Noite", "Preco": 680, "Nota": "Íris, Jasmim, Baunilha", "Origem": "Importado", "Imagem": "https://gstatic.com"},
        {"Nome": "Bleu de Chanel", "Marca": "Chanel", "Familia": "Amadeirado", "Ocasiao": "Noite / Formal", "Preco": 890, "Nota": "Citros, Incenso, Cedro", "Origem": "Importado", "Imagem": "https://gstatic.com"},
        {"Nome": "Sauvage", "Marca": "Dior", "Familia": "Fougère / Aromático", "Ocasiao": "Versátil", "Preco": 750, "Nota": "Bergamota, Pimenta, Ambroxan", "Origem": "Importado", "Imagem": "https://gstatic.com"},
        {"Nome": "Invictus", "Marca": "Rabanne", "Familia": "Aquático / Amadeirado", "Ocasiao": "Versátil / Esportivo", "Preco": 640, "Nota": "Notas Marinhas, Toranja, Folha de Louro", "Origem": "Importado", "Imagem": "https://vtexassets.com"},
        {"Nome": "Libre", "Marca": "Yves Saint Laurent", "Familia": "Fougère Oriental", "Ocasiao": "Noite / Formal", "Preco": 790, "Nota": "Lavanda, Baunilha de Madagascar, Flor de Laranjeira", "Origem": "Importado", "Imagem": "https://gstatic.com"},
        {"Nome": "212 VIP Rosé", "Marca": "Carolina Herrera", "Familia": "Floral Frutal", "Ocasiao": "Noite / Festas", "Preco": 710, "Nota": "Champagne Rosé, Flor de Pêssego, Almíscar", "Origem": "Importado", "Imagem": "https://lojasrenner.com.br"},
        {"Nome": "Scandal", "Marca": "Jean Paul Gaultier", "Familia": "Chypre Floral Honey", "Ocasiao": "Noite / Balada", "Preco": 740, "Nota": "Mel, Gardênia, Patchouli", "Origem": "Importado", "Imagem": "https://magehub.com.br"},
        {"Nome": "Le Male", "Marca": "Jean Paul Gaultier", "Familia": "Oriental Fougère", "Ocasiao": "Casual / Noite", "Preco": 690, "Nota": "Menta, Lavanda, Baunilha", "Origem": "Importado", "Imagem": "https://jeanpaulgaultier.com"},
        {"Nome": "Acqua di Giò", "Marca": "Giorgio Armani", "Familia": "Cítrico / Aquático", "Ocasiao": "Dia / Verão", "Preco": 620, "Nota": "Notas Marinhas, Limão, Alecrim", "Origem": "Importado", "Imagem": "https://gstatic.com"},
        {"Nome": "Light Blue", "Marca": "Dolce & Gabbana", "Familia": "Cítrico / Floral", "Ocasiao": "Dia / Verão", "Preco": 550, "Nota": "Maçã Verde, Bambu, Limão Siciliano", "Origem": "Importado", "Imagem": "https://gstatic.com"},
        # --- NACIONAIS ---
        {"Nome": "Natura Essencial Feminino", "Marca": "Natura", "Familia": "Floral Clássico", "Ocasiao": "Casual / Elegante", "Preco": 175, "Nota": "Jasmim, Violeta, Complexo Cítrico", "Origem": "Nacional", "Imagem": "https://gstatic.com"},
        {"Nome": "Natura Essencial Masculino", "Marca": "Natura", "Familia": "Amadeirado Elegante", "Ocasiao": "Trabalho / Formal", "Preco": 175, "Nota": "Cedro, Âmbar, Notas Especiadas", "Origem": "Nacional", "Imagem": "https://gstatic.com"},
        {"Nome": "Malbec", "Marca": "O Boticário", "Familia": "Amadeirado Vínico", "Ocasiao": "Trabalho / Noite", "Preco": 219, "Nota": "Carvalho, Álcool Vínico, Patchouli", "Origem": "Nacional", "Imagem": "https://gstatic.com"},
        {"Nome": "Lily", "Marca": "O Boticário", "Familia": "Floral Bouquet", "Ocasiao": "Dia / Eventos", "Preco": 319, "Nota": "Lírio de Grasse, Baunilha, Sândalo", "Origem": "Nacional", "Imagem": "https://gstatic.com"},
        {"Nome": "Époque Tropical", "Marca": "Granado", "Familia": "Amadeirado Floral", "Ocasiao": "Dia / Verão", "Preco": 278, "Nota": "Mandarina, Caju, Magnólia", "Origem": "Nacional", "Imagem": "https://gstatic.com"},
        {"Nome": "Boemia", "Marca": "Phebo", "Familia": "Ambarado Especiado", "Ocasiao": "Noite / Outono", "Preco": 365, "Nota": "Pimenta-preta, Olíbano, Couro", "Origem": "Nacional", "Imagem": "https://gstatic.com"},
        {"Nome": "Amyi 6.24", "Marca": "Amyi", "Familia": "Frutal Moderno", "Ocasiao": "Assinatura / Versátil", "Preco": 420, "Nota": "Flor de Magnólia, Pera Silvestre, Sândalo-Vanilla", "Origem": "Nacional", "Imagem": "https://amyi.co"},
        {"Nome": "Gigi", "Marca": "Avatim", "Familia": "Floriental Amadeirado", "Ocasiao": "Casual / Noite", "Preco": 290, "Nota": "Orquídea Serenade, Baunilha, Musk", "Origem": "Nacional", "Imagem": "https://gstatic.com"}
    ]
    return pd.DataFrame(perfumes)

df = carregar_dados()

# 4. ELEMENTOS DO CABEÇALHO PRINCIPAL
st.markdown("<h1>✨ ESSENCE STUDIO PREMIUM</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #5e514c; font-size: 15px; font-weight: 500; letter-spacing: 0.5px; margin-top:0;'>Curadoria Unissex de Alta Perfumaria Nacional e Internacional</p>", unsafe_allow_html=True)

# 5. FILTROS NA BARRA LATERAL (SIDEBAR)
st.sidebar.markdown("<h3 style='color: #2c2523; font-weight: 700; margin-top: 20px;'>🔍 Filtrar Catálogo</h3>", unsafe_allow_html=True)
origem_selecionada = st.sidebar.radio("Procedência:", ["Todos", "Nacional", "Importado"])

familias = ["Todas"] + list(df["Familia"].unique())
familia_selecionada = st.sidebar.selectbox("Família Olfativa", familias)

ocasiao_selecionada = st.sidebar.selectbox("Ocasião de Uso", ["Todas", "Dia / Verão", "Versátil", "Noite / Formal", "Noite / Balada", "Casual / Noite", "Trabalho / Noite", "Trabalho / Formal", "Noite / Festas"])
preco_max = st.sidebar.slider("Preço Máximo (R$)", min_value=150, max_value=1000, value=1000, step=50)

df_filtrado = df[df["Preco"] <= preco_max]
if origem_selecionada != "Todos":
df_filtrado = df_filtrado[df_filtrado["Origem"] == origem_selecionada]
if familia_selecionada != "Todas":
df_filtrado = df_filtrado[df_filtrado["Familia"] == familia_selecionada]
if ocasiao_selecionada != "Todas":
df_filtrado = df_filtrado[df_filtrado["Ocasiao"].str.contains(ocasiao_selecionada, na=False)]
st.write(f"### ✨ Fragrâncias Disponíveis ({len(df_filtrado)})")
if df_filtrado.empty:
st.warning("Nenhuma fragrância corresponde aos critérios selecionados.")
else:
cols = st.columns(3)
for index, row in df_filtrado.reset_index().iterrows():
with cols[index % 3]:
# Define a cor da tag dependendo da nacionalidade do perfume
tag_class = "tag tag-nacional" if row['Origem'] == "Nacional" else "tag tag-importado"
# Montagem estruturada do Card em HTML
st.markdown(f"""




{row['Nome']}
CASA: {row['Marca'].upper()}

{row['Origem']}
{row['Familia']}

Uso: {row['Ocasiao']}
Acorde: {row['Nota']}
R$ {row['Preco']},00

""", unsafe_allow_html=True)
# Botão interativo do Streamlit logo abaixo do card HTML
if st.button("Detalhes da Fragrância", key=f"btn_{row['Nome']}", use_container_width=True):
st.info(f"{row['Nome']} de {row['Marca']} destaca-se por sua excelente evolução olfativa focada em {row['Nota']}.")
st.markdown("
", unsafe_allow_html=True)
st.markdown("", unsafe_allow_html=True)
if st.button("Iniciar Análise de Assinatura Olfativa Privada", use_container_width=True):
st.balloons()
st.success("Mapeamento ativo! Descubra os seus acordes ideais em breve.")
