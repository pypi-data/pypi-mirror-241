from pytrxmat.trx import TRX
import pandas as pd
import pytest

@pytest.fixture()
def trx():
    return TRX('trx.mat')

def test_open_file(trx :TRX):
    return

def test_key_lists(trx):
    assert(trx.__scalar_features__.intersection(trx.__time_series_features__) == set([]))
    assert(trx.__scalar_features__.union(
           trx.__time_series_features__.union(
           trx.__composite_array_features__.union(
           trx.__string_features__))) == trx.__fields__)

def test_get_scalar(trx :TRX):
    scalar = trx.get('numero_larva_num')
    assert(scalar[0].shape == (1,1))

def test_get_ts(trx :TRX):
    ts = trx.get('y_neck')
    assert(ts[0].shape[1] == 1 and ts[0].shape[0] > 1)

def test_get_multiple_ts(trx :TRX):
    ts = trx.get(['x_tail', 'y_tail'])

def test_get_ts_and_scalar(trx :TRX):
    mixed_array = trx.get(['numero_larva_num', 'x_tail', 'x_spine'])
    print(mixed_array[0].head())

def test_get_bunched_scalar(trx :TRX):
    bunched_scalar = trx.get_composite_array('duration_large')
    print(bunched_scalar[0])
    bunched_scalars = trx.get_composite_array(['duration_large', 'n_duration_large'])
    print(bunched_scalars[0])

def test_get_scalar_list_larvae(trx :TRX):
    scalar = trx.get('numero_larva_num', l=[6,7])

def test_get_ts_list_larvae(trx :TRX):
    ts = trx.get('x_tail', l=[6,7])

def test_get_multiple_ts_list_larvae(trx :TRX):
    print(trx._l)
    ts = trx.get(['x_tail', 'y_tail'], l=[6,7])

def test_get_scalar_slice_larvae(trx :TRX):
    scalar = trx.get('numero_larva_num', l=slice(5))

def test_get_ts_slice_larvae(trx :TRX):
    ts = trx.get('x_tail', l=slice(5))

def test_get_multiple_ts_slice_larvae(trx :TRX):
    ts = trx.get(['x_tail', 'y_tail'], l=slice(5))

def test_get_string(trx: TRX):
    s = trx.get_string(['neuron', 'protocol'])
    print(s[:5])

def test_get_string_asarray_false(trx: TRX):
    s = trx.get_string(['neuron', 'protocol'], asarray=False)
    print(s)

if __name__ == '__main__':
    trx = TRX('trx.mat')
    test_get_scalar_list_larvae(trx)
    test_get_ts_list_larvae(trx)
    test_get_ts_and_scalar(trx)
    test_get_bunched_scalar(trx)
    test_get_string(trx)
    test_get_string_asarray_false(trx)