import urllib.request
import json
url = 'http://educacao.dadosabertosbr.com/api/escolas/buscaavancada?situacaoFuncionamento=1&energiaInexistente=on&aguante=on&esgotoInexistente=on&cozinha=on'
retorno = urllib.request.urlopen(url).read()
retorno = json.loads(retorno.decode('utf-8'))
print('Números de  todas as escolas em funcionamento que não tenham energia, água nem esgoto, e que tenham cozinha ')
#print(retorno) # para imprimir tudo
for escola in retorno[1]:
    print('Nome = {}, Cidade-UF = {}-{}'.
          format(escola['nome'],escola['cidade'],
                 escola['estado']))


