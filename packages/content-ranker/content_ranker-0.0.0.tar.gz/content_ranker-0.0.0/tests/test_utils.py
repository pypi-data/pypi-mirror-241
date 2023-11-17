import pytest
from pathlib import Path
from resources import RESOURCES_PATH

from content_ranker.utils import ColorHtml

RESOURCES_PATH_UTILS = RESOURCES_PATH / "utils"

def read_all_html(html_path):
    for path in html_path.glob("*.html"):
        with open(path.as_posix(), 'r') as f:
            yield f.read()


@pytest.mark.parametrize("html_with_labels", read_all_html(RESOURCES_PATH_UTILS))
def test_colors(html_with_labels):
    color_html = ColorHtml()
    color_html.parse(html_with_labels)
    assert True




