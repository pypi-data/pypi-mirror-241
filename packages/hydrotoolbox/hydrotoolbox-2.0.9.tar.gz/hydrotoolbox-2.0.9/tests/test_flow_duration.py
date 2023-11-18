import pandas as pd
import pytest

from hydrotoolbox import hydrotoolbox


@pytest.mark.parametrize(
    "input_ts, exceedance_probabilities, columns, source_units, start_date, end_date, dropna, clean, round_index, skiprows, index_type, names, target_units, expected",
    [
        # Test ID: 01-01
        # Test Description:
        #    Testing the happy path with realistic values.
        (
            pd.DataFrame({"A": [1, 2, 3, 4, 5]}),
            (99.5, 99, 98, 95, 90, 75, 50, 25, 10, 5, 2, 1, 0.5),
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
            pd.DataFrame(
                {"A": [5, 5, 5, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1]},
                index=[
                    0.995,
                    0.99,
                    0.98,
                    0.95,
                    0.9,
                    0.75,
                    0.5,
                    0.25,
                    0.1,
                    0.05,
                    0.02,
                    0.01,
                    0.005,
                ],
            ),
        ),
        # Test ID: 01-02
        # Test Description:
        #    Testing the edge case where input_ts is an empty DataFrame.
        (
            pd.DataFrame(),
            (99.5, 99, 98, 95, 90, 75, 50, 25, 10, 5, 2, 1, 0.5),
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
            pd.DataFrame(),
        ),
        # Test ID: 01-03
        # Test Description:
        #    Testing the error case where exceedance_probabilities is an empty tuple.
        (
            pd.DataFrame({"A": [1, 2, 3, 4, 5]}),
            (),
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
            pd.DataFrame(),
        ),
    ],
    ids=[
        "happy_path",
        "edge_case_empty_input_ts",
        "error_case_empty_exceedance_probabilities",
    ],
)
def test_flow_duration(
    input_ts,
    exceedance_probabilities,
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
    # Act
    result = hydrotoolbox.flow_duration(
        input_ts=input_ts,
        exceedance_probabilities=exceedance_probabilities,
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
    pd.testing.assert_frame_equal(result, expected)
