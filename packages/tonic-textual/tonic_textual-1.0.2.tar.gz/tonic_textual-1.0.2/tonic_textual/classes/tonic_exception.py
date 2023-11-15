from requests.exceptions import HTTPError

class DatasetNameAlreadyExists(Exception):
    """
        Raised when there is an attempt to create a dataset with a name that already exists.
    """
    def __init__(self, errors):
        # Call the base class constructor with the parameters it needs
        super().__init__("The dataset name already exists. Dataset names must be unique. Choose a different name.")

        # Now for your custom code...
        self.errors = errors

class DatasetFileMatchesExistingFile(HTTPError):
    """
        Raised when the content in a file to upload matches the content in an existing file in the dataset.
    """
    def __init__(self, errors):
        super().__init__(errors.response.content or "The file content matches content in an existing dataset file. Choose a different file.")

        self.errors = errors
