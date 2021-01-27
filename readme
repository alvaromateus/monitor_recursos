# Monitor de recursos

##  O Projeto tem dois objetivos: 1) realizar o monitoramento de equipamentos e 2) Apresentar dados coletados de forma que seja possível analisar quais equipamentos com maior disponibilidade mostrando inclusive gráfico com histórico de cada equipamento monitorado. Neste gráfico há a suavisão dos dados utilizando média móvel exponencial.

### Projeto também é dividido em duas partes que roda localmente e outra parte em um servidor web que utiliza o framework Django. 
Os módulos locais ficam na pasta monitor_transmissor_local nos arquivos monitor.py e transmissor.py, bastando executar com o python estes arquivos

A pasta raiz é o projeto Django onde para a instalação necessário ter Python 3 e pip previamente instalado (recomendado criação de ambiente virtual), além dos seguintes passos:

- Instalar as dependências com o comando pip install -r requeriments.txt
- Abrir o arquivo config_example.json e alterar as variáveis conforme seu ambiente, ao final o arquivo deve ser renomeado para config.json
- Após isso basta executar o comando python manage.py runserver ip_local:porta (O mesmo do arquivo config.json no parâmetro url_server)
