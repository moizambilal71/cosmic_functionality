# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import sympy.physics.mechanics.linearize as module_0
import sympy.utilities.iterables as module_1


def test_case_0():
    bytes_0 = b"C1\xa0\xd6\xa6D`\xdb\x89\xc6"
    linearizer_0 = module_0.Linearizer(
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        q_d=bytes_0,
        r=bytes_0,
        linear_solver=bytes_0,
    )
    assert (
        f"{type(linearizer_0).__module__}.{type(linearizer_0).__qualname__}"
        == "sympy.physics.mechanics.linearize.Linearizer"
    )
    assert (
        f"{type(linearizer_0.f_0).__module__}.{type(linearizer_0.f_0).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_0) == 10
    assert (
        f"{type(linearizer_0.f_1).__module__}.{type(linearizer_0.f_1).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_1) == 10
    assert (
        f"{type(linearizer_0.f_2).__module__}.{type(linearizer_0.f_2).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_2) == 10
    assert (
        f"{type(linearizer_0.f_3).__module__}.{type(linearizer_0.f_3).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_3) == 10
    assert (
        f"{type(linearizer_0.f_4).__module__}.{type(linearizer_0.f_4).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_4) == 10
    assert (
        f"{type(linearizer_0.f_c).__module__}.{type(linearizer_0.f_c).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_c) == 10
    assert (
        f"{type(linearizer_0.f_v).__module__}.{type(linearizer_0.f_v).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_v) == 10
    assert (
        f"{type(linearizer_0.f_a).__module__}.{type(linearizer_0.f_a).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_a) == 10
    assert (
        f"{type(linearizer_0.q).__module__}.{type(linearizer_0.q).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.q) == 10
    assert (
        f"{type(linearizer_0.u).__module__}.{type(linearizer_0.u).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.u) == 10
    assert (
        f"{type(linearizer_0.q_i).__module__}.{type(linearizer_0.q_i).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.q_i) == 0
    assert (
        f"{type(linearizer_0.q_d).__module__}.{type(linearizer_0.q_d).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.q_d) == 10
    assert (
        f"{type(linearizer_0.u_i).__module__}.{type(linearizer_0.u_i).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.u_i) == 0
    assert (
        f"{type(linearizer_0.u_d).__module__}.{type(linearizer_0.u_d).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.u_d) == 0
    assert (
        f"{type(linearizer_0.r).__module__}.{type(linearizer_0.r).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.r) == 10
    assert (
        f"{type(linearizer_0.lams).__module__}.{type(linearizer_0.lams).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.lams) == 0
    assert linearizer_0.perm_mat is None


def test_case_1():
    bytes_0 = b"\xed\x08\x9a\x97"
    linearizer_0 = module_0.permutation_matrix(bytes_0, bytes_0)
    assert (
        f"{type(linearizer_0).__module__}.{type(linearizer_0).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0) == 16


def test_case_2():
    list_0 = []
    var_0 = module_0.permutation_matrix(list_0, list_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(var_0) == 0


@pytest.mark.xfail(strict=True)
def test_case_3():
    none_type_0 = None
    module_0.permutation_matrix(none_type_0, none_type_0)


def test_case_4():
    bytes_0 = b"W\xae\x00\xdaM\xce\x1d\xc2"
    linearizer_0 = module_0.Linearizer(
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        linear_solver=bytes_0,
    )
    assert (
        f"{type(linearizer_0).__module__}.{type(linearizer_0).__qualname__}"
        == "sympy.physics.mechanics.linearize.Linearizer"
    )
    assert (
        f"{type(linearizer_0.f_0).__module__}.{type(linearizer_0.f_0).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_0) == 8
    assert (
        f"{type(linearizer_0.f_1).__module__}.{type(linearizer_0.f_1).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_1) == 8
    assert (
        f"{type(linearizer_0.f_2).__module__}.{type(linearizer_0.f_2).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_2) == 8
    assert (
        f"{type(linearizer_0.f_3).__module__}.{type(linearizer_0.f_3).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_3) == 8
    assert (
        f"{type(linearizer_0.f_4).__module__}.{type(linearizer_0.f_4).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_4) == 8
    assert (
        f"{type(linearizer_0.f_c).__module__}.{type(linearizer_0.f_c).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_c) == 8
    assert (
        f"{type(linearizer_0.f_v).__module__}.{type(linearizer_0.f_v).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_v) == 8
    assert (
        f"{type(linearizer_0.f_a).__module__}.{type(linearizer_0.f_a).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_a) == 8
    assert (
        f"{type(linearizer_0.q).__module__}.{type(linearizer_0.q).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.q) == 8
    assert (
        f"{type(linearizer_0.u).__module__}.{type(linearizer_0.u).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.u) == 8
    assert (
        f"{type(linearizer_0.q_i).__module__}.{type(linearizer_0.q_i).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.q_i) == 8
    assert (
        f"{type(linearizer_0.q_d).__module__}.{type(linearizer_0.q_d).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.q_d) == 0
    assert (
        f"{type(linearizer_0.u_i).__module__}.{type(linearizer_0.u_i).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.u_i) == 0
    assert (
        f"{type(linearizer_0.u_d).__module__}.{type(linearizer_0.u_d).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.u_d) == 0
    assert (
        f"{type(linearizer_0.r).__module__}.{type(linearizer_0.r).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.r) == 0
    assert (
        f"{type(linearizer_0.lams).__module__}.{type(linearizer_0.lams).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.lams) == 0
    assert linearizer_0.perm_mat is None


@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"C1\xa0\xd6\xa6D`\xdb\x89\xc6"
    linearizer_0 = module_0.Linearizer(
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        q_d=bytes_0,
        r=bytes_0,
        linear_solver=bytes_0,
    )
    assert (
        f"{type(linearizer_0).__module__}.{type(linearizer_0).__qualname__}"
        == "sympy.physics.mechanics.linearize.Linearizer"
    )
    assert (
        f"{type(linearizer_0.f_0).__module__}.{type(linearizer_0.f_0).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_0) == 10
    assert (
        f"{type(linearizer_0.f_1).__module__}.{type(linearizer_0.f_1).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_1) == 10
    assert (
        f"{type(linearizer_0.f_2).__module__}.{type(linearizer_0.f_2).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_2) == 10
    assert (
        f"{type(linearizer_0.f_3).__module__}.{type(linearizer_0.f_3).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_3) == 10
    assert (
        f"{type(linearizer_0.f_4).__module__}.{type(linearizer_0.f_4).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_4) == 10
    assert (
        f"{type(linearizer_0.f_c).__module__}.{type(linearizer_0.f_c).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_c) == 10
    assert (
        f"{type(linearizer_0.f_v).__module__}.{type(linearizer_0.f_v).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_v) == 10
    assert (
        f"{type(linearizer_0.f_a).__module__}.{type(linearizer_0.f_a).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_a) == 10
    assert (
        f"{type(linearizer_0.q).__module__}.{type(linearizer_0.q).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.q) == 10
    assert (
        f"{type(linearizer_0.u).__module__}.{type(linearizer_0.u).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.u) == 10
    assert (
        f"{type(linearizer_0.q_i).__module__}.{type(linearizer_0.q_i).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.q_i) == 0
    assert (
        f"{type(linearizer_0.q_d).__module__}.{type(linearizer_0.q_d).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.q_d) == 10
    assert (
        f"{type(linearizer_0.u_i).__module__}.{type(linearizer_0.u_i).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.u_i) == 0
    assert (
        f"{type(linearizer_0.u_d).__module__}.{type(linearizer_0.u_d).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.u_d) == 0
    assert (
        f"{type(linearizer_0.r).__module__}.{type(linearizer_0.r).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.r) == 10
    assert (
        f"{type(linearizer_0.lams).__module__}.{type(linearizer_0.lams).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.lams) == 0
    assert linearizer_0.perm_mat is None
    linearizer_0.linearize(A_and_B=bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    bytes_0 = b""
    linearizer_0 = module_0.Linearizer(
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        q_d=bytes_0,
        r=bytes_0,
        linear_solver=bytes_0,
    )
    assert (
        f"{type(linearizer_0).__module__}.{type(linearizer_0).__qualname__}"
        == "sympy.physics.mechanics.linearize.Linearizer"
    )
    assert (
        f"{type(linearizer_0.f_0).__module__}.{type(linearizer_0.f_0).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_0) == 0
    assert (
        f"{type(linearizer_0.f_1).__module__}.{type(linearizer_0.f_1).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_1) == 0
    assert (
        f"{type(linearizer_0.f_2).__module__}.{type(linearizer_0.f_2).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_2) == 0
    assert (
        f"{type(linearizer_0.f_3).__module__}.{type(linearizer_0.f_3).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_3) == 0
    assert (
        f"{type(linearizer_0.f_4).__module__}.{type(linearizer_0.f_4).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_4) == 0
    assert (
        f"{type(linearizer_0.f_c).__module__}.{type(linearizer_0.f_c).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_c) == 0
    assert (
        f"{type(linearizer_0.f_v).__module__}.{type(linearizer_0.f_v).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_v) == 0
    assert (
        f"{type(linearizer_0.f_a).__module__}.{type(linearizer_0.f_a).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_a) == 0
    assert (
        f"{type(linearizer_0.q).__module__}.{type(linearizer_0.q).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.q) == 0
    assert (
        f"{type(linearizer_0.u).__module__}.{type(linearizer_0.u).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.u) == 0
    assert (
        f"{type(linearizer_0.q_i).__module__}.{type(linearizer_0.q_i).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.q_i) == 0
    assert (
        f"{type(linearizer_0.q_d).__module__}.{type(linearizer_0.q_d).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.q_d) == 0
    assert (
        f"{type(linearizer_0.u_i).__module__}.{type(linearizer_0.u_i).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.u_i) == 0
    assert (
        f"{type(linearizer_0.u_d).__module__}.{type(linearizer_0.u_d).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.u_d) == 0
    assert (
        f"{type(linearizer_0.r).__module__}.{type(linearizer_0.r).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.r) == 0
    assert (
        f"{type(linearizer_0.lams).__module__}.{type(linearizer_0.lams).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.lams) == 0
    assert linearizer_0.perm_mat is None
    linearizer_0.linearize(simplify=linearizer_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    bytes_0 = b""
    linearizer_0 = module_0.Linearizer(
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        linear_solver=bytes_0,
    )
    assert (
        f"{type(linearizer_0).__module__}.{type(linearizer_0).__qualname__}"
        == "sympy.physics.mechanics.linearize.Linearizer"
    )
    assert (
        f"{type(linearizer_0.f_0).__module__}.{type(linearizer_0.f_0).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_0) == 0
    assert (
        f"{type(linearizer_0.f_1).__module__}.{type(linearizer_0.f_1).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_1) == 0
    assert (
        f"{type(linearizer_0.f_2).__module__}.{type(linearizer_0.f_2).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_2) == 0
    assert (
        f"{type(linearizer_0.f_3).__module__}.{type(linearizer_0.f_3).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_3) == 0
    assert (
        f"{type(linearizer_0.f_4).__module__}.{type(linearizer_0.f_4).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_4) == 0
    assert (
        f"{type(linearizer_0.f_c).__module__}.{type(linearizer_0.f_c).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_c) == 0
    assert (
        f"{type(linearizer_0.f_v).__module__}.{type(linearizer_0.f_v).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_v) == 0
    assert (
        f"{type(linearizer_0.f_a).__module__}.{type(linearizer_0.f_a).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_a) == 0
    assert (
        f"{type(linearizer_0.q).__module__}.{type(linearizer_0.q).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.q) == 0
    assert (
        f"{type(linearizer_0.u).__module__}.{type(linearizer_0.u).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.u) == 0
    assert (
        f"{type(linearizer_0.q_i).__module__}.{type(linearizer_0.q_i).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.q_i) == 0
    assert (
        f"{type(linearizer_0.q_d).__module__}.{type(linearizer_0.q_d).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.q_d) == 0
    assert (
        f"{type(linearizer_0.u_i).__module__}.{type(linearizer_0.u_i).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.u_i) == 0
    assert (
        f"{type(linearizer_0.u_d).__module__}.{type(linearizer_0.u_d).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.u_d) == 0
    assert (
        f"{type(linearizer_0.r).__module__}.{type(linearizer_0.r).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.r) == 0
    assert (
        f"{type(linearizer_0.lams).__module__}.{type(linearizer_0.lams).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.lams) == 0
    assert linearizer_0.perm_mat is None
    linearizer_0.linearize(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    bytes_0 = b""
    linearizer_0 = module_0.Linearizer(
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
    )
    assert (
        f"{type(linearizer_0).__module__}.{type(linearizer_0).__qualname__}"
        == "sympy.physics.mechanics.linearize.Linearizer"
    )
    assert (
        f"{type(linearizer_0.f_0).__module__}.{type(linearizer_0.f_0).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_0) == 0
    assert (
        f"{type(linearizer_0.f_1).__module__}.{type(linearizer_0.f_1).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_1) == 0
    assert (
        f"{type(linearizer_0.f_2).__module__}.{type(linearizer_0.f_2).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_2) == 0
    assert (
        f"{type(linearizer_0.f_3).__module__}.{type(linearizer_0.f_3).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_3) == 0
    assert (
        f"{type(linearizer_0.f_4).__module__}.{type(linearizer_0.f_4).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_4) == 0
    assert (
        f"{type(linearizer_0.f_c).__module__}.{type(linearizer_0.f_c).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_c) == 0
    assert (
        f"{type(linearizer_0.f_v).__module__}.{type(linearizer_0.f_v).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_v) == 0
    assert (
        f"{type(linearizer_0.f_a).__module__}.{type(linearizer_0.f_a).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_a) == 0
    assert (
        f"{type(linearizer_0.q).__module__}.{type(linearizer_0.q).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.q) == 0
    assert (
        f"{type(linearizer_0.u).__module__}.{type(linearizer_0.u).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.u) == 0
    assert (
        f"{type(linearizer_0.q_i).__module__}.{type(linearizer_0.q_i).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.q_i) == 0
    assert (
        f"{type(linearizer_0.q_d).__module__}.{type(linearizer_0.q_d).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.q_d) == 0
    assert (
        f"{type(linearizer_0.u_i).__module__}.{type(linearizer_0.u_i).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.u_i) == 0
    assert (
        f"{type(linearizer_0.u_d).__module__}.{type(linearizer_0.u_d).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.u_d) == 0
    assert (
        f"{type(linearizer_0.r).__module__}.{type(linearizer_0.r).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.r) == 0
    assert (
        f"{type(linearizer_0.lams).__module__}.{type(linearizer_0.lams).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.lams) == 0
    assert linearizer_0.perm_mat is None
    var_0 = module_1.flatten(bytes_0, bytes_0)
    tuple_0 = (linearizer_0, var_0)
    linearizer_0.linearize(tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    bytes_0 = b""
    linearizer_0 = module_0.Linearizer(
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        linear_solver=bytes_0,
    )
    assert (
        f"{type(linearizer_0).__module__}.{type(linearizer_0).__qualname__}"
        == "sympy.physics.mechanics.linearize.Linearizer"
    )
    assert (
        f"{type(linearizer_0.f_0).__module__}.{type(linearizer_0.f_0).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_0) == 0
    assert (
        f"{type(linearizer_0.f_1).__module__}.{type(linearizer_0.f_1).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_1) == 0
    assert (
        f"{type(linearizer_0.f_2).__module__}.{type(linearizer_0.f_2).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_2) == 0
    assert (
        f"{type(linearizer_0.f_3).__module__}.{type(linearizer_0.f_3).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_3) == 0
    assert (
        f"{type(linearizer_0.f_4).__module__}.{type(linearizer_0.f_4).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_4) == 0
    assert (
        f"{type(linearizer_0.f_c).__module__}.{type(linearizer_0.f_c).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_c) == 0
    assert (
        f"{type(linearizer_0.f_v).__module__}.{type(linearizer_0.f_v).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_v) == 0
    assert (
        f"{type(linearizer_0.f_a).__module__}.{type(linearizer_0.f_a).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_a) == 0
    assert (
        f"{type(linearizer_0.q).__module__}.{type(linearizer_0.q).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.q) == 0
    assert (
        f"{type(linearizer_0.u).__module__}.{type(linearizer_0.u).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.u) == 0
    assert (
        f"{type(linearizer_0.q_i).__module__}.{type(linearizer_0.q_i).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.q_i) == 0
    assert (
        f"{type(linearizer_0.q_d).__module__}.{type(linearizer_0.q_d).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.q_d) == 0
    assert (
        f"{type(linearizer_0.u_i).__module__}.{type(linearizer_0.u_i).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.u_i) == 0
    assert (
        f"{type(linearizer_0.u_d).__module__}.{type(linearizer_0.u_d).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.u_d) == 0
    assert (
        f"{type(linearizer_0.r).__module__}.{type(linearizer_0.r).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.r) == 0
    assert (
        f"{type(linearizer_0.lams).__module__}.{type(linearizer_0.lams).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.lams) == 0
    assert linearizer_0.perm_mat is None
    dict_0 = {linearizer_0: linearizer_0}
    linearizer_0.linearize(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_10():
    bytes_0 = b"\xb5\xcfR\xfb\xcfx\x05#dV\x05\xf1\xba\x8b>\xd4O\x85"
    linearizer_0 = module_0.Linearizer(
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        q_d=bytes_0,
        u_d=bytes_0,
    )
    assert (
        f"{type(linearizer_0).__module__}.{type(linearizer_0).__qualname__}"
        == "sympy.physics.mechanics.linearize.Linearizer"
    )
    assert (
        f"{type(linearizer_0.f_0).__module__}.{type(linearizer_0.f_0).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_0) == 18
    assert (
        f"{type(linearizer_0.f_1).__module__}.{type(linearizer_0.f_1).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_1) == 18
    assert (
        f"{type(linearizer_0.f_2).__module__}.{type(linearizer_0.f_2).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_2) == 18
    assert (
        f"{type(linearizer_0.f_3).__module__}.{type(linearizer_0.f_3).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_3) == 18
    assert (
        f"{type(linearizer_0.f_4).__module__}.{type(linearizer_0.f_4).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_4) == 18
    assert (
        f"{type(linearizer_0.f_c).__module__}.{type(linearizer_0.f_c).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_c) == 18
    assert (
        f"{type(linearizer_0.f_v).__module__}.{type(linearizer_0.f_v).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_v) == 18
    assert (
        f"{type(linearizer_0.f_a).__module__}.{type(linearizer_0.f_a).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_a) == 18
    assert (
        f"{type(linearizer_0.q).__module__}.{type(linearizer_0.q).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.q) == 18
    assert (
        f"{type(linearizer_0.u).__module__}.{type(linearizer_0.u).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.u) == 18
    assert (
        f"{type(linearizer_0.q_i).__module__}.{type(linearizer_0.q_i).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.q_i) == 0
    assert (
        f"{type(linearizer_0.q_d).__module__}.{type(linearizer_0.q_d).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.q_d) == 18
    assert (
        f"{type(linearizer_0.u_i).__module__}.{type(linearizer_0.u_i).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.u_i) == 0
    assert (
        f"{type(linearizer_0.u_d).__module__}.{type(linearizer_0.u_d).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.u_d) == 18
    assert (
        f"{type(linearizer_0.r).__module__}.{type(linearizer_0.r).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.r) == 0
    assert (
        f"{type(linearizer_0.lams).__module__}.{type(linearizer_0.lams).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.lams) == 0
    assert linearizer_0.perm_mat is None
    linearizer_0.linearize(simplify=bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_11():
    bytes_0 = b""
    bytes_1 = b"\xa6l4\x8f`r\x032L&\xf9\xc1%"
    linearizer_0 = module_0.Linearizer(
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_1,
        bytes_1,
        bytes_1,
        bytes_1,
        bytes_1,
        u_d=bytes_0,
        r=bytes_0,
    )
    assert (
        f"{type(linearizer_0).__module__}.{type(linearizer_0).__qualname__}"
        == "sympy.physics.mechanics.linearize.Linearizer"
    )
    assert (
        f"{type(linearizer_0.f_0).__module__}.{type(linearizer_0.f_0).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_0) == 0
    assert (
        f"{type(linearizer_0.f_1).__module__}.{type(linearizer_0.f_1).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_1) == 0
    assert (
        f"{type(linearizer_0.f_2).__module__}.{type(linearizer_0.f_2).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_2) == 0
    assert (
        f"{type(linearizer_0.f_3).__module__}.{type(linearizer_0.f_3).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_3) == 0
    assert (
        f"{type(linearizer_0.f_4).__module__}.{type(linearizer_0.f_4).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_4) == 0
    assert (
        f"{type(linearizer_0.f_c).__module__}.{type(linearizer_0.f_c).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_c) == 0
    assert (
        f"{type(linearizer_0.f_v).__module__}.{type(linearizer_0.f_v).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_v) == 13
    assert (
        f"{type(linearizer_0.f_a).__module__}.{type(linearizer_0.f_a).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.f_a) == 13
    assert (
        f"{type(linearizer_0.q).__module__}.{type(linearizer_0.q).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.q) == 13
    assert (
        f"{type(linearizer_0.u).__module__}.{type(linearizer_0.u).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.u) == 13
    assert (
        f"{type(linearizer_0.q_i).__module__}.{type(linearizer_0.q_i).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.q_i) == 13
    assert (
        f"{type(linearizer_0.q_d).__module__}.{type(linearizer_0.q_d).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.q_d) == 0
    assert (
        f"{type(linearizer_0.u_i).__module__}.{type(linearizer_0.u_i).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.u_i) == 0
    assert (
        f"{type(linearizer_0.u_d).__module__}.{type(linearizer_0.u_d).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.u_d) == 0
    assert (
        f"{type(linearizer_0.r).__module__}.{type(linearizer_0.r).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.r) == 0
    assert (
        f"{type(linearizer_0.lams).__module__}.{type(linearizer_0.lams).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(linearizer_0.lams) == 0
    assert linearizer_0.perm_mat is None
    linearizer_0.linearize(A_and_B=bytes_1)
