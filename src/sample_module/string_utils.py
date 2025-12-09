"""String utility functions to demonstrate code formatting and linting."""


class StringUtils:
    """A utility class for string operations."""

    @staticmethod
    def reverse_string(text: str) -> str:
        """Reverse a string.

        Args:
            text: The string to reverse

        Returns:
            The reversed string
        """
        return text[::-1]

    @staticmethod
    def is_palindrome(text: str) -> bool:
        """Check if a string is a palindrome.

        Ignores spaces, punctuation, and case when checking.

        Args:
            text: The string to check

        Returns:
            True if the string is a palindrome, False otherwise
        """
        # Remove non-alphanumeric characters and convert to lowercase
        cleaned = "".join(char.lower() for char in text if char.isalnum())
        return cleaned == cleaned[::-1]

    @staticmethod
    def capitalize_words(text: str) -> str:
        """Capitalize the first letter of each word.

        Args:
            text: The string to capitalize

        Returns:
            String with each word capitalized
        """
        return " ".join(word.capitalize() for word in text.split())

    @staticmethod
    def count_vowels(text: str) -> int:
        """Count the number of vowels in a string.

        Args:
            text: The string to analyze

        Returns:
            Number of vowels in the string
        """
        vowels = "aeiouAEIOU"
        return sum(1 for char in text if char in vowels)

    @staticmethod
    def remove_whitespace(text: str) -> str:
        """Remove all whitespace from a string.

        Args:
            text: The string to process

        Returns:
            String with all whitespace removed
        """
        return "".join(text.split())
