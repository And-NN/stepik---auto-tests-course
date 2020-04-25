def test_substring(full_string, substring):
    position = full_string.find(substring)
    assert position != -1, f"expected '{substring}' to be substring of '{full_string}'"


print(test_substring('fulltext', 'some_value'))
print(test_substring('some_text', 'some'))