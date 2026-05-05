import os
import tempfile
import unittest

from lab6 import find_min_latency, run_files, solve


class TestLab6(unittest.TestCase):
    def test_pdf_example(self):
        n = 6
        clients = [1, 5, 6]
        edges = [
            (1, 2, 10),
            (2, 3, 80),
            (3, 4, 50),
            (4, 5, 20),
            (2, 6, 40),
            (3, 6, 100),
        ]
        self.assertEqual(find_min_latency(n, clients, edges), 100)

    def test_solve_from_text(self):
        text = (
            "6 6\n"
            "1 5 6\n"
            "1 2 10\n"
            "2 3 80\n"
            "3 4 50\n"
            "4 5 20\n"
            "2 6 40\n"
            "3 6 100"
        )
        self.assertEqual(solve(text), 100)

    def test_reads_and_writes_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            in_path = os.path.join(tmp, "gamsrv.in")
            out_path = os.path.join(tmp, "gamsrv.out")
            with open(in_path, "w", encoding="utf-8") as f:
                f.write("3 2\n1 3\n1 2 5\n2 3 7")
            run_files(in_path, out_path)
            with open(out_path, "r", encoding="utf-8") as f:
                self.assertEqual(f.read().strip(), "7")


if __name__ == "__main__":
    unittest.main()
