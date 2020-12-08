from github.open_db import open_db
import pandas as pd
import numpy as np
from scipy import sparse
from metriche import met

import warnings
warnings.filterwarnings("ignore")

class sparse_matrix:
    def __init__(self,dict_rows,dataset,metric,lam=0.5):
        self.dict_rows = dict_rows
        self.dataset = dataset
        self.metric = metric
        self.lam = lam
        
        
    def calc(self,user1):
        
        
        '''funzione per trovare i vettori a,b,a_2,b_2 
            a,b (intersezione) come utente1 ed utente2 hanno votato gli stessi item
            a_2 restanti voti di utente1
            b_2 restanti voti di utente2'''
        def find_vectors(id_user1,id_user2,dataset):
            a = []
            b = []
             
            indexes_1 = dataset[id_user1].indices
            indexes_2 = dataset[id_user2].indices
            
            intersection = np.intersect1d(indexes_1, indexes_2)
            
            for index in intersection:
                a.append(dataset[id_user1,index])
                b.append(dataset[id_user2,index])
            
            a_2 = [dataset[id_user1,index] for index in dataset[id_user1].indices if index not in intersection]
            b_2 = [dataset[id_user2,index] for index in dataset[id_user2].indices if index not in intersection]
            
            return a,b,a_2,b_2 
        
        '''adesso inizio il calcolo, per ogni utente, prendo la relativa riga,
        e confronto con ogni altro utente, al termine inserisco i valori nella
        riga del rispettivo dataframe '''
        print(user1)
        row1 = self.dict_rows[user1]
        
        sim = {}
        
        
        '''ciclo per il secondo utente, da confrontare con il primo'''
        for user2 in self.dict_rows:
            row2 = self.dict_rows[user2]
            
            '''con la funzione find_vectors trovo i vettori a,b_a_2,b_2, dove:
            a,b sono i vettori contenenti i voti dati da user1 e user2 agli stessi items
            a_2 e' il vettore contenente i restanti voti di user1
            b_2 e' il vettore contenente i restanti voti di user2'''
            a,b,a_2,b_2 = find_vectors(row1,row2,self.dataset)
        
            
            sim[user2] = getattr(met(a,b,a_2,b_2,self.lam), self.metric)() #calcolo similarita
            

        '''faccio ritornare tutti i valori necessari'''
        #return [user1,sim_pearson,sim_prima,sim_seconda,sim_terza]
        return [user1,sim]
        
    
    
    '''con run faccio il multiprocessing, avviando un pool per ogni utente'''
    def run(self,users):
        rs = map(self.calc,users)
        return rs


if __name__ == '__main__':
    
    '''apro training movielens con class opendb 100k con pandas'''
    #tab = pd.read_csv(r"C:\Users\giusc\eclipse-workspace\tesi\u.data",sep="\t",names=["user_id","item_id","rating","timestamp"])
    #tab = pd.read_csv(r"C:\Users\giusc\eclipse-workspace\tesi\test1\train_movielens.csv",sep=",")
    input_path = input("Insert input path :\n")
    output_path = input("Insert output path :\n")
    metric = input("Wich metric do you want to use?\n")
    lam = float(input("select the value of lambda"))
    csr,rows_index,cols_index = open_db(input_path,type=1,sep=",").main()
    
    '''inizializzo i dataframe per i risultati, uno per ogni formula'''
    sim = {"users":rows_index.keys()}
    final_table = pd.DataFrame(data=sim)
    final_table = final_table.set_index("users")
    
    
    '''richiamo la classe sparse_matrix per il calcolo'''
    a = sparse_matrix(rows_index,csr,metric,lam).run(rows_index)
    
    
    '''inserisco i valori nella tabella finale'''
    for obj in a:
        user = obj[0]
        final_table[user] = obj[1].values()

    
    
    '''mostro a schermo le tabelle finali e le salvo in file csv'''
    
    print(final_table)
    final_table.to_csv(output_path)