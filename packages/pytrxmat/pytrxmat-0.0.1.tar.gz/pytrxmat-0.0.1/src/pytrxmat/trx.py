from h5py import File
import pandas as pd
import numpy as np

__fields__ = set(['As_smooth_5', 'S', 'S_deriv_smooth_5', 'S_smooth_5', 'angle_downer_upper_deriv_smooth_5', 'angle_downer_upper_smooth_5', 'angle_upper_lower_deriv_smooth_5',
                        'angle_upper_lower_smooth_5', 'back', 'back_large', 'back_strong', 'back_weak', 'ball_proba', 'bend_proba', 'cast', 'cast_large', 'cast_strong', 'cast_weak',
                        'curl_proba', 'd_eff_head_norm_deriv_smooth_5', 'd_eff_head_norm_smooth_5', 'd_eff_tail_norm_deriv_smooth_5', 'd_eff_tail_norm_smooth_5', 'duration_large',
                        'duration_large_small', 'eig_deriv_smooth_5', 'eig_smooth_5', 'full_path', 'global_state', 'global_state_large_state', 'global_state_small_large_state',
                        'head_velocity_norm_smooth_5', 'hunch', 'hunch_large', 'hunch_strong', 'hunch_weak', 'id', 'larva_length_deriv_smooth_5', 'larva_length_smooth_5',
                        'motion_to_u_tail_head_smooth_5', 'motion_to_v_tail_head_smooth_5', 'motion_velocity_norm_smooth_5', 'n_duration', 'n_duration_large', 'n_duration_large_small',
                        'nb_action', 'nb_action_large', 'nb_action_large_small', 'neuron', 'numero_larva', 'numero_larva_num', 'pipeline', 'proba_global_state', 'prod_scal_1', 'prod_scal_2',
                        'protocol', 'roll', 'roll_large', 'roll_strong', 'roll_weak', 'run', 'run_large', 'run_strong', 'run_weak', 'small_motion', 'start_stop', 'start_stop_large',
                        'start_stop_large_small', 'stimuli', 'stop', 'stop_large', 'stop_strong', 'stop_weak', 'straight_and_light_bend_proba', 'straight_proba', 't', 't_start_stop',
                        't_start_stop_large', 't_start_stop_large_small', 'tail_velocity_norm_smooth_5', 'x_center', 'x_contour', 'x_head', 'x_neck', 'x_neck_down', 'x_neck_top',
                        'x_spine', 'x_tail', 'y_center', 'y_contour', 'y_head', 'y_neck', 'y_neck_down', 'y_neck_top', 'y_spine', 'y_tail'])
__scalar_features__ = set(['numero_larva_num', 'pipeline'])
__string_features__ = set(['full_path', 'id', 'neuron', 'numero_larva', 'protocol', 'stimuli'])
__composite_array_features__ = set(['duration_large', 'duration_large_small','n_duration', 'n_duration_large', 'n_duration_large_small', 'nb_action', 'nb_action_large', 'start_stop',
                                    'start_stop_large', 'start_stop_large_small', 'nb_action_large_small', 't_start_stop', 't_start_stop_large', 't_start_stop_large_small'])
__time_series_features__ = set(['As_smooth_5', 'S', 'S_deriv_smooth_5', 'S_smooth_5', 'angle_downer_upper_deriv_smooth_5', 'angle_downer_upper_smooth_5', 'angle_upper_lower_deriv_smooth_5',
                                'angle_upper_lower_smooth_5', 'back', 'back_large', 'back_strong', 'back_weak', 'ball_proba', 'bend_proba', 'cast', 'cast_large', 'cast_strong', 'cast_weak',
                                'curl_proba', 'd_eff_head_norm_deriv_smooth_5', 'd_eff_head_norm_smooth_5', 'd_eff_tail_norm_deriv_smooth_5', 'd_eff_tail_norm_smooth_5', 'eig_deriv_smooth_5',
                                'eig_smooth_5', 'global_state', 'global_state_large_state', 'global_state_small_large_state', 'head_velocity_norm_smooth_5', 'hunch', 'hunch_large', 'hunch_strong',
                                'hunch_weak', 'larva_length_deriv_smooth_5', 'larva_length_smooth_5', 'motion_to_u_tail_head_smooth_5', 'motion_to_v_tail_head_smooth_5', 'motion_velocity_norm_smooth_5',
                                'proba_global_state', 'prod_scal_1', 'prod_scal_2', 'roll', 'roll_large', 'roll_strong', 'roll_weak', 'run', 'run_large', 'run_strong', 'run_weak', 'small_motion',
                                'stop', 'stop_large', 'stop_strong', 'stop_weak', 'straight_and_light_bend_proba', 'straight_proba', 't', 'tail_velocity_norm_smooth_5', 'x_center', 'x_contour',
                                'x_head', 'x_neck', 'x_neck_down', 'x_neck_top', 'x_spine', 'x_tail', 'y_center', 'y_contour', 'y_head', 'y_neck', 'y_neck_down', 'y_neck_top', 'y_spine', 'y_tail'])

