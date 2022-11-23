from paginator.paginator import Paginator

if __name__ == "__main__":
    # Example A
    paginatorA = Paginator(current_page=4, total_pages=5, boundaries=1, around=0)
    paginatorA.print_paginator()

    # Example B
    paginatorB = Paginator(current_page=4, total_pages=10, boundaries=2, around=2)
    paginatorB.print_paginator()
