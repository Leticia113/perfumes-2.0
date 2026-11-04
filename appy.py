import streamlit as st
import pandas as pd

# 1. CONFIGURAÇÃO PREMIUM DA PÁGINA
st.set_page_config(
    page_title="Essence Studio Premium",
    page_icon="✨",
    layout="wide"
)

# Estilização forçada via CSS para garantir leitura total e fundo elegante
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #f7ebe6 0%, #f0dfd5 50%, #e3cebf 100%); }
    h1 { color: #2c2523 !important; font-family: 'Playfair Display', serif; text-align: center; font-size: 2.8rem; }
    
    /* Corrige o menu lateral: força todas as labels dos filtros a ficarem brancas */
    [data-testid="stSidebar"] label, 
    [data-testid="stSidebar"] p, 
    [data-testid="stSidebar"] span, 
    [data-testid="stSidebar"] h3 { 
        color: #ffffff !important; 
        font-weight: bold !important;
        font-size: 14px !important;
    }
    
    /* Cores das fontes na área de exibição principal */
    h3, p, span, label { color: #3a312e !important; }
    .stMarkdown p { color: #3a312e !important; }
    </style>
""", unsafe_allow_html=True)

# 2. BANCO DE DADOS INTEGRADO COM LINKS DE IMAGEM DA WEB HIGIENIZADOS
@st.cache_data
def carregar_dados():
    perfumes = [
        # --- FILA SUPERIOR: IMPORTADOS (La Vie Est Belle liderando em primeiro) ---
        {
            "Nome": "La Vie Est Belle", "Marca": "Lancôme", "Familia": "Floral / Doces", "Ocasiao": "Casual / Noite", "Preco": 680, "Nota": "Íris, Jasmim, Baunilha", "Origem": "Importado", 
            "Imagem": "https://unsplash.com"
        },
        {
            "Nome": "Bleu de Chanel", "Marca": "Chanel", "Familia": "Amadeirado", "Ocasiao": "Noite / Formal", "Preco": 890, "Nota": "Citros, Incenso, Cedro", "Origem": "Importado", 
            "Imagem": "https://unsplash.com"
        },
        {
            "Nome": "Sauvage", "Marca": "Dior", "Familia": "Fougère / Aromático", "Ocasiao": "Versátil", "Preco": 750, "Nota": "Bergamota, Pimenta, Ambroxan", "Origem": "Importado", 
            "Imagem": "https://unsplash.com"
        },
        {
            "Nome": "Invictus", "Marca": "Rabanne", "Familia": "Aquático / Amadeirado", "Ocasiao": "Versátil / Esportivo", "Preco": 640, "Nota": "Notas Marinhas, Toranja, Folha de Louro", "Origem": "Importado", 
            "Imagem": "https://unsplash.com"
        },
        {
            "Nome": "Libre", "Marca": "Yves Saint Laurent", "Familia": "Fougère Oriental", "Ocasiao": "Noite / Formal", "Preco": 790, "Nota": "Lavanda, Baunilha de Madagascar, Flor de Laranjeira", "Origem": "Importado", 
            "Imagem": "https://unsplash.com"
        },
        {
            "Nome": "212 VIP Rosé", "Marca": "Carolina Herrera", "Familia": "Floral Frutal", "Ocasiao": "Noite / Festas", "Preco": 710, "Nota": "Champagne Rosé, Flor de Pêssego, Almíscar", "Origem": "Importado", 
            "Imagem": "https://unsplash.com"
        },
        {
            "Nome": "Scandal", "Marca": "Jean Paul Gaultier", "Familia": "Chypre Floral Honey", "Ocasiao": "Noite / Balada", "Preco": 740, "Nota": "Mel, Gardênia, Patchouli", "Origem": "Importado", 
            "Imagem": "https://unsplash.com"
        },
        {
            "Nome": "Le Male", "Marca": "Jean Paul Gaultier", "Familia": "Oriental Fougère", "Ocasiao": "Casual / Noite", "Preco": 690, "Nota": "Menta, Lavanda, Baunilha", "Origem": "Importado", 
            "Imagem": "https://unsplash.com"
        },
        {
            "Nome": "Acqua di Giò", "Marca": "Giorgio Armani", "Familia": "Cítrico / Aquático", "Ocasiao": "Dia / Verão", "Preco": 620, "Nota": "Notas Marinhas, Limão, Alecrim", "Origem": "Importado", 
            "Imagem": "https://unsplash.com"
        },
        {
            "Nome": "Good Girl", "Marca": "Carolina Herrera", "Familia": "Oriental", "Ocasiao": "Noite / Balada", "Preco": 720, "Nota": "Amêndoa, Café, Jasmim, Cacau", "Origem": "Importado", 
            "Imagem": "https://unsplash.com"
        },
        {
            "Nome": "Light Blue", "Marca": "Dolce & Gabbana", "Familia": "Cítrico / Floral", "Ocasiao": "Dia / Verão", "Preco": 550, "Nota": "Maçã Verde, Bambu, Limão Siciliano", "Origem": "Importado", 
            "Imagem": "https://unsplash.com"
        },
        # --- NACIONAIS REQUISITADOS ---
        {
            "Nome": "Natura Essencial Feminino", "Marca": "Natura", "Familia": "Floral Clássico", "Ocasiao": "Casual / Elegante", "Preco": 175, "Nota": "Jasmim, Violeta, Complexo Cítrico", "Origem": "Nacional", 
            "Imagem": "https://unsplash.com"
        },
        {
            "Nome": "Natura Essencial Masculino", "Marca": "Natura", "Familia": "Amadeirado Elegante", "Ocasiao": "Trabalho / Formal", "Preco": 175, "Nota": "Cedro, Âmbar, Notas Especiadas", "Origem": "Nacional", 
            "Imagem": "https://unsplash.com"
        },
        {
            "Nome": "Malbec", "Marca": "O Boticário", "Familia": "Amadeirado Vínico", "Ocasiao": "Trabalho / Noite", "Preco": 219, "Nota": "Carvalho, Álcool Vínico, Patchouli", "Origem": "Nacional", 
            "Imagem": "https://unsplash.com"
        },
        {
            "Nome": "Lily", "Marca": "O Boticário", "Familia": "Floral Bouquet", "Ocasiao": "Dia / Eventos", "Preco": 319, "Nota": "Lírio de Grasse, Baunilha, Sândalo", "Origem": "Nacional", 
            "Imagem": "https://unsplash.com"
        },
        {
            "Nome": "Époque Tropical", "Marca": "Granado", "Familia": "Amadeirado Floral", "Ocasiao": "Dia / Verão", "Preco": 278, "Nota": "Mandarina, Caju, Magnólia", "Origem": "Nacional", 
            "Imagem": "https://unsplash.com"
        },
        {
            "Nome": "Boemia", "Marca": "Phebo", "Familia": "Ambarado Especiado", "Ocasiao": "Noite / Outono", "Preco": 365, "Nota": "Pimenta-preta, Olíbano, Couro", "Origem": "Nacional", 
            "Imagem": "https://unsplash.com"
        },
        {
            "Nome": "Amyi 6.24", "Marca": "Amyi", "Familia": "Frutal Moderno", "Ocasiao": "Assinatura / Versátil", "Preco": 420, "Nota": "Flor de Magnólia, Pera Silvestre, Sândalo-Vanilla", "Origem": "Nacional", 
            "Imagem": "https://unsplash.com"
        },
        {
            "Nome": "Gigi", "Marca": "Avatim", "Familia": "Floriental Amadeirado", "Ocasiao": "Casual / Noite", "Preco": 290, "Nota": "Orquídea Serenade, Baunilha, Musk", "Origem": "Nacional", 
            "Imagem": "https://unsplash.com"
        }
    ]
    return pd.DataFrame(perfumes)

df = carregar_dados()

# 3. CABEÇALHO DA PLATAFORMA
st.markdown("<h1>✨ ESSENCE STUDIO PREMIUM</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-weight: 500;'>Curadoria de Alta Perfumaria Nacional e Internacional</p>", unsafe_allow_html=True)

# 4. PAINEL DE CONTROLE LATERAL (SIDEBAR)
st.sidebar.markdown("### 🔍 Filtrar Catálogo")
origem = st.sidebar.radio("Procedência:", ["Todos", "Nacional", "Importado"])
familia = st.sidebar.selectbox("Família Olfativa", ["Todas"] + list(df["Familia"].unique()))
ocasiao = st.sidebar.selectbox("Ocasião", ["Todas", "Dia / Verão", "Versátil", "Noite / Formal", "Noite / Balada", "Casual / Noite", "Trabalho / Noite"])
preco_max = st.sidebar.slider("Preço Máximo (R$)", 150, 1000, 1000, 50)

# 5. MOTOR DE FILTRAGEM DO DATA FRAME
df_filtrado = df[df["Preco"] <= preco_max]
if origem != "Todos":
    df_filtrado = df_filtrado[df_filtrado["Origem"] == origem]
if familia != "Todas":
    df_filtrado = df_filtrado[df_filtrado["Familia"] == familia]
if ocasiao != "Todas":
    df_filtrado = df_filtrado[df_filtrado["Ocasiao"].str.contains(ocasiao, na=False)]

# 6. DISTRIBUIÇÃO E RENDERIZAÇÃO DO GRID PRINCIPAL
st.write(f"### 🛍️ Fragrâncias Disponíveis ({len(df_filtrado)})")

if df_filtrado.empty:
    st.warning("Nenhum perfume encontrado com os critérios selecionados.")
else:
    cols = st.columns(3)
    for index, row in df_filtrado.reset_index().iterrows():
        with cols[index % 3]:
            with st.container(border=True):
                st.image(row["Imagem"], use_container_width=True)
                st.subheader(row["Nome"])
                st.caption(f"Casa: {row['Marca']} | {row['Origem']}")
                st.write(f"**Família:** {row['Familia']}")
                st.write(f"**Uso:** {row['Ocasiao']}")
                st.write(f"**Notas:** *{row['Nota']}*")
                st.metric(label="Preço", value=f"R$ {row['Preco']},00")
                
                if st.button("Detalhes", key=f"btn_{row['Nome']}", use_container_width=True):
                    st.info(f"{row['Nome']} destaca-se por sua excelente evolução focada em {row['Nota']}.")

# 7. SEÇÃO DE ASSINATURA PRIVADA
st.markdown("---")
if st.button("Iniciar Análise de Assinatura Olfativa Privada", use_container_width=True):
    st.balloons()
    st.success("Mapeamento ativo!")


