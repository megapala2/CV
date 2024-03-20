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
        width=680

    )
                        
    plotQualifiq.update_traces(
        textfont_size=19, 
        textposition="inside", 
        #cliponaxis=False,
        insidetextanchor="middle",
        hovertemplate=None,

    )

    plotQualifiq.update_layout(
        #autosize=True,
    
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
Estudante de Data Science - Entuasiasta de decisões data driven!
♿️ PCD [CID H54-4]
"""
EMAIL = "rudolphthales1@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": ["https://www.linkedin.com/in/thales-rudolph-b7511a16a/", [os.path.join(os.getcwd(), "assets", "ICONS", "LINKEDIN.png")]],
    "GitHub": ["https://github.com/megapala2", [os.path.join(os.getcwd(), "assets", "ICONS", "GITHUB.png")]],
    "Spotify": ["https://open.spotify.com/intl-pt/artist/4FnGzOZznKXkYlc09miMkU", [os.path.join(os.getcwd(), "assets", "ICONS", "SPOTIFY.png")]]
}
PROJECTS = {
    "🏆 SIO - Sistema Integrado de Orçamentos": "https://www.linkedin.com/feed/update/urn:li:activity:7174088031795044353/",
    "🏆 Dashboard de vendas para lojas de varejo": "https://www.linkedin.com/in/thales-rudolph-b7511a16a/",
    "🏆 Planilhas automatizadas em VBA": "https://www.linkedin.com/in/thales-rudolph-b7511a16a/"

}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)



# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download currículo completo",
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

tab1, tab2, tab3, tab4 = habilidades.tabs(['Experiencias e qualificações ', 'Hard Skills', 'Soft Skills', 'Experiências Profissionais', ])


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
                                                                         
                                                                        
- ✔️ 4 anos de experiência em extração e consolidação de bases de dados;
- ✔️ Conhecimento avançado de Excel e Python;
- ✔️ Entendimento de técnicas e regulamentos normativos de dados;
- ✔️ Facilidade e velocidade em aprender;
- ✔️ Conhecimento fluente e proficiente da língua inglesa;
- ✔️ Bom orador e comunicador.

"""
)


# --- HARD SKILLS ---

tab2.plotly_chart(plotHard, use_container_width=True)

# --- SOFT SKILLS ---

tab3.plotly_chart(plotSoft, use_container_width=True)

# --- HISTÓRICO DE TRABALHO ---

tab4.write('\n')



# --- TRABALHO 6
with tab4.expander("**💼 Auxiliar Administrativo | METODO ENGENHARIA**"):     
   
    st.write("📅 09/2023  - Atualmente")
    st.write(
        """
    - ✔️ Auxilio no orçamento de obras do setor industrial, recebendo cotações do suprimentos e preenchendo os dados correspondentes
    - ✔️ Criação planilhas automatizadas para a área de orçamentos
    - ✔️ Desenvolvimento de ferramentas em Python que auxiliem nos fluxos diários
    - ✔️ Plataforma de cotações para fornecedores utilizando a biblioteca Streamlit
    - ✔️ Concientizar a equipe nos fluxos corretos de tratamento e estruturação de dados

    """
    )


# --- TRABALHO 5
with tab4.expander("**💼 Autônomo  | Compositor Musical (MUGUES)**"):      
    
    st.write("📅 03/2021 - 09/2023")
    st.write(
        """
    - ✔️ Negociação com clientes internacionais para desenvolvimento de trilhas personalizadas
    - ✔️ Mixagem e tratamento de áudio de trilhas
    - ✔️ Negociação sobre direitos comerciais
    - ✔️ Postagem das músicas nas plataformas de streaming
    - ✔️ Marketing e desenvolvimento de marca pessoal

    """
    )

# --- TRABALHO 4
with tab4.expander("**💼 Gerente de produção  | DRAWN MASK (YOUTUBER)**"):      
    
    st.write("📅 06/2020 - 03/2021")
    st.write(
        """
    - ✔️ Liderar equipe de 5+ editores para cronograma editorial de vídeos
    - ✔️ Desenvolver estratégias para diminuição da rotatividade de editores do canal
    - ✔️ Negociação com marcas para parcerias comerciais
    - ✔️ Planejamento estratégico de lançamento dos vídeos
    - ✔️ Gerenciar o pagamento dos editores

    """
    )


# --- TRABALHO 3
with tab4.expander("**💼 Auxiliar de Frota  | RODALOG SOLUÇÕES EM LOGISTICA**"):    

    st.write("📅 01/2019 - 06/2020")
    st.write(
        """
    - ✔️ Auxiliar todas as áreas com suas respectivas demandas de dados: RH, DP, produtividade, gestão, manutenção e segurança
    - ✔️ Trabalhar em todos os indicadores em busca da sustentabilidade do VPO na AMBEV
    - ✔️ Inserir informações de frota e de financeiro no sistema TOTVS da empresa
    - ✔️ Participar de reuniões diárias, semanais e mensais para discutir indicadores e ações para nossa unidade
    - ✔️ Criar dashboards interativos e reaproveitáveis para todas as áreas utilizando do meu conhecimento de macros, VBA e fórmulas matriciais.

    """
    )


# --- TRABALHO 2
with tab4.expander("**💼 Assistente Adminstrativo  | Unidão Tansportes**"):

    st.write("📅 05/2018 - 01/2019")
    st.write(
        """
    
    - ✔️ Trabalhar na organização de arquivos de DP e Jurídico
    - ✔️ Criação de planilhas de controle de RH, DP e processos judiciais automatizadas utilizando de fórmulas e programação VBA
    - ✔️ Desenvolvimento de Macros (com linguagem VBA) para automatizar processos de dados
    - ✔️ Preenchimento de informações no ERP da empresa

    """
    )

# --- TRABALHO 1
with tab4.expander("**💼 Líder | Projeto Tribos nas Trilhas da Cidadania**"):

    st.write("📅 01/2012 - 10/2015")
    st.write(
        """
    - ✔️ Representar anualmente a escola em fóruns regionais, elaborando falas e discursos sobre ações que foram feitas ao decorrer do ano. 
    - ✔️ Planejar as ações e atividades, visando melhorar o ambiente escolar e das comunidades próximas.  
    - ✔️ Realizar e participar de reuniões semanais para elaborar o planejamento e atividades do grupo, além de
    motivar os alunos no engajamento do projeto Tribos. 

    """, unsafe_allow_html=True
    )

st.subheader("Projetos")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
