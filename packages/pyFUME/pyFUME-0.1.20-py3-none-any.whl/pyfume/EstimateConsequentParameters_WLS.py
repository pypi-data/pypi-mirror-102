import numpy as np
from scipy.optimize import curve_fit
from sklearn.linear_model import LinearRegression
import numpy.matlib

class ConsequentEstimator(object):
    def __init__(self, x_train, y_train, partition_matrix):
        self.x_train=x_train
        self.y_train=y_train
        self.partition_matrix=partition_matrix
        
    def suglms(self, x_train, y_train, partition_matrix, global_fit=True, df=0):
        # SUGLMS estimates the consequent parameters in the Sugeno-Takagi model
        #     using least squares.
        #
        #    Input:
        #       X .....    input data matrix
        #        Y .....    output data vector
        #       F ..... fuzzy partition matrix (membership degrees),
        #                optional, defaults to ones(size(y)) for
        #                which SUGLMS is a standard linear regression
        #       DF ... default value returned when the sum of grades
        #               equals to one (optional, defaults to 0)
        #        FLAG .. set to 1 to get local weighted LMS estimates
        #    
        #    Output:
        #       P .....    consequents parameters for every cluster
        #        Ym ....    global model output for the given input data
        #        Yl ....    output of local submodels (corresponding to clusters)
        #        Ylm ...    output of local submodels with data corresponding to
        #               degrees < 0.2 masked with NaN's (for plots)
        #
        #    Example:
        #    x = (0:0.02:1)'; y = sin(7*x);
        #       f = mgrade(x',mfequ(x,2,3))';
        #       [p,ym,yl,ylm] = suglms([x ones(size(x))],y,f);
        #    subplot(211); plot(x,ylm,'.',x,[y ym]); title('Fitting y = sin(7*x)')
        #    subplot(212); plot(x,f); title('Membership functions')
        # (c) Robert Babuska, 1994-95
        
#        x_train=[11,12,13
#                 21,22,23
#                 31,32,33
#                 41,42,43
#                 51,52,53]
#        
#        y_train=[1
#                 2
#                 3
#                 4
#                 5]
#        
#        partition_matrix=[0.2, 0.8
#                          0.4, 0.6
#                          0.6, 0.4
#                          0.8, 0.2
#                          1.0, 0.0]
#        
#        
        x=x_train.copy()
        y=y_train.copy()
        f=partition_matrix.copy()
        
        # Check if input X contains one column of ones (for the constant). If not, add it.
        u=np.unique(x[:,-1])
        if u.shape[0]!=1 or u[0]!=1:
            x = np.hstack((x,np.ones((x.shape[0],1))))
    
        # Find the number of data points (mx & mx) , the number of variables (nx) and the
        # number of clusters (nf) 
        mx,nx=x.shape
        mf,nf=f.shape
        
        # Calculate the sum of the degree of fulfillement (DOF) for each data point
        sumDOF=np.sum(f, 1)
        
        
        # When degree of fulfillment is zero (which means no rule is applicable), set to one
        NoRule = sumDOF == 0
        sumDOF[NoRule] = 1
        sumDOF = np.matlib.repmat(sumDOF,nf,1).T
        
        # Auxillary variables
        f1 = x.flatten()
        s = np.matlib.repmat(f1,nf,1).T
        xx = np.reshape(s, (nx,nf*mx), order='F')
        s = xx.T  
        x1=np.reshape(s,(mx,nf*nx),order='F') 
        x=x.T                                # reshape data matrix
        
        
        if nf == 1:
           global_fit = False
        
        if global_fit == True:                                          # Global least mean squares estimates 
            # (reshaped) vector of f devided by the sum of each row of f
            # (normalised membership degree)
            xx = (f.T.flatten()/sumDOF.T.flatten())
            
            # reshape partition matrix
            s= np.matlib.repmat(xx,nx,1).T
            f1 = np.reshape(s, (mx,nf*nx), order='F')                
            x1 = f1*x1
            y1 = 
        
            # Find least squares solution
#            xp = np.linalg.lstsq(x1,y,rcond=None)
            
            # Perform QR decomposition
            Q,R = np.linalg.qr(x1)          # qr decomposition of x1
            Qy = np.dot(Q.T,y1)             # computing Q^T*b (project y onto the range of x1)
            xx = np.linalg.solve(R,Qy)
            
            
        elif global_fit == False:           # local weighted least mean squares estimates
            # Pre-allocate variable
            p=np.zeros([nf,nx])
            for i in range (0,nf):
                # Weight the points with the cluster membership
                W=np.sqrt(np.diag(f[:,i]))
                x1 = np.dot(W,x)
                y1 = np.dot(W,y)
               
                # Perform QR decomposition
                Q,R = np.linalg.qr(x1)      # qr decomposition of x1
                Qy = np.dot(Q.T,y1)         # computing Q^T*b (project by onto the range of x1)
                
                #perform least-squares
                p[i] = np.linalg.solve(R,Qy)
        return p
    
    def sugfunc(self, x1, x2, a, b, c):
        return a*x1 + b*x2 + c   
    