![Ironhack logo](https://i.imgur.com/1QgrNNw.png)



# Projeto final | Sistema de Recomendação de Filmes 🎬


<p align="center">
  <img src="https://media.giphy.com/media/kd9BlRovbPOykLBMqX/giphy.gif">
</p>


# Descrição

O intuito do projeto foi criar, a partir de um dataset, um sistema de recomendação de filmes para o usuário
usando metodologias e técnicas que foram aprendidas durante o curso.


# Pré-requisito

1. [Python](https://www.python.org/)
2. [Jupyter Notebook](https://jupyter.org/try)
3. [Pandas](https://pandas.pydata.org/)
4. [Scikit Lean](https://pypi.org/project/scikit-learn/)
5. [OMDB Api](http://www.omdbapi.com/)
6. [Streamlit](https://streamlit.io)


# Desenvolvimento

## Limpeza dos dados:

Após selecionar os datasets que seriam usados no projeto, foram feitas análises nos respectivos para
filtrar apenas os dados que teriam relevância no decorrer do projeto.

![image3](https://raw.githubusercontent.com/Viniciusneri1/projeto-recomenda-es-de-filmes/main/img3.png)

## Machine Learning 

### Pontuação de semelhança:

Como ele decide qual item é mais semelhante ao item que o usuário gosta? Aqui usamos as pontuações de similaridade.

É um valor numérico que varia de zero a um, que ajuda a determinar o quanto dois itens são semelhantes entre si em uma escala de zero a um.
Esse escore de similaridade é obtido medindo-se a similaridade entre os detalhes do texto de ambos os itens.
Portanto, a pontuação de semelhança é a medida de semelhança entre dados de texto de dois itens. Isso pode ser feito por semelhança de cosseno.


### Semelhança de cossenos - Como funciona:

Similaridade de cosseno é uma métrica usada para medir o quão semelhantes os dados são, independentemente de seu tamanho.
Matematicamente, ele mede o cosseno do ângulo entre dois vetores projetados em um espaço multidimensional. 
A semelhança do cosseno é vantajosa porque, mesmo que os dois documentos semelhantes estejam distantes pela distância euclidiana
(devido ao tamanho do documento), é provável que eles ainda estejam orientados mais próximos. Quanto menor o ângulo, maior a similaridade do cosseno.

![image](https://user-images.githubusercontent.com/36665975/70401457-a7530680-1a55-11ea-9158-97d4e8515ca4.png)

[Semelhanca de cossenos](https://www.machinelearningplus.com/nlp/cosine-similarity/)


## Streamlit:

Após conclusão de todos os processos anteriores, o último passo foi transferir o código para o streamlit para criação da aplicacão Web.




![image2](https://github.com/Viniciusneri1/projeto-recomenda-es-de-filmes/blob/main/img4.png)
.






## Agradecimentos:

Raiana Rocha

Yuri Felix

Diego Dias

Matheus Zavagli

Pedro Felix

Pedro Prado
