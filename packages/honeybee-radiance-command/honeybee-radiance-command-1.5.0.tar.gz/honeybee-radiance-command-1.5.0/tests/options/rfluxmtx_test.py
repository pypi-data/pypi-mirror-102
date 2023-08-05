"""Test rfluxmtx options."""
from honeybee_radiance_command.options.rfluxmtx import RfluxmtxOptions
import pytest
import honeybee_radiance_command._exception as exceptions


def test_default():
    options = RfluxmtxOptions()
    assert options.to_radiance() == ''


def test_assignment():
    options = RfluxmtxOptions()
    options.v = True
    assert options.v == True
    assert options.to_radiance() == '-v'


def test_reassignment():
    options = RfluxmtxOptions()
    options.v = True
    assert options.v == True
    assert options.to_radiance() == '-v'
    # remove assigned values
    options.v = None
    assert options.v == None
    assert options.to_radiance() == ''


def test_protected_assignment():
    options = RfluxmtxOptions()
    with pytest.raises(exceptions.ProtectedOptionError):
        options.f = 'bins.cal'
    with pytest.raises(exceptions.ProtectedOptionError):
        options.e = '2*$1=$2'
    with pytest.raises(exceptions.ProtectedOptionError):
        options.m = 'modifier'
    with pytest.raises(exceptions.ProtectedOptionError):
        options.m = None
        options.M = './suns.mod'
