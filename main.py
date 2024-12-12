import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px





st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("Data Visualization Dashboard")


st.markdown("### Explorando diferentes bibliotecas de visualización en Python")











with st.expander("Introducción", expanded=True):
    st.markdown("""
    Esta aplicación demuestra el uso de diferentes bibliotecas de visualización en Python:
    * **Matplotlib**: Biblioteca base para visualización
    * **Seaborn**: Graficos interactivos
    * **Streamlit**: Framework para aplicaciones de datos
    """)    





try:
    
    # Cargando los dataframe
    

    ruido_sensible_df = pd.read_csv('data/es-sensible-al-ruido.csv')

    cn_audible_df = pd.read_csv('data/cun-audible-es-el-ruido.csv')

    ruido_ambiental_pertu_df = pd.read_csv('data/el-ruido-ambiental-pertu.csv')
    


    st.success("🛸 Datos cargados exitosamente")

    st.divider()
    # Visualizaciones con Matplotlib
    
    st.subheader("🎨 Visualizaciones con Marplotlib")

    with st.container():
        col1,col2 = st.columns(2)

        with col1:
            
            cantidad_visualizacion = 10

            st.subheader("Grafico de Dispersión")

            # Primer grafico

            fig, ax = plt.subplots(figsize =(8,6))
            
            
            categoria_ruido = ruido_sensible_df["Category"]

            resultado_ruido = ruido_sensible_df['Resultado']
            

            ax.scatter(x=categoria_ruido,y=resultado_ruido, color='blue', alpha=0.6)

            plt.xticks(rotation=90)
            plt.title('¿Es sensible al ruido?')
            plt.xlabel('Categorias')
            plt.ylabel("Resultados")
            
            st.pyplot(fig)
            plt.close()

            # Segundo grafico

            fig2, ax2 = plt.subplots(figsize =(8,6))

            categoria_audible = cn_audible_df["Category"]

            resultado_audible = cn_audible_df['Resultado']
            

            ax2.scatter(x=categoria_audible,y=resultado_audible, color='green', alpha=0.6)

            plt.xticks(rotation=90)
            plt.title('¿Cuán audible es el ruido ambiental?')
            plt.xlabel('Categorias')
            plt.ylabel("Resultados")
            
            st.pyplot(fig2)
            plt.close()


            # Tercer grafico

            fig3, ax3 = plt.subplots(figsize =(8,6))


            categoria_perturbante = ruido_ambiental_pertu_df["Category"]

            resultado_perturbante = ruido_ambiental_pertu_df['Resultado']
            
            ax3.scatter(x=categoria_perturbante,y=resultado_perturbante, color='green', alpha=0.6)

            plt.xticks(rotation=90)
            plt.title('El ruido ambiental ¿Pertuba su dormir?')
            plt.xlabel('Categorias')
            plt.ylabel("Resultados")
            
            st.pyplot(fig3)
            plt.close()

        with col2:
            st.subheader("Graficos de Barras")

            # Figura 1

            fig, ax = plt.subplots(figsize=(8,6))

            categoria_ruido = ruido_sensible_df["Category"]

            resultado_ruido = ruido_sensible_df['Resultado']

           

            ax.bar(categoria_ruido,resultado_ruido, color='skyblue')

            plt.xticks(rotation=90)
            plt.title('¿Es sensible al ruido?')
            plt.xlabel('Categorias')
            plt.ylabel("Resultados")
        
            st.pyplot(fig)
            plt.close()


            # Figura 2

            fig2, ax2 = plt.subplots(figsize=(8,6))

            categoria_audible = cn_audible_df["Category"]

            resultado_audible = cn_audible_df['Resultado']

            ax2.bar(categoria_audible,resultado_audible, color='skyblue')

            plt.xticks(rotation=90)
            plt.title('¿Cuán audible es el ruido ambiental?')
            plt.xlabel('Categorias')
            plt.ylabel("Resultados")
        
            st.pyplot(fig2)
            plt.close()


            # Figura 3

            fig3, ax3 = plt.subplots(figsize=(8,6))

            categoria_perturbante = ruido_ambiental_pertu_df["Category"]

            resultado_perturbante = ruido_ambiental_pertu_df['Resultado']

            ax3.bar(categoria_perturbante,resultado_perturbante, color='skyblue')

            plt.xticks(rotation=90)
            plt.title('El ruido ambiental ¿Pertuba su dormir?')
            plt.xlabel('Categorias')
            plt.ylabel("Resultados")
            
            st.pyplot(fig3)
            plt.close()


    # Visualizaciones con Seaborn
    st.subheader("🎨 Visualizaciones con Seaborn")

    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Grafico de Violin")

            # FIGURA 1

            fig, ax= plt.subplots(figsize = (8,6))

            

            sns.violinplot(data=ruido_sensible_df)
            plt.xticks(rotation=90)
            plt.title('¿Es sensible al ruido?')
            st.pyplot(fig)
            plt.close()

            # FIGURA 2

            fig2,ax2 = plt.subplots(figsize = (8,6))

            

            sns.violinplot(data=cn_audible_df)
            plt.xticks(rotation=90)
            plt.title('¿Cuán audible es el ruido ambiental?')
            st.pyplot(fig2)
            plt.close()

            # FIGURA 3

            fig3,ax3 = plt.subplots(figsize = (8,6))

            

            sns.violinplot(data=ruido_ambiental_pertu_df)
            plt.xticks(rotation=90)
            plt.title('El ruido ambiental ¿Pertuba su dormir?')
            st.pyplot(fig3)
            plt.close()




        with col2:
            st.subheader("Gráfico de caja")

            # Figura 1


            fig, ax = plt.subplots(figsize = (8,6))

            sns.boxenplot(data=ruido_sensible_df,
                          x='Category',
                          y='Resultado',
                          ax=ax
                          )

            plt.xticks(rotation=90)
            plt.title('¿Es sensible al ruido?')
            st.pyplot(fig)
            plt.close()     

            # Figura 2

            fig2, ax2 = plt.subplots(figsize = (8,6))

            sns.boxenplot(data=cn_audible_df,
                            x='Category',
                            y='Resultado',
                            ax=ax2
                        )

            plt.xticks(rotation=90)
            plt.title('¿Cuán audible es el ruido ambiental?')
            st.pyplot(fig2)
            plt.close()  

            # Figura 3
            
            fig3, ax3 = plt.subplots(figsize = (8,6))

            sns.boxenplot(data=ruido_ambiental_pertu_df,
                            x='Category',
                            y='Resultado',
                            ax=ax3
                        )

            plt.xticks(rotation=90)
            plt.title('El ruido ambiental ¿Pertuba su dormir?')
            st.pyplot(fig3)
            plt.close()  


    # Visualizaciones Interactivas con Plotly      
    with st.container(): 

        
        # Grafico de lineas
        st.subheader("Grafico de linea interactivo")

        # Grafico 1
        fig = px.line(data_frame=ruido_sensible_df,
                      x='Category',
                      y='Resultado',
                      title='¿Es sensible al ruido?',
                      markers=True
                      )
        st.plotly_chart(fig,use_container_width=True)

        # Grafico 2


        fig2 = px.line(data_frame=cn_audible_df,
                      x='Category',
                      y='Resultado',
                      title='¿Cuán audible es el ruido ambiental?',
                      markers=True
                      )
        st.plotly_chart(fig2,use_container_width=True)


        # Grafico 3


        fig3 = px.line(data_frame=ruido_ambiental_pertu_df,
                      x='Category',
                      y='Resultado',
                      title='El ruido ambiental ¿Pertuba su dormir?',
                      markers=True
                      )
        st.plotly_chart(fig3,use_container_width=True)



        # GRAFICO DE PIE            
        st.subheader("Grafico de Pastel o Torta")

        # Grafico 1

        fig = px.pie(data_frame=ruido_sensible_df,
                        values='Resultado',
                        names='Category',
                        title='¿Es sensible al ruido?'
                      )
        st.plotly_chart(fig,use_container_width=True)


        # Grafico 2


        fig2 = px.pie(data_frame=cn_audible_df,
                        values='Resultado',
                        names='Category',
                        title='¿Cuán audible es el ruido ambiental?'
                      )
        st.plotly_chart(fig2,use_container_width=True)

        # Grafico 3

        fig3 = px.pie(data_frame=ruido_ambiental_pertu_df,
                        values='Resultado',
                        names='Category',
                        title='El ruido ambiental ¿Pertuba su dormir?'
                      )
        st.plotly_chart(fig3,use_container_width=True)


    # ============== Sessión interactiva ===================
    st.header("🤖 Sección Interactiva")

    dataset_choice = st.radio(
        "Selecciona el conjunto de datos:",
        ["¿Es Sensible al ruido?","¿Cuán audible es el ruido ambiental?","EL ruido ambiental ¿Perturba su dormir?"]
    )

    if dataset_choice == "¿Es Sensible al ruido?":
        df = ruido_sensible_df


    elif dataset_choice == "¿Cuán audible es el ruido ambiental?":
        df = cn_audible_df


    elif dataset_choice =="EL ruido ambiental ¿Perturba su dormir?":
        df = ruido_ambiental_pertu_df


    else:
        print("Selecciona un opcion")


    # Selector de visualización 

    chart_type = st.selectbox(
        "Selecciona el tipo de gráfico:",
        ["Barras", "Dispersión", "Linea"]
    )


    # Selector de datos
    x_axis = st.selectbox("Selecciona el eje X", df.columns)
    y_axis = st.selectbox("Selecciona el eje y", df.columns)


    if chart_type == "Barras":
        fig = px.bar(df, x=x_axis, y=y_axis)
    elif chart_type == "Dispersión":
        fig = px.scatter(df, x=x_axis, y=y_axis)
    elif chart_type == "Linea":
        fig = px.line(df,x=x_axis,y=y_axis)
    else:
        print("Selecciona una opcion correcta")


    st.plotly_chart(fig, use_container_width=True)


except Exception as e:
    print(f'❌ Error el leer los dataframe: {str(e)}')


