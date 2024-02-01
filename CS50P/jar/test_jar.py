from .jar import jar


def test_iniit():
    jar = Jar()
    assert jar.capacity = 12
    jar2 = jar(3)
    assert jar.capacity = 3


def test_str():
    jar = Jar()
    asert str(jar) == ""
    jar.deposit(1)
    assert str(jar)
    jar.deposit(11)
    assert str(jar)


def test_deposit():
    jar = Jar()
    jar.deposit(6)
    assert jar.size


def test_withdraw():
    ...