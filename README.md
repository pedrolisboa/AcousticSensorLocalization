## ASL - Trabalho final

Reprodução dos resultados encontrados para um método em forma fechada de localização de sensores acústicos.

### Configurações

Nessa análise, os resultados estão sendo gerados com Python 3.5. Os arquivos estão no formato ipynb, e podem ser lidos com a aplicação Jupyter Notebook.

```
$ pip install --upgrade pip
$ pip install jupyter
```

A configuração pode ser feita dentro de um virtualenv. O pacote usado para criá-lo foi o virtualenvwrapper

```
$ pip install virtualenvwrapper
$ mkvirtualenv--python=python3.5 nome_venv
```

Para rodar a análise, deve-se instalar os pacotes listados no arquivo requirements.txt.


```
$ pip install -r requirements.txt
```

Deve-se também adicionar um kernel no ipython com o ambiente configurado.

```
$ ipython kernel install --user --name=nome_venv
```

Em seguida, basta rodar o jupyter no diretório do projeto e selecionar os notebooks.

```
$ jupyter notebook
```


## Referências

Haddad, Diego & Nunes, Leonardo & Martins, Wallace & Biscainho, Luiz & Lee, Bowon. (2013). Closed-Form Solutions for Robust Acoustic Sensor Localization. IEEE Workshop on Applications of Signal Processing to Audio and Acoustics. 1-4. 10.1109/WASPAA.2013.6701810. 
