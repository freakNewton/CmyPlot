from plotting.utils import functions as func


def test_fetch_columns_options():

    data = [{"col1": ["row1", "row2"], "col2": ["row1", "row2"]}]

    # column option dropdown
    expected = [{"label": "col1", "value": "col1"}, {"label": "col2", "value": "col2"}]
    output = func.fetch_columns_options(data)
    assert output == expected

    # column option for tables
    expected = [{"name": "col1", "id": "col1"}, {"name": "col2", "id": "col2"}]
    output = func.fetch_columns_options(data, table=True)
    assert output == expected


def test_validate_store_data():

    # No data
    data = None
    expected = False
    output = func.validate_store_data(data)
    assert output == expected

    # data, but no df
    data = {"other": "not the df"}
    expected = False
    output = func.validate_store_data(data)
    assert output == expected

    # df is none
    data = {"df": None}
    expected = False
    output = func.validate_store_data(data)
    assert output == expected

    # df has data
    data = {"df": [{"col1": ["row1", "row2"], "col2": ["row1", "row2"]}]}
    expected = True
    output = func.validate_store_data(data)
    assert output == expected
