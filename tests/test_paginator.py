import pytest

from paginator.paginator import Paginator


@pytest.mark.parametrize(
    "current_page,total_pages, boundaries, around, expected_result",
    [
        (0, 5, 3, 0, [1, 2, 3, 4, 5]),
        (0, 2, 5, 0, [1, 2]),
        (0, 20, 3, 0, [1, 2, 3, 18, 19, 20]),
        (4, 5, 1, 0, [1, 5]),
        (4, 10, 2, 2, [1, 2, 9, 10]),
    ],
)
def test_get_boundary_pages(
    current_page, total_pages, boundaries, around, expected_result
):
    paginator = Paginator(
        current_page=current_page,
        total_pages=total_pages,
        boundaries=boundaries,
        around=around,
    )
    result = paginator.get_boundary_pages()
    assert result == expected_result


@pytest.mark.parametrize(
    "current_page,total_pages, boundaries, around, expected_result",
    [
        (3, 5, 0, 0, [3]),
        (2, 2, 0, 2, [1, 2]),
        (3, 10, 0, 5, [1, 2, 3, 4, 5, 6, 7, 8]),
        (4, 5, 1, 0, [4]),
        (4, 10, 2, 2, [2, 3, 4, 5, 6]),
    ],
)
def test_get_current_boundary_pages(
    current_page, total_pages, boundaries, around, expected_result
):
    paginator = Paginator(
        current_page=current_page,
        total_pages=total_pages,
        boundaries=boundaries,
        around=around,
    )
    result = paginator.get_current_boundary_pages()
    assert result == expected_result


@pytest.mark.parametrize(
    "current_page,total_pages, boundaries, around, expected_result",
    [
        (3, 5, 0, 0, "... 3 ..."),
        (3, 4, 0, 1, "... 2 3 4"),
        (5, 10, 1, 2, "1 ... 3 4 5 6 7 ... 10"),
        (5, 10, 0, 2, "... 3 4 5 6 7 ..."),
        (4, 5, 1, 0, "1 ... 4 5"),
        (4, 10, 2, 2, "1 2 3 4 5 6 ... 9 10"),
        (0, 0, 0, 0, "No results to print!"),
    ],
)
def test_print_paginator(
    current_page, total_pages, boundaries, around, expected_result, capsys
):
    paginator = Paginator(
        current_page=current_page,
        total_pages=total_pages,
        boundaries=boundaries,
        around=around,
    )
    paginator.print_paginator()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_result
