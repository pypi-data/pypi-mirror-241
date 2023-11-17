#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2020-2023 Alibaba Group Holding Limited.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import pyarrow as pa

import pytest

try:
    import polars
except ImportError:
    polars = None

from vineyard.core import default_builder_context
from vineyard.core import default_resolver_context
from vineyard.data import register_builtin_types

register_builtin_types(default_builder_context, default_resolver_context)


def test_arrow_array(vineyard_client):
    arr = pa.array([1, 2, None, 3])
    object_id = vineyard_client.put(arr)
    assert arr.equals(vineyard_client.get(object_id))

    arr = pa.array([1, 2.0, None, 3.0])
    object_id = vineyard_client.put(arr)
    assert arr.equals(vineyard_client.get(object_id))

    arr = pa.array([None, None, None, None])
    object_id = vineyard_client.put(arr)
    assert arr.equals(vineyard_client.get(object_id))

    arr = pa.array(["a", None, None, None])
    object_id = vineyard_client.put(arr)
    assert arr.cast(pa.large_string()).equals(vineyard_client.get(object_id))

    arr = pa.array(["a", "bb", "ccc", "dddd"])
    object_id = vineyard_client.put(arr)
    assert arr.cast(pa.large_string()).equals(vineyard_client.get(object_id))

    arr = pa.array([True, False, True, False])
    object_id = vineyard_client.put(arr)
    assert arr.equals(vineyard_client.get(object_id))

    arr = pa.array([True, False, None, None])
    object_id = vineyard_client.put(arr)
    assert arr.equals(vineyard_client.get(object_id))

    nested_arr = pa.array([[], None, [1, 2], [None, 1]])
    object_id = vineyard_client.put(nested_arr)
    assert vineyard_client.get(object_id).values.equals(nested_arr.values)


def test_record_batch(vineyard_client):
    arrays = [
        pa.array([1, 2, 3, 4]),
        pa.array(['foo', 'bar', 'baz', None]),
        pa.array([True, None, False, True]),
    ]
    batch = pa.RecordBatch.from_arrays(arrays, ['f0', 'f1', 'f2'])
    _object_id = vineyard_client.put(batch)  # noqa: F841
    # processing tables that contains string is not roundtrip, as StringArray
    # will be transformed to LargeStringArray
    #
    # assert batch.equals(vineyard_client.get(object_id))


def test_table(vineyard_client):
    arrays = [
        pa.array([1, 2, 3, 4]),
        pa.array(['foo', 'bar', 'baz', None]),
        pa.array([True, None, False, True]),
    ]
    batch = pa.RecordBatch.from_arrays(arrays, ['f0', 'f1', 'f2'])
    batches = [batch] * 5
    table = pa.Table.from_batches(batches)
    _object_id = vineyard_client.put(table)  # noqa: F841
    # processing tables that contains string is not roundtrip, as StringArray
    # will be transformed to LargeStringArray
    #
    # assert table.equals(vineyard_client.get(object_id))


@pytest.mark.skipif(polars is None, reason='polars is not installed')
def test_polars_dataframe(vineyard_client):
    arrays = [
        pa.array([1, 2, 3, 4]),
        pa.array(['foo', 'bar', 'baz', None]),
        pa.array([True, None, False, True]),
    ]
    batch = pa.RecordBatch.from_arrays(arrays, ['f0', 'f1', 'f2'])
    batches = [batch] * 5
    table = pa.Table.from_batches(batches)
    dataframe = polars.DataFrame(table)
    _object_id = vineyard_client.put(dataframe)  # noqa: F841
    # processing tables that contains string is not roundtrip, as StringArray
    # will be transformed to LargeStringArray
    #
    # assert table.equals(vineyard_client.get(object_id))
