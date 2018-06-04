from solution import Codec

new_codec = Codec()


def test_empty():
    """
    test if given string are empty
    """
    assert new_codec.encode('') is False 


def test_string():
    """
    test short url
    """
    site = 'google.com'
    assert site == new_codec.decode(new_codec.encode(site)) 


def test_long_site():
    site = 'https://www.youtube.com/watch?v=7oQ-Usd7Tes'
    assert site == new_codec.decode(new_codec.encode(site))