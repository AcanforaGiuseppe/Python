"""
test code for the Report class(es)
"""
import pytest

from report2 import Row, Report


@pytest.fixture
def example_report():
    """
    utility function to provide a fresh report to test with
    """
    report = Report(limit=4)

    populate_report(report)
    return report


def populate_report(report):
    """
    utility function to populate an existing Report with
    some additional data

    :param report: the report object to populate

    The Report will be populated in place
    """
    report.add_row(Row("Natasha", "Smith", "WA"))
    report.add_row(Row("Devin", "Lei", "WA"))
    report.add_row(Row("Bob", "Li", "CA"))
    report.add_row(Row("Tracy", "Jones", "OR"))
    report.add_row(Row("Johnny", "Jakes", "WA"))
    report.add_row(Row("Derek", "Wright", "WA"))
    report.add_row(Row("Jordan", "Cooper", "WA"))
    report.add_row(Row("Mike", "Wong", "WA"))


def test_row_init():
    """
    test that a new row has the proper attributes initialized
    """
    row1 = Row("Joe", "Camel", "WA")

    assert row1.fname == "Joe"
    assert row1.lname == "Camel"
    assert row1.state == "WA"


def test_row_id_unique():
    """ two Rows should have unique IDs """
    row1 = Row("Joe", "Camel", "WA")
    row2 = Row("Bob", "Camel", "WA")

    assert row1.id != row2.id


def test_report_length(example_report):
    """
    test report size method
    """
    # the test data has 8 rows
    assert len(example_report) == 8


def test_number_of_pages(example_report):
    """
    check that the number of pages is correct
    """
    assert example_report.get_number_of_pages() == 2


def test_row_str(mocker):
    mocker.patch("report.uuid4", return_value="cane")
    row = Row("Giuseppe", "Acanfora", "IT")
    assert str(row) == "id:cane, name:Giuseppe, lastname:Acanfora, state:IT"


def test_add_row():
    report = Report(5)
    row = Row("Giuseppe", "Acanfora", "IT")
    report.add_row(row)
    assert len(report.rows) == 1
    assert row == report.rows[-1]


def test_remove_row(example_report):
    row = example_report.rows[4]
    example_report.remove_row(row.id)
    assert len(example_report) == 7
    assert row not in example_report


def test_number_of_pages_rounds_up_to_next_int(example_report):
    """
    check that the number of pages is correct
    """
    example_report.add_row(Row("Giuseppe", "Acanfora", "IT"))
    assert example_report.get_number_of_pages() == 3


def test_get_paged_row(example_report):
    page_2 = example_report.get_paged_rows(None, 2)
    assert len(page_2) == 4
    assert page_2[0] == example_report.rows[4]
    assert page_2[1] == example_report.rows[5]
    assert page_2[2] == example_report.rows[6]
    assert page_2[3] == example_report.rows[7]


def test_get_paged_rows_with_empty_page(example_report):
    page_3 = example_report.get_paged_rows('lname', 3)
    assert len(page_3) == 0


def test_get_paged_rows_sorted(example_report):
    page_2 = example_report.get_paged_rows('fname', 2)
    report = Report(2)
    populate_report(report)
    report.rows.sort(key=lambda x: getattr(x, 'fname'))
    assert len(page_2) == 4
    assert page_2[0].lname == report.rows[4].lname
    assert page_2[1].lname == report.rows[5].lname
    assert page_2[2].lname == report.rows[6].lname
    assert page_2[3].lname == report.rows[7].lname


def test_get_paged_rows_sorted_reverse(example_report):
    page_2 = example_report.get_paged_rows('-fname', 2)
    report = Report(2)
    populate_report(report)
    report.rows.sort(key=lambda x: getattr(x, 'fname'))
    assert len(page_2) == 4
    assert page_2[0].lname == report.rows[3].lname
    assert page_2[1].lname == report.rows[2].lname
    assert page_2[2].lname == report.rows[1].lname
    assert page_2[3].lname == report.rows[0].lname
