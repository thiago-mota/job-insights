from src.pre_built.counter import count_ocurrences


def test_counter():
    word_ocurrence = 646
    assert count_ocurrences('data/jobs.csv', 'Salesforce') == word_ocurrence
