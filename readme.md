# Monitor de recursos

##  O Projeto tem dois objetivos: 
1) Realizar o monitoramento de equipamentos 
2) Apresentar os dados coletados de forma que seja possível analisar quais equipamentos possuem maior disponibilidade mostrando também projeções gráficas específicas de equipamentos elecionados. A projeção gráfica utiliza a suavisão dos dados utilizando média móvel exponencial.

## Projeto também é dividido em duas partes: 
1) Os módulos locais ficam na pasta "monitor_transmissor_local" nos arquivos "monitor.py" e "transmissor.py", bastando executar com estes arquivos com o python <arquivo.py> (Python 3 e pip são requisitos básicos para módulos locais e servidor web). 
Estes módulos fazem o monitoramento e transmissão para o servidor. Antes de rodar o transmissor é necessário ter rodado o monitor durante algum tempo, para que existam dados suficientes para análise (20 minutos são suficientes). Para executar estes dois módulos é preciso instalar as  dependências com o comando abaixo dentro da pasta raiz:
- pip install -r requeriments.txt

2) Um servidor web que recebe as informações de todos os equipamentos monitorados, sendo que os arquivos ficam na pasta raiz. O projeto foi desenvolvido utilizando o framework Django com banco de dados Postgresql. Para instalação é preciso seguir os passos abaixo:

- Instalar as dependências com o comando pip install -r requeriments.txt
- Instalar o servidor de banco de dados Postgresql
- Abrir o arquivo config_example.json e alterar as variáveis conforme seu ambiente, ao final o arquivo deve ser renomeado para config.json
- Após isso basta executar o comando python manage.py runserver ip_local:porta (O mesmo do arquivo config.json no parâmetro url_server)
- Ao final é possível acessar no navegador de internet a url do servidor onde será possível verificar as opções disponíveis