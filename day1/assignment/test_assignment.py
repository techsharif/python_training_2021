import unittest
from functions import readAllData, computeAverageForClasses, misclassified

# file name
SHORT_FILE_NAME = 'short_data.txt'
COMPLETE_FILE_NAME = 'complete_data.txt'
COMPLETE_FINAL_FILE_NAME = 'complete_data_final.txt'


class TestAssignment01(unittest.TestCase):

    def test_read_all_data(self):
        data = readAllData(SHORT_FILE_NAME)
        result_data = [
            ('15.79311545', 'YES'), 
            ('10.95644178', 'YES'), 
            ('27.77413952', 'NO'), 
            ('18.41013616', 'NO'), 
            ('18.74485271', 'NO'), 
            ('22.44869209', 'NO'), 
            ('18.09242441', 'NO'), 
            ('15.24850737', 'NO'), 
            ('11.21480959', 'YES'), 
            ('13.195037', 'NO')
        ]
        self.assertEqual(data, result_data)

    def test_compute_average_for_classes(self):
        data = readAllData(SHORT_FILE_NAME)
        average = computeAverageForClasses(data)
        result_data = {'YES': 12.654788940000001, 'NO': 19.13054132285714}
        for key, value in result_data.items():
            average[key] = int(average[key] * 1000000)
            result_data[key] = int(result_data[key] * 1000000)

        self.assertEqual(average, result_data)

    def test_misclassified(self):
        data = readAllData(SHORT_FILE_NAME)
        average = computeAverageForClasses(data)
        misclasified = misclassified(data)
        result_data = [('15.24850737', 'NO'), ('13.195037', 'NO')]

        self.assertEqual(misclasified, result_data)

    def test_compute_average_for_classes_complete(self):
        data = readAllData(COMPLETE_FILE_NAME)
        average = computeAverageForClasses(data)
        result_data = {'YES': 11.016275211379998, 'NO': 19.25457457829}
        for key, value in result_data.items():
            average[key] = int(average[key] * 1000000)
            result_data[key] = int(result_data[key] * 1000000)
        self.assertEqual(average, result_data)

    def test_misclassified_complete(self):
        data = readAllData(COMPLETE_FILE_NAME)
        average = computeAverageForClasses(data)
        misclasified = misclassified(data)

        self.assertEqual(len(misclasified), 47)

    def test_compute_average_for_classes_complete_final(self):
        data = readAllData(COMPLETE_FINAL_FILE_NAME)
        average = computeAverageForClasses(data)
        result_data = {'YES': 10.287209574866667, 'NO': 20.240770106972597, 'OK': 97.84553928928842}
        for key, value in result_data.items():
            average[key] = int(average[key] * 1000000)
            result_data[key] = int(result_data[key] * 1000000)
        self.assertEqual(average, result_data)

    def test_misclassified_complete_final(self):
        data = readAllData(COMPLETE_FINAL_FILE_NAME)
        average = computeAverageForClasses(data)
        misclasified = misclassified(data)

        self.assertEqual(len(misclasified), 36)

if __name__ == '__main__':
    unittest.main()
