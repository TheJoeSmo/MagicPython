"normal {{ normal }} normal {fo.__add__!s}".format(fo=1)


"             : source.python, string.quoted.double.python
normal        : source.python, string.quoted.double.python
{{            : constant.character.format.python, source.python, string.quoted.double.python
 normal       : source.python, string.quoted.double.python
}}            : constant.character.format.python, source.python, string.quoted.double.python
 normal       : source.python, string.quoted.double.python
{fo.__add__   : constant.character.format.python, source.python, string.quoted.double.python
!s            : constant.character.format.python, source.python, storage.type.format.python, string.quoted.double.python
}             : constant.character.format.python, source.python, string.quoted.double.python
"             : source.python, string.quoted.double.python
.             : source.python
format        : meta.function-call.python, source.python
(             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.arguments.begin.python, source.python
fo            : meta.function-call.arguments.python, meta.function-call.python, source.python, variable.parameter.function-call.pyhton
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, source.python
1             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, source.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.python