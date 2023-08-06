import unittest
from os.path import join 
from os import getcwd, remove
from foxTemplateEngine import transform



def compare_files(path_to_first: str, path_to_second: str) -> bool:

    answer = True
    with open(path_to_first) as first, open(path_to_second) as second:
        first_gen = (line for line in first)
        second_gen = (line for line in second)
        for line in first_gen:
            for line_ in second_gen:
                if line != line_:
                    answer = False
                break
    
    return answer


class EngineTest(unittest.TestCase):
    
    def test_loops(self):
        current_dir = getcwd()
        for_test_path = join(current_dir, 'tests/input/test_loops')
        output_path = join(current_dir, 'tests/output/test_loops')
        fox_file = join(current_dir, 'tests/input/test_loops.html')
        transform(for_test_path, {})
        self.assertTrue(compare_files(output_path, fox_file))
        remove(join(current_dir, 'tests/input/test_loops.html')) # Удаление файлы, созданного во время теста

    def test_variable(self):
        current_dir = getcwd()
        for_test_path = join(current_dir, 'tests/input/test_variable')
        output_path = join(current_dir, 'tests/output/test_variable')
        fox_file = join(current_dir, 'tests/input/test_variable.html')
        transform(for_test_path, {
            'test_var': 'Hello, World!'
        })
        self.assertTrue(compare_files(output_path, fox_file))
        remove(join(current_dir, 'tests/input/test_variable.html')) # Удаление файлы, созданного во время теста

    def test_all(self):
        current_dir = getcwd()
        for_test_path = join(current_dir, 'tests/input/test_all')
        output_path = join(current_dir, 'tests/output/test_all')
        fox_file = join(current_dir, 'tests/input/test_all.html')
        transform(for_test_path, {
            'var': 'Hello, World!'
        })
        self.assertTrue(compare_files(output_path, fox_file))
        remove(join(current_dir, 'tests/input/test_all.html')) # Удаление файлы, созданного во время теста


if __name__ == '__main__':
    unittest.main()