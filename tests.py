import unittest
import slv398


class TestInitBoard(unittest.TestCase):

    def test_4x4(self):
        board_size = 4
        board_data = [[0 for i in range(board_size)] for j in range(board_size)]
        board = slv398.SudokuBoard(board_size, board_data)
        slv398.init_domain(board, False)
        self.assertEqual(
            [[[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
             [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
             [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
             [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]],
            board.CurrentGameBoard)

    def test_9x9(self):
        board_size = 9
        board_data = [[0 for i in range(board_size)] for j in range(board_size)]
        board = slv398.SudokuBoard(board_size, board_data)
        slv398.init_domain(board, False)
        self.assertEqual(
            [[[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
             [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
             [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
             [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
             [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
             [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
             [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
             [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
             [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]]],
            board.CurrentGameBoard)

    def test_no_forward_checking(self):
        board_size = 4
        board_data = [[0 for i in range(board_size)] for j in range(board_size)]
        board_data[0][0] = 1
        board = slv398.SudokuBoard(board_size, board_data)
        slv398.init_domain(board, False)
        self.assertEqual(
            [[1, [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
             [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
             [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
             [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]],
            board.CurrentGameBoard)

    def test_with_forward_checking(self):
        board_size = 4
        board_data = [[0 for i in range(board_size)] for j in range(board_size)]
        board_data[0][0] = 1
        board = slv398.SudokuBoard(board_size, board_data)
        slv398.init_domain(board, True)
        self.assertEqual(
            [[1, [2, 3, 4], [2, 3, 4], [2, 3, 4]],
             [[2, 3, 4], [2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
             [[2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
             [[2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]],
            board.CurrentGameBoard)

    def test_impossible(self):
        board_size = 4
        board_data = [[0 for i in range(board_size)] for j in range(board_size)]
        board_data[0][0] = 1
        board_data[1][0] = 1
        board = slv398.SudokuBoard(board_size, board_data)
        slv398.init_domain(board, True)
        self.assertEqual(
            [[1, [2, 3, 4], [2, 3, 4], [2, 3, 4]],
             [1, [2, 3, 4], [2, 3, 4], [2, 3, 4]],
             [[2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
             [[2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]],
            board.CurrentGameBoard)

    def test_solve_4x4(self):
        newboard = slv398.init_board("input_puzzles/easy/4_4.sudoku")
        slv398.init_domain(newboard, False)
        self.assertEqual(True, slv398.is_complete(slv398.solve(newboard)))

    def test_solve_9x9(self):
        newboard = slv398.init_board("input_puzzles/easy/9_9.sudoku")
        slv398.init_domain(newboard, False)
        self.assertEqual(True, slv398.is_complete(slv398.solve(newboard)))

    def test_board_valid(self):
        newboard = slv398.init_board("input_puzzles/easy/4_4.sudoku")
        slv398.init_domain(newboard, False)
        self.assertEqual(True, slv398.is_board_valid(newboard))

    def test_FC_solve_4x4(self):
        print "test_FC_solve_4x4"
        newboard = slv398.init_board("input_puzzles/easy/4_4.sudoku")
        slv398.init_domain(newboard, True)
        self.assertEqual(True, slv398.is_complete(slv398.solve(newboard, True)))

    def test_FC_solve_9x9(self):
        print "test_FC_solve_9x9"
        newboard = slv398.init_board("input_puzzles/easy/9_9.sudoku")
        slv398.init_domain(newboard, True)
        self.assertEqual(True, slv398.is_complete(slv398.solve(newboard, True)))

    def test_MRV_solve_9x9(self):
        print "test_MRV_solve_9x9"
        newboard = slv398.init_board("input_puzzles/easy/9_9.sudoku")
        slv398.init_domain(newboard, True)
        self.assertEqual(True, slv398.is_complete(slv398.solve(newboard, True, True)))

    def test_MRV_solve_4x4(self):
        print "test_MRV_solve_4x4"
        newboard = slv398.init_board("input_puzzles/easy/4_4.sudoku")
        slv398.init_domain(newboard, True)
        self.assertEqual(True, slv398.is_complete(slv398.solve(newboard, True, True)))


class TestConstraints(unittest.TestCase):

    def test_basic_4(self):
        board_size = 4
        board_data = [[0 for i in range(board_size)] for j in range(board_size)]
        board = slv398.SudokuBoard(board_size, board_data)
        slv398.init_domain(board, True)
        self.assertEqual(8, slv398.count_constraints(board, 0, 0))

    def test_basic_9(self):
        board_size = 9
        board_data = [[0 for i in range(board_size)] for j in range(board_size)]
        board = slv398.SudokuBoard(board_size, board_data)
        slv398.init_domain(board, True)
        self.assertEqual(21, slv398.count_constraints(board, 0, 0))

    def test_more_4(self):
        board_size = 4
        board_data = [[0 for i in range(board_size)] for j in range(board_size)]
        board_data[0][1] = 1
        board = slv398.SudokuBoard(board_size, board_data)
        slv398.init_domain(board, True)
        board.print_board()
        self.assertEqual(7, slv398.count_constraints(board, 0, 0))