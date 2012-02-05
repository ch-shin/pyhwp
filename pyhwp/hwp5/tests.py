def test_suite():
    from unittest import defaultTestLoader as TL
    from unittest import TestSuite as TS
    import test_treeop
    import test_binmodel
    import test_dataio
    import test_xmlmodel
    import test_xmlformat
    import test_filestructure
    import test_storage
    import test_recordstream
    import test_odtxsl
    tests = [test_storage, test_filestructure, test_binmodel, test_dataio, test_xmlmodel, test_xmlformat, test_odtxsl]
    tests.append(test_recordstream)
    tests.append(test_treeop)
    return TS((TL.loadTestsFromModule(m) for m in tests))
