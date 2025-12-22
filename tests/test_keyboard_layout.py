"""Tests for macOS keyboard layout fix."""
import sys
import pytest

pytestmark = pytest.mark.skipif(
    sys.platform != 'darwin',
    reason="macOS keyboard layout tests only run on macOS"
)

def test_isPrintableChar():
    from pyautogui._pyautogui_osx import _isPrintableChar
    assert _isPrintableChar('a') == True
    assert _isPrintableChar('Z') == True
    assert _isPrintableChar('0') == True
    assert _isPrintableChar('@') == True
    assert _isPrintableChar('enter') == False
    assert _isPrintableChar('tab') == False

def test_typeUnicodeChar_exists():
    from pyautogui._pyautogui_osx import _typeUnicodeChar
    assert callable(_typeUnicodeChar)