__feature_type__ = {field:'scalar' if field in __scalar_features__ 
                    else ('string' if field in __string_features__ 
                    else ('timeseries' if field in __time_series_features__
                    else ('composite' if field in __composite_array_features__ 
                    else None))) for field in __fields__}


class TRX:
    __fields__ = __fields__
    __scalar_features__ = __scalar_features__
    __string_features__ = __string_features__
    __composite_array_features__ = __composite_array_features__
    __time_series_features__ = __time_series_features__
    
    __feature_type__ = __feature_type__
    
    __sliceable_feature__ = dict(l='numero_larva_num', t='t')

    def __init__(self, handle, l=None, t=None):
        self._handle = handle
        self._f = File(self._handle)
        self._l = np.array([a.item() for a in self.get_as_array(TRX.__sliceable_feature__['l'])]) if l is None else l
        self._t = [a.flatten() for a in self.get_as_array(TRX.__sliceable_feature__['t'])] if t is None else t
    

    def get_composite_array(self, key):
        '''
        takes a key and builds the array or list of arrays that represent it
        '''
        if isinstance(key, str):
            assert(key in TRX.__composite_array_features__)
            data = [[self._f[ref][()] for ref in self._f[l][:,0]] for l in self._f['trx'][key][0,:]]
            return data
        elif isinstance(key, list):
            larvae = [{} for _ in self._l]
            for k in key:
                assert(k in TRX.__composite_array_features__)
                data = [[self._f[ref][()] for ref in self._f[l][:,0]] for l in self._f['trx'][k][0,:]]
                for dat, l in zip(data, larvae):
                    l[k] = dat
            return larvae
        raise ValueError()
    
    def get_string(self, key, asarray=True):
        '''
        Takes a string feature name or a list of string feature names and returns the features as string, handling the int-to-char conversion.
        If asarray == True (default), returns a string for each larva. Since often the strings are the same for every larva and are actually
        file metadata, one can use asarray == False to get the strings of the first larva.
        '''
        if isinstance(key, str):
            assert(key in TRX.__string_features__)
            if asarray:
                data = ["".join([chr(c) for c in self._f[ref][:,0]]) for ref in self._f['trx'][key][0,:]]
            else:
                data = "".join([chr(c) for c in self._f[self._f['trx'][key][0,0]][:,0]])
            return data
        elif isinstance(key, list):
            larvae = [{} for _ in self._l] if asarray else {}
            for k in key:
                assert(k in TRX.__string_features__)
                if asarray:
                    data = ["".join([chr(c) for c in self._f[ref][:,0]]) for ref in self._f['trx'][k][0,:]]
                    for dat, l in zip(data, larvae):
                        l[k] = dat
                else:
                    data = "".join([chr(c) for c in self._f[self._f['trx'][k][0,0]][:,0]])
                    larvae[k] = data
            return larvae
        raise ValueError()
    
    def get_as_array(self, key, **kwargs):
        '''
            Returns a list of arrays containing the features requested in key, one per larva, with optional selection of a subset of larvae or a subset of times.
            Signature :
                key:str|list(str), [l:slice|array_like], [t:tuple(float, float)|tuple(float, int)|tuple(int, float)] -> list(array_like)
            - Key can be the name of a time series or scalar feature in trx.mat files or a list of such names.
            - Larvae selection is performed using the l keyword argument. l can either be a slice or a subset of larva_numero_num.
            - Time selection is performed using the t keyword argument. The behavior depends on the precise datatypes :
                * tuple(float, float) : return all times t_sel such that t[0] <= t_sel < t[1].
                * tuple(float, int) : return up to t[1] points after the intial time t[0].
                * tuple(int, float) : return up to t[0] points before the finalal time t[1].

                There is no guarantee that the shapes are the same across larvae due to missing data.
                If no points verify the condition, returns an array whith second dimension equal to 0.

            The shape of the returned arrays is 
                - (num_features, 1) if only scalars were requested
                - (num_features, time) if only time series were requested
                - (num_features, time) if scalar arrays and time series were requested, where scalars are broadcasted to match the time axis
        '''
        l_arg = kwargs['l'] if 'l' in kwargs else slice(None)
        indexer = l_arg if isinstance(l_arg, slice) else np.argwhere(np.isin(self._l, l_arg)).flatten()

        
        columns = []
        # feature selection
        if isinstance(key, str):
            assert(key in TRX.__time_series_features__.union(TRX.__scalar_features__))
            refs = self._f['trx'][key]
            arrays = [self._f[ref][:] for ref in refs[0,indexer]]
            if key == 'numero_larva_num':
                arrays = [a.astype(int) for a in arrays]
            columns.append(arrays[0].shape[0])

        elif isinstance(key, list):
            to_stack = []
            for k in key:
                assert(k in TRX.__time_series_features__.union(TRX.__scalar_features__))
                arrays = self.get_as_array(k, l=l_arg)
                if to_stack == []:
                    to_stack = [[] for _ in arrays]
                for a, aa in zip(arrays, to_stack):
                    aa.append(a)
                columns.append(arrays[0].shape[0])

            broadcast_scalars = any([k in self.__scalar_features__ for k in key])
            if broadcast_scalars:
                to_stack = [[np.broadcast_to(a, (1, t.shape[0])) if k in TRX.__scalar_features__ else a for a, k in zip(aa, key)] for t, aa in zip(self._t[l_arg], to_stack) ]
            arrays = [np.vstack(aa) for aa in to_stack]

        # time slicing
        if 't' in kwargs:
            t1, t2 = kwargs['t']
            if isinstance(t1, float) and isinstance(t2, float):
                arrays = [a[:, np.logical_and(t >= t1, t < t2)] for a, t in zip(arrays, self._t[indexer])]
            elif isinstance(t1, float) and isinstance(t2, int):
                start_points = [np.min(np.where(t >= t1)) if (t >= t1).any() else None for t in self._t[indexer]]
                arrays = [a[:, s:s+t2] if s is not None else np.empty((a.shape[0],0)) for a, s in zip(arrays, start_points)]
            elif isinstance(t1, int) and isinstance(t2, float):
                raise NotImplementedError()
            else:
                raise ValueError("'t' can only be of type Tuple(float, float), Tuple(float, int), or Tuple(int, float)")

        if 'return_columns' in kwargs and kwargs['return_columns']:
            return arrays, columns
        return arrays
    
    def get_as_df(self, key, **kwargs):
        '''
            Returns a list of dataframes containing the features requested in key, with optional selection of a subset of larvae or a subset of times.
            Signature :
                key:str|list(str), [l:slice|array_like], [t:tuple(float, float)|tuple(float, int)|tuple(int, float)] -> list(array_like)
            - Key can be the name of a time series or scalar feature in trx.mat files or a list of such names.
            - Larvae selection is performed using the l keyword argument. l can either be a slice or a subset of larva_numero_num.
            - Time selection is performed using the t keyword argument. The behavior depends on the precise datatypes :
                * tuple(float, float) : return all times t_sel such that t[0] <= t_sel < t[1].
                * tuple(float, int) : return up to t[1] points after the intial time t[0].
                * tuple(int, float) : return up to t[0] points before the finalal time t[1].

                There is no guarantee that the shapes are the same across larvae due to missing data.
                If no points verify the condition, returns an array whith second dimension equal to 0.
        '''
        arrays, columns = self.get_as_array(key, return_columns=True, **kwargs)
        if isinstance(key, str) and key in TRX.__fields__:
            key = [key]
        key = sum([[k+f'_{i}' for i in range(c)] if c>1 else [k] for c, k in zip(columns, key)], [])
        dataframes = [pd.DataFrame(data=a.transpose(), columns=key) for a in arrays]
        return dataframes
    
    def get(self, key, **kwargs):
        '''
            Alias for get_as_df.
        '''
        return self.get_as_df(key, **kwargs)