import mistune
import notion_client

from notionfier.helpers.notion_params import build_notion_page_params
from notionfier.models.base import NotionObject
from notionfier.modules.renderer import NotionfierRender


class NotionPageBuilder:
    def __init__(self, token: str, renderer: NotionfierRender | None = None, plugins: list[str] | None = None) -> None:
        self.token = token
        renderer = renderer or NotionfierRender()
        if plugins is None:
            plugins = [
                "task_lists",
                "table",
                "url",
                "def_list",
                "strikethrough",
                "footnotes",
            ]
        self.parser = mistune.create_markdown(renderer=renderer, plugins=plugins)

    def parse_content(self, content: str) -> list[NotionObject]:
        return self.parser(content)

    async def acreate_page(self, parent_page_id: str, name: str, content: str):
        client = notion_client.AsyncClient(auth=self.token)
        return await client.pages.create(
            **build_notion_page_params(
                parent_page_id, name, self.parse_content(content)
            )
        )

    def create_page(self, parent_page_id: str, name: str, content: str):
        client = notion_client.Client(auth=self.token)
        return client.pages.create(
            **build_notion_page_params(
                parent_page_id, name, self.parse_content(content)
            )
        )
