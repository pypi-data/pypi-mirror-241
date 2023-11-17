import dataclasses as _dataclasses
import xml.dom.minidom as _minidom

import Bio.Seq as _Seq
import Bio.SeqIO as _SeqIO
import Bio.SeqRecord as _SR


@_dataclasses.dataclass(frozen=True)
class Summary:
    query_id: str
    subject_id: str
    bit_score: float
    evalue: float
    def __post_init__(self):
        cls = type(self)
        ann = cls.__annotations__
        for n, t in ann.items():
            v = getattr(self, n)
            if type(v) is not t:
                raise TypeError(f"{v} is not of the type {t}.")
    @classmethod
    def from_text(cls, text):
        data = _minidom.parseString(text)
        kwargs = dict()
        kwargs['query_id'] = _get(data, 'BlastOutput', 'BlastOutput_iterations', 'Iteration', 'Iteration_query-def')
        kwargs['subject_id'] = _get(data, 'BlastOutput', 'BlastOutput_iterations', 'Iteration', 'Iteration_hits', 'Hit', 'Hit_id')
        kwargs['bit_score'] = float(_get(data, 'BlastOutput', 'BlastOutput_iterations', 'Iteration', 'Iteration_hits', 'Hit', 'Hsp', 'Hsp_bit-score'))
        kwargs['evalue'] = float(_get(data, 'BlastOutput', 'BlastOutput_iterations', 'Iteration', 'Iteration_hits', 'Hit', 'Hsp', 'Hsp_evalue'))
        return cls(**kwargs)
    @classmethod
    def from_file(cls, file):
        with open(file, 'r') as s:
            text = s.read()
        return cls.from_text(text)
    @classmethod
    def _get(data, *keys, kind=str):
        if data is None:
            return None
        ans = data
        try:
            for key in keys:
                ans = ans.getElementsByTagName(key)[0]
            ans = ans.childNodes[0]
        except ValueError:
            return float('nan')
        except IndexError:
            return float('nan')
        ans = ans.nodeValue
        if type(ans) is not str:
            raise TypeError()
        return ans 
