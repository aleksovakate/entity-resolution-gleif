import random
import pandas as pd


def generate_anomalies(n: int) -> pd.DataFrame:
    """
    Generate n synthetic anomalous entity records.
    Returns a DataFrame with columns: LEI, legal_name, lang, jurisdiction.
    LEIs are formatted like 'FAKE_ANOM_0001'.
    """
    templates = [
    # Keyboard mashes
    "asdfasdf",
    "asdf asdf",
    "qwerty inc",
    "qwertyuiop",
    "zzzz holdings",
    "ddddd ltd",
    "fffffff",
    "hjkl bank",
    "lkjhgfdsa",
    "poiuytrewq",
    
    # Random consonants / nonsense letters
    "xpqzm corp",
    "wvxyz ltd",
    "qkjz bank",
    "vbnm holdings",
    "rtyq inc",
    "zxcv group",
    "mnbv enterprises",
    "fghj llc",
    
    # Pop culture / obvious fakes
    "Donald Duck Bank",
    "Mickey Mouse Holdings",
    "Skywalker Industries",
    "Gotham City Holdings",
    "Hogwarts School Inc",
    "Wakanda Forever Ltd",
    "Stark Industries Fake",
    "Wayne Enterprises Test",
    "Gryffindor Capital",
    "Westeros Bank",
    "Mordor Mining Corp",
    "Narnia Trading Company",
    
    # Single chars / very short
    "X",
    "aa",
    "zz",
    "qq",
    "123",
    "...",
    "!!!",
    "???",
    
    # Mixed nonsense
    "Test Test Test",
    "abc abc abc",
    "foo bar baz",
    "lorem ipsum holdings",
    "placeholder name",
    "delete me inc",
    "TODO update name",
    "untitled company",
    "company name here",
    "fake fake fake llc",
    
    # Gibberish words
    "blarg corp",
    "splork industries",
    "wibble bank",
    "wobble holdings",
    "flarp ltd",
]
    random.seed(42)
    chosen = random.choices(templates, k=n)
    leis = [f"FAKE_ANOM_{i:04d}" for i in range(1, n+1)]
    
    return pd.DataFrame({
        "LEI": leis,
        "legal_name": chosen,
        "lang": [None] * n,
        "jurisdiction": [None] * n,
    })
    

def generate_duplicates(source_df: pd.DataFrame, n: int) -> pd.DataFrame:
    """
    Pick n random rows from source_df and create slight perturbations.
    Returns a DataFrame of duplicates with new LEIs like 'FAKE_DUP_0001',
    plus a column 'original_lei' linking each duplicate to its source.
    """
    pass


def inject(clean_df: pd.DataFrame, anomalies: pd.DataFrame, duplicates: pd.DataFrame) -> pd.DataFrame:
    """
    Concatenate clean_df + anomalies + duplicates.
    Shuffle the result so injected rows aren't all at the end.
    Reset index.
    """
    pass