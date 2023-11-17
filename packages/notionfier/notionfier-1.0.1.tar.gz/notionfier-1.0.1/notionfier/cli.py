import os

import click

from notionfier import NotionPageBuilder


@click.group()
def cli():
    pass


@cli.command("import")
@click.option("-t", "--token", type=str, required=True, help="The Notion auth token.")
@click.option("-pid", "--parent-page-id", type=str, required=True, help="The page id of the parent page.")
@click.option("-f", "--file-path", type=str, required=True, help="Path to your markdown file.")
def import_notion(token: str, parent_page_id: str, file_path: str):
    with open(file_path, encoding="utf-8") as fi:
        content = fi.read()

    builder = NotionPageBuilder(token)
    builder.create_page(parent_page_id, os.path.basename(file_path), content)


def main():
    cli()


if __name__ == "__main__":
    main()
