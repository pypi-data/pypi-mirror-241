import logging, sys, os

def _initialize_logger() -> None:
    """Initializes the theutil logger"""
    _LOGGER = logging.getLogger("theutil")
    _LOGGER.setLevel(logging.INFO)
    path = f'{os.getcwd()}/{(os.path.splitext(os.path.basename(sys.argv[0]))[0])}_script_logging.txt'
    
    if (os.path.exists(path)): os.remove(path)
    
    _file_handler = logging.FileHandler(path)
    _file_formatter = logging.Formatter(fmt="%(name)s :: %(levelname)s :: %(message)s")
    _file_handler.setFormatter(_file_formatter)
    
    _LOGGER.addHandler(_file_handler)
    _LOGGER.info("Logging initialized")
    
def get_theutil_logger(file: str) -> logging.Logger:
    """Gets the theutil logger for the given python file
    
    :param file: The __file__ variable for the python file
    
    Returns:
        A Logger instance using a name with format `theutil.file`
    """
    return logging.getLogger(f'theutil.{os.path.basename(os.path.splitext(file)[0])}')