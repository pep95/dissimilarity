'''
opendb e convert it into a sparse matrix
csr

@author: giusc
'''
import pandas as pd
import numpy as np
from scipy import sparse

class open_db:
    def __init__(self, path,type=1,sep = "\t", columns = ["user_id","item_id","rating","timestamp"] ):
        self.path = path
        self.type = type
        self.sep = sep
        self.columns = columns
    
    def main(self):
        
        '''open db with pandas'''
        tab = pd.read_csv(self.path, sep=self.sep)#,names= self.columns)
        print(tab)
        '''creation of lists: users, items and ratings'''
        users = list(tab["user_id"])
        items = list(tab["item_id"])
        rating = list(tab["rating"])
        
        ''' cretion of vectors rows and cols
        rows = sorted list of users without duplicates
        cols = sorted list of items without duplicates'''
        rows = np.unique(users)
        cols = np.unique(items)
        
        '''for rows and cols I create 2 dicts
        rows_index is a dict formed by key=user_id and key=i-th index that will have in the sparse matrix
        cols_index is a dict formed by key=item_id and key=i-th index that will have in the sparse matrix'''
        i = 0
        rows_index = {}
        for row in rows:
            rows_index[row] = i
            i = i+1
        i = 0
        cols_index = {}
        for col in cols:
            cols_index[col] = i
            i = i+1
        
        '''rate is a dict formed by key=[index_user,index_item] and value=rating'''
        rate = {}
        for i in range(len(users)):
            rate[rows_index[users[i]],cols_index[items[i]]] = rating[i]
        
        
        
        '''I initialize a table (pivot_table) of dimensions [number_rows,number_columns] composed by zeros only'''
        pivot_table = np.zeros((len(rows), len(cols)))
        
        '''I replace the right values of the zeros, in the appropriate places'''
        for key in rate:
            pivot_table[key] = rate[key]
        if self.type==1:
            ''' I convert the pivot_table into csr matrix
            csr is a sparse matrix row-based, like this:
                (895, 421)    3.0
                (895, 422)    3.0
                (895, 424)    2.0
                (895, 425)    2.0 
                '''
            csr = sparse.csr_matrix(pivot_table)
            return csr,rows_index,cols_index
        else:
            ''' I convert the pivot_table into csc matrix
            csc is a sparse matrix column-based, like this:
                (895, 421)    3.0
                (895, 422)    3.0
                (895, 424)    2.0
                (895, 425)    2.0 
                '''
            csr = sparse.csr_matrix(pivot_table)
            return csr,rows_index,cols_index