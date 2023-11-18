from .utils import rand


class StringGen:
    @staticmethod
    def gen_string(n: int, char_set):
        """
        Generate a random string of a specified length using characters from a given character set.

        Parameters:
            - `n` (int): Length of the generated string.
            - `char_set`: Set of characters to choose from.

        Returns:
            - str: The generated random string.
        """
        return rand.gen_string(n, char_set)

    @staticmethod
    def gen_string_matrix(n, m, char_set):
        """
        Generate a matrix of random strings.

        Parameters:
            - `n` (int): Number of rows in the matrix.
            - `m` (int): Number of columns in the matrix.
            - `char_set`: Set of characters to choose from.

        Returns:
            - str: The generated matrix of random strings.
        """
        return "\n".join(StringGen.gen_string(m, char_set) for _ in range(n))