from bamt.networks.hybrid_bn import HybridBN
from operator import itemgetter
from sklearn import preprocessing
import bamt.preprocessors as pp
import numpy as np
import scipy.stats as stats
import math

class WorkDefectCountNet(HybridBN):
    def __init__(self, structure):
        super(WorkDefectCountNet, self).__init__()
        self.structure = structure

    def fit(self, data):
        encoder = preprocessing.LabelEncoder()
        p = pp.Preprocessor([('encoder', encoder)])
        coded_data, _ = p.apply(data)
        self.add_nodes(p.info)
        self.set_structure(edges=self.structure)
        self.fit_parameters(data) 
        
   
    def get_defect_count(self, evidence, quantile=0.5):
        try:
            # sample = self.sample(1000, evidence=evidence)
            # quntile_value = np.quantile(sample['count'].values,q=quantile)
            mu, var = self.get_dist('count', evidence)
            if var == 0:
                return mu
            elif math.isnan(mu):
                return 0
            else:
                quantile_value = stats.norm.ppf(q=quantile, loc=mu, scale=var)
                return quantile_value
        except:
            return 0

