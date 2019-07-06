import unittest
from filtrark.safe_eval import SafeEval


class TestSafeEval(unittest.TestCase):

    def setUp(self):
        self.safe_eval = SafeEval()

    def test_safe_eval_object_creation(self):
        self.assertTrue(isinstance(self.safe_eval, SafeEval))

    def test_safe_eval_doesnt_have_globals_or_locals_by_default(self):
        with self.assertRaises(TypeError) as e:
            self.safe_eval('>>> dir()')

    def test_safe_eval_doesnt_evaluate_unprefixed_strings(self):
        result = self.safe_eval('8 + 8')
        self.assertEqual(result, '8 + 8')

    def test_safe_eval_evaluate_simple_expression(self):
        result = self.safe_eval('>>> 2 + 2')
        self.assertEqual(result, 4)

    def test_safe_eval_forbidden_characters(self):
        forbidden_expressions = [
            '>>> __name__',
            '>>> 4 ** 4'
        ]

        for expression in forbidden_expressions:
            result = self.safe_eval(expression)
            self.assertEqual(result, expression)
