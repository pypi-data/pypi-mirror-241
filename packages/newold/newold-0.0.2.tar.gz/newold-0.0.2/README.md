# newold

Print only new values to stdout, or those that weren't seen in a while.

## Usage

In order to allow old values, newold requires a database to store the values last seen time. You can specify the database file with `--db` parameter or `NEWOLD_DB` environment variable.

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
$ export NEWOLD_DB=/tmp/in.db
$ cat /tmp/inputs.txt | newold
four
```

Without a database only new values are printed to stdout. This behaves like an`uniq` command that doesn't require the lines to be ordered:
```
$ cat /tmp/inputs.txt
one
two
one
three
$ cat /tmp/inputs.txt | newold
one
two
three
```
