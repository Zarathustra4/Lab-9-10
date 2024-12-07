import pytest
from main import generate_safe_password, is_password_save


def test_password_safety():
    password = generate_safe_password()
    assert len(password) > 8
    assert is_password_save(password)[0]


def test_safety_checker():
    unsafe_password = "qwerty"
    safe_password = "Ddmso12Bdk?1d!"

    assert not is_password_save(unsafe_password)[0]
    assert is_password_save(safe_password)[0]


if __name__ == "__main__":
    pytest.main()
