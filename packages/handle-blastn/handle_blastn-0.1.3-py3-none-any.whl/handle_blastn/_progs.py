import fileunity as _fu

from . import _clines, _summaries


def summarize(
    infile: str,
):
    summary = _summaries.Summary.from_file(infile)
    return _fu.TOMLUnit(vars(summary))

def _query_format(query, query_format):
    if query_format != 'infer':
        return query_format
    trunk, ext = _os.path.splitext(query)
    if ext in ['.phd']:
        return 'phd'
    if ext in ['.ab1']:
        return 'abi'
    if ext in ['.fasta', '.fas', '.fa']:
        return 'fasta'
    return 'Seq'

def run_cmd(
    query,
    *,
    query_format:dict(choices=['infer', 'Seq', 'fasta', 'abi', 'phd'])='infer',
    cmd: str = "blastn",
    db: str,
):
    query_format = _query_format(query, query_format)

    with _clines.Cline.manager(cmd=cmd, db=db) as cline:
        if informat == 'fasta':
            cline.query = query
        elif informat == 'Seq':
            cline.dump(intake)
        else:
        	rec = _SeqIO.read(intake, informat)
            cline.dump(rec)
        cline.exec()
        return _fu.TextUnit.from_file(cline.out)

        


