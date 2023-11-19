from .keywords import ChainKeywords

class ChainLibrary(ChainKeywords):
    """``ChainLibrary`` is a Robot Framework library for running keywords in chain.

    Following keywords are included:

    - `Replace Strings`
    - `Chain Keywords`
    """

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
