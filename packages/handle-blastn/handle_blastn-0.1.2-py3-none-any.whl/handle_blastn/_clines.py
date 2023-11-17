import contextlib as _contextlib
import dataclasses as _dataclasses
import os as _os
import subprocess as _subprocess
import tempfile as _tmp

import Bio.SeqIO as _SeqIO
import Bio.SeqRecord as _SR

from ._summaries import *


@_dataclasses.dataclass
class Cline:
    cmd:str="blastn"
    db:str
    query:str
    out:str
    def __iter__(self):
        l = [
            self.cmd,
            '-db', self.db,
            '-task', 'blastn',
            '-dust', 'no',
            '-outfmt', '5',
            '-max_target_seqs', '1',
            '-evalue', '0.0001',
            '-sorthits', '1',
            '-query', self.query, 
            '-out', self.out,
        ]
        return (x for x in l)
    def dump(self, obj):
        if type(obj) is not _SR.SeqRecord:
            obj = _SR.SeqRecord(obj)
        return _SeqIO.write(self.query, "fasta", obj)
    def exec(self, **kwargs):
        _subprocess.run(list(self), **kwargs)
    def summarize(self):
        return Summary.from_file(self.out)
    def simple_run(self, obj, **kwargs):
        self.dump(obj)
        self.exec(**kwargs)
        return self.summarize(self)
    @classmethod
    def _file(cls, file, *, directory, filename):
        if file is None:
            return _os.path.join(directory, filename)
        return str(file)
    @classmethod
    @_contextlib.contextmanager
    def manager(cls, *args, query=None, out=None, **kwargs):
        if (query is None) or (out is None):
            inner_manager = _tmp.TemporaryDirectory()
        else:
            inner_manager = _contextlib.nullcontext()
        with inner_manager as directory:
            query = cls._file(query, directory=directory, filename="query.fasta")
            out = cls._file(out, directory=directory, filename="out.txt")
            yield cls(*args, query=query, out=out, **kwargs)






