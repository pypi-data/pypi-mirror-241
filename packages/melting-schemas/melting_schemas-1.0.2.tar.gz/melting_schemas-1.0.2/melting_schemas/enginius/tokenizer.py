from redb.core import BaseDocument


class CountTokensRequest(BaseDocument):
    engine: str
    content: str | list[dict]


class CountTokensResponse(BaseDocument):
    token_count: int


class TokenizeRequest(BaseDocument):
    engine: str
    content: str


class TokenizeResponse(BaseDocument):
    tokens: list[int]
