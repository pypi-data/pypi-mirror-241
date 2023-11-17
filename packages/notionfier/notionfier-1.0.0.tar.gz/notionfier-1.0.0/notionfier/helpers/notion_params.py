import dataclasses
from typing import Any

from notionfier.models.block import NotionObject


def build_children_params(children: list[NotionObject]) -> list[dict[str, Any]]:
    return [
        dataclasses.asdict(x, dict_factory=lambda x: {k: v for (k, v) in x if v is not None}) for x in children
    ]


def build_notion_page_params(parent_page_id: str, name: str, children: list[NotionObject]) -> dict[str, Any]:
    return {
        "parent": {"page_id": parent_page_id},
        "properties": {"title": {"title": [{"text": {"content": name}}]}},
        "children": build_children_params(children),
    }
