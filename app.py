from pathlib import Path
import streamlit as st
from PIL import Image
import plotly.express as px
import pandas as pd
import os
import plotly.graph_objs as go

def skill_chart(dfQualifiq):
    color_map = {row['QUALIFICATION']: row['COLOR'] for index, row in dfQualifiq.iterrows()}

    plotQualifiq = px.bar(
        x=dfQualifiq['LEVEL'], 
        y=dfQualifiq['QUALIFICATION'], 
        color=dfQualifiq['QUALIFICATION'],
        text=dfQualifiq['QUALIFICATION'],  
        color_discrete_map=color_map,  
        width=690,
       
    )
                        
    plotQualifiq.update_traces(
        textfont_size=19, 
        textposition="inside", 
        cliponaxis=False,
        insidetextanchor="middle",
        hovertemplate=None,

    )

    plotQualifiq.update_layout(
        autosize=True,
        hovermode="x unified",
        showlegend=False,
        xaxis_title=None, 
        yaxis_title=None,
        yaxis={"visible":False},
        xaxis={"visible":False},
        
    )

    plotQualifiq.update_yaxes(tickfont_family="Arial Black")


    for index, row in dfQualifiq.iterrows():
        plotQualifiq.add_layout_image(
            source=Image.open(row['IMAGEM']),
            x=0.2,
            y=row['QUALIFICATION'],  # Use o rótulo como posição y
            xref="x",
            yref="y",
            xanchor="center",
            yanchor="middle",
            sizex=1,
            sizey=1,
            
        
        )
    return plotQualifiq

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"



PAGE_TITLE = "Currículo | Thales Rudolph | ♿️ PCD [CID H54-4]"
PAGE_ICON = "📊"
NAME = "Thales Rudolph"
DESCRIPTION = """
Analista de dados
♿️ PCD [CID H54-4]
"""
EMAIL = "rudolphthales1@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": ["https://www.linkedin.com/in/thales-rudolph-b7511a16a/", [os.path.join(os.getcwd(), "assets", "ICONS", "LINKEDIN.png")]],
    "GitHub": ["https://github.com/megapala2", [os.path.join(os.getcwd(), "assets", "ICONS", "GITHUB.png")]],
    "Spotify": ["https://open.spotify.com/intl-pt/artist/4FnGzOZznKXkYlc09miMkU", [os.path.join(os.getcwd(), "assets", "ICONS", "SPOTIFY.png")]]
}
PROJECTS = {
    "📊 Dashboard PCDs Online Brasil": {
        "description": "O projeto é um dashboard de uma base de currículos de candidatos PCD com a intuição de ajudar recrutadores a acharem candidatos ideais",
        "link": "https://pcdonlinebrasil.streamlit.app/",
        "technologies": ["Python", "Streamlit", "LGPD", "Pandas", "googlesheetsapi"]
    },
    "📊 WorsPlacesToWork Dashboard": {
        "description": "O projeto contabiliza os dados da planilha que viralizou em março de 2024 das empresas tóxicas do Brasil, ela contabiliza as empresas que mais aparecem nessa planilha pública",
        "link": "https://worstplacetowork.streamlit.app/",
        "technologies": ["Pandas", "Streamlit", "fuzzywuzzy", "plotlyexpress"]
    },
    "📊 Miband Dashboard": {
        "description": "O projeto limpa dados que são coletados pelo meu smartwatch!",
        "link": "https://mibandfit.streamlit.app/",
        "technologies": ["Pandas", "Streamlit", "plotlyexpress"]
    },
    "📊 SIO - Sistema Integrado de Orçamentos": {
        "description": "O projeto visa desenvolver um sistema de orçamento de obras em python!",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7174088031795044353/",
        "technologies": ["Pandas", "Streamlit", "aggrid", "googlesheetsapi", "MYSQL"]
    },
    
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)



# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap='small')
st.markdown(
    """
    <style>
        div [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True
)

with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download currículo",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
st.write('\n')

st.markdown(
    """
    <style>
        div[data-testid="column"]:nth-of-type(1)
        {
            text-align: center;
        } 

        div[data-testid="column"]:nth-of-type(2)
        {
            text-align: center;
        } 

        div[data-testid="column"]:nth-of-type(3)
        {
            text-align: center;
        } 
    </style>
    """,unsafe_allow_html=True
)

cols = st.columns(len(SOCIAL_MEDIA))


for index, (platform, values) in enumerate(SOCIAL_MEDIA.items()):
     cols[index].write(f"[{platform}]({values[0]})")
     

st.write('\n')
st.write('\n')
habilidades = st.container(border=True)

tab1, tab2, tab3, tab4, tab5 = habilidades.tabs(['Experiencias e qualificações ', 'Projetos' ,'Hard Skills', 'Soft Skills', 'Experiências Profissionais', ])


dfHard = pd.read_json(f'{ os.getcwd()  }/assets/DADOS/hard.json')
dfHard['IMAGEM'] = [os.path.join(os.getcwd(), "assets", "ICONS", f"{qualification}.png") for qualification in dfHard['QUALIFICATION']]

dfSoft = pd.read_json(f'{ os.getcwd()  }/assets/DADOS/soft.json')
dfSoft['IMAGEM'] = [os.path.join(os.getcwd(), "assets", "ICONS", f"{qualification}.png") for qualification in dfSoft['QUALIFICATION']]



plotHard = skill_chart(dfHard)
plotSoft = skill_chart(dfSoft)




# --- Experiências e qualificações ---
st.write('\n')
st.write('\n')



tab1.write(
    """
- \n
- \n
                                                                         
                                                                        
- ✔️ 5 anos de experiência em processo ETL de pipeline de dados;
- ✔️ Conhecimento avançado de Excel e Python;
- ✔️ Entendimento de técnicas e regulamentos normativos de dados;
- ✔️ Facilidade e velocidade em aprender;
- ✔️ Conhecimento fluente e proficiente da língua inglesa;
- ✔️ Bom orador e comunicador.

"""
)

# --- PROJETOS ---

for project, details in PROJECTS.items():
    with tab2.expander(f'**{project}**'):
        st.write('---------------------')
        st.write(f"**✏️ Descrição**")
        st.write(details['description'])
        st.write('---------------------')
        st.write("**💻 Tecnologias**")
        st.write(", ".join(details["technologies"]))
        st.write('---------------------')
        st.write(f"**[🔗 LINK PARA O PROJETO 🔗]({details['link']})**")


# --- HARD SKILLS ---

tab3.plotly_chart(plotHard, use_container_width=True, static=True)

# --- SOFT SKILLS ---

tab4.plotly_chart(plotSoft, use_container_width=True, static=True)

# --- HISTÓRICO DE TRABALHO ---

tab5.write('\n')



# --- TRABALHO 1
with tab5.expander("**💼 Auxiliar Administrativo | METODO ENGENHARIA**"):     
   
    st.write("📅 09/2023  - Atualmente")
    st.write(
        """
    - ✔️ Desenvolvimento de soluções de BI para o setor de orçamentos;
    - ✔️ Desenvolvimento do SIO (sistema integrado de orçamentos) para auxiliar o processo interno de orçamentos, criando uma aplicação ;
          Python que conecta em um banco de dados, fazendo o front-end para cada etapa do processo;
    - ✔️ Apresentações e reuniões com o time para demonstrar boas práticas na área de dados;
    - ✔️ Procura e desenvolvimento de novas tecnologias de dados para auxiliar na tomada de decisão;
    - ✔️ Concientizar a equipe nos fluxos corretos de tratamento e estruturação de dados.

    """
    )


# --- TRABALHO 2
with tab5.expander("**💼 Auxiliar de Frota  | RODALOG SOLUÇÕES EM LOGISTICA**"):    

    st.write("📅 01/2019 - 06/2020")
    st.write(
        """
    - ✔️ Desenvolver pipelines e dataviz para as áreas da unidade: Segurança, manutenção, produtividade, RH, etc. 
          Resultando em melhoras de 70% nos KPIs de segurança, diminuição de custos de 30% no consumo de combustível 
          e melhora de 100% em KPIs produtividade perante o encontro de diversos pontos de melhoria;
    - ✔️ Apresentação de relatórios de forma diária, semanal e mensal para o parceiro AMBEV;
    - ✔️ Capacitação para os analistas de cada área em como trabalhar com dados de forma mais eficiente;
    - ✔️ Desenvolvimento RPA para diversas rotinas administrativas (extração de arquivos, preenchimento de formulários);
    - ✔️ Apresentação da parte de dados em auditorias internas mantendo a qualidade VPO;
    - ✔️ Ações nível Brasil com o parceiro AMBEV para melhorar KPIs já existentes.

    """
    )


# --- TRABALHO 3
with tab5.expander("**💼 Assistente Adminstrativo  | Unidão Tansportes**"):

    st.write("📅 05/2018 - 01/2019")
    st.write(
        """
    
    - ✔️ Digitalização dos arquivos de DP e jurídico com controle interno sobre cada documento utilizando Excel;
    - ✔️ Criação de planilhas de controle de processos judiciais automatizadas utilizando de fórmulas e programação VBA, 
          onde são demonstrados os principais dados em dashboards interativos;
    - ✔️ Desenvolver planilhas automáticas e padronizadas para os indicadores de DP/RH, 
          além de mesclar todas as filiais em uma única planilha com filtro e gráfico dinâmicos;
    - ✔️ Desenvolvimento de Macros (com linguagem VBA) para RPA, onde seja possível automatizar trabalhos de inserção ou formatação de dados;
    - ✔️ Atender motoristas e requisitar assinaturas e documentos para os mesmos, além de checar incongruências nas informações;
    - ✔️ Checar inconsistências de dados no sistema.

    """
    )



st.subheader('Perfil Profissional')
st.write('----------------------------------------')
st.write("""
         Sou um jovem de 24 anos, quero me inserir no mercado na área de análise de dados! Eu aprendo rápido e sempre foco na base teórica dos assuntos,
         por isso tenho facilidade de me adaptar as mais diversas ferramentas. 
         
         Visualização de dados ou ETL, tenho confiança em me adaptar as ferramentas, pois entendo da base teórica de dados!

         No momento estou me especializando em BIG DATA e no tempo livre trabalhando com RAG (Retrieval Augmented Generation) e em como utilizar LLMs de maneira eficiente para resolver
         questões de dados!

         
         """)
