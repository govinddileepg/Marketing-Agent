from __future__ import annotations

from dataclasses import dataclass
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen


@dataclass
class WebsiteSnapshot:
    url: str
    final_url: str
    title: str
    description: str
    headings: list[str]
    links: list[str]
    text: str


class _PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title_parts: list[str] = []
        self.description = ""
        self.headings: list[str] = []
        self.links: list[str] = []
        self.text_parts: list[str] = []
        self._in_title = False
        self._in_script_or_style = False
        self._current_heading: list[str] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        if tag == "title":
            self._in_title = True
        elif tag in {"script", "style", "noscript"}:
            self._in_script_or_style = True
        elif tag == "meta" and attrs_dict.get("name", "").lower() == "description":
            self.description = attrs_dict.get("content", "") or ""
        elif tag in {"h1", "h2", "h3"}:
            self._current_heading = []
        elif tag == "a" and attrs_dict.get("href"):
            self.links.append(attrs_dict["href"] or "")

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False
        elif tag in {"script", "style", "noscript"}:
            self._in_script_or_style = False
        elif tag in {"h1", "h2", "h3"} and self._current_heading is not None:
            value = " ".join(self._current_heading).strip()
            if value:
                self.headings.append(value)
            self._current_heading = None

    def handle_data(self, data: str) -> None:
        value = " ".join(data.split())
        if not value or self._in_script_or_style:
            return
        if self._in_title:
            self.title_parts.append(value)
        if self._current_heading is not None:
            self._current_heading.append(value)
        self.text_parts.append(value)


def fetch_website(url: str, timeout: int = 15) -> WebsiteSnapshot:
    parsed = urlparse(url if urlparse(url).scheme else f"https://{url}")
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError("A valid http(s) website URL is required")

    normalized = parsed.geturl()
    request = Request(
        normalized,
        headers={"User-Agent": "Marketing-Agent/0.1 (+business-analysis)"},
    )
    with urlopen(request, timeout=timeout) as response:
        content_type = response.headers.get("Content-Type", "")
        if "html" not in content_type.lower():
            raise ValueError("The supplied URL did not return an HTML page")
        body = response.read(1_500_000).decode("utf-8", errors="replace")
        final_url = response.geturl()

    parser = _PageParser()
    parser.feed(body)

    base = final_url
    links = [urljoin(base, link) for link in parser.links if link]
    text = " ".join(parser.text_parts)

    return WebsiteSnapshot(
        url=normalized,
        final_url=final_url,
        title=" ".join(parser.title_parts).strip(),
        description=parser.description.strip(),
        headings=parser.headings[:30],
        links=links[:100],
        text=text[:30_000],
    )
