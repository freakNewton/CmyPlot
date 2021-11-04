import pandas as pd

from plotting.pages.table import table_callbacks as tc

df = pd.DataFrame({"x1": [0, 1, 2], "x2": [6, 7, 8], "y": [0, 0, 0]})
data = {"df": df.to_dict("records")}


def test_initialize_table_data():

    data_out, cols = tc.initialize_table_data.__wrapped__(data)
    assert data_out == data["df"]
    assert len(cols) == len(df)
    first_col = cols[0]
    assert "name" in first_col and "id" in first_col
