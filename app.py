import streamlit as st

# Configurações da página
st.set_page_config(
    page_title="Streamlit: Transforme suas ideias em aplicativos",
    page_icon=":rocket:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': "Aplicativo criado com Streamlit por [Seu Nome](https://github.com/seu_usuario)."
    }
)

# Sidebar - Menu de Navegação
menu = st.sidebar.radio(
    "Menu de Navegação",
    ["Introdução", "O Que é o Streamlit?", "Por Que o Streamlit é Revolucionário?", 
     "Como Começar com o Streamlit?", "Exemplo de Caso de Uso", "Conclusão"]
)

# Cabeçalho principal
st.sidebar.write("---")
st.sidebar.write("Navegue pelas seções do artigo utilizando o menu acima. 🚀")

# Conteúdo das seções
if menu == "Introdução":
    st.title("Transforme Suas Ideias em Aplicativos com Python")
    st.markdown("""
    **Você sabia que pode criar aplicativos web com Python de maneira simples, rápida e gratuita?**
    O **Streamlit** é uma ferramenta incrível que transforma scripts Python em aplicativos interativos. 
    E o melhor: você pode testar suas aplicações **online e gratuitamente** por meio do 
    **Streamlit Community Cloud**! 🎉
    """)
elif menu == "O Que é o Streamlit?":
    st.title("O Que é o Streamlit?")
    st.markdown("""
    O **Streamlit** é um framework de código aberto que permite criar aplicativos web para 
    visualização e interação com dados de maneira extremamente simples.  
    Com ele, você pode:
    - Construir interfaces interativas para seus modelos e análises.
    - Compartilhar dashboards de visualização de dados.
    - Testar e validar ideias rapidamente com colegas e clientes.
    """)
elif menu == "Por Que o Streamlit é Revolucionário?":
    st.title("Por Que o Streamlit é Revolucionário?")
    st.markdown("""
    - **Fácil de usar:** Basta instalar o pacote, escrever seu código Python e rodar o aplicativo.  
    - **Código limpo:** O código é intuitivo e fácil de entender, mesmo para iniciantes.  
    - **Desempenho incrível:** Com poucos comandos, você pode criar gráficos, tabelas, sliders e outros elementos interativos.  
    - **Deploy gratuito:** Através do **Streamlit Community Cloud**, você pode publicar e compartilhar seu aplicativo sem custos.
    """)
elif menu == "Como Começar com o Streamlit?":
    st.title("Como Começar com o Streamlit?")
    st.markdown("""
    1. **Instale o Streamlit:**  
       ```bash
       pip install streamlit
       ```

    2. **Crie seu primeiro app:**  
       ```python
       import streamlit as st

       st.title("Meu Primeiro App com Streamlit!")
       st.write("Olá, mundo! Este é meu primeiro aplicativo com Python e Streamlit.")
       ```

    3. **Execute o app:**  
       ```bash
       streamlit run app.py
       ```

    4. **Publique online gratuitamente:**  
       - Crie uma conta no [Streamlit Community Cloud](https://share.streamlit.io/).
       - Faça o upload do seu repositório GitHub com o código do app.
       - Compartilhe o link gerado com o mundo!
    """)
elif menu == "Exemplo de Caso de Uso":
    st.title("Exemplo de Caso de Uso")
    st.markdown("""
    Imagine que você é um analista de dados e acabou de construir um modelo de previsão de vendas. 
    Com o Streamlit, você pode:
    - Criar gráficos interativos com o desempenho do modelo.
    - Adicionar sliders para ajustar variáveis de entrada.
    - Compartilhar com a equipe para que todos possam testar o modelo em tempo real.
    """)
elif menu == "Conclusão":
    st.title("Conclusão")
    st.markdown("""
    Não importa se você é iniciante ou um profissional experiente, o Streamlit pode revolucionar a maneira como você compartilha suas ideias e projetos.  
    E com a possibilidade de publicar e testar **gratuitamente no Streamlit Community Cloud**, você não tem nada a perder!  
    🚀 **Teste agora mesmo e descubra o poder do Streamlit!** 💻
    """)

# Rodapé com ícone do GitHub
st.write("---")
st.markdown(
    """
    📌 Aplicativo criado com [Streamlit](https://streamlit.io).  
    Contribua ou veja o código no [GitHub](https://github.com/valfridonovais/apresentacao_streamlit).
    """, unsafe_allow_html=True
)
