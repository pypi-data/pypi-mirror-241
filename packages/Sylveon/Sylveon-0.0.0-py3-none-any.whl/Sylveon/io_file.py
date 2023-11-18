import os
import platform
import subprocess


class IOFile:
    running_cmd = None

    def __init__(self, path_dir :str = "",prefix: str = "", id: int = None, **kwargs):
        """
        Initialize an IOFile instance.

        Parameters:
            - `prefix` (str): Prefix for the file names.
            - `id` (int): ID for the file names.
            - `**kwargs`: Additional arguments, such as 'extension' and 'disable_output'.
        """
        input_extension = kwargs.get("extension", ".in")
        output_extension = kwargs.get("extension", ".out")
        id = "" if id is None else str(id)
        self.input_file_name = os.path.join(path_dir,"{}{}{}".format(prefix, id, input_extension))
        self.output_file_name = os.path.join(path_dir,"{}{}{}".format(prefix, id, output_extension))
        disable_output = kwargs.get("disable_output", False)
        if IOFile.running_cmd is None:
            disable_output = True
        self.input_file = open(self.input_file_name, 'w+')
        if disable_output:
            self.output_file = None
        else:
            self.output_file = open(self.output_file_name, 'w+')
        self.__input_is_first_symbol = True

    def __del__(self):
        self.input_file.close()
        self.output_file.close()

    def __input_write_aux(self, *args, **kwargs):
        """
        Helper function for writing to the input file.

        Parameters:
            - `*args`: Variable number of arguments to write.
            - `**kwargs`: Additional keyword arguments, such as 'separator'.
        """
        separator = kwargs.get("separator", " ")
        for arg in args:
            if isinstance(arg, (list, tuple)):
                self.__input_write_aux(*arg, **kwargs)
            else:
                if not self.__input_is_first_symbol:
                    self.input_file.write(str(separator))
                self.input_file.write(str(arg))
                self.__input_is_first_symbol = False

    def __input_write(self, *args, **kwargs):
        """
        Write to the input file.

        Parameters:
            - `*args`: Variable number of arguments to write.
            - `**kwargs`: Additional keyword arguments, such as 'separator'.
        """
        self.__input_write_aux(*args, **kwargs)
        self.__input_is_first_symbol = True
        self.input_file.write('\n')

    def input_writeln(self, *args, **kwargs):
        """
        Write a line to the input file.

        Parameters:
            - `*args`: Variable number of arguments to write.
            - `**kwargs`: Additional keyword arguments, such as 'separator'.
        """
        self.__input_write(*args, **kwargs)

    def input_write_mat(self, matrix, **kwargs):
        """
        Write a matrix to the input file.

        Parameters:
            - `matrix`: 2D matrix to write.
            - `**kwargs`: Additional keyword arguments, such as 'separator'.
        """
        for array in matrix:
            self.__input_write(*array, **kwargs)

    @staticmethod
    def __try_to_compile_cpp(std_file_path, *args):
        """
        Try to compile a C++ file.

        Parameters:
            - `std_file_path` (str): Path to the C++ file.
            - `*args`: Additional command-line arguments for compilation.

        Returns:
            - list: Command to run the compiled C++ executable.
        """
        os_type = platform.system().lower()
        if os_type == "windows":
            extension = ".exe"
        elif os_type == "linux":
            extension = ".o"
        else:
            raise "Unknown system type: {}".format(os_type)

        if "-o" in args:
            pos = args.index("-o")
            if pos + 1 < len(args):
                executable_path = args[pos + 1]
                executable_path = os.path.realpath(executable_path)
                if not executable_path.endswith(extension):
                    executable_path += extension
        else:
            executable_path = os.path.splitext(std_file_path)[0]
            if not executable_path.endswith(extension):
                executable_path += extension
            args = list(args) + ["-o", executable_path]

        cmd = ["g++", std_file_path] + list(args)
        print(cmd)
        result = subprocess.run(cmd, stderr=subprocess.PIPE, text=True)

        if result.returncode == 0:
            print("The file {} compiled successfully".format(std_file_path))
        else:
            raise Exception(
                "The file {} failed to compile. The return code is {}. Here are the error messages from stderr:\n{}".
                format(std_file_path, result.returncode, result.stderr))
        return [executable_path]

    @staticmethod
    def set_std(std_file_path, *args):
        """
        Set the standard file for running.

        Parameters:
            - `std_file_path` (str): Path to the standard file.
            - `*args`: Additional command-line arguments for execution.
        """
        std_file_path = os.path.realpath(std_file_path)
        extension = os.path.splitext(std_file_path)[-1]
        if extension.lower() in [".c++", ".cpp", ".cc", ".cxx"]:
            IOFile.running_cmd = IOFile.__try_to_compile_cpp(std_file_path, *args)
        elif extension.lower() in [".py"]:
            IOFile.running_cmd = ["python", std_file_path] + list(args)
        else:
            raise ValueError("Unknown extension for file: {}".format(extension))
        print(IOFile.running_cmd)

    def gen_output(self):
        if self.output_file is None:
            raise "Output is disable."
        self.input_file.flush()
        self.input_file.seek(0)
        result = subprocess.run(self.running_cmd, stdin=self.input_file, stdout=self.output_file,
                                stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            raise Exception("The return code is {}. Here are the error messages from stderr:\n{}".
                            format(result.returncode, result.stderr))
        else:
            print("Input file {} generate output successfully.".format(self.input_file_name))


if __name__ == '__main__':
    test_data = IOFile("p", 1)
    test_data.input_writeln(1, 2, 3, 4, [1, 2, 3], [1, 4, 5, 6], [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    test_data.input_write_mat([[1, 2, 3], [4, 5, 6]])
    test_data.input_writeln("aaa", "b", ["AAA", '1234', ["456", 456]])
    IOFile.set_std("main.cpp")
    IOFile.set_std("main.cpp", "-o", "main3.exe")
    IOFile.set_std("1.py", "-o", "main3.exe")
