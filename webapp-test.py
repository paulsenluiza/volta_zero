import streamlit as st
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

# Função para carregar dados com @st.cache
@st.cache
def load_data():
    data = pd.DataFrame({
        'A': np.random.randn(100),
        'B': np.random.randn(100),
        'C': np.random.randn(100),
    })
    return data

# Aplicação Streamlit
st.title("Exemplo de Aplicação Streamlit")
st.markdown("Este exemplo utiliza múltiplos conceitos de Streamlit.")

# 1. Carregar dados com @st.cache
st.subheader("Carregar dados com @st.cache")
data = load_data()

# 2. Exibir dados
st.write("Aqui estão alguns dados gerados aleatoriamente:", data.head())

# 3. Criando colunas
col1, col2 = st.columns(2)
with col1:
    st.write("Primeira coluna")
    st.line_chart(data['A'])
with col2:
    st.write("Segunda coluna")
    st.bar_chart(data['B'])

# 4. Barra de progresso
st.subheader("Barra de Progresso")
progress_bar = st.progress(0)
for i in range(100):
    progress_bar.progress(i + 1)
    time.sleep(0.05)

# 5. Slider de valor
st.subheader("Slider de Valor")
slider_value = st.slider("Escolha um valor", 0, 100)
st.write(f"Você escolheu: {slider_value}")

# 6. Caixa de seleção
checkbox_value = st.checkbox("Ativar opção")
if checkbox_value:
    st.write("A opção está ativada!")

# 7. Sessão com session_state
st.subheader("Sessão com session_state")
if 'counter' not in st.session_state:
    st.session_state.counter = 0

increment_button = st.button("Incrementar contador")
if increment_button:
    st.session_state.counter += 1

st.write(f"Contador atual: {st.session_state.counter}")

# 8. Exibindo tabela
st.subheader("Tabela Dinâmica")
st.dataframe(data)

# 9. Exibindo uma imagem
st.subheader("Exibindo uma Imagem")
st.image('https://www.streamlit.io/images/brand/streamlit-mark-dark.svg', caption="Logo do Streamlit", width=200)

# 10. Gráfico com matplotlib
st.subheader("Gráfico com Matplotlib")
fig, ax = plt.subplots()
ax.plot(data['A'], label="Coluna A")
ax.plot(data['B'], label="Coluna B")
ax.legend()
st.pyplot(fig)

# 11. Seleção de Variáveis com Selectbox
st.subheader("Seleção de Variáveis")
option = st.selectbox("Escolha uma variável", ['A', 'B', 'C'])
st.write(f"Você escolheu a variável: {option}")
st.line_chart(data[option])

# 12. Exemplo de Markdown
st.markdown("""
# Exemplo de Markdown
Você pode adicionar **markdown** em Streamlit para formatar texto.
""")

# 13. Expansão de Conteúdo
with st.expander("Clique aqui para ver mais"):
    st.write("Mais informações sobre o exemplo de código.")

# 14. Exibindo Código
st.subheader("Exibindo Código")
code = '''import streamlit as st
st.title("Exemplo de Código")'''
st.code(code, language='python')

# 15. Barra lateral com opção de escolha
st.sidebar.subheader("Opções Laterais")
option_sidebar = st.sidebar.selectbox("Escolha uma variável", ['A', 'B', 'C'])
st.sidebar.write(f"Você escolheu a variável: {option_sidebar}")

# 16. Exemplo de texto com markdown e formatação
st.markdown("### Subtítulo em Markdown com **negrito** e *itálico*")

# 17. Áudio com Streamlit
st.subheader("Reprodução de Áudio")
st.audio('https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3', format="audio/mp3")

# 18. Exibindo imagens da webcam
st.subheader("Captura de Imagem")
if st.button("Tirar foto"):
    st.image(data['A'], caption="Imagem da Webcam", use_column_width=True)

# 19. Exibindo vídeo
st.subheader("Exibindo Vídeo")
st.video('https://www.youtube.com/watch?v=1gkTV-Qrf94')

# 20. Exemplo de uso de checkbox e múltiplas opções
st.subheader("Seleção Múltipla com Checkbox")
selected_options = st.multiselect(
    'Escolha suas opções favoritas',
    ['Python', 'Java', 'C++', 'JavaScript', 'Ruby'],
    default=['Python', 'JavaScript']
)
st.write(f"Você escolheu: {selected_options}")
