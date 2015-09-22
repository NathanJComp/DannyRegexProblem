# DannyRegexProblem
The problem this code is designed to solve is as follows:
We are given a string which is composed of blocks delimited by ".". Each block is <=8 characters long.
We need to determine if a given string matches a given pattern, where a pattern consists of 
"%": matches any single non "." character
"*": matches from the current position in the string to the next "." or the end of string, if EOS comes before any "."
"**": matches any number of "."-delimited segments (can be 0)
".": only matches "."
other characters match only themselves.

For example
*.**.%ef.gh* would match 
abc.def.ghij (** matches nothing in this case)
abc.blah.blah.blah.blah.xef.ghaaaa
