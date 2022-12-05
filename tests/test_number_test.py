#!/usr/bin/env python3


def test_import():
    """ Test if module successfully imports """
    try:
        import number_test
    except ModuleNotFoundError as exc:
        assert False, exc
