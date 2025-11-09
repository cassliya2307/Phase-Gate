import unittest

from student_grade_functions import*

class TestStudentGradeFunction(unittest.TestCase):
	
	def test_the_get_total_function(self):
		actual = get_subject_total_for_each_student([[2,3] , [8,9]])
		expected = [5.0 , 17.0]
		self.assertEqual(actual , expected)	
	
	def test_the_get_average_function(self):
		actual = get_subject_average_for_each_student([[5,5] , [2,2]])
		expected = ["5.0" , "2.0"]
		self.assertEqual(actual , expected)

	def test_the_student_record_function(self):
		actual = get_student_records([[2,3] , [8,9]] ,["sasha" , "dora"], ["maths" , "physics"])
		expected = [["sasha" , 2 , 3 , 5, "2.5"] , ["dora" , 8 , 9 , 17 , "8.5"]]
		self.assertEqual(actual , expected)

	def test_the_get_number_of_passes_function(self):
		actual = get_number_of_passes([[40 , 10]])
		expected = [1]
		self.assertEqual(actual , expected)


	def test_the_get_number_of_failes_function(self):
		actual = get_number_of_failes([[40 , 10]])
		expected = [1]
		self.assertEqual(actual , expected)

	
