from unittest.mock import patch

import pytest
from toolbox_utils import tsutils

from hydrotoolbox.hydrotoolbox import indices


# Mocking the tsutils.common_kwds and ind.Indices classes to isolate the function for testing
@patch("hydrotoolbox.hydrotoolbox.tsutils.common_kwds")
@patch("hydrotoolbox.hydrotoolbox.ind.Indices")
def test_indices(mock_indices, mock_common_kwds):
    # Test cases
    test_cases = [
        # Happy path tests
        {
            "test_id": "HP_01",
            "indice_codes": ["MA1", "MA2"],
            "input_ts": "-",
            "water_year": "A-SEP",
            "drainage_area": 1,
            "use_median": False,
            "columns": None,
            "source_units": None,
            "start_date": None,
            "end_date": None,
            "dropna": "no",
            "clean": False,
            "round_index": None,
            "skiprows": None,
            "index_type": "datetime",
            "names": None,
            "target_units": None,
            "expected_result": {
                "MA1: Mean of all daily flows": mock_indices().MA1(),
                "MA2: Median of all daily flows": mock_indices().MA2(),
            },
        },
        # Edge cases
        {
            "test_id": "EC_01",
            "indice_codes": [],
            "input_ts": "-",
            "water_year": "A-SEP",
            "drainage_area": 1,
            "use_median": False,
            "columns": None,
            "source_units": None,
            "start_date": None,
            "end_date": None,
            "dropna": "no",
            "clean": False,
            "round_index": None,
            "skiprows": None,
            "index_type": "datetime",
            "names": None,
            "target_units": None,
            "expected_result": {},
        },
        # Error cases
        {
            "test_id": "EC_01",
            "indice_codes": ["INVALID_CODE"],
            "input_ts": "-",
            "water_year": "A-SEP",
            "drainage_area": 1,
            "use_median": False,
            "columns": None,
            "source_units": None,
            "start_date": None,
            "end_date": None,
            "dropna": "no",
            "clean": False,
            "round_index": None,
            "skiprows": None,
            "index_type": "datetime",
            "names": None,
            "target_units": None,
            "expected_result": {},
            "expected_exception": AttributeError,
        },
    ]

    @pytest.mark.parametrize(
        "test_case",
        test_cases,
        ids=[tc["test_id"] for tc in test_cases],
    )
    def test_indices_parametrized(test_case):
        # Arrange
        mock_common_kwds.return_value = "mocked_flow"
        mock_indices.return_value = "mocked_indices_class"

        # Act
        if "expected_exception" in test_case:
            with pytest.raises(test_case["expected_exception"]):
                result = indices(
                    *test_case["indice_codes"],
                    input_ts=test_case["input_ts"],
                    water_year=test_case["water_year"],
                    drainage_area=test_case["drainage_area"],
                    use_median=test_case["use_median"],
                    columns=test_case["columns"],
                    source_units=test_case["source_units"],
                    start_date=test_case["start_date"],
                    end_date=test_case["end_date"],
                    dropna=test_case["dropna"],
                    clean=test_case["clean"],
                    round_index=test_case["round_index"],
                    skiprows=test_case["skiprows"],
                    index_type=test_case["index_type"],
                    names=test_case["names"],
                    target_units=test_case["target_units"],
                )
        else:
            result = indices(
                *test_case["indice_codes"],
                input_ts=test_case["input_ts"],
                water_year=test_case["water_year"],
                drainage_area=test_case["drainage_area"],
                use_median=test_case["use_median"],
                columns=test_case["columns"],
                source_units=test_case["source_units"],
                start_date=test_case["start_date"],
                end_date=test_case["end_date"],
                dropna=test_case["dropna"],
                clean=test_case["clean"],
                round_index=test_case["round_index"],
                skiprows=test_case["skiprows"],
                index_type=test_case["index_type"],
                names=test_case["names"],
                target_units=test_case["target_units"],
            )

            # Assert
            assert result == test_case["expected_result"]
