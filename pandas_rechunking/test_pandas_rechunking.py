import solution as s
import pandas as pd
from pandas.testing import assert_frame_equal
import pytest
from itertools import islice

@pytest.fixture
def dataframes():
    df0 = pd.DataFrame({'A': [1, 2, 3]})
    df1 = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6]})
    df2 = pd.DataFrame({'A': [1, 2]})
    df3 = pd.DataFrame({'A': [3, 4, 5]})
    df4 = pd.DataFrame({'A': [6, 7, 8, 9]})
    df5 = pd.DataFrame({'A': [1, 2, 3, 4]})
    df6 = pd.DataFrame({'A': [5, 6, 7, 8]})
    df7 = pd.DataFrame({'A': [9, 10, 11, 12]})
    df8 = pd.DataFrame()
    df9 = pd.DataFrame()
    return [df0, df1, df2, df3, df4, df5, df6, df7, df8, df9]


def test_single_dataframe_smaller_than_fixed_size(dataframes):
    # arrange
    dataframes = [dataframes[0]]
    fixed_size = 5
    expected_output = [pd.DataFrame({'A': [1, 2, 3]})]

    # act
    output = list(s.rechunk_dataframes(dataframes, fixed_size))

    # assert
    assert len(output) == len(expected_output)
    for out, exp in zip(output, expected_output):
        assert_frame_equal(out, exp)

def test_single_dataframe_larger_than_fixed_size(dataframes):
    # arrange
    dataframes = [dataframes[1]]
    fixed_size = 4
    expected_output = [pd.DataFrame({'A': [1, 2, 3, 4]}), pd.DataFrame({'A': [5, 6]})]

    # act
    output = list(s.rechunk_dataframes(dataframes, fixed_size))

    # assert
    assert len(output) == len(expected_output)
    for out, exp in zip(output, expected_output):
        assert_frame_equal(out, exp)


def test_multiple_dataframes_combined_length_smaller_than_fixed_size(dataframes):
    # arrange
    dataframes = dataframes[2:5]
    fixed_size = 10
    expected_output = [pd.concat(dataframes, ignore_index=True)]
    
    # act
    output = list(s.rechunk_dataframes(dataframes, fixed_size))

    # assert
    assert len(output) == len(expected_output)
    for out, exp in zip(output, expected_output):
        assert_frame_equal(out, exp)


def test_multiple_dataframes_combined_length_larger_than_fixed_size(dataframes):
    # arrange
    dataframes = dataframes[5:8]
    fixed_size = 6
    expected_output = [pd.DataFrame({'A': [1, 2, 3, 4, 5, 6]}), pd.DataFrame({'A': [7, 8, 9, 10, 11, 12]})]

    # act
    output = list(s.rechunk_dataframes(dataframes, fixed_size))

    # assert
    assert len(output) == len(expected_output)
    for out, exp in zip(output, expected_output):
        assert_frame_equal(out, exp)


def test_empty_dataframes(dataframes):
    # arrange
    dataframes = dataframes[8:10]
    fixed_size = 5
    expected_output = []
    
    # act
    output = list(s.rechunk_dataframes(dataframes, fixed_size))

    # assert
    assert len(output) == len(expected_output)
    for out, exp in zip(output, expected_output):
        assert_frame_equal(out, exp)


def test_multi_column_dataframes(dataframes):
    # arrange
    df1 = pd.DataFrame({
        'Name': ['John', 'Jane', 'Mike', 'Emily'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'London', 'Paris', 'Sydney']
    })

    df2 = pd.DataFrame({
        'Name': ['Alex', 'Bob'],
        'Age': [25, 30],
        'City': ['Chicago', 'Madrid']
    })

    df3 = pd.DataFrame({
        'Name': ['Jack', 'Peter', 'Paul', 'Jacob', 'Isaac', 'Carl', 'Simon', 'Emmy'],
        'Age': [25, 30, 35, 28, 23, 12, 45, 19],
        'City': ['New York', 'London', 'Paris', 'Sydney', 'Washington', 'Cannes', 'Edinburgh', 'Birmingham']
    })

    dataframes = [df1, df2, df3]
    fixed_size = 3
    expected_output = [pd.DataFrame({
        'Name': ['John', 'Jane', 'Mike'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']
        }),
        pd.DataFrame({
            'Name': ['Emily', 'Alex', 'Bob'],
            'Age': [28, 25, 30],
            'City': ['Sydney', 'Chicago', 'Madrid']
        }),
        pd.DataFrame({
        'Name': ['Jack', 'Peter', 'Paul'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']
        }),
        pd.DataFrame({
        'Name': ['Jacob', 'Isaac', 'Carl'],
        'Age': [28, 23, 12],
        'City': ['Sydney', 'Washington', 'Cannes']
        }),
        pd.DataFrame({
            'Name': ['Simon', 'Emmy'],
            'Age': [45, 19],
            'City': ['Edinburgh', 'Birmingham']
        })
    ]
    
    # act
    output = list(s.rechunk_dataframes(dataframes, fixed_size))

    # assert
    assert len(output) == len(expected_output)
    for out, exp in zip(output, expected_output):
        assert_frame_equal(out, exp)