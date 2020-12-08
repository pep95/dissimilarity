'''
proposed metrics
pearson

'''
import numpy as np
class met:
    def __init__(self,a,b,a2,b2,lam=0.5):
        self.a = a
        self.b = b
        self.a2 = a2
        self.b2 = b2
        self.lam = lam
    
    def pcc(self):
        if len(self.b)==0:
            return np.nan
        av_a = np.average(self.a)
        av_b = np.average(self.b)
        
        num = 0
        first_den = 0
        second_den = 0
        
        for i in range(len(self.a)):
            num += (self.a[i]-av_a)*(self.b[i]-av_b)
            first_den += (self.a[i]-av_a)*(self.a[i]-av_a)
            second_den += (self.b[i]-av_b)*(self.b[i]-av_b)
        
        first_den = np.sqrt(first_den)
        second_den = np.sqrt(second_den)
        return round(num/(first_den*second_den),6)
    
    
    def psas(self):
        if len(self.b)==0:
            return np.nan
        av_b = np.average(self.b)
        num = 0
        first_den = 0
        second_den = 0
        
        new_a = np.append(self.a, self.a2)
        new_b = np.append(self.b, self.b2)
        
        av_new_a = np.average(new_a)
        av_new_b = np.average(new_b)
        
        for i in range(len(self.b)):
            num += (self.b[i]-av_b)*(self.b[i]-av_b)
            
        for i in range(len(new_a)):
            first_den += (new_a[i]-av_new_a)*(new_a[i]-av_new_a)
        
        for i in range(len(new_b)):
            second_den += (new_b[i]-av_new_b)*(new_b[i]-av_new_b)
        
        first_den = np.sqrt(first_den)    
        second_den = np.sqrt(second_den)
        
        return round(num/(first_den*second_den),6)
    
    def pfss(self):
        if len(self.b)==0:
            return np.nan
        av_a = np.average(self.a)
        av_b = np.average(self.b)
        
        num = 0
        
        for i in range(len(self.a)):
            num += (self.a[i]-av_a)*(self.b[i]-av_b)
        
        first_den = 0
        second_den = 0
        
        new_a = np.append(self.a, self.a2)
        new_b = np.append(self.b, self.b2)
        
        av_new_a = np.average(new_a)
        av_new_b = np.average(new_b)
        
        for i in range(len(new_a)):
            first_den += (new_a[i]-av_new_a)*(new_a[i]-av_new_a)
        
        for i in range(len(new_b)):
            second_den += (new_b[i]-av_new_b)*(new_b[i]-av_new_b)
        
        first_den = np.sqrt(first_den)    
        second_den = np.sqrt(second_den)
        
        inverse_jaccard = (len(self.a)+len(self.a2)+len(self.b2))/len(self.a)
        
        
        return round((num/(first_den*second_den))*inverse_jaccard,6)
    
    def pad(self):
        if len(self.b)==0:
            return np.nan
        av_a = np.average(self.a)
        av_b = np.average(self.b)
        
        num = 0
        
        for i in range(len(self.a)):
            num += (self.a[i]-av_a)*(self.b[i]-av_b)
        
        first_den = 0
        second_den = 0
        
        new_a = np.append(self.a, self.a2)
        new_b = np.append(self.b, self.b2)
        
        av_new_a = np.average(new_a)
        av_new_b = np.average(new_b)
        
        for i in range(len(new_a)):
            first_den += (new_a[i]-av_new_a)*(new_a[i]-av_new_a)
        
        for i in range(len(new_b)):
            second_den += (new_b[i]-av_new_b)*(new_b[i]-av_new_b)
        
        first_den = np.sqrt(first_den)    
        second_den = np.sqrt(second_den)
        
        return round(((second_den*second_den)-num)/(first_den*second_den),6)
    
    def pfas(self):
        if len(self.b)==0:
            return np.nan
        av_a = np.average(self.a)
        av_b = np.average(self.b)
        
        num = 0
        
        for i in range(len(self.a)):
            num += (self.a[i]-av_a)*(self.b[i]-av_b)
        
        first_den = 0
        second_den = 0
        
        new_a = np.append(self.a, self.a2)
        new_b = np.append(self.b, self.b2)
        
        av_new_a = np.average(new_a)
        av_new_b = np.average(new_b)
        
        for i in range(len(new_a)):
            first_den += (new_a[i]-av_new_a)*(new_a[i]-av_new_a)
        
        for i in range(len(new_b)):
            second_den += (new_b[i]-av_new_b)*(new_b[i]-av_new_b)
        
        first_den = np.sqrt(first_den)    
        second_den = np.sqrt(second_den)
        
        fattore  = (len(self.a)/len(new_a)) * ((2*len(self.a))/(len(new_a)+len(new_b)))
        
       
        return round((num/(first_den*second_den))*fattore,6)
          
        
    def psef(self):
        if len(self.b)==0:
            return np.nan
        av_a = np.average(self.a)
        av_b = np.average(self.b)
        
        num = 0
        
        for i in range(len(self.a)):
            num += (self.a[i]-av_a)*(self.b[i]-av_b)
        
        first_den = 0
        second_den = 0
        
        new_a = np.append(self.a, self.a2)
        new_b = np.append(self.b, self.b2)
        
        av_new_a = np.average(new_a)
        av_new_b = np.average(new_b)
        
        for i in range(len(new_a)):
            first_den += (new_a[i]-av_new_a)*(new_a[i]-av_new_a)
        
        for i in range(len(new_b)):
            second_den += (new_b[i]-av_new_b)*(new_b[i]-av_new_b)
        
        first_den = np.sqrt(first_den)    
        second_den = np.sqrt(second_den)
        
        return round(num/(first_den*second_den),6)
    
    def aapf(self):
        ob = met(self.a,self.b,self.a2,self.b2,self.lam)
        return round(ob.pearson()-(self.lam*ob.psef()),6)
    
    def mapf(self):
        ob = met(self.a,self.b,self.a2,self.b2,self.lam)
        return round(ob.pearson()/ob.psef(),6)
    
    def aaps(self):
        ob = met(self.a,self.b,self.a2,self.b2,self.lam)
        return round(ob.pearson()-(self.lam*ob.pfss()),6)
    
    def maps(self):
        ob = met(self.a,self.b,self.a2,self.b2,self.lam)
        return round(ob.pearson()/ob.pfss(),6)
    
    def aapa(self):
        ob = met(self.a,self.b,self.a2,self.b2,self.lam)
        return round(ob.pearson()-(self.lam*ob.pfas()),6)
    
    def mapa(self):
        ob = met(self.a,self.b,self.a2,self.b2,self.lam)
        return round(ob.pearson()/ob.pfas(),6)
    
    def aapsa(self):
        ob = met(self.a,self.b,self.a2,self.b2,self.lam)
        return round(ob.pearson()-(self.lam*ob.psas()),6)
    
    def mapsa(self):
        ob = met(self.a,self.b,self.a2,self.b2,self.lam)
        return round(ob.pearson()/ob.psas(),6)
    
    def aapad(self):
        ob = met(self.a,self.b,self.a2,self.b2,self.lam)
        return round(ob.pearson()-(self.lam*ob.pad()),6)
    
    def mapad(self):
        ob = met(self.a,self.b,self.a2,self.b2,self.lam)
        return round(ob.pearson()/ob.pad(),6)
    