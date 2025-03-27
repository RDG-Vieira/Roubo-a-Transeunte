# Roubo a Transeunte
 Estudo de aprendizado de máquina focado em roubos a transeuntes ocorridos no Distrito Federal, com análise detalhada por regiões administrativas, abrangendo os anos de 2019 e 2024.

# Análise de Crimes de Roubo a Transeuntes no Distrito Federal (2019 e 2024)

Este projeto segue o roteiro do **CRISP-DM** para estruturar as etapas de análise e tratamento dos dados relacionados aos crimes de roubo a transeuntes no Distrito Federal (DF) nos anos de 2019 e 2024. O objetivo central é identificar quais regiões administrativas apresentaram aumento ou redução nesse tipo de crime durante os períodos analisados.

Utilizando algoritmos de aprendizado de máquina e técnicas de agrupamento, o estudo busca compreender padrões regionais e temporais que possam fornecer insights valiosos para o planejamento de medidas de segurança pública. Métodos de visualização, como *K-Means, DBSCAN ou agrupamento hierárquico*, serão aplicados para enriquecer a análise e facilitar a interpretação dos resultados.

# Objetivo do Projeto
- Analisar os dados de roubo a transeuntes nos anos de 2019 e 2024, com foco nas regiões administrativas do DF.
- Agrupar os dados utilizando algoritmos de aprendizado de máquina, para revelar padrões e tendências específicas por região e ano.
- Fornecer insights práticos que possam ajudar o governo a implementar políticas de segurança adaptadas às necessidades de cada região.

# Metodologia
Este trabalho começa com a criação de uma tabela CSV manualmente elaborada a partir de dados reais, extraídos diretamente do site da Secretaria de Segurança Pública (SSP) do DF. Como o site não disponibiliza uma API para extração automática, os dados foram coletados e organizados manualmente.

# Etapas do Processo:
1. Tratamento e criação das colunas:
   - A tabela foi processada em Python, onde duas novas colunas foram adicionadas:
     - Uma coluna que combina a região administrativa com o ano.
     - Outra coluna que agrega o total de crimes cometidos em cada região e ano.

2. Agrupamento e visualização:
   - Algoritmos de agrupamento como *K-Means, DBSCAN ou agrupamento hierárquico* serão aplicados aos dados tratados.
   - Visualizações serão geradas para facilitar a análise e interpretação dos resultados.

3. Geração de insights para segurança pública :
   - A análise busca compreender quais regiões administrativas apresentam características específicas, como alta criminalidade, e como essas informações podem orientar *medidas eficazes de segurança* para cada local.

# Resultados Esperados
- Identificação de padrões de aumento ou redução de crimes por região e ano.
- Visualizações que tornam os dados mais acessíveis e compreensíveis para aplicação prática.
- Sugestões para políticas de segurança mais eficazes e alinhadas às necessidades específicas de cada região administrativa.

# Dados Utilizados
- *Fonte:* Secretaria de Segurança Pública (SSP) do DF.
- *Formato:* Tabela CSV criada manualmente com dados tratados e enriquecidos em Python.


