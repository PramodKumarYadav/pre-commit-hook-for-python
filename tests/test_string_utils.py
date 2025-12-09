"""Tests for the StringUtils class."""

from src.sample_module.string_utils import StringUtils


class TestStringUtils:
    """Test cases for StringUtils class."""

    def test_reverse_string(self):
        """Test string reversal."""
        assert StringUtils.reverse_string("hello") == "olleh"
        assert StringUtils.reverse_string("") == ""
        assert StringUtils.reverse_string("a") == "a"
        assert StringUtils.reverse_string("Python") == "nohtyP"

    def test_is_palindrome(self):
        """Test palindrome detection."""
        assert StringUtils.is_palindrome("racecar") is True
        assert StringUtils.is_palindrome("A man a plan a canal Panama") is True
        assert StringUtils.is_palindrome("hello") is False
        assert StringUtils.is_palindrome("") is True
        assert StringUtils.is_palindrome("a") is True

    def test_capitalize_words(self):
        """Test word capitalization."""
        assert StringUtils.capitalize_words("hello world") == "Hello World"
        assert (
            StringUtils.capitalize_words("python programming") == "Python Programming"
        )
        assert StringUtils.capitalize_words("a") == "A"
        assert StringUtils.capitalize_words("") == ""

    def test_count_vowels(self):
        """Test vowel counting."""
        assert StringUtils.count_vowels("hello") == 2
        assert StringUtils.count_vowels("aeiou") == 5
        assert StringUtils.count_vowels("AEIOU") == 5
        assert StringUtils.count_vowels("bcdfg") == 0
        assert StringUtils.count_vowels("") == 0
        assert StringUtils.count_vowels("Python Programming") == 4

    def test_remove_whitespace(self):
        """Test whitespace removal."""
        assert StringUtils.remove_whitespace("hello world") == "helloworld"
        assert StringUtils.remove_whitespace("  a  b  c  ") == "abc"
        assert StringUtils.remove_whitespace("nospace") == "nospace"
        assert StringUtils.remove_whitespace("") == ""
