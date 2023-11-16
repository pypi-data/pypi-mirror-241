from pytest import raises

import numpy as np
import h5py

from ..backend import create_base_dataset
from ..hashtable import Hashtable
from .helpers import setup_vfile
from .. import VersionedHDF5File

def test_hashtable(h5file):
    create_base_dataset(h5file, 'test_data', data=np.empty((0,)))
    with Hashtable(h5file, 'test_data') as h:
        assert len(h) == 0
        h[b'\xff'*32] = slice(0, 1)
        assert len(h) == 1
        assert h[b'\xff'*32] == slice(0, 1)
        assert h.largest_index == 1
        assert bytes(h.hash_table[0][0]) == b'\xff'*32
        assert tuple(h.hash_table[0][1]) == (0, 1)
        assert h == {b'\xff'*32: slice(0, 1)}

        with raises(TypeError):
            h['\x01'*32] = slice(0, 1)
        with raises(ValueError):
            h[b'\x01'] = slice(0, 1)
        with raises(TypeError):
            h[b'\x01'*32] = (0, 1)
        with raises(ValueError):
            h[b'\x01'*32] = slice(0, 4, 2)

def test_from_raw_data():
    with setup_vfile('test.h5') as f:
        vf = VersionedHDF5File(f)
        with vf.stage_version('0') as sv:
            sv.create_dataset('test_data', data=np.arange(100), chunks=(10,))

        h = Hashtable(f, 'test_data')
        h_dataset = h.hash_table_dataset
        h2 = Hashtable.from_raw_data(f, 'test_data',
                                     hash_table_name='test_hash_table')
        h2_dataset = h2.hash_table_dataset
        assert h2_dataset.name == '/_version_data/test_data/test_hash_table'
        np.testing.assert_equal(h_dataset[:], h2_dataset[:])

def test_hashtable_multidimension(h5file):
    # Ensure that the same data with different shape hashes differently
    create_base_dataset(h5file, 'test_data', data=np.empty((0,)))
    h = Hashtable(h5file, 'test_data')
    assert h.hash(np.ones((1, 2, 3,))) != h.hash(np.ones((3, 2, 1)))

def test_issue_208():
    with setup_vfile('test.h5') as f:
        vf = VersionedHDF5File(f)
        with vf.stage_version('0') as sv:
            sv.create_dataset('bar', data=np.arange(10))

    with h5py.File('test.h5', 'r+') as f:
        vf = VersionedHDF5File(f)
        with vf.stage_version('1') as sv:
            sv['bar'].resize((12,))
            sv['bar'][8:12] = sv['bar'][6:10]
            sv['bar'][6:8] = [0, 0]

def test_object_dtype_hashes_values(tmp_path):
    """Test that object dtype arrays hash values, not element ids.

    See https://github.com/deshaw/versioned-hdf5/issues/256 for more
    information.
    """
    filename = tmp_path / "test.h5"
    N = 100
    with h5py.File(filename, mode="w") as f:
        file = VersionedHDF5File(f)
        s = ""
        for i in range(N):
            s += "a"
            arr = np.array([s], dtype=object)

            with file.stage_version(f"r{i}") as group:
                group.create_dataset(
                    "values", shape=(1,), dtype=h5py.string_dtype(length=None), data=arr
            )

    with h5py.File(filename, mode="r") as f:
        file = VersionedHDF5File(f)
        for i in range(N):
            assert file[f"r{i}"]["values"][()] == b"a"*(i+1)


def test_object_dtype_hashes_concatenated_values(tmp_path):
    """Test that object dtype arrays hash values which concatenate
    to the same string to different hashes.
    See https://github.com/deshaw/versioned-hdf5/issues/288.
    """
    filename = tmp_path / "test.h5"
    with h5py.File(filename, mode="w") as f:
        file = VersionedHDF5File(f)
        with file.stage_version("r0") as group:
            group.create_dataset(
                "values",  dtype=h5py.string_dtype(encoding='ascii'),
                data=np.array([b"a", b"b", b"cd"], dtype=object),
                maxshape=(None,), chunks=(100,)
            )
        with file.stage_version("r1") as group:
            group["values"] = np.array([b"ab", b"", b"cd"], dtype=object)
        with file.stage_version("r2") as group:
            group["values"] = np.array([b"ab", b"c", b"d"], dtype=object)

    with h5py.File(filename, mode="r") as f:
        file = VersionedHDF5File(f)
        np.testing.assert_equal(file["r0"]["values"][:], np.array([b"a", b"b", b"cd"], dtype=object))
        np.testing.assert_equal(file["r1"]["values"][:], np.array([b"ab", b"", b"cd"], dtype=object))
        np.testing.assert_equal(file["r2"]["values"][:], np.array([b"ab", b"c", b"d"], dtype=object))
