# alx-interview

### Directory: [0x00-pascal_triangle](https://github.com/masonk16/alx-interview/tree/main/0x00-pascal_triangle)

Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of `n`:

* Returns an empty list if `n <= 0`
* You can assume `n` will be always an integer

<hr>

### Directory: [0x01-lockboxes](https://github.com/masonk16/alx-interview/tree/main/0x01-lockboxes)

You have `n` number of locked boxes in front of you. Each box is numbered sequentially from `0` to `n - 1` and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

* Prototype: `def canUnlockAll(boxes)`
* `boxes` is a list of lists
* A key with the same number as a box opens that box
* You can assume all keys will be positive integers
  * There can be keys that do not have boxes
* The first box `boxes[0]` is unlocked
* Return `True` if all boxes can be opened, else return `False`

<hr>

### Directory: [0x02-minimum_operations](https://github.com/masonk16/alx-interview/tree/main/0x02-minimum_operations)

In a text file, there is a single character `H`. Your text editor can execute only two operations in this file: `Copy All` and `Paste`. Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n` `H` characters in the file.

* Prototype: `def minOperations(n)`
* Returns an integer
* If `n` is impossible to achieve, return `0`

**Example:**

`n = 9`

`H` => `Copy All` => `Paste` => `HH` => `Paste` => `HHH` => `Copy All` => `Paste` => `HHHHHH` => `Paste` => `HHHHHHHHH`

Number of operations: `6`

<hr>

### Directory: [0x03-log_parsing](https://github.com/masonk16/alx-interview/tree/main/0x03-log_parsing)

Write a script that reads `stdin` line by line and computes metrics:

* Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>` (if the format is not this one, the line must be skipped)
* After every 10 lines and/or a keyboard interruption (`CTRL + C`), print these statistics from the beginning:
  * Total file size: `File size: <total size>`
  * where `<total size>` is the sum of all previous `<file size>` (see input format above)
  * Number of lines by status code:
    * possible status code: `200`, `301`, `400`, `401`, `403`, `404`, `405` and `500`
    * if a status code doesn’t appear or is not an integer, don’t print anything for this status code
    * format: `<status code>: <number>`
    * status codes should be printed in ascending order

<hr>

### Directory: [0x04-utf8_validation](https://github.com/masonk16/alx-interview/tree/main/0x04-utf8_validation)

Write a method that determines if a given data set represents a valid UTF-8 encoding.

* Prototype: `def validUTF8(data)`
* Return: `True` if data is a valid UTF-8 encoding, else return `False`
* A character in UTF-8 can be 1 to 4 bytes long
* The data set can contain multiple characters
* The data will be represented by a list of integers
* Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer

<hr>

### Directory: [0x05-nqueens](https://github.com/masonk16/alx-interview/tree/main/0x05-nqueens)

![Chess grandmaster Judit Polgár, the strongest female chess player of all time](http://www.crestbook.com/files/Judit-photo1_602x433.jpg "Chess grandmaster Judit Polgár, the strongest female chess player of all time")

Chess grandmaster [Judit Polgár](https://en.wikipedia.org/wiki/Judit_Polg%C3%A1r), the strongest female chess player of all time

The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.

* Usage: `nqueens N`
  * If the user called the program with the wrong number of arguments, print `Usage: nqueens N`, followed by a new line, and exit with the status `1`
* where N must be an integer greater or equal to `4`
  * If N is not an integer, print `N must be a number`, followed by a new line, and exit with the status 1
  * If N is smaller than `4`, print `N must be at least 4`, followed by a new line, and exit with the status 1
* The program should print every possible solution to the problem
  * One solution per line
  * Format: see example
  * You don’t have to print the solutions in a specific order
* You are only allowed to import the `sys` module

Read: [Queen](https://intranet.alxswe.com/rltoken/ghWqI1wvx6g-Ul7nrufMKA), [Backtracking](https://intranet.alxswe.com/rltoken/-hgZbgRFkwmxaKnLnCIuEQ)

<hr>

### Directory: [0x06-starwars_api](https://github.com/masonk16/alx-interview/tree/main/0x06-starwars_api)

Write a script that prints all characters of a Star Wars movie:

* The first positional argument passed is the Movie ID - example: `3` = “Return of the Jedi”
* Display one character name per line **in the same order as the “characters” list in the `/films/` endpoint**
* You must use the [Star wars API](https://swapi-api.alx-tools.com/)
* You must use the `request` module

<hr>
