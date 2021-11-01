import game


def test_step():
    matrix_tests = (
        (([0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]), True),

        (([1, 1, 1],
          [1, 1, 1],
          [1, 1, 1]), False),

        (([2, 2, 2],
          [0, 2, 2],
          [0, 2, 2]), True),

        (([0, 0, 0],
          [1, 1, 1],
          [1, 1, 2]), True),
    )

    for test in matrix_tests:
        assert game.step_possibility(test[0]) is test[1], test[0]


def test_step_check():
    matrix_tests = (
        ('0 1', ([0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]), [0, 1]),

        ('p 1', ([0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]), None),
    )

    for test in matrix_tests:
        assert game.step_check(test[0], test[1]) == test[2], test[0]


def test_save_step():
    matrix_tests = (
        [0, 1], ([0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]), 'Alex', ([0, 'Alex', 0],
                                      [0, 0, 0],
                                      [0, 0, 0])
    )

    assert game.save_step(matrix_tests[0], matrix_tests[1], matrix_tests[2]) == matrix_tests[3]


test_step()
test_step_check()
test_save_step()
