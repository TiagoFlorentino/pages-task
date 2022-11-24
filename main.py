import click

from paginator.paginator import Paginator


@click.command()
@click.option("--current-page", "-cp", default=0)
@click.option("--total-pages", "-tp", default=0)
@click.option("--boundaries", "-bo", default=0)
@click.option("--around", "-ar", default=0)
def main_paginator_print(
    current_page: int, total_pages: int, boundaries: int, around: int
):
    paginator = Paginator(
        current_page=current_page,
        total_pages=total_pages,
        boundaries=boundaries,
        around=around,
    )
    paginator.print_paginator()


if __name__ == "__main__":
    main_paginator_print()
