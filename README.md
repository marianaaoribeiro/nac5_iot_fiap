<h1 align="center">
   <p>Projeto de Visão Computacional - Angle Gauge</p>
</h1>
<p align="center">
   <img src="https://i.imgur.com/FhWK0zA.jpg" width="128">
</p>
<h4 align="center">   
   <p><b><i>Medição de ângulos através de segmentação de cores</i></b></p>   
</h4>


## Informações

**Nome Da Aluna:** Mariana Alves de Oliveira Ribeiro - RM: 86125

**Turma:** 2TDSG

**Ano:** 2021

## Descrição

Angle gauge foi desenvolvido para a matéria de Disruptive Architectures IOT and IA, do curso de Análise e Desenvolvimentos de Sistemas da FIAP.
O intuito do projeto é uma aplicação de visão computacional desenvolvida em Python, cujo consegue medir o ângulo de dois pontos maiores segmentados na imagem por filtros HSV. 

## Diagrama do projeto

<img src="https://i.imgur.com/iyGM9uM.png" width="550">

## Como instalar e configurar

### 1. Windows

#### 1.1 Escolha uma versão do Python que seja superior à 3.6

   - https://www.python.org/downloads/windows/

#### 1.2 No instalador, siga os seguintes passos

![](https://python.org.br/images/instalacao-windows/03.png)

#### 1.2 Abra seu terminal e instale a última versão do OpenCV

    pip install opencv-python

### 2. Linux - Ubuntu

#### 2.1 Instale uma versão Python que seja superior à 3.6 e em seguida a última versão do OpenCV

    sudo apt install python3.6
    pip3 install opencv-python

## Usabilidade

### Filtros HSV
Para começar detectar os objetos, precisamos escolher um filtro HSV que se adeque melhor a nossa necessidade.
Execute o programa **utils/hsv_tool.py**, serve como uma ferramenta para segmentar as cores e assim escolher o filtro que atenda a necessidade. Considerando que o nosso objetivo são cores brancas estarem expostas.

![](https://docs.opencv.org/3.4.15/Threshold_inRange_Tutorial_Result_input.jpeg)
![](https://docs.opencv.org/3.4.15/Threshold_inRange_Tutorial_Result_output.jpeg)

### Angle Gauge
Após ter os valores dos filtros em mãos, adicione na linha de código como parâmetros, considerando -l1 e -u1 comos lower e upper dos filtros baixos, e -l2 e -u2 dos filtros altos.

    python angauge.py -l1 0,91,63 -u1 180,171,139 -l2 0,92,64 -u2 180,167,140
    
![Resultado](https://i.imgur.com/cA0KPGq.png)


## Vídeo Demonstração + Explicação

* [Apresentação de Projeto NAC5](https://youtu.be/nPXXH2LFCwE)

## Referências 

* [OpenCV Doc.](https://docs.opencv.org/3.4.15)
* [OpenCV Threshold_inRange](https://docs.opencv.org/3.4.15/da/d97/tutorial_threshold_inRange.html)
