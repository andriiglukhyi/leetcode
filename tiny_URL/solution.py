from hashlib import sha256
class Codec:
    
    dict = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if len(longUrl) == 0:
            return False
        hash = sha256(longUrl.encode()).hexdigest()[:5]
        self.dict[hash] = longUrl
        return hash

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.dict[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))