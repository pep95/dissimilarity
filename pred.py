import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


    
class rec:
    def __init__(self,path_train,path_user_user,n):
          
        '''funcion for create a dict key=user_id ;value= top50neighbors'''
        def neighbor(df,n):
            neighbors = {}
            for col in df.columns:
                df2 = df.drop([int(col)]).sort_values(by=col, ascending=False)
                neighbors[col] = list(df2.index)[:self.n]
            return neighbors
          
        '''function for find rated and not rated items and average of ratings(for each user)'''
        def rated(df):
            users = np.unique(df.index)
            items = np.unique(df["item_id"])
            rated = {}
            not_rated = {}
            averages = {}
            for user in users:
                rated[user] = list(df[df.index==user]["item_id"])
                not_rated[user] = [x for x in items if x not in rated[user]]
                averages[user] = np.average(df[df.index==user]["rating"])
            return rated,not_rated,averages
             
                  
                  
        self.n = n
          
        self.train = pd.read_csv(path_train).drop(columns=["Unnamed: 0"]).set_index("user_id")
          
        self.user_user = pd.read_csv(path_user_user).set_index("users")
          
          
        self.neighbors = neighbor(self.user_user,self.n)
        
        self.rated,self.not_rated,self.averages = rated(self.train)
        
        self.users = np.unique(self.train.index)
        
    def main(self,user):
        
        '''function for calculate prediction'''
        def pred(user,item):
            average = self.averages[user]
            neighbor_rated = [userid for userid in self.neighbors[str(user)] if item in self.rated[userid]] #vicini che hanno votato l'item in questione
            
            if len(neighbor_rated)==0:
                return np.nan
            
            num = 0
            den = 0
            
            for user2 in neighbor_rated:
                num += float(self.user_user[str(user)][self.user_user.index==user2])*(float(self.train[(self.train.index==user2)&(self.train["item_id"]==item)]["rating"]) -self.averages[user2])
                den += float(self.user_user[str(user)][self.user_user.index==user2])
            
            return round(average+(num/den),2)
        
        print(user)
        top = {}
        
        for item in self.not_rated[user]:
            pr = pred(user,item)
            
            if (np.isnan(pr)):
                pass
            else:
                top[item] = pr
        top = {k: v for k, v in sorted(top.items(), key=lambda item: item[1], reverse=True)} #key sorting by descending order of values
        
        us = []
        it = []
        ra = []
        
        for i in range(10):
            us.append(user)
            it.append(list(top.keys())[i])
            ra.append(top[list(top.keys())[i]])
        
        return us,it,ra
        
    def run(self):
        us = []
        it = []
        ra = []
        for user in self.users:
            r = (self.main(user))
            us.append(r[0])
            it.append(r[1])
            ra.append(r[2])
        return us,it,ra
    
if __name__ == '__main__':
    
    path_train = input("insert path of training set file\n")
    print(pd.read_csv(path_train))
    input()
    path_user_user = input("insert path of user user table\n")
    path_output = input("insert path of output file\n")
    n = int(input("insert the number of neighbors\n"))
    

    
    us,it,rat = rec(path_train,path_user_user,n).run()
    
    us_res = []
    it_res = []
    ra_res = []
    for i in range(len(us)):
        us_res += us[i]
        it_res += it[i]
        ra_res += rat[i]
    
    df = pd.DataFrame(data={'user':us_res,'item':it_res,'rating':ra_res})
    print(df)
    df.to_csv(path_output)
    