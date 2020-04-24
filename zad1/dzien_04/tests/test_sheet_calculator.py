import unittest

from dzien_04.csv_execise import SheetCalculator


class TestSheetCalculator(unittest.TestCase):
    def test_get_column(self):
        sheet_calculator = SheetCalculator([[
            "column1","column2","column3"],
            [1,2,3]
        ])
        expected_result = ["column3",3]

        # WHEN
        result = sheet_calculator.get_column(2)
        # THEN
        assert  result == expected_result
        #2
        self.assertEqual(result,expected_result)

    def test_get_column_index_minus(self):
        # GIVEN
        sheet_calculator = SheetCalculator([
            ['column1', 'column2', 'column3'],
            [1, 2, 3]
        ])
        expected_result = ['column3', 3]
        argument = -1
        # WHEN
        result = sheet_calculator.get_column(argument)
        # THEN
        self.assertEqual(expected_result, result)


    def test_get_column_index_out_of_range(self):
        sheet_calculator = SheetCalculator([[
            "column1", "column2", "column3"],
            [1, 2, 3]
        ])

        exected_result = None

        argument = 4
# when

        with self.assertRaises(IndexError) as exeption:
            result = sheet_calculator.get_column(argument)

    #THEN
    #print(exeption)


    def test_get_row(self):
        #GIVEN
        sheet_calculator = SheetCalculator([
            ["column1" , "column2", "column3"],
            [1,2,3]
        ])
        expected_result = ["column1","column2","column3"]

        #WHEN
        result = sheet_calculator.get_row(0)
        print(result)
        #THEN
        self.assertEqual(result,expected_result)