from pathlib import Path
from unittest import TestCase

from memoi import cached, TextFileRepo, signature, hash_str, N


@cached(TextFileRepo('./store'))
def string_function(*args, **kwargs):
    return "this is just a string"


class TestSignature(TestCase):
    def test_signature(self):
        self.assertEqual("print()", signature(print,[],{}))
        self.assertEqual("print(1, '1')", signature(print,[1, '1'],{}))
        self.assertEqual("print(a=4, b='33')", signature(print,[],{'a':4, 'b': '33'}))
        self.assertEqual("print(1, a=[1, '2'])", signature(print,[1],{'a': [1, '2']}))


class TestTextFileRepo(TestCase):
    def setUp(self) -> None:
        Path('./store/memo.sqlite').unlink(missing_ok=True)

    @cached(TextFileRepo('./store'))
    def string_method(self, *args, **kwargs):
        return "this is yet another string"

    def test_cache(self):
        tfr = TextFileRepo('./store')

        self.assertEqual(
            string_function(1, 2, 3, a='a', b='b'),
            "this is just a string")
        cid1 = hash_str("string_function(1, 2, 3, a='a', b='b')")
        timestamp1 = tfr.when(cid1)
        self.assertIsNotNone(timestamp1)

        self.assertEqual(
            self.string_method(1, 2, 3, a='a', b='b'),
            "this is yet another string")
        cid2 = hash_str("string_method(<test_memoi.TestTextFileRepo testMethod=test_cache>, 1, 2, 3, a='a', b='b')")
        timestamp2 = tfr.when(cid2)
        self.assertIsNotNone(timestamp2)
        self.assertNotEqual(timestamp1, timestamp2)

        self.assertEqual(
            string_function(1, 2, 3, a='a', b='b'),
            "this is just a string")
        timestamp3 = tfr.when(cid1)
        self.assertEqual(timestamp1, timestamp3)

        Path(f"./store/{cid1[:N]}/{cid1}").unlink()
        self.assertEqual(
            string_function(1, 2, 3, a='a', b='b'),
            "this is just a string")
        timestamp4 = tfr.when(cid1)
        self.assertNotEqual(timestamp1, timestamp4)
