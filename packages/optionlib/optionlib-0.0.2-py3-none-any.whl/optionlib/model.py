from sklearn.ensemble import GradientBoostingRegressor
from joblib import Parallel, delayed
import pandas as pd
import numpy as np

class Model():
    '''Object for market prediction model'''
    def __init__(self,
                 base_data,
                 horizon,
                 abs_y = True,
                 earnings = None,
                 earnings_window = False,
                 eval_date = None
                ):
        
        self.data = base_data.assign(
            pct_delta_ahead = lambda x: x.Close.pct_change(horizon).shift(-horizon)
        )
        self.horizon = horizon
        
        if eval_date is None:
            self.X = self.data.dropna().filter(regex = 'pct_delta_\d|shiller|T1|VIX|hv|Volume')
            self.y = self.data.dropna()[['pct_delta_ahead']]
            self.X_pred = self.data.filter(regex = 'pct_delta_\d|shiller|T1|VIX|hv|Volume').tail(1)
        else:
            self.X = self.data.dropna().filter(
                regex = 'pct_delta_\d|shiller|T1|VIX|hv|Volume'
            ).iloc[:self.data.index.get_loc(eval_date) - horizon,:]
            self.y = self.data.loc[self.X.index,['pct_delta_ahead']]
            self.X_pred = self.data.filter(regex = 'pct_delta_\d|shiller|T1|VIX|hv|Volume').loc[[eval_date],:]
        
        self.abs_y = abs_y
        self.earnings = earnings
        self.earnings_window = earnings_window
        
        if self.earnings is not None:
            self.X = self.X.join(earnings)
            self.X = self.X.assign(
                earnings_window = lambda x: x.earnings_release[::-1].rolling(horizon,min_periods = 1).max().fillna(0)
            ).drop(columns = 'earnings_release')
            
    
    def fit_quantiles(self,cores = -1):

        if self.earnings is not None:
            self.X_pred['earnings_window'] = int(self.earnings_window)

        def qtile_fit(q):
            mod = GradientBoostingRegressor(loss = 'quantile',alpha = q/100)
            if self.abs_y:
                mod.fit(self.X,self.y.abs().values.ravel())
            else:
                mod.fit(self.X,self.y.values.ravel())
            return mod.predict(self.X_pred)[0]
        
        qtile_out = Parallel(n_jobs=cores,verbose = 10)(delayed(qtile_fit)(i) for i in range(1,100))
        
        qtile_model = pd.DataFrame(
            qtile_out,
            index = [i/100 for i in range(1,100)],
            columns = ['model_qtiles']
        )
        
        if self.abs_y:
            qtile_obs_abs = self.y.abs().rename(columns = {'pct_delta_ahead':'observed_abs'}).quantile(
                [round(i,2) for i in np.linspace(0.01,.99,99)]
            )

            qtile_merge = qtile_model.join(qtile_obs_abs,how = 'outer')

            self.model_qtiles = qtile_merge

            adj_factor = qtile_merge.sum().model_qtiles/qtile_merge.sum().observed_abs

            qtile_obs = self.y.rename(columns = {'pct_delta_ahead':'observed'}).quantile(
                [round(i,2) for i in np.linspace(0.01,.99,99)]
            )

            quantiles = qtile_obs.assign(
                temp = lambda x: (x.observed/x.observed.abs()).fillna(1),
                temp1 = lambda x: x.temp/x.temp.shift(1),
                temp2 = lambda x: x.index.where(x.observed.lt(0))/x.temp1.idxmin(),
                temp3 = lambda x: (x.index.where(x.observed.ge(0))*-1+1)/(1-x.temp1.idxmin()),
                reweighted = lambda x: (x.temp2.mask(x.temp2.isna(),x.temp3)*(adj_factor-1)+1)*x.observed,
                reweighted_tails = lambda x: x.observed*adj_factor
            )
            
            self.quantiles = quantiles[['observed','reweighted','reweighted_tails']]
            self.adj_factor = adj_factor
        else:
            quantiles = self.y.rename(columns = {'pct_delta_ahead':'observed'}).quantile(
                [round(i,2) for i in np.linspace(0.01,.99,99)]
            ).join(qtile_model).rename(columns = {'model_qtiles':'reweighted'})
            
            self.quantiles = quantiles[['observed','reweighted',]]