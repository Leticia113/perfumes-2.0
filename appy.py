import streamlit as st
import pandas as pd

# Configuração premium de página
st.set_page_config(
    page_title="Essence Studio Premium",
    page_icon="✨",
    layout="wide"
)

# Estilização Global Avançada - Unissex, Minimalista e Luxuosa
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
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
    
    /* Cards Premium Unissex - Vidro Minimalista Espelhado */
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
    
    /* Container interno para alinhamento e proporção perfeita das fotos */
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
    .tag-importado {
        background: #2c2523;
    }
    .tag-nacional {
        background: #8c7365;
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

# Banco de dados centralizado mapeado com as fotos exatas enviadas por você
@st.cache_data
def carregar_dados():
    perfumes = [
        # ==================== IMPORTADOS ====================
        {
            "Nome": "La Vie Est Belle", "Marca": "Lancôme", "Familia": "Floral / Doces", "Ocasiao": "Casual / Noite", "Preco": 680, "Nota": "Íris, Jasmim, Baunilha", "Origem": "Importado",
            "Imagem": "https://gstatic.com"
        },
        {
            "Nome": "Bleu de Chanel", "Marca": "Chanel", "Familia": "Amadeirado", "Ocasiao": "Noite / Formal", "Preco": 890, "Nota": "Citros, Incenso, Cedro", "Origem": "Importado",
            "Imagem": "https://gstatic.com"
        },
        {
            "Nome": "Sauvage", "Marca": "Dior", "Familia": "Fougère / Aromático", "Ocasiao": "Versátil", "Preco": 750, "Nota": "Bergamota, Pimenta, Ambroxan", "Origem": "Importado",
            "Imagem": "https://gstatic.com"
        },
        {
            "Nome": "Invictus", "Marca": "Rabanne", "Familia": "Aquático / Amadeirado", "Ocasiao": "Versátil / Esportivo", "Preco": 640, "Nota": "Notas Marinhas, Toranja, Folha de Louro", "Origem": "Importado",
            "Imagem": "https://coopera.vtexassets.com/arquivos/ids/24975236/17047257737792.jpg?v=638404205688370000"
        },
        {
            "Nome": "Libre", "Marca": "Yves Saint Laurent", "Familia": "Fougère Oriental", "Ocasiao": "Noite / Formal", "Preco": 790, "Nota": "Lavanda, Baunilha de Madagascar, Flor de Laranjeira", "Origem": "Importado",
            "Imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTE1kbo-HrufE51lldhKFTigmYPvEKRNo9w61q1iUSfA5_hUhvP-w9FhYks&s=10"
        },
        {
            "Nome": "212 VIP Rosé", "Marca": "Carolina Herrera", "Familia": "Floral Frutal", "Ocasiao": "Noite / Festas", "Preco": 710, "Nota": "Champagne Rosé, Flor de Pêssego, Almíscar", "Origem": "Importado",
            "Imagem": "https://img.lojasrenner.com.br/item/535183333/original/3.jpg"
        },
        {
            "Nome": "Scandal", "Marca": "Jean Paul Gaultier", "Familia": "Chypre Floral Honey", "Ocasiao": "Noite / Balada", "Preco": 740, "Nota": "Mel, Gardênia, Patchouli", "Origem": "Importado",
            "Imagem": "https://flavios.magehub.com.br/media/catalog/product/f/l/flavios_img_0571813_1777245265737.jpg"
        },
        {
            "Nome": "Le Male", "Marca": "Jean Paul Gaultier", "Familia": "Oriental Fougère", "Ocasiao": "Casual / Noite", "Preco": 690, "Nota": "Menta, Lavanda, Baunilha", "Origem": "Importado",
            "Imagem": "https://medias.jeanpaulgaultier.com/cdn-cgi/image/width=390,quality=90,format=avif/medias/sys_master/images/h93/h50/10688839352350/Tryptique-2-le-male-edt-jean-paul-gaultier/Tryptique-2-le-male-edt-jean-paul-gaultier.png"
        },
        {
            "Nome": "Acqua di Giò", "Marca": "Giorgio Armani", "Familia": "Cítrico / Aquático", "Ocasiao": "Dia / Verão", "Preco": 620, "Nota": "Notas Marinhas, Limão, Alecrim", "Origem": "Importado",
            "Imagem": "https://gstatic.com"
        },
        {
            "Nome": "Good Girl", "Marca": "Carolina Herrera", "Familia": "Oriental", "Ocasiao": "Noite / Balada", "Preco": 720, "Nota": "Amêndoa, Café, Jasmim, Cacau", "Origem": "Importado",
            "Imagem": "https://lojasrenner.com.br"
        },
        {
            "Nome": "Light Blue", "Marca": "Dolce & Gabbana", "Familia": "Cítrico / Floral", "Ocasiao": "Dia / Verão", "Preco": 550, "Nota": "Maçã Verde, Bambu, Limão Siciliano", "Origem": "Importado",
            "Imagem": "https://gstatic.com"
        },
        # ==================== NACIONAIS ====================
        {
            "Nome": "Natura Essencial Feminino", "Marca": "Natura", "Familia": "Floral Clássico", "Ocasiao": "Casual / Elegante", "Preco": 175, "Nota": "Jasmim, Violeta, Complexo Cítrico", "Origem": "Nacional",
            "Imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS3K3SIK_y4UrbcDoUyU1YojySCT11VKU2SvCItgc2Dsg&s=10"
        },
        {
            "Nome": "Natura Essencial Masculino", "Marca": "Natura", "Familia": "Amadeirado Elegante", "Ocasiao": "Trabalho / Formal", "Preco": 175, "Nota": "Cedro, Âmbar, Notas Especiadas", "Origem": "Nacional",
            "Imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQYNqP1oNTJFQKm2RnnxNX-JSyKlmlRW3MPHvQSnxoc7A&s=10"
        },
        {
            "Nome": "Malbec", "Marca": "O Boticário", "Familia": "Amadeirado Vínico", "Ocasiao": "Trabalho / Noite", "Preco": 219, "Nota": "Carvalho, Álcool Vínico, Patchouli", "Origem": "Nacional",
            "Imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQPgMB84-7glNPmCbkH0FCKEDf-Lu0rDedPP50RXLYwXQ&s=10"
        },
        {
            "Nome": "Lily", "Marca": "O Boticário", "Familia": "Floral Bouquet", "Ocasiao": "Dia / Eventos", "Preco": 319, "Nota": "Lírio de Grasse, Baunilha, Sândalo", "Origem": "Nacional",
            "Imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSD7LyxhUnNZo9JZVWjVLe35Ogv0Afxmqszj6dhJfAV7A&s=10"
        },
        {
            "Nome": "Époque Tropical", "Marca": "Granado", "Familia": "Amadeirado Floral", "Ocasiao": "Dia / Verão", "Preco": 278, "Nota": "Mandarina, Caju, Magnólia", "Origem": "Nacional",
            "Imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxC_wNWU7JOm0Xw8a5lpujJXefDaGkfMz0QXu_KiAM7A&s=10"
        },
        {
            "Nome": "Boemia", "Marca": "Phebo", "Familia": "Ambarado Especiado", "Ocasiao": "Noite / Outono", "Preco": 365, "Nota": "Pimenta-preta, Olíbano, Couro", "Origem": "Nacional",
            "Imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUC_ShzSoYAK8ePZPrDRbq-gzu6sai9BZVocNzGXV89w&s=10"
        },
        {
