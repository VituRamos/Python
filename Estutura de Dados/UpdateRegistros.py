from io import SEEK_END, SEEK_SET 
import sys
import re

class Game:
    # construtor do objeto Game
    def __init__(self, titulo=None, produtora=None, genero=None,
        plataforma=None, ano=None, classificacao=None, preco=None,
        midia=None, tamanho=None):
        self.titulo = titulo
        self.produtora = produtora
        self.genero = genero
        self.plataforma = plataforma
        self.ano = ano
        self.classificacao = classificacao
        self.preco = preco
        self.midia = midia
        self.tamanho = tamanho
        
    def __str__(self):
        return f"Titulo: {self.titulo}, Produtora: {self.produtora}, Genero: {self.genero}, Plataforma: {self.plataforma}, Ano: {self.ano}, Classificacao: {self.classificacao}, Preco: {self.preco}, Midia: {self.midia}, Tamanho: {self.tamanho}"

#-----------------------------------------------------------------------------------------------------
def adicionaRegistro(arquivo, game, registros, top):

    with open(arquivo, 'w+') as arquivo_saida:
        
        arquivo_saida.write("REG.N="+str(registros)+" "+"TOP="+str(top)+"\n")
        
        if top == -1:
            arquivo_saida.seek(0, SEEK_END)
            for game in games:
                arquivo_saida.write(f"{game.titulo}|{game.produtora}|{game.genero}|{game.plataforma}|{game.ano}|{game.classificacao}|{game.preco}|{game.midia}|{game.tamanho}|\n")
        else:
            arquivo_saida.seek(0)
            arquivo_saida.seek((top*(top-1)), SEEK_SET)    

    arquivo_saida.close()

#-----------------------------------------------------------------------------------------------------
def LerOperacoes(arquivo, game, registros, top):
    
    removed_games=[]
    
    with open(arquivo, 'r') as arquivo_operacoes:
        for linha in arquivo_operacoes:
            linha = linha.strip()
            if linha:
                operacao, *parametros = linha.split(",")
                
                if operacao == 'd':
                    
                    key = (parametros[0]).strip()
                    removed_games.extend(removeGame(games, key, registros, top))
                       
                elif operacao == 'i':
                    
                    titulo = parametros[0]
                    produtora = parametros[1]
                    genero = parametros[2]
                    plataforma = parametros[3]
                    ano = parametros[4]
                    classificacao = parametros[5]
                    preco = parametros[6]
                    midia = parametros[7]
                    tamanho = parametros[8]
                    game = Game(titulo.strip(), produtora.strip(), genero.strip(), plataforma.strip(), ano.strip(),
                                classificacao.strip(), preco.strip(), midia.strip(), tamanho.strip())
                    adicionaGame(games, game)
                    print(f"Jogo {game.titulo} adicionado com sucesso.")
    
    return removed_games
   
#-----------------------------------------------------------------------------------------------------
def removeGame(games, key, registros, top):
    removed_games = []
    
    for game in games:
        key_comparacao = game.titulo + game.ano
        key_comparacao = ''.join(key_comparacao.split()).upper()

        if key == key_comparacao:
            registros -= 2
            game.titulo = "*" + game.titulo
            removed_games.append(game)
            print(removed_games[0])
            atualiza_temp(games, registros, top, removed_games)
    
    return removed_games
    
#-----------------------------------------------------------------------------------------------------

def adicionaGame(games, game):
    
    if not any(game.titulo + game.ano == g.titulo + g.ano for g in games):
        games.append(game)
        
    return games

#-----------------------------------------------------------------------------------------------------
def atualiza_temp(games, registros, top, removed_games):
    games = [game for game in games if game.titulo is not None]
    adicionaRegistro(sys.argv[3], games+removed_games,registros,top)
#-----------------------------------------------------------------------------------------------------
def storageCompaction(games,registros,top,removed_games):
    games = [game for game in games if game.titulo is not None]
    removed_games = [game for game in games if game.titulo is None]    
    adicionaRegistro(sys.argv[4], games + removed_games,registros,top)
#-----------------------------------------------------------------------------------------------------

def tiraDaLista(games, registros):
    for game in games:
        if game.titulo[0] == '*':
            x = games.index(game)
            games.pop(x)
            registros -=1

    return registros

#-----------------------------------------------------------------------------------------------------

if len(sys.argv) == 5:

    games = []
    removed_games = []
    registros=0
    top=0
    
    with open(sys.argv[1],"r") as arquivo_games:
        
        if arquivo_games == None:
            print("Erro ao abrir o arquivo ",arquivo_games)
            exit()
            
        else:
            for i,linha in enumerate(arquivo_games):
                if i==0:
                    
                    numeros = re.findall(r'-?\d+', linha)
                    registros = int(numeros[0])
                    top = int(numeros[1])
                    
                else:
                    linha = linha.strip()
                    if linha:
                        titulo, produtora, genero, plataforma, ano, classificacao, preco, midia, tamanho = linha.split('|')
                        game = Game(titulo.strip(),produtora.strip(),genero.strip(),plataforma.strip(), ano.strip(),
                                    classificacao.strip(),preco.strip(),midia.strip(), tamanho.strip())
                        games.append(game)

    registros = len(games)
    adicionaRegistro(sys.argv[3], games + removed_games, registros,top)
    removed_games = LerOperacoes(sys.argv[2], games,registros, top)    
    registros = tiraDaLista(games,registros)
    registros = len(games)
    storageCompaction(games,registros,top, removed_games)          
        
else:
    print("Numero de argumentos invalido!")
    
