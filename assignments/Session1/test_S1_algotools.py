import unittest
import S1_algotools

class TestAlgoTools(unittest.TestCase):
    
    #Tests Exercise 1
    def test_average_above_zero_non_zeros_values(self):
        result = S1_algotools.average_above_zero([1,2,3,-5])
        self.assertEqual(result,2.0)
        
    def test_average_above_zero_with_zeros_values(self):
        result = S1_algotools.average_above_zero([1,2,3,0,-7])
        self.assertEqual(result,2.0)

    def test_average_above_zero_with_negative_values(self):
        with self.assertRaises(ValueError):
            S1_algotools.average_above_zero([0,-7])  

    def test_average_above_zero_with_only_negative_values(self):
        with self.assertRaises(ValueError):
            S1_algotools.average_above_zero([-5,-60,-7]) 

    def test_average_above_zero_with_string_values(self):
        with self.assertRaises(TypeError):
            S1_algotools.average_above_zero(['ab','c'])

    def test_average_above_zero_with_empty_tab(self):
        with self.assertRaises(ValueError):
            S1_algotools.average_above_zero([]) 
            
    def test_average_above_zero_with_string_param(self):
        with self.assertRaises(ValueError):
            S1_algotools.average_above_zero("test string")
            
    def test_average_above_zero_with_integer_param(self):
        with self.assertRaises(ValueError):
            S1_algotools.average_above_zero(3)   
            
    #Tests Exercise 2
    def test_max_value_with_non_zeros_values(self):
        result = S1_algotools.max_value([1,2,3,-5])
        self.assertEqual(result,(3,2))
        
    def test_max_value_with_zeros_values(self):
        result = S1_algotools.max_value([1,2,3,0,-7])
        self.assertEqual(result,(3,2))

    def test_max_value_with_negative_values(self):
        result = S1_algotools.max_value([0,-7])
        self.assertEqual(result,(0,0))

    def test_max_value_with_only_negative_values(self):
        result = S1_algotools.max_value([-5,-60,-7])
        self.assertEqual(result,(-5,0))

    def test_max_value_with_string_values(self):
        with self.assertRaises(TypeError):
            S1_algotools.max_value(['ab','c'])  

    def test_max_value_with_empty_tab(self):
        with self.assertRaises(ValueError):
            S1_algotools.max_value([])  

    def test_max_value_with_string_param(self):
        with self.assertRaises(ValueError):
            S1_algotools.max_value("test string")
            
    def test_max_value_with_integer_param(self):
        with self.assertRaises(ValueError):
            S1_algotools.max_value(3)
            
   #Tests Exercise 3
    def test_reverseTable_with_non_zeros_values(self):
        result = S1_algotools.reverseTable([1,2,3,-5])
        self.assertEqual(result,[-5, 3, 2, 1])
        
    def test_reverseTable_with_zeros_values(self):
        result = S1_algotools.reverseTable([1,2,3,-5,0])
        self.assertEqual(result,[0,-5, 3, 2, 1])

    def test_reverseTable_with_negative_values(self):
        result = S1_algotools.reverseTable([0,-7])
        self.assertEqual(result,[-7,0])

    def test_reverseTable_with_only_negative_values(self):
        result = S1_algotools.reverseTable([-5,-60,-7])
        self.assertEqual(result,[-7, -60, -5])

    def test_reverseTable_with_string_values(self):
        result = S1_algotools.reverseTable(['a','dsfdfs','po',4])
        self.assertEqual(result,[4,'po', 'dsfdfs', 'a'])

    def test_reverseTable_with_only_string_values(self):
        result = S1_algotools.reverseTable(['a','dsfdfs','po'])
        self.assertEqual(result,['po', 'dsfdfs', 'a'])

    def test_reverseTable_with_empty_tab(self):
        result = S1_algotools.reverseTable([])
        self.assertEqual(result,[])

    def test_reverseTable_with_string_param(self):
        with self.assertRaises(ValueError):
            S1_algotools.reverseTable("test string")
            
    def test_reverseTable_with_integer_param(self):
        with self.assertRaises(ValueError):
            S1_algotools.reverseTable(3)   