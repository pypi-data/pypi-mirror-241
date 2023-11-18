import pytest

from ...core.vector import Rotator3D, Vector3D, distance3D


class TestVector3D:

    def test_instance(self):
        Vector3D()
        Vector3D(0, 0, 0)
        Vector3D(1, 2, 3)
        Vector3D(1.0, 2, 3)
        Vector3D(1, 2.0, 3)
        Vector3D(1, 2, 3.0)
        Vector3D(-1, -2, -3)

    def test_type(self):
        with pytest.raises(TypeError):
            Vector3D(1, 2, 3)
            Vector3D(1.0, 2, 3)
            Vector3D("1", 2, 3)
            Vector3D([1], 2, 3)
            Vector3D((1,), 2, 3)
            Vector3D({1}, 2, 3)
            Vector3D({1: 1}, 2, 3)
            Vector3D(True, 2, 3)
            Vector3D(None, 2, 3)

            Vector3D(1, 2, 3)
            Vector3D(1, 2.0, 3)
            Vector3D(1, "2", 3)
            Vector3D(1, [2], 3)
            Vector3D(1, (2,), 3)
            Vector3D(1, {2}, 3)
            Vector3D(1, {2: 2}, 3)
            Vector3D(1, True, 3)
            Vector3D(1, None, 3)

            Vector3D(1, 2, 3)
            Vector3D(1, 2, 3.0)
            Vector3D(1, 2, "3")
            Vector3D(1, 2, [3])
            Vector3D(1, 2, (3,))
            Vector3D(1, 2, {3})
            Vector3D(1, 2, {3: 3})
            Vector3D(1, 2, True)
            Vector3D(1, 2, None)

    def test_access(self):
        v = Vector3D(1, 2, 3)
        assert v.x == 1
        assert v.y == 2
        assert v.z == 3

        assert isinstance(v.x, float)
        assert isinstance(v.y, float)
        assert isinstance(v.z, float)

    def test_add(self):
        v1 = Vector3D(1, 2, 3)
        v2 = Vector3D(1, 2, 3)
        assert v1 + v2 == Vector3D(2, 4, 6)

    def test_sub(self):
        v1 = Vector3D(1, 2, 3)
        v2 = Vector3D(1, 2, 3)
        assert v1 - v2 == Vector3D(0, 0, 0)

    def test_mul(self):
        v = Vector3D(1, 2, 3)
        c = 1
        assert v * c == Vector3D(1, 2, 3)

        v = Vector3D(1, 2, 3)
        c = 2
        assert v * c == Vector3D(2, 4, 6)

        v = Vector3D(1, 2, 3)
        c = 0
        assert v * c == Vector3D(0, 0, 0)

        v = Vector3D(1, 2, 3)
        c = -1
        assert v * c == Vector3D(-1, -2, -3)

    def test_div(self):
        v = Vector3D(1, 2, 3)
        c = 1
        assert v / c == Vector3D(1, 2, 3)

        v = Vector3D(1, 2, 3)
        c = 2
        assert v / c == Vector3D(0.5, 1, 1.5)

        v = Vector3D(1, 2, 3)
        c = -1
        assert v / c == Vector3D(-1, -2, -3)

    def test_eq(self):
        v1 = Vector3D(1, 2, 3)
        v2 = Vector3D(1, 2, 3)
        assert v1 == v2

        v1 = Vector3D(1, 2, 3)
        v2 = Vector3D(1, 2, 4)
        assert v1 != v2

        v1 = Vector3D(1, 2, 3)
        v2 = Vector3D(1, 3, 3)
        assert v1 != v2

        v1 = Vector3D(1, 2, 3)
        v2 = Vector3D(2, 2, 3)
        assert v1 != v2

    def test_str(self):
        v = Vector3D(1, 2, 3)
        assert str(v) == "(1.0, 2.0, 3.0)"

        v = Vector3D(1.0, 2.0, 3.0)
        assert str(v) == "(1.0, 2.0, 3.0)"

        v = Vector3D(1.0, 2, 3)
        assert str(v) == "(1.0, 2.0, 3.0)"

        v = Vector3D(1, 2.0, 3)
        assert str(v) == "(1.0, 2.0, 3.0)"

        v = Vector3D(1, 2, 3.0)
        assert str(v) == "(1.0, 2.0, 3.0)"

        v = Vector3D(-1, -2, -3)
        assert str(v) == "(-1.0, -2.0, -3.0)"

    def test_repr(self):
        v = Vector3D(1, 2, 3)
        assert repr(v) == "Vector3D(1.0, 2.0, 3.0)"

        v = Vector3D(1.0, 2.0, 3.0)
        assert repr(v) == "Vector3D(1.0, 2.0, 3.0)"

        v = Vector3D(1.0, 2, 3)
        assert repr(v) == "Vector3D(1.0, 2.0, 3.0)"

        v = Vector3D(1, 2.0, 3)
        assert repr(v) == "Vector3D(1.0, 2.0, 3.0)"

        v = Vector3D(1, 2, 3.0)
        assert repr(v) == "Vector3D(1.0, 2.0, 3.0)"

        v = Vector3D(-1, -2, -3)
        assert repr(v) == "Vector3D(-1.0, -2.0, -3.0)"

    def test_abs(self):
        v = Vector3D(1, 2, 3)
        assert abs(v) == Vector3D(1, 2, 3)

        v = Vector3D(1.0, 2.0, 3.0)
        assert abs(v) == Vector3D(1.0, 2.0, 3.0)

        v = Vector3D(-1, 2, 3)
        assert abs(v) == Vector3D(1, 2, 3)

        v = Vector3D(1, -2, 3)
        assert abs(v) == Vector3D(1, 2, 3)

        v = Vector3D(1, 2, -3)
        assert abs(v) == Vector3D(1, 2, 3)

        v = Vector3D(-1, -2, -3)
        assert abs(v) == Vector3D(1, 2, 3)

        v = Vector3D(0, 0, 0)
        assert abs(v) == Vector3D(0, 0, 0)

    def test_hash(self):
        v = Vector3D(1, 2, 3)
        assert hash(v) == hash((1, 2, 3))

        v = Vector3D(1.0, 2.0, 3.0)
        assert hash(v) == hash((1.0, 2.0, 3.0))


