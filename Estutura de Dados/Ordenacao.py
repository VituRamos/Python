import sys
import random
import time
cont_trocas = 0
ms = 0

#----------------------------------InsertionSort---------------------------------#
def InsertionSort(vetor):
    
    global cont_trocas
    global ms
    
    #comeca pelo segundo elemento
    for i in range(1, len(vetor)):
        
        #auxiliares
        aux = vetor[i]
        j = i-1
        
        #enquanto o numero antecessor for >= 0 e auxiliar for menor que numero na posicao j
        while j >= 0 and aux < vetor[j] :
            
                #proxima posicao do vetor recebe anterior
                vetor[j + 1] = vetor[j]
                j -= 1
                cont_trocas += 1
        
        #insere elemento na posicao correta
        vetor[j + 1] = aux
        
    print("InsertionSort: ",vetor,", ",cont_trocas, "comp, ",end="")
    saida.write("InsertionSort: "+ str(vetor)+ ", "+ str(cont_trocas) +" comp, ")
#--------------------------------------------------------------------------------#

 
#----------------------------------SelectionSort---------------------------------#
def SelectionSort(vetor):

    global cont_trocas
    global ms
    
    #percorrer vetor
    for i in range(0,len(vetor)-1):
    
        #auxiliar
        menor = i
        
        #percorrer vetor elemento+1
        for j in range(i+1, len(vetor)):
    
            #se elemento na posicao j for menor que elemento na posicao menor (achar menor valor)
            if vetor[menor] > vetor[j]:
                
                #menor recebe nova posicao de menor valor
                menor = j
    
    #trocar elemento menor pelo valor inicial
    vetor[i], vetor[menor] = vetor[menor], vetor[i]

    print("SelectionSort: ",vetor,", ",cont_trocas, "comp, ",end="")
    saida.write("SelectionSort: "+ str(vetor)+ ", "+ str(cont_trocas) +" comp, ")
#--------------------------------------------------------------------------------#

 
#------------------------------------BubbleSort----------------------------------#
def BubbleSort(vetor,tamanho_vetor):
    
    global cont_trocas
    global ms
    
    trocou = True

    #enquanto vetor nao estiver ordenado
    while trocou == True:

        trocou = False

        #percorrer vetor
        for i in range(0, tamanho_vetor-1):
          
            #se elemento da prox posicao < anterior
            if vetor[i] > vetor[i + 1]:
                
                #troca elementos
                vetor[i], vetor[i + 1] = vetor[i + 1], vetor[i]
                cont_trocas += 1; 
                trocou = True

    print("BubbleSort: ",vetor,", ",cont_trocas, "comp, ",end="")
    saida.write("BubbleSort: "+ str(vetor)+ ", "+ str(cont_trocas) +" comp, ")
#--------------------------------------------------------------------------------#


#-------------------------------------MergeSort----------------------------------#
def MergeSort(vetor):
    
    global cont_trocas
    global ms
    
    #se vrtor nao for unitario
    if len(vetor)>1:
        
        #dividir vetor
        mid = len(vetor)//2
        parte1 = vetor[:mid]
        parte2 = vetor[mid:]

        #chamar funcao para cada parte do vetor
        MergeSort(parte1)
        MergeSort(parte2)

        #auxiliares
        i = 0
        j = 0
        k = 0
        
        #enquanto i < tamanho da primeira parte do vetor e j < tamanho da segunda parte do vetor
        while i < len(parte1) and j < len(parte2):
            
            #se elemento[i] da primeira parte < elemento[j] da segunda parte, vetor[k] recebe menor elemento da primeira parte
            if parte1[i] < parte2[j]:
                vetor[k]=parte1[i]
                i+=1
                cont_trocas += 1
            
            #senao vetor[k] recebe elemento da segunda parte
            else:
                vetor[k]=parte2[j]
                j+=1
                cont_trocas += 1
                
            #incremento de posicao do novo vetor
            k+=1

        #insere elementos que sobraram da primeira parte no novo vetor
        while i < len(parte1):
            vetor[k]=parte1[i]
            i=i+1
            k=k+1

        #insere elementos que sobraram da segunda parte no novo vetor
        while j < len(parte2):
            vetor[k]=parte2[j]
            j=j+1
            k=k+1
    
def InserirMerge():
    
    MergeSort(vetor_inicial)
    
    print("MergeSort: ",vetor_inicial,", ",cont_trocas, "comp, ",end="")
    saida.write("MergeSort: "+ str(vetor_inicial)+ ", "+ str(cont_trocas) +" comp, ")

#--------------------------------------------------------------------------------#


#-------------------------------------QuickSort----------------------------------#
def QuickSort(vetor,Inicio,Fim):
    
    if Inicio<Fim:
        
        #particionar o vetor utilizando pivo
        Pivo = Particiona(vetor,Inicio,Fim)
        QuickSort(vetor,Inicio,Pivo-1)
        QuickSort(vetor,Pivo+1,Fim)

