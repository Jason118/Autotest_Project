# -*- coding: utf-8 -*-
from selenium.common.exceptions import WebDriverException
from ConfigParser import NoSectionError, NoOptionError


class Error(Exception):
    """Base package Exception."""
    pass


class FileException(Error):
    """Base file exception.Thrown when a file is not available.

    For example:

        file not exists.
    """
    pass


class ConfigFileException(FileException):
    """Thrown when config file not exists."""
    pass


class ConfigError(Error):
    """Thrown when basic config error, such as no [path] section or no 'base' option."""
    pass


class DataFileNotAvailableException(FileException):
    """Thrown when data file not available."""
    pass


class SheetTypeError(Error):
    """Thrown when sheet type passed in not int or str."""
    pass


class SheetError(Error):
    """Thrown when specified sheet not exists."""
    pass


class DataError(Error):
    """Thrown when something wrong with the data."""
    pass


class LogFileNotAvailableException(FileException):
    """Thrown when log file not available."""
    pass


class LogError(Error):
    """Thrown when something wrong when logging."""
    pass


class ReportFileNotAvailableException(FileException):
    """Thrown when report file not available."""
    pass


class ReportError(Error):
    """Thrown when something wrong when generate the report file."""
    pass


class DriverNotExistsException(WebDriverException):
    """Thrown when driver not exists."""
    pass


class UnSupportBrowserTypeException(WebDriverException):
    """Thrown when the browser type not support."""
    pass


class ParameterError(Error):
    """Thrown when pass wrong parameter to a method."""
    pass


class UploadFileError(Error):
    """Thrown when upload files not available."""
    pass


class UploadWindowNotOpenError(Error):
    """Thrown when upload window not open."""
    pass


class UploadWindowOpenError(Error):
    """Thrown when open upload window error."""
    pass


class UnSupportMethod(Error):
    """Thrown when http method not allowed."""
    pass


class UnSupportFileType(Error):
    """Thrown when test generator find an un support file type."""
    pass


class EncryptError(Error):
    """Thrown when Encrypt Error, such as sign without private key or encrypt without salt."""
    pass
