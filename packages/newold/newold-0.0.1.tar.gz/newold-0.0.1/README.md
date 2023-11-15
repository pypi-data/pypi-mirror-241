# newold

Print only new values to stdout, or those that weren't seen in a while.

## Usage

Here is an usage example:
```
$ cat /tmp/inputs.txt
one
two
three
$ # new values are printed
$ cat /tmp/inputs.txt | newold --db /tmp/in.db
one
two
three
$ # values are not printed
$ cat /tmp/inputs.txt | newold --db /tmp/in.db
$ sleep 5
$ # values older than 4 seconds are printed
$ cat /tmp/inputs.txt | newold --db /tmp/in.db --seconds 4
one
two
three
$ echo four >> /tmp/inputs.txt
$ # new values are printed
$ cat /tmp/inputs.txt | newold --db /tmp/in.db
four
```
