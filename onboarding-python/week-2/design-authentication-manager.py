class AuthenticationManager:
    

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokenId_dict = {} # "token":"expiry time"

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokenId_dict[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokenId_dict and currentTime < self.tokenId_dict[tokenId]:
            self.tokenId_dict[tokenId] = self.timeToLive + currentTime


    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for token, expiry in  self.tokenId_dict.items():
            if expiry > currentTime:
                count += 1
        return count