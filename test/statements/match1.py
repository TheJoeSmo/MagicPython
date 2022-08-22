match a:
    case 400:
        1
    case 404:
        2
    case 418:
        3
    case _:
        4



match         : keyword.control.flow.python, source.python
              : source.python
a             : source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
case          : keyword.control.flow.python, source.python
              : source.python
400           : constant.numeric.dec.python, source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
1             : constant.numeric.dec.python, source.python
              : source.python
case          : keyword.control.flow.python, source.python
              : source.python
404           : constant.numeric.dec.python, source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
2             : constant.numeric.dec.python, source.python
              : source.python
case          : keyword.control.flow.python, source.python
              : source.python
418           : constant.numeric.dec.python, source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
3             : constant.numeric.dec.python, source.python
              : source.python
case          : keyword.control.flow.python, source.python
              : source.python
_             : source.python
:             : punctuation.separator.colon.python, source.python
              : source.python
4             : constant.numeric.dec.python, source.python
