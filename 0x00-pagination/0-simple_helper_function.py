#!/usr/bin/env python3
"""Pagination helper
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieves index range from a given page
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
