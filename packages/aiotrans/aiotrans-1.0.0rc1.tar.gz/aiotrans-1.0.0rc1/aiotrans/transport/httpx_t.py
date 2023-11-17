import html

from .base import Transport

try:
    import httpx
except ImportError:
    pass


class HttpxTransport(Transport):
    def __init__(self):
        from uconst import Constructor
        self.Constructor = Constructor
        self.conn = httpx.AsyncClient()

    async def send(self, target_lang: str, source_lang: str, text: str) -> str:
        url = self.Constructor("translate.google.com") / "m"

        response = await self.conn.get(
            str(url),
            params={"tl": target_lang, "sl": source_lang, "q": text},
        )

        return html.unescape(response.text)

    async def close(self):
        await self.conn.aclose()
