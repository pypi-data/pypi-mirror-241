import datetime

class ILogger:
    LOG_FILE_ERROR = "logs/error.log"
    LOG_FILE_WARNING = "logs/warning.log"

    @staticmethod
    def log(message, level):
        if len(message) > 100:
            raise ValueError("Le message ne doit pas dépasser 100 caractères.")

        if level not in ['ERROR', 'WARNING']:
            raise ValueError("Niveau invalide. Les niveaux valides sont 'ERROR' ou 'WARNING'.")

        formatted_message = f"{level}: [{datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')}] {message}"

        log_file = ILogger.LOG_FILE_ERROR if level == 'ERROR' else ILogger.LOG_FILE_WARNING
        with open(log_file, 'a') as file:
            file.write(formatted_message + '\n')

    @staticmethod
    def get_logs(level):
        if level not in ['ERROR', 'WARNING']:
            raise ValueError("Niveau invalide. Les niveaux valides sont 'ERROR' ou 'WARNING'.")

        log_file = ILogger.LOG_FILE_ERROR if level == 'ERROR' else ILogger.LOG_FILE_WARNING
        with open(log_file, 'r') as file:
            logs = file.readlines()

        return logs
