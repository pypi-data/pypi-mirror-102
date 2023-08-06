# actorname

## Name

**actorname** − an [RFC1178](https://tools.ietf.org/html/rfc1178) implementation to generate pronounceable, sometimes even memorable, "pet names", consisting of a random combination of adverbs, an adjective, and an animal name

## Synopsis

- Complete version:
```
usage: actorname [-w|--words INT] [-l|--letters INT] [-s|--separator STR] [-d|--dir STR] [-c|--complexity INT] [-u|--ubuntu]
```

- Python version:
```bash
usage: actorname [-h] [-w WORDS] [-l LETTERS] [-s SEPARATOR]
```

## Options
- `-w|--words` number of words in the name, default is 2,
- `-l|--letters` maximum number of letters in each word, default is unlimited,
- `-s|--separator` string used to separate name words, default is `'-'`,
- `-d|--dir` directory containing `adverbs.txt`, `adjectives.txt`, `names.txt`, default is `/usr/share/actorname/`,
- `-c|--complexity` [0, 1, 2]; 0 = easy words, 1 = standard words, 2 = complex words, default=1,
- `-u|--ubuntu` generate ubuntu-style names, alliteration of first character of each word.

## Description

This utility will generate "pet names", consisting of a random combination of an adverb, adjective, and an animal name. These are useful for unique hostnames or container names, for instance.

As such, ActorName tries to follow the tenets of Zooko’s triangle. Names are:

- human meaningful
- decentralized
- secure

Besides this shell utility, there are also native libraries: [python-actorname](https://pypi.org/project/actorname/), [python3-actorname](https://pypi.org/project/actorname/), and [golang-actorname](https://github.com/dustinkirkland/golang-actorname). Here are some programmatic examples in code:

## Examples

```bash
$ actorname
wiggly-yellowtail

$ actorname --words 1
robin

$ actorname --words 3
primly-lasting-toucan

$ actorname --words 4
angrily-impatiently-sage-longhorn

$ actorname --separator ":"
cool:gobbler

$ actorname --separator "" --words 3
comparablyheartylionfish

$ actorname --ubuntu
amazed-asp

$ actorname --complexity 0
massive-colt
```

----

## Code

Besides this shell utility, there are also native libraries: python-actorname, python3-actorname, and golang-actorname. Here are some programmatic examples in code:

### **Golang Example**
Install it with apt:
```bash
$ sudo apt-get install golang-actorname
```

Or here's an example in golang code:

```golang
package main

import (
        "flag"
        "fmt"
        "math/rand"
        "time"
        "github.com/dustinkirkland/golang-actorname"
)

var (
        words = flag.Int("words", 2, "The number of words in the pet name")
        separator = flag.String("separator", "-", "The separator between words in the pet name")
)

func init() {
        rand.Seed(time.Now().UTC().UnixNano())
}

func main() {
        flag.Parse()
        rand.Seed(time.Now().UnixNano())
        fmt.Println(actorname.Generate(*words, *separator))
}
```

### **Python Example**
See: [on pypi](https://pypi.python.org/pypi/actorname).

Install it with [pip](https://pip.pypa.io/):
```bash
$ [sudo] pip install actorname
```

```python
#!/usr/bin/python
import argparse
import actorname
import sys

parser = argparse.ArgumentParser(description='Generate human readable random names')
parser.add_argument('-w', '--words', help='Number of words in name, default=2', default=2)
parser.add_argument('-l', '--letters', help='Maximum number of letters per word, default=6', default=6)
parser.add_argument('-s', '--separator', help='Separator between words, default="-"', default="-")
parser.options = parser.parse_args()
sys.stdout.write(actorname.Generate(int(parser.options.words), parser.options.separator, int(parser.options.letters)) + "\n")
```

## Author

This manpage and the utility were written by Mark Christopher West &lt;markchristopherwest@gmail.com&gt; for Ubuntu systems (but may be used by others). Permission is granted to copy, distribute and/or modify this document and the utility under the terms of the Apache2 License.

The complete text of the Apache2 License can be found in `/usr/share/common-licenses/Apache-2.0` on Debian/Ubuntu systems.