#Particiona
def Particiona(vetor,Inicio,Fim):
    
        Esq = Inicio
        Dir = Fim
        
        #definir primeiro elemento como pivo
        Pivo = vetor[Inicio]
        
        #enquanto posicao da esquerda for menor que da direita
        while Esq<Dir:
            
            #enquanto elemento da esquerda for <= pivo e posicao da esquerda for menor ou igual ao fim, incrementa posicao esquerda
            while vetor[Esq]<=Pivo and Esq<=Fim:
                Esq = Esq+1
            
            #enquanto elemento da direta for > pivo e posicao da direta for maior ou igual ao inicio, incrementa posicao esquerda
            while vetor[Dir]>Pivo and Dir>=Inicio:
                Dir = Dir-1
            
            #troca elementos de posicao caso encontre um elemento da esquerda > pivo e elemento da direita < vetor
            if Esq<Dir:
                vetor[Esq],vetor[Dir] = vetor[Dir],vetor[Esq]
                cont_trocas += 1
        
        #troca elemento da direta com inicio para nova comparacao        
        vetor[Dir],vetor[Inicio] = vetor[Inicio],vetor[Dir]
        cont_trocas += 1
        
        return Dir

def InserirQuick():
    
    QuickSort(vetor_inicial,0,len(vetor_inicial)-1)
    
    print("QuickSort: ",vetor_inicial,", ",cont_trocas, "comp, ",end="")
    saida.write("QuickSort: "+ str(vetor_inicial)+ ", "+ str(cont_trocas) +" comp, ")


#--------------------------------------------------------------------------------#


#--------------------------------------HeapSort----------------------------------#
def Heapify(vetor, tamanho_vetor, i):
    
    global cont_trocas
    
    #maior elemento comor raiz, esquerda e direita
    maior = i  
    l = 2 * i + 1  
    r = 2 * i + 2  

    #verificar se folha da esquerda é maior que raiz
    if l < tamanho_vetor and vetor[i] < vetor[l]:
        maior = l
  
    #verificar se folha da direita é maior que raiz
    if r < tamanho_vetor and vetor[maior] < vetor[r]:
        maior = r

    #se a raiz nao for o maior elemento, trocar
    if maior != i:
        (vetor[i], vetor[maior]) = (vetor[maior], vetor[i])  
        cont_trocas+=1
        
        #chamar heapfy para raiz
        Heapify(vetor, tamanho_vetor, maior)
  
