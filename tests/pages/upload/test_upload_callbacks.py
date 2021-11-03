import pandas as pd

from src.plotting.pages.upload import upload_callbacks as uc

df = pd.DataFrame({
    'x1': [0, 1, 2],
    'x2': [6, 7, 8],
    'y': [0, 0, 0]
})
data = {'df': df.to_dict('records')}


def test_update_upload():
    contents = 'data:application/vnd.ms-excel;base64,eDEseDIseQ0KMCw2LDANCjEsNywwDQoyLDgsMA0K'
    filename = 'example.xml'

    info, data_out = uc.update_upload.__wrapped__(contents, filename)
    assert info == 'Error uploading, something is wrong with the file.'
    assert data_out is None

    filename = 'example.csv'
    info, data_out = uc.update_upload.__wrapped__(contents, filename)
    assert info == 'File uploaded successfully: ' + filename
    assert data_out == data


def test_set_button_status():

    global data
    output = uc.set_button_status.__wrapped__(data)
    assert output == [False, False]

    data = {}
    output = uc.set_button_status.__wrapped__(data)
    assert output == [True, True]
