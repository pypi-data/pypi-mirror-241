import pytest

_ = pytest.importorskip("duckdb.experimental.spark")

from duckdb.experimental.spark.sql.types import Row
import textwrap
import duckdb


class TestSparkReadJson(object):
    def test_read_json(self, spark, tmp_path):
        file_path = tmp_path / 'basic.parquet'
        file_path = file_path.as_posix()
        duckdb.execute(f"COPY (select 42 a, true b, 'this is a long string' c) to '{file_path}' (FORMAT JSON)")
        df = spark.read.json(file_path)
        res = df.collect()
        assert res == [Row(a=42, b=True, c='this is a long string')]
