from robot.errors import DataError
from robot.libraries.BuiltIn import (BuiltIn, run_keyword_variant)
from robot.libraries.String import String
from robot.utils import is_string


class ChainLibrary:
    """``ChainLibrary`` is a Robot Framework library for running keywords in chain.

    Following keywords are included:

    - `Replace Strings`
    - `Chain Keywords`
    """

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, separator: str = 'AND') -> None:
        self._built_in = BuiltIn()
        self._string = String()
        self._separator = separator

    def replace_strings(self, string: str, **kwargs) -> str:
        """Replaces ``search_for`` in the given ``string`` with ``replace_with``,
        being ``kwargs`` a dictionary of ``search_for=replace_with`` arguments.

        A modified version of the string is returned and the original string is
        not altered.

        Examples:
        | ${str} | `Replace Strings` | Hello, world! | Hello=Hi | world=John Doe |
        | `Should Be Equal` | ${str} | Hi, John Doe! |
        """
        replaced_string = string
        for key, value in kwargs.items():
            replaced_string = self._string.replace_string(replaced_string, key, value)
        return replaced_string

    @run_keyword_variant(resolve=0, dry_run=True)
    def chain_keywords(self, *keywords):
        """Executes all the given keywords in a chain.

        By default keywords can be run with arguments using ``AND`` as a
        separator between keywords. The keywords are executed so that the first
        argument is the first keyword and proceeding arguments until the first
        ``AND`` are arguments to it. First argument after the first ``AND`` is the
        second keyword and proceeding arguments until the next ``AND`` and the
        returned value of the previous keyword are its arguments. And so on.

        Examples:
        | ${text} | `Chain Keywords` | `Name` | AND | `Catenate` | SEPARATOR=${SPACE} | Hello |
        | `Should Be Equal` | ${text} | Hello John Doe |
        | `Chain Keywords` | `Random Number` | AND | `Set Test Variable` | ${RANDOM_NUMBER} |

        Notice that the ``AND`` control argument must be used explicitly and
        cannot itself come from a variable. If you need to use literal ``AND``
        string as argument, you can modify the separator by passing a parameter
        to the library.

        Examples:
        | `Library` | ChainLibrary | -> |
        """
        if not keywords or not is_string(keywords[0]):
            raise RuntimeError('Keyword name must be a string.')
        if self._is_separator(keywords[0]) or self._is_separator(keywords[-1]):
            raise DataError(f'{self._separator.upper()} must have a keyword before and after.')
        return self._run_chained_keywords(self._split_chained_keywords(keywords))

    def _run_chained_keywords(self, keywords: list):
        args = [None]
        for kw in keywords:
            if any(args):
                kw.append(args[-1])
            if arg := self._built_in.run_keyword(*kw):
                args.append(arg)
        return args[-1]

    def _split_chained_keywords(self, keywords: list) -> list:
        replace_list = []
        tmp = []
        for i, kw in enumerate(keywords):
            if self._is_separator(kw):
                if self._is_separator(keywords[i + 1]):
                    raise DataError(f'{self._separator.upper()} must have a keyword before and after.')
                else:
                    replace_list.append(tmp)
                    tmp = []
            else:
                tmp.append(kw)
        replace_list.append(tmp)
        return replace_list

    def _is_separator(self, arg) -> bool:
        return is_string(arg) and arg.upper() == self._separator.upper()
