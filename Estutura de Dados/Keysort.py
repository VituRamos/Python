import sys
#==============================Funcoes-de-Ordenacao================================
def QuickSort(vetor,Inicio,Fim):
    
    if Inicio<Fim:
        Pivo = Particiona(vetor,Inicio,Fim)                 #particionar o vetor utilizando pivo
        QuickSort(vetor,Inicio,Pivo-1)
        QuickSort(vetor,Pivo+1,Fim)
    return vetor

def Particiona(vetor,Inicio,Fim):
    
    Esq = Inicio
    Dir = Fim
    Pivo = vetor[Inicio]
        
    while Esq<Dir:
        while vetor[Esq]<=Pivo and Esq<=Fim:
            Esq = Esq+1
        while vetor[Dir]>Pivo and Dir>=Inicio:
            Dir = Dir-1
        if Esq<Dir:
            vetor[Esq],vetor[Dir] = vetor[Dir],vetor[Esq]   
               
    vetor[Dir],vetor[Inicio] = vetor[Inicio],vetor[Dir]
    return Dir
#----------------------------------------------------------------------------------
def Heapify(vetor, tamanho_vetor, i):
    
    maior = i  
    l = 2 * i + 1  
    r = 2 * i + 2  

    if l < tamanho_vetor and vetor[i] < vetor[l]:
        maior = l
    if r < tamanho_vetor and vetor[maior] < vetor[r]:
        maior = r
    if maior != i:
        (vetor[i], vetor[maior]) = (vetor[maior], vetor[i])  
        Heapify(vetor, tamanho_vetor, maior)
  
def HeapSort(vetor):
    tamanho_vetor = len(vetor)
    for i in range(tamanho_vetor // 2 - 1, -1, -1):         #MaxHeap
        Heapify(vetor, tamanho_vetor, i)
    for i in range(tamanho_vetor - 1, 0, -1):               #Extrair elementos e fazer as trocas
        (vetor[i], vetor[0]) = (vetor[0], vetor[i])  
        Heapify(vetor, i, 0)
    return vetor
#----------------------------------------------------------------------------------
def MergeSort(vetor):
    
    if len(vetor)>1:
        
        mid = len(vetor)//2                                 #Dividir vetor
        parte1 = vetor[:mid]
        parte2 = vetor[mid:]

        MergeSort(parte1)                                   #Chamar funcao para cada parte do vetor
        MergeSort(parte2)

        i = 0
        j = 0
        k = 0
        
        while i < len(parte1) and j < len(parte2):
            if parte1[i] < parte2[j]:
                vetor[k]=parte1[i]
                i+=1
            else:
                vetor[k]=parte2[j]
                j+=1
            k+=1
        while i < len(parte1):
            vetor[k]=parte1[i]
            i=i+1
            k=k+1
        while j < len(parte2):
            vetor[k]=parte2[j]
            j=j+1
            k=k+1
    return vetor
#----------------------------------------------------------------------------------
def InsertionSort(vetor):
    
    for i in range(1, len(vetor)):
        aux = vetor[i]
        j = i-1
        while j >= 0 and aux < vetor[j] :
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = aux
    return vetor
#==============================Estrutura-Heroi=====================================
class Heroi:
    def __init__(self):
        self.chave = []
        self.primeiroNome = []
        self.sobrenome = []
        self.nomeHeroi = []
        self.poder = []
        self.fraqueza = []
        self.cidade = []
        self.profissao = []                                                     

    def setHeroi(self, chave, primeiroNome, sobrenome, nomeHeroi, poder, fraqueza, cidade, profissao):
        self.chave.append(chave)
        self.primeiroNome.append(primeiroNome)
        self.sobrenome.append(sobrenome)
        self.nomeHeroi.append(nomeHeroi)
        self.poder.append(poder)
        self.fraqueza.append(fraqueza)
        self.cidade.append(cidade)
        self.profissao.append(profissao)

    def getNome(self, n):
        return (self.primeiroNome[n])

    def getHeroi(self, n):
        return (self.chave[n]+'|'+self.primeiroNome[n]+'|'+self.sobrenome[n]+'|'+self.nomeHeroi[n]+'|'+self.poder[n]+'|'+self.fraqueza[n]+'|'+self.cidade[n]+'|'+self.profissao[n])
    
#==============================Leitura-do-Arquivo==============================
if len(sys.argv) == 3:
    Entrada = open(sys.argv[1],'r')
    Entrada.seek(0,0)                                                                  

    Linha = (Entrada.readline()).replace('\n', '') 
 
    if (Linha == '' or Linha == ' '):                     #Verifica se o arquivo esta vazio                               
        print("ERRO -> Arquivo vazio!")
        exit()
#==============================Cabecalho==========================================
    CabecalhoArqSaida = Linha
    Cabecalho = Linha.split()
    VetorCabecalho = []
    for i in Cabecalho:
        Valor = i.split('=')
        VetorCabecalho.append(Valor[1])
#==============================Registros==========================================
    Registro = Heroi()
    VetorElementos = []    
    for y in range(int(VetorCabecalho[2])):
        LinhaArquivo = (Entrada.readline()).replace('\n', '') 
        
        if (LinhaArquivo == ''):                                   #Verifica se o arquivo esta vazio                            
            print("ERRO -> Nao ha registro no arquivo")
            exit() 
        LinhaArquivo = LinhaArquivo.split('|')
        VetorElementos.append(LinhaArquivo[0])
        Registro.setHeroi(chave=LinhaArquivo[0], primeiroNome=LinhaArquivo[1], sobrenome=LinhaArquivo[2], 
                        nomeHeroi=LinhaArquivo[3], poder=LinhaArquivo[4], fraqueza=LinhaArquivo[5],
                        cidade=LinhaArquivo[6],profissao=LinhaArquivo[7])
        
#==============================Ordenar-Vetor=====================================
    VetorOrdenado = [] 
    #Quick Sort
    if (VetorCabecalho[3] == 'Q'):
        VetorOrdenado = QuickSort(VetorElementos,0,len(VetorElementos)-1)
        
    #Heap Sort
    elif (VetorCabecalho[3] == 'H'):
        VetorOrdenado = HeapSort(VetorElementos)
        
    #Merge Sort
    elif (VetorCabecalho[3] == 'M'):
        VetorOrdenado = MergeSort(VetorElementos)
        
    #Insertion Sort
    elif (VetorCabecalho[3] == 'I'):
        VetorOrdenado = InsertionSort(VetorElementos)
        
    #Caso Erro   
    else:
        print("ERRO -> O sort inserido nao existe")
        exit()
        
#==============================Ordenacao-Vetor=====================================
    if (VetorCabecalho[4] == "D"):
        VetorOrdenado.reverse()
        
    elif (VetorCabecalho[4] != "C"):
        print("ERRO -> A ordenacao inserida nao existe")
        exit()    
#==============================Escrita-Arquivo=====================================
    Saida = open(sys.argv[2],'w')
    Saida.seek(0,0)                                                                    
    Saida.write(CabecalhoArqSaida)
    for l in VetorOrdenado:
        for i in range(int(VetorCabecalho[2])):
            if Registro.chave[i] == str(l):
                RegistroBusca = Registro.getHeroi(i)
                Saida.write('\n'+RegistroBusca)

    Entrada.close()
    Saida.close()    

else:
    print("ERRO -> Quantidade incorreta de argumentos")
    exit()