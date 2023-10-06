import sys
#------------------------------------Estrutura-Musicas------------------------------------#
class Musicas:
    def __init__(self):
        self.ano = []
        self.duracao=[]
        self.titulo=[]
        self.artista=[]
        self.genero=[]
        self.idioma=[]
        self.n = 0
    
    def setMusicas(self,ano,duracao,titulo,artista,genero,idioma):
        self.ano.append(ano)
        self.duracao.append(duracao)
        self.titulo.append(titulo)
        self.artista.append(artista)
        self.genero.append(genero)
        self.idioma.append(idioma)
        self.n = self.n+1 
        
    def getMusicas(self,n):
        return(self.ano[n]+"|"+self.duracao[n]+"|"+self.titulo[n]+"|"+self.artista[n]+
               "|"+self.genero[n]+"|"+self.idioma[n])
    
#------------------------------------Abrir-Arquivos------------------------------------#  
if len(sys.argv) == 4:
    
    ArquivoMusicas = open(sys.argv[1],"r")
    ArquivoMusicas.seek(0,0)

    ArquivoConsulta = open(sys.argv[2],"r")
    ArquivoConsulta.seek(0,0)

    ArquivoSaida = open(sys.argv[3],"w")
    ArquivoSaida.seek(0,0)
#------------------------------------Leitura-Arquivo-Musicas------------------------------------#      
    LinhaArquivoMusicas = ArquivoMusicas.readline().replace("\n","")

    if (LinhaArquivoMusicas==""):                                           #verifica se o arquivo esta vazio
        print("Arquivo de musicas vazio!")
        exit()
        
#------------------------------------Leitura-Arquivo-Consulta-----------------------------------#    
    LinhaArquivoConsulta = ArquivoConsulta.readline().replace("\n","")
    if (LinhaArquivoConsulta == ""):
        print("Arquivo de consulta vazio!")
        exit()
    Categoria = LinhaArquivoConsulta

    LinhaArquivoConsulta = ArquivoConsulta.readline().replace("\n","")
    if (LinhaArquivoConsulta == ""):
        print("Arquivo esta incompleto!")
        exit() 
    SubCategoria = LinhaArquivoConsulta

#------------------------------------Cabecalho------------------------------------# 
    Cabecalho = LinhaArquivoMusicas.split()
    VetorCabecalho = []

    for campo in Cabecalho:
        Dados = campo.split("=")
        VetorCabecalho.append(Dados[1])                                 #VetorCabecalho[n]->Size,Top,Qtde,Status

#------------------------------------Registro-Musicas-----------------------------------# 
    Registro = Musicas()
    Aux = False

    for quantidadeMusicas in range(int(VetorCabecalho[2])):
        LinhaArquivoMusicas = ArquivoMusicas.readline().replace("\n","")
        LinhaArquivoMusicas = LinhaArquivoMusicas.split("|")
        Registro.setMusicas(ano=LinhaArquivoMusicas[0],duracao=LinhaArquivoMusicas[1],titulo=LinhaArquivoMusicas[2],
                        artista=LinhaArquivoMusicas[3],genero=LinhaArquivoMusicas[4],idioma=LinhaArquivoMusicas[5])

#------------------------------------Condicoes-de-Busca---------------------------------# 

    if Categoria.upper() == "ANO":
        for quantidadeMusicasBusca in range(int(VetorCabecalho[2])):         #
            if (Registro.ano[quantidadeMusicasBusca] == SubCategoria):
                RegistroConsulta = Registro.getMusicas(quantidadeMusicasBusca)
                print(RegistroConsulta)
                ArquivoSaida.write(RegistroConsulta+"\n")
                Aux = True
                
    elif Categoria.upper() == "DURACAO":
        for quantidadeMusicasBusca in range(int(VetorCabecalho[2])):
            if (Registro.duracao[quantidadeMusicasBusca] == SubCategoria):
                RegistroConsulta = Registro.getMusicas(quantidadeMusicasBusca)
                print(RegistroConsulta)
                ArquivoSaida.write(RegistroConsulta+"\n")
                Aux = True
                
    elif Categoria.upper() == "TITULO":
        for quantidadeMusicasBusca in range(int(VetorCabecalho[2])):
            if (Registro.titulo[quantidadeMusicasBusca] == SubCategoria):
                RegistroConsulta = Registro.getMusicas(quantidadeMusicasBusca)
                print(RegistroConsulta)
                ArquivoSaida.write(RegistroConsulta+"\n")
                Aux = True
                
    elif Categoria.upper() == "ARTISTA":
        for quantidadeMusicasBusca in range(int(VetorCabecalho[2])):
            if (Registro.artista[quantidadeMusicasBusca] == SubCategoria):
                RegistroConsulta = Registro.getMusicas(quantidadeMusicasBusca)
                print(RegistroConsulta)
                ArquivoSaida.write(RegistroConsulta+"\n")
                Aux = True
                
    elif Categoria.upper() == "GENERO":
        for quantidadeMusicasBusca in range(int(VetorCabecalho[2])):
            if (Registro.genero[quantidadeMusicasBusca] == SubCategoria):
                RegistroConsulta = Registro.getMusicas(quantidadeMusicasBusca)
                print(RegistroConsulta)
                ArquivoSaida.write(RegistroConsulta+"\n")
                Aux = True
                
    elif Categoria.upper() == "IDIOMA":
        for quantidadeMusicasBusca in range(int(VetorCabecalho[2])):
            if (Registro.idioma[quantidadeMusicasBusca] == SubCategoria):
                RegistroConsulta = Registro.getMusicas(quantidadeMusicasBusca)
                print(RegistroConsulta)
                ArquivoSaida.write(RegistroConsulta+"\n")
                Aux = True
                
    else:
        print("Parametro informado nao existe")
        
    if Aux == False:
        print("Nenhum registro da categoria"+Categoria+"encontrado\n")
        ArquivoSaida.write("Nenhum registro da categoria"+Categoria+"encontrado\n")
        
#------------------------------------Fechar-Arquivos---------------------------------# 
    ArquivoMusicas.close()
    ArquivoConsulta.close()
    ArquivoSaida.close()
    
else:
    print("Quantidade incorreta de argumentos!")
    exit()