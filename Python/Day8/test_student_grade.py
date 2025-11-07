import unittest
from student_grade_function import*

class TestForStudentGrades(unittest.TestCase):

	def test_the_function_get_student(grades):
		actual = get_number_of_students(3)
		expected = [3 , 3 , 3]
		grades.assertEqual(actual , expected)

	
	def test_the_calculate_the_sum_of_grades_function(space):
		actual = calculate_the_sum_of_grades([[2, 4] ,[3, 5],  [1, 1]])
		expected = [6, 8, 2]
		space.assertEqual(actual , expected)

	def test_the_calculate_average_of_grades(ave):
		actual = calculate_average_of_grades([30] , 2)
		expected = [15.0]
		ave.assertEqual(actual , expected)