class TestRotator3D:

    def test_instance(self):
        Rotator3D()
        Rotator3D(0, 0, 0)
        Rotator3D(1, 2, 3)
        Rotator3D(1.0, 2, 3)
        Rotator3D(1, 2.0, 3)
        Rotator3D(1, 2, 3.0)
        Rotator3D(-1, -2, -3)

    def test_type(self):
        with pytest.raises(TypeError):
            Rotator3D(1, 2, 3)
            Rotator3D(1.0, 2, 3)
            Rotator3D("1", 2, 3)
            Rotator3D([1], 2, 3)
            Rotator3D((1,), 2, 3)
            Rotator3D({1}, 2, 3)
            Rotator3D({1: 1}, 2, 3)
            Rotator3D(True, 2, 3)
            Rotator3D(None, 2, 3)

            Rotator3D(1, 2, 3)
            Rotator3D(1, 2.0, 3)
            Rotator3D(1, "2", 3)
            Rotator3D(1, [2], 3)
            Rotator3D(1, (2,), 3)
            Rotator3D(1, {2}, 3)
            Rotator3D(1, {2: 2}, 3)
            Rotator3D(1, True, 3)
            Rotator3D(1, None, 3)

            Rotator3D(1, 2, 3)
            Rotator3D(1, 2, 3.0)
            Rotator3D(1, 2, "3")
            Rotator3D(1, 2, [3])
            Rotator3D(1, 2, (3,))
            Rotator3D(1, 2, {3})
            Rotator3D(1, 2, {3: 3})
            Rotator3D(1, 2, True)
            Rotator3D(1, 2, None)

    def test_access(self):
        v = Rotator3D(1, 2, 3)
        assert v.x == 0.017453292519943295
        assert v.y == 0.03490658503988659
        assert v.z == 0.05235987755982989

        assert isinstance(v.x, float)
        assert isinstance(v.y, float)
        assert isinstance(v.z, float)

    def test_str(self):
        v = Rotator3D(1, 2, 3)
        assert str(v) == "(0.017453292519943295, 0.03490658503988659, 0.05235987755982989)"

        v = Rotator3D(1.0, 2.0, 3.0)
        assert str(v) == "(0.017453292519943295, 0.03490658503988659, 0.05235987755982989)"

        v = Rotator3D(1.0, 2, 3)
        assert str(v) == "(0.017453292519943295, 0.03490658503988659, 0.05235987755982989)"

        v = Rotator3D(1, 2.0, 3)
        assert str(v) == "(0.017453292519943295, 0.03490658503988659, 0.05235987755982989)"

        v = Rotator3D(1, 2, 3.0)
        assert str(v) == "(0.017453292519943295, 0.03490658503988659, 0.05235987755982989)"

        v = Rotator3D(-1, -2, -3)
        assert str(v) == "(-0.017453292519943295, -0.03490658503988659, -0.05235987755982989)"

    def test_repr(self):
        v = Rotator3D(1, 2, 3)
        assert repr(v) == "Rotator3D(0.017453292519943295, 0.03490658503988659, 0.05235987755982989)"

        v = Rotator3D(1.0, 2.0, 3.0)
        assert repr(v) == "Rotator3D(0.017453292519943295, 0.03490658503988659, 0.05235987755982989)"

        v = Rotator3D(1.0, 2, 3)
        assert repr(v) == "Rotator3D(0.017453292519943295, 0.03490658503988659, 0.05235987755982989)"

        v = Rotator3D(1, 2.0, 3)
        assert repr(v) == "Rotator3D(0.017453292519943295, 0.03490658503988659, 0.05235987755982989)"

        v = Rotator3D(1, 2, 3.0)
        assert repr(v) == "Rotator3D(0.017453292519943295, 0.03490658503988659, 0.05235987755982989)"

        v = Rotator3D(-1, -2, -3)
        assert repr(v) == "Rotator3D(-0.017453292519943295, -0.03490658503988659, -0.05235987755982989)"


