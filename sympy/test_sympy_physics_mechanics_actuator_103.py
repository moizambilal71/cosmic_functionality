# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import sympy.physics.mechanics.actuator as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    module_0.ForceActuator(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    module_0.LinearSpring(bool_0, bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 1056.4477704102292
    module_0.LinearDamper(float_0, float_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    object_0 = module_1.object()
    module_0.TorqueActuator(object_0, object_0, object_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    module_0.TorqueActuator(bool_0, bool_0, bool_0)


def test_case_5():
    tuple_0 = ()
    with pytest.raises(TypeError):
        module_0.DuffingSpring(tuple_0, tuple_0, tuple_0)
