from collections import defaultdict
class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.token_to_ttl = defaultdict(int)

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.token_to_ttl[tokenId] = currentTime+self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.token_to_ttl and self.token_to_ttl[tokenId] > currentTime:
            self.token_to_ttl[tokenId] = currentTime+self.ttl

    def countUnexpiredTokens(self, currentTime: int) -> int:
        token_to_del, unexpired_count = [], 0
        for token in self.token_to_ttl:
            if self.token_to_ttl[token] <= currentTime:
                token_to_del.append(token)
                continue
            unexpired_count += 1
        for token in token_to_del:
            del self.token_to_ttl[token]
        return unexpired_count
