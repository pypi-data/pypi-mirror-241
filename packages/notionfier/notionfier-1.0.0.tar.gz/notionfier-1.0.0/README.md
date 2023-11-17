# Notionfier: Import Markdown Pages to Notion.so

Fork of https://github.com/Arsenal591/notionfier

- updated dependencies
- published to PyPi
- reformatted, updated python version

Import markdown files to Notion.so using its [official API](https://developers.notion.com/).

**Requirments**: Python >= 3.11.

## Features

- All markdown basic syntax.
- Some markdown extended syntax:
  - Tables.
  - Code blocks.
  - Footnotes.
  - Definition lists.
  - Strikethrough.
  - Task lists.
  - Automatic URL Linking.

## Usage

- Firstly, follow the [instruction](https://developers.notion.com/docs/getting-started) to create an notion integration and share a page with the integration.

### CLI

```
notionfier import -t={{YOUR NOTION TOKEN}} -pid={{PAGE ID}} -f={{FILE PATH}}
```

### Programmatically

```python
from notionfier import NotionPageBuilder

token = "TOKEN"
builder = NotionPageBuilder(token)

parent_page_id = "123"
name = "Import Markdown File"
content = "##Markdown!!!"

# For sync
builder.create_page(parent_page_id, name, content)

# For async
await builder.acreate_page(parent_page_id, name, content)
```

## TODOs

- [ ] Highlighting.
- [ ] MathJax.
- [ ] Support local image files.
- [ ] Handle deeply (> 3 levels) nested children properly.
- [ ] Deal with Notion API's [request limits](https://developers.notion.com/reference/request-limits).
- [ ] More tests on markdown extensions.

## LICENSE

[MIT License](https://opensource.org/licenses/MIT)
