from .__version__ import __version__
from abc import ABC, abstractmethod

import hashlib
from pathlib import Path
import sqlite3
import datetime as dt

N = 2


class RepoException(Exception):
    """Any Exception thrown by a Repo method"""


class Repo(ABC):
    """"""
    @abstractmethod
    def reproduce(self, cid:str):
        raise RepoException()

    @abstractmethod
    def remember(self, cid:str, sig:str, result:any):
        raise RepoException()


class TextFileRepo(Repo):
    def __init__(self, store: str, sqlite: str = None):
        self.db = sqlite or f'{store}/memo.sqlite'
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS store (cid TEXT PRIMARY KEY, signature TEXT, timestamp TEXT)")
        con.close()

        self.store = store

    def file_path(self, cid):
        return Path(f'{self.store}/{cid[:N]}/{cid}')

    def reproduce(self, cid:str):
        con = sqlite3.connect(self.db)
        try:
            cur = con.cursor()
            cur.execute("SELECT signature FROM store WHERE cid = ?", (cid,))
            [_] = cur.fetchall()
        except Exception as e:
            raise RepoException() from e
        finally:
            con.close()

        fpath = self.file_path(cid)
        try:
            with fpath.open('r', encoding='utf-8') as fp:
                return fp.read()
        except FileNotFoundError as f:
            con = sqlite3.connect(self.db)
            try:
                cur = con.cursor()
                cur.execute("DELETE FROM store WHERE cid = ?", (cid,))
                con.commit()
            except Exception as e:
                raise RepoException() from e
            finally:
                con.close()
            raise RepoException() from f

    def remember(self, cid:str, sig: str, result: str):
        now = dt.datetime.now(tz=None).isoformat()
        fpath = self.file_path(cid)
        fpath.parent.mkdir(exist_ok=True)
        with fpath.open('w', encoding='utf-8') as fp:
            fp.write(result)

        con = sqlite3.connect(self.db)
        try:
            cur = con.cursor()
            cur.execute("INSERT INTO store (cid, signature, timestamp) VALUES (?, ?, ?)", (cid, sig, now))
            con.commit()
        finally:
            con.close()
    
    def when(self, cid:str):
        con = sqlite3.connect(self.db)
        try:
            cur = con.cursor()
            cur.execute("SELECT timestamp FROM store WHERE cid = ?", (cid,))
            [timestamp] = cur.fetchall()
        finally:
            con.close()
        return timestamp


def hash_str(string: str):
    h = hashlib.md5()
    h.update(string.encode())
    return h.hexdigest()


def a_str(args: list):
    return str(args)[1:-1] if args else ""


def kw_str(args, kwargs: dict):
    if not kwargs:
        return ""
    prefix = ", " if args else ""
    kwsigs = []
    for k,v in sorted(kwargs.items()):
        kwsigs.append(f"{k}={str([v])[1:-1]}")
    return prefix + ", ".join(kwsigs)


def signature(func, args, kwargs):
    return f"{func.__name__}({a_str(args)}{kw_str(args, kwargs)})"


def cached(store: Repo):
    def sd_cached(func):
        def cached_func(*args, **kargs):
            sig = signature(func, args, kargs)
            cid = hash_str(sig)
            try:
                return store.reproduce(cid)
            except RepoException:
                result = func(*args, **kargs)
                try:
                    store.remember(cid, sig, result)
                except RepoException:
                    pass
                return result
        return cached_func
    return sd_cached
