from pigLatin import pigLatin

def test_noVowls(): # Test if the word has no vowels
    assert pigLatin("d") == "day"
    
def test_nonAlpha(): # Test if there is a numeric character in the word
    assert pigLatin("dg2") == "Invalid input .. Try again"
    
def test_beginVowel(): # Test words that begin with a vowel
    assert pigLatin("away") == "awayway"

def test_beginConsenant(): # Test words that begin with a consonant
    assert pigLatin("hamza") == "amzahay"