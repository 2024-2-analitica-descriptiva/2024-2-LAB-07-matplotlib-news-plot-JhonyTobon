"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
# pylint: disable=import-outside-toplevel

import os
import pandas as pd
import matplotlib.pyplot as plt

def pregunta_01():


    output_dir = os.path.abspath("./files/plots")  # Ruta absoluta
    

    plt.Figure()

    colors = {
        'Television': 'dimgrey',
        'Newspaper': 'grey',
        'Internet': 'tab:blue',
        'Radio': 'lightgrey'

    }

    zorder = {
        'Television': 1,
        'Newspaper': 1,
        'Internet': 2,
        'Radio': 1
    }

    linewidths = {
        'Television': 2,
        'Newspaper': 2,
        'Internet': 4,
        'Radio': 2
    }
    df= pd.read_csv('files/input/news.csv', index_col=0)
    for col in df.columns:
        plt.plot(df[col],
                color = colors[col], 
                label = col,
                zorder = zorder[col],
                linewidth = linewidths[col],
            )

    plt.title('How people get their news', fontsize=16)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    for col in df.columns:
        first_year = df.index[0]
        plt.scatter(
            x=first_year,
            y=df[col][first_year],
            color=colors[col],
            zorder=zorder[col],
            )
        
        plt.text(
            first_year - 0.2,
            df[col][first_year],
            col + ' ' + str(df[col][first_year]) + '%',
            ha= 'right',
            va= 'center',
            color = colors[col],

        )

        last_year = df.index[-1]
        plt.scatter(
            x=last_year,
            y=df[col][last_year],
            color=colors[col],
            )
        
        plt.text(
            last_year + 0.2,
            df[col][last_year],
            str(df[col][last_year]) + '%',
            ha= 'left',
            va= 'center',
            color = colors[col],

        )

    plt.xticks(
        ticks=df.index,
        labels=df.index,
        ha='center'
    )

    output_path = os.path.join(output_dir, "news.png")

    try:
        plt.tight_layout()
        plt.savefig(output_path)
        print(f"Gráfico guardado en: {output_path}")
    except Exception as e:
        print(f"Error al guardar el gráfico: {e}")

    plt.tight_layout()
    plt.savefig('news.png')    
    return  plt.Figure
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
