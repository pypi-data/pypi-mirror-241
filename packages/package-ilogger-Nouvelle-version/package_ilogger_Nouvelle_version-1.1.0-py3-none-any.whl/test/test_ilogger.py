import unittest
from ilogger.ilogger import ILogger

class TestILogger(unittest.TestCase):

    def setUp(self):
        # Supprimer les fichiers de logs existants avant les tests
        ILogger.log("Test message d'erreur.", "ERROR")
        ILogger.log("Tester message d'avertissement.", "WARNING")

    def test_log_error(self):
        logs = ILogger.get_logs("ERROR")
        self.assertIn("Test error message.", logs[0])

    def test_log_warning(self):
        logs = ILogger.get_logs("WARNING")
        self.assertIn("Test warning message.", logs[0])

if __name__ == '__main__':
    unittest.main()
