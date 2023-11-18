import pandas as pd
import pytest
from toolbox_utils import tsutils

from hydrotoolbox.hydrotoolbox import recession


@pytest.mark.parametrize(
    "input_ts, columns, source_units, start_date, end_date, dropna, clean, round_index, skiprows, index_type, names, target_units, expected",
    [
        # Test ID: 1-1
        # Test Description:
        # Happy path test with realistic values.
        (
            "-",
            None,
            None,
            None,
            None,
            "no",
            False,
            None,
            None,
            "datetime",
            None,
            None,
            {"col1": [0.5]},
        ),
        # Test ID: 1-2
        # Test Description:
        # Edge case with empty input time series.
        (
            "",
            None,
            None,
            None,
            None,
            "no",
            False,
            None,
            None,
            "datetime",
            None,
            None,
            {},
        ),
        # Test ID: 1-3
        # Test Description:
        # Error case with non-existing input time series.
        (
            "non_existing_file",
            None,
            None,
            None,
            None,
            "no",
            False,
            None,
            None,
            "datetime",
            None,
            None,
            pytest.raises(FileNotFoundError),
        ),
    ],
    ids=["happy_path", "edge_empty_input", "error_non_existing_file"],
)
def test_recession(
    input_ts,
    columns,
    source_units,
    start_date,
    end_date,
    dropna,
    clean,
    round_index,
    skiprows,
    index_type,
    names,
    target_units,
    expected,
):
    # Arrange
    # Mocking tsutils.read_iso_ts to return a DataFrame with a single column and a single row.
    tsutils.read_iso_ts = lambda *args, **kwargs: pd.DataFrame({"col1": [1.0]})
    tsutils.common_kwds = lambda *args, **kwargs: pd.DataFrame({"col1": [1.0]})

    # Act
    result = recession(
        input_ts=input_ts,
        columns=columns,
        source_units=source_units,
        start_date=start_date,
        end_date=end_date,
        dropna=dropna,
        clean=clean,
        round_index=round_index,
        skiprows=skiprows,
        index_type=index_type,
        names=names,
        target_units=target_units,
    )

    # Assert
    assert result == expected
