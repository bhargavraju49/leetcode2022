class Codec:
    def __init__(self):
        self.k = {}

    def encode(self, longUrl: str) -> str:
        x = hash(longUrl)
        self.k[x] = longUrl
        return x
        

    def decode(self, shortUrl: str) -> str:
        return self.k[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))