class TestDistance3D:
    def test_operation(self):
        assert distance3D(Vector3D(0, 0, 0), Vector3D(0, 0, 0)) == 0
        assert distance3D(Vector3D(0, 0, 0), Vector3D(1, 0, 0)) == 1
        assert distance3D(Vector3D(0, 0, 0), Vector3D(0, 1, 0)) == 1
        assert distance3D(Vector3D(0, 0, 0), Vector3D(0, 0, 1)) == 1
        assert distance3D(Vector3D(0, 0, 0), Vector3D(1, 1, 1)) == 1.7320508075688772
        assert distance3D(Vector3D(0, 0, 0), Vector3D(1, 2, 3)) == 3.7416573867739413
        assert distance3D(Vector3D(0, 0, 0), Vector3D(-1, -2, -3)) == 3.7416573867739413
        assert distance3D(Vector3D(1, 2, 3), Vector3D(1, 2, 3)) == 0

    def test_type(self):
        with pytest.raises(TypeError):
            distance3D(1, Vector3D(0, 0, 0))
            distance3D(1.0, Vector3D(0, 0, 0))
            distance3D("1", Vector3D(0, 0, 0))
            distance3D([1], Vector3D(0, 0, 0))
            distance3D((1,), Vector3D(0, 0, 0))
            distance3D({1}, Vector3D(0, 0, 0))
            distance3D({1: 1}, Vector3D(0, 0, 0))
            distance3D(True, Vector3D(0, 0, 0))
            distance3D(None, Vector3D(0, 0, 0))
