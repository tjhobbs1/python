from class_defintions import student as s
import unittest

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = s.Student('hobbs','ty','BIS',3.23)

    def tearDown(self):
        del self.student

    def test_object_created_all_attributes(self):
         assert self.student.last_name == 'hobbs'
         assert self.student.first_name == 'ty'
         assert self.student.major == 'BIS'
         assert self.student.gpa == 3.23

    def test_student_str(self):
        self.assertEqual(str(self.student),'Name: hobbs,ty Major: BIS GPA: 3.23')

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            student = s.Student('123', 'Daisy',"CIS")

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            student = s.Student('Smith', '123',"CIS")

    def test_object_not_created_error_major(self):
        with self.assertRaises(TypeError):
            student = s.Student('Smith', '123')

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            student = s.Student('Smith', 'Ty',"CIS","ABC")






