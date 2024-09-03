#!/usr/bin/env python3
"""Defines function named index_range that takes two
integer arguments page and page_size
"""


def index_range(page: int, page_size: int) -> (int, int):
    """Returns the endpage and the startpage of

    Keyword arguments:
    page -- the page
    page_size -- the size of the page
    Return: the endpage idex and the startpage index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
