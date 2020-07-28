from vector import Vector

def test_create_vector_object():
    v = Vector()
    assert isinstance(v, Vector)

def test_check_dimensions():
    v1 = Vector(3, 4)
    v2 = Vector(3, 4, 5)
    assert v1.dim == 2
    assert v2.dim == 3
    assert v1.storage == (3, 4)
    assert v2.storage == (3,4,5)

def test_add_vectors():
    v1 = Vector(3, 4)
    v2 = Vector(5, 6)
    v3 = v1 + v2
    assert v3.dim == 2

def test_vector_dot_product():
    v1 = Vector(3,4,5)
    v2 = Vector(5,6,7)
    scalar = v1 * v2
    assert isinstance(scalar, float)
    assert scalar == (15 + 24 + 35)

def test_scale_vector():
    v1 = Vector(3,4,5)
    v2 = v1 * 2
    assert isinstance(v2, Vector)
    assert v2.dim == 3
    assert v2.storage == (6,8,10)

def test_vector_norm():
    v1 = Vector(3,4)
    norm = v1.norm()
    assert norm == 5