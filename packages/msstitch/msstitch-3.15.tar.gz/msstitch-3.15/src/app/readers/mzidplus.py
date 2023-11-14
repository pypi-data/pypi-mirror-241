"""Reader methods for mzIdentML, tsv as generated by MSGF+"""

from app.readers import xml as basereader

def get_mzid_namespace(mzidfile):
    return basereader.get_namespace_from_top(mzidfile, None)


def mzid_spec_result_generator(mzidfile, namespace):
    return basereader.generate_tags_multiple_files(
        [mzidfile],
        'SpectrumIdentificationResult',
        ['cvList',
         'AnalysisSoftwareList',
         'SequenceCollection',
         'AnalysisProtocolCollection',
         'AnalysisCollection',
         ],
        namespace)


def generate_mzid_peptides(mzidfile, namespace):
    return basereader.generate_tags_multiple_files(
        [mzidfile],
        'Peptide',
        ['cvList',
         'AnalysisSoftwareList',
         'DataCollection',
         'AnalysisProtocolCollection',
         'AnalysisCollection',
         ],
        namespace)


def get_mzid_peptidedata(peptide, xmlns):
    pep_id = peptide.attrib['id']
    sequence = peptide.find('{}PeptideSequence'.format(xmlns)).text
    mods = {}
    for mod in peptide.findall('{}Modification'.format(xmlns)):
        modweight = round(float(mod.attrib['monoisotopicMassDelta']), 3)
        if modweight > 0:
            modweight = '+{}'.format(modweight)
        else:
            modweight = str(modweight)
        location = int(mod.attrib['location'])
        try:
            mods[location] += modweight
        except KeyError:
            mods[location] = modweight
    outseq = []
    for pos, aa in enumerate(sequence):
        if pos in mods:
            outseq.append('{}'.format(mods[pos]))
        outseq.append(aa)
    if pos + 1 in mods:
            outseq.append('{}'.format(mods[pos + 1]))
    return pep_id, ''.join(outseq)


def generate_mzid_spec_id_items(mzidfile, namespace, xmlns, specfn_idmap):
    specid_tag = '{0}SpectrumIdentificationItem'.format(xmlns)
    for specresult in mzid_spec_result_generator(mzidfile, namespace):
        specscanid = specresult.attrib['spectrumID']
        mzmlid = get_specresult_mzml_id(specresult)
        mzmlfn = specfn_idmap[mzmlid]
        for spec_id_item in specresult.findall(specid_tag):
            pep_id = spec_id_item.attrib['peptide_ref']
            yield (specscanid, mzmlfn, pep_id, spec_id_item)


def mzid_specdata_generator(mzidfile, namespace):
    return basereader.generate_tags_multiple_files(
        [mzidfile],
        'SpectraData',
        ['cvList',
         'AnalysisSoftwareList',
         'SequenceCollection',
         'AnalysisProtocolCollection',
         'AnalysisCollection',
         ],
        namespace)


def get_mzid_specfile_ids(mzidfn, namespace):
    """Returns mzid spectra data filenames and their IDs used in the
    mzIdentML file as a dict. Keys == IDs, values == fns"""
    sid_fn = {}
    for specdata in mzid_specdata_generator(mzidfn, namespace):
        sid_fn[specdata.attrib['id']] = specdata.attrib['name']
    return sid_fn


def get_specresult_mzml_id(specresult):
    return specresult.attrib['spectraData_ref']
