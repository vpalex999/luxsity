"""
Calculate the minumum positive number that is not a possible sum from a list of positive integers.
In the input:
    numbers - array of integers

 At the output: number
 Example:
[2,1,4,10] -->  8

we can get 1, 2, 2 + 1 = 3, 4, 4 + 1 = 5, 2 + 4 = 6,  2 + 1 + 4 = 7, not 8

cases:
[x, x] => base
[1, 1] => None, max=1
[1, 2] => None, max=3
[1, 3] => 2, max=4


00
01
10
11

"""

import pytest


def get_bin_seq(size: int) -> str:

    if size == 1:
        yield '1'
    else:
        for _ in range(pow(2, size)):
            r = "{0:0b}".format(_)
            defferense = size - len(r)
            if defferense:
                r = f"{'0'*defferense }{r}"
            yield r


def get_missing_value(numbers: list):
    numbers.sort()

    num_set = set()

    for sute in get_bin_seq(len(numbers)):
        if "1" in sute:
            local_summ = 0
            for count, value in enumerate(sute):
                if value == "1":
                    local_summ += numbers[count]
            num_set.add(local_summ)

    for num in range(1, sum(numbers) + 2):
        if num not in num_set:
            return num


cases = [
    ([2, 1, 5], 4),
    ([2, 1, 4, 10], 8),
    ([5, 1, 2, 4, 10, 3], 26),
]


cases_binary = [
    (2, ['00', '01', '10', '11'])
]


@pytest.mark.parametrize("size, sute_seq", cases_binary)
def test_get_binary_sequence(size, sute_seq):
    assert list(get_bin_seq(size)) == sute_seq


@ pytest.mark.parametrize("numbers, expect_missing", cases)
def test_missing(numbers, expect_missing):
    assert get_missing_value(numbers) == expect_missing