def HeapSort(vetor):
    
    global cont_trocas
    tamanho_vetor = len(vetor)
  
    #MaxHeap
    for i in range(tamanho_vetor // 2 - 1, -1, -1):
        Heapify(vetor, tamanho_vetor, i)
  
    #Extrair elementos e fazer as trocas
    for i in range(tamanho_vetor - 1, 0, -1):
        (vetor[i], vetor[0]) = (vetor[0], vetor[i])  
        Heapify(vetor, i, 0)
        cont_trocas+=1

    print("HeapSort: ",vetor,", ",cont_trocas, "comp, ",end="")
    saida.write("HeapSort: "+ str(vetor)+ ", "+ str(cont_trocas) +" comp, ")

#--------------------------------------------------------------------------------#

if len(sys.argv) == 3:

    #Abrir arquivo de entrada 
    entrada=open(sys.argv[1],"r")

    #Abrir arquivo de saida
    saida=open(sys.argv[2],"w")

    #Receber dados do arquivo de entrada
    valor = (entrada.readline()).replace('\n','')
    opcao = (entrada.readline()).replace('\n','')

    #Variaveis para calcular ms
    comeco = 0
    fim = 0
    ms = 0

    #Vetor inicial
    vetor_inicial=[]
    tamanho_vetor = int(valor)

    if opcao == "c":
        
        for i in range(tamanho_vetor):
            vetor_inicial.append(i+1)
        
        #Funcao insertion + inserir ms 
        comeco = time.perf_counter()
        InsertionSort(vetor_inicial)
        fim = time.perf_counter()
        
        ms = ((fim-comeco) * 1000)
        print(ms, "ms\n")
        saida.write(str(ms) + " ms\n")
        
        #Funcao selection + inserir ms
        comeco = time.perf_counter()
        SelectionSort(vetor_inicial)
        fim = time.perf_counter()
        
        ms = ((fim-comeco) * 1000)
        print(ms, "ms\n")
        saida.write(str((ms)) + " ms\n")

        #Funcao bubble + inserir ms
        comeco = time.perf_counter()
        BubbleSort(vetor_inicial,tamanho_vetor)
        fim = time.perf_counter()
        
        ms = ((fim-comeco) * 1000)
        print(ms, "ms\n")
        saida.write(str((ms)) + " ms\n")

        #Funcao merge + inserir ms
        comeco = time.perf_counter()
        InserirMerge()
        fim = time.perf_counter()
        
        ms = ((fim-comeco) * 1000)
        print(ms, "ms\n")
        saida.write(str((ms)) + " ms\n")

        #Funcao quick + inserir ms
        comeco = time.perf_counter()
        InserirQuick()
        fim = time.perf_counter()
        
        ms = ((fim-comeco) * 1000)
        print(ms, "ms\n")
        saida.write(str((ms)) + " ms\n")

        #Funcao heap + inserir ms
        comeco = time.perf_counter()
        HeapSort(vetor_inicial)
        fim = time.perf_counter()
        
        ms = ((fim-comeco) * 1000)
        print(ms, "ms\n")
        saida.write(str((ms)) + " ms\n")
        

        #Fechar arquivos 
        entrada.close()
        saida.close()
        exit()

    if opcao == "d":
        
        for i in range(0,tamanho_vetor):
            vetor_inicial.append(tamanho_vetor-i)
        
        #Funcao insertion + inserir ms 
        comeco = time.perf_counter()
        InsertionSort(vetor_inicial)
        fim = time.perf_counter()
        
        ms = ((fim-comeco) * 1000)
        print(ms, "ms\n")
        saida.write(str(ms) + " ms\n")

        #Funcao selection + inserir ms
        comeco = time.perf_counter()
        SelectionSort(vetor_inicial)
        fim = time.perf_counter()
        
        ms = ((fim-comeco) * 1000)
        print(ms, "ms\n")
        saida.write(str((ms)) + " ms\n")

        #Funcao bubble + inserir ms
        comeco = time.perf_counter()
        BubbleSort(vetor_inicial,tamanho_vetor)
        fim = time.perf_counter()
        
        ms = ((fim-comeco) * 1000)
        print(ms, "ms\n")
        saida.write(str((ms)) + " ms\n")

        #Funcao merge + inserir ms
        comeco = time.perf_counter()
        InserirMerge()
        fim = time.perf_counter()
        
        ms = ((fim-comeco) * 1000)
        print(ms, "ms\n")
        saida.write(str((ms)) + " ms\n")

        #Funcao quick + inserir ms
        comeco = time.perf_counter()
        InserirQuick()
        fim = time.perf_counter()
        
        ms = ((fim-comeco) * 1000)
        print(ms, "ms\n")
        saida.write(str((ms)) + " ms\n")

        #Funcao heap + inserir ms
        comeco = time.perf_counter()
        HeapSort(vetor_inicial)
        fim = time.perf_counter()
        
        ms = ((fim-comeco) * 1000)
        print(ms, "ms\n")
        saida.write(str((ms)) + " ms\n")

        #Fechar arquivos 
        entrada.close()
        saida.close()
        exit()

    if opcao == "r":
        
        for i in range(tamanho_vetor):
            vetor_inicial.append(random.randint(0,32000))
        
        #Funcao insertion + inserir ms 
        comeco = time.perf_counter()
        InsertionSort(vetor_inicial)
        fim = time.perf_counter()
        
        ms = ((fim-comeco) * 1000)
        print(ms, "ms\n")
        saida.write(str(ms) + " ms\n")

        #Funcao selection + inserir ms
        comeco = time.perf_counter()
        SelectionSort(vetor_inicial)
        fim = time.perf_counter()
        
        ms = ((fim-comeco) * 1000)
        print(ms, "ms\n")
        saida.write(str((ms)) + " ms\n")

        #Funcao bubble + inserir ms
        comeco = time.perf_counter()
        BubbleSort(vetor_inicial,tamanho_vetor)
        fim = time.perf_counter()
        
        ms = ((fim-comeco) * 1000)
        print(ms, "ms\n")
        saida.write(str((ms)) + " ms\n")

        #Funcao merge + inserir ms
        comeco = time.perf_counter()
        InserirMerge()
        fim = time.perf_counter()
        
        ms = ((fim-comeco) * 1000)
        print(ms, "ms\n")
        saida.write(str((ms)) + " ms\n")

        #Funcao quick + inserir ms
        comeco = time.perf_counter()
        InserirQuick()
        fim = time.perf_counter()
        
        ms = ((fim-comeco) * 1000)
        print(ms, "ms\n")
        saida.write(str((ms)) + " ms\n")

        #Funcao heap + inserir ms
        comeco = time.perf_counter()
        HeapSort(vetor_inicial)
        fim = time.perf_counter()
        
        ms = ((fim-comeco) * 1000)
        print(ms, "ms\n")
        saida.write(str((ms)) + " ms\n")

        #Fechar arquivos 
        entrada.close()
        saida.close()
        exit()

#caso erro
else:
    saida = open("Saida.txt","w")
    saida.write("Numero de argumentos invalido!")
    saida.close()
    exit()
