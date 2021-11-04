from plotting.pages.graph.components import graph_options as go


def test_create_attribute_dropdown():
    attributes = ["item1", "item2"]
    expected = len(attributes) * 2 + 1
    output = go.create_attribute_dropdown(attributes, "id")
    assert len(output) == expected


def test_create_label_dropdown():
    labels = ["item1", "item2"]
    expected = len(labels) * 2 + 1
    output = go.create_label_dropdown(labels, "id")
    assert len(output) == expected
