Simport numpy as np

from .SimpfulModelBuilder import SugenoFISBuilder
from .Clustering import Clusterer
from .EstimateAntecendentSet import AntecedentEstimator
from .EstimateConsequentParameters import ConsequentEstimator
from .Tester import SugenoFISTester


x_train=np.array(range(105))

class ClusterChoser(object):
    def __init__(self, x_train, y_train, k_cross_val=10):
        self.x_train=x_train
        self.y_train=y_train
        
        def determineNumberClusters(self, x_train, y_train, k_cross_val=10, min_clusters=2, max_clusters=20, **kwargs):
            # shuffle data
            idx=np.arange(len(x_train))
            np.random.shuffle(idx)
            
            # split in k groups
            folds = np.array_split(idx,k_cross_val)
            
            # create an object of class Clusterer and set the required settings
            cl = Clusterer(self.x_train, self.y_train, nr_clus=0)
        
            if 'cluster_method' not in kwargs.keys(): kwargs['cluster_method'] = 'fcm'
        
            if kwargs['cluster_method'] == 'fcm':
                if 'fcm_m' not in kwargs.keys(): kwargs['fcm_m'] = 2
                if 'fcm_max_iter' not in kwargs.keys(): kwargs['fcm_maxiter'] = 1000
                if 'fcm_error' not in kwargs.keys(): kwargs['fcm_error'] = 0.005
    
            elif kwargs['cluster_method'] == 'fstpso':
                if 'fstpso_n_particles' not in kwargs.keys(): kwargs['fstpso_n_particles'] = None
                if 'fstpso_maxiter' not in kwargs.keys(): kwargs['fstpso_maxiter'] = 100
                if 'fstpso_path_fit_dump' not in kwargs.keys(): kwargs['fstpso_path_fit_dump'] = None
                if 'fstpso_path_sol_dump' not in kwargs.keys(): kwargs['fstpso_path_sol_dump'] = None
                
            if 'mf_shape' not in kwargs.keys(): kwargs['mf_shape'] = 'gauss'
            if 'global_fit' not in kwargs.keys(): kwargs['global_fit'] = True 
            if 'save_simpful_code' not in kwargs.keys(): kwargs['save_simpful_code'] = False
            if 'operators' not in kwargs.keys(): kwargs['operators'] = None
            
            for c in range (min_clusters,max_clusters):
                cl.nr_clus=c
                for k in range(0,k_cross_val): 
                    # select the indices used for validation
                    idx_val = folds[k]
                    
                    # Use other indices for training
                    idx_train = list(set(range(len(idx))) - set(idx_val))
                    
                    # Select training data for this interation
                    trx=np.array(idx_train)
                    cl.x_train=x_train[trx]
                    cl.y_train=x_train[trx]

                    # Cluster the training data (in input-output space) using FCM or FST-PSO
                    if kwargs['cluster_method'] == 'fcm':
                        self.cluster_centers, self.partition_matrix, _ = cl.cluster(cluster_method='fcm', fcm_m=kwargs['fcm_m'], 
                                                                                    fcm_maxiter=kwargs['fcm_maxiter'], fcm_error=kwargs['fcm_error'])
                    elif kwargs['cluster_method'] == 'fstpso':
                        self.cluster_centers, self.partition_matrix, _ = cl.cluster(cluster_method='fstpso', 
                                                                                    fstpso_n_particles=kwargs['fstpso_n_particles'], fstpso_max_iter=kwargs['fstpso_max_iter'],
                                                                                    fstpso_path_fit_dump=kwargs['fstpso_path_fit_dump'], fstpso_path_sol_dump=kwargs['fstpso_path_sol_dump'])
                    
                    # Estimate the membership funtions of the system (default shape: gauss)
                    self._antecedent_estimator = AntecedentEstimator(self.x_train, self.partition_matrix)
                    self.antecedent_parameters = self._antecedent_estimator.determineMF(mf_shape=kwargs['mf_shape'], merge_threshold=merge_threshold)
                    what_to_drop = self._antecedent_estimator._info_for_simplification
        
                    # Estimate the parameters of the consequent (default: global fitting)
                    ce = ConsequentEstimator(self.x_train, self.y_train, self.partition_matrix)
                    self.consequent_parameters = ce.suglms(self.x_train, self.y_train, self.partition_matrix, 
                                               global_fit=kwargs['global_fit'])
        
                    # Build a first-order Takagi-Sugeno model using Simpful
                    simpbuilder = SugenoFISBuilder(
                            self.antecedent_parameters, 
                            self.consequent_parameters, 
                            self.variable_names, 
                            extreme_values = self._antecedent_estimator._extreme_values,
                            operators=kwargs["operators"], 
                            save_simpful_code=kwargs['save_simpful_code'], 
                            fuzzy_sets_to_drop=what_to_drop)

                    self.model = simpbuilder.simpfulmodel

            
            
            
            