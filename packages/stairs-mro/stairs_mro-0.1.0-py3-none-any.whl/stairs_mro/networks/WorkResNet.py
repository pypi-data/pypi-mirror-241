from bamt.networks.hybrid_bn import HybridBN
from operator import itemgetter
from sklearn import preprocessing
import bamt.preprocessors as pp
import numpy as np
import scipy.stats as stats
import math

class WorkResNet(HybridBN):
    def __init__(self, structure):
        super(WorkResNet, self).__init__()
        self.structure = structure

    def fit(self, data):
        encoder = preprocessing.LabelEncoder()
        p = pp.Preprocessor([('encoder', encoder)])
        coded_data, _ = p.apply(data)
        self.add_nodes(p.info)
        self.set_structure(edges=self.structure)
        self.fit_parameters(data) 
        
    def get_res_probability(self, evidence):
        try:
            # sample = self.sample(1000, evidence=evidence)
            # prob_dict = (sample['res_parent'].value_counts() / sample.shape[0]).to_dict()
            probs = self.get_dist('res_parent', evidence)
            vals = self.distributions['res_parent']['vals']
            prob_dict = dict()
            for i, v in enumerate(vals):
                prob_dict[v] = probs[i]
            top_n = dict(sorted(prob_dict.items(), key=itemgetter(1), reverse=True))
            return top_n
        except:
            return {}
        
        
    def get_res_hours(self, evidence, quantile=0.5):
        try:
            # sample = self.sample(1000, evidence=evidence)
            # quntile_value = np.quantile(sample['res_parent_hours'].values,q=quantile)
            mu, var = self.get_dist('res_parent_hours', evidence)
            if var == 0:
                return mu
            elif math.isnan(mu):
                return 0
            else:
                quantile_value = stats.norm.ppf(q=quantile, loc=mu, scale=var)
                return quantile_value
        except:
            return 0
    def get_res_users(self, evidence, quantile=0.5):
        try:
            # sample = self.sample(1000, evidence=evidence)
            # quntile_value = np.quantile(sample['res_parent_users'].values,q=quantile)
            mu, var = self.get_dist('res_parent_users', evidence)
            if var == 0:
                return mu
            elif math.isnan(mu):
                return 0
            else:
                quantile_value = stats.norm.ppf(q=quantile, loc=mu, scale=var)
                return quantile_value
        except:
            return 0


        






