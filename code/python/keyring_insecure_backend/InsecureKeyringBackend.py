# keyring.py
#
# Insecure Keyring Backend implementation.
#
# author  : stefan schablowski
# contact : stefan.schablowski@desmodyne.com
# created : 2025-03-11


# Keyring > Write your own keyring backend:
#   https://github.com/jaraco/keyring ...
#    ... ?tab=readme-ov-file#write-your-own-keyring-backend


# TODO: review exception handling, establish / align with conv


# NOTE: need to import entire package
import logging

from logging import basicConfig, info

# https://pypi.org/project/keyring
from keyring.backend import KeyringBackend
# https://pypi.org/project/platformdirs
from platformdirs    import user_config_path, user_log_path
# https://pypi.org/project/rich
from rich.console    import Console
from rich.logging    import RichHandler
# https://pypi.org/project/PyYAML
from yaml            import safe_load

from .ConfFileModel import ConfFileModel

from pydantic import ValidationError
from yaml     import YAMLError


class InsecureKeyringBackend(KeyringBackend):
    """
    An insecure Keyring backend that stores secrets in plain text.
    """

    # TODO: doc
    priority = 30


    # name of this application, used to determine local user folders:
    #   https://platformdirs.readthedocs.io/en/latest/api.html ...
    #    ... #platformdirs.api.PlatformDirsABC.appname
    _application_name: str = 'InsecureKeyringBackend'

    # name of configuration file
    _conf_file_name:   str = 'keyring_insecure_backend.yaml'


    def __init__(self) -> None:
        """
        Initialize class instance.

        Args:
            None.

        Returns:
            None.

        Raises:
            OSError, ValidationError, YAMLError.
        """

        # NOTE: keyring doesn't seem to do any proper exception handling:
        #   displays a message 'Error initializing plugin EntryPoint ... ',
        #   but then just spills any execeptions raised here with full stack
        # TODO: keyring apparently calls this code twice

        super().__init__()

        try:
            conf = self._proc_conf(self._application_name, self._conf_file_name)
            self._set_up_logging(conf)
        except (OSError, ValidationError, YAMLError):
            raise

        info('InsecureKeyringBackend started ✅')


    def delete_password(self, service: str, username: str) -> None:
        """
        TODO: doc
        """

        raise NotImplementedError


    def get_password(self, service: str, username: str) -> str:
        """
        TODO: doc
        """

        return 'some password'


    def set_password(self, service: str, username: str, password: str) -> None:
        """
        TODO: doc
        """

        raise NotImplementedError


    def _proc_conf(self, app_name: str, file_name: str) -> ConfFileModel:
        """
        Load configuration file and prepare configuration for use.

        Args:
            app_name:  Name of this application.
            file_name: Name of configuration file.

        Returns:
            A ConfFileModel configuration object.

        Raises:
            OSError, ValidationError, YAMLError.
        """

        path_to_conf_root = user_config_path(app_name)
        path_to_log_root  = user_log_path(app_name)

        path_to_conf_file = path_to_conf_root / file_name

        # NOTE: as opposed to e.g. json.loads(...),
        # pyyaml does not support loading from text
        # --> open file, load from file-like object
        try:
            with open(path_to_conf_file, 'r') as stream:
                try:
                    conf_dict = safe_load(stream)
                except YAMLError:
                    raise
        except OSError:
            raise

        try:
            conf = ConfFileModel(**conf_dict)
        except ValidationError:
            raise

        conf.path_to_log_file = path_to_log_root / conf.path_to_log_file

        return conf


    def _set_up_logging(self, conf: ConfFileModel) -> None:
        """
        Set up logging to file configured in configuration file.

        Args:
            conf: A ConfFileModel configuration object.

        Returns:
            None.

        Raises:
            OSError.
        """

        # rich > log to file:
        #   https://rich.readthedocs.io/en/stable/console.html#file-output
        #
        # NOTE: truncate log file during development:
        #   https://stackoverflow.com/a/13576390
        # $ > ~/Library/Logs/InsecureKeyringBackend/keyring_insecure_backend.log

        path_to_log_file = conf.path_to_log_file

        if not path_to_log_file.parent.exists():
            try:
                path_to_log_file.parent.mkdir(parents=True)
            except OSError:
                raise

        # TODO: get these from conf
        datefmt   = '[%Y%m%d-%H%M%S]'
        log_level = 'info'

        format    = '$message'
        style     = '$'

        # NOTE: log file would usually be opened in a context, e.g.
        #   with open(path_to_log_file, 'a') as log_file:
        # and code up to the basicConfig(...) call would indented;
        # however, this fails upon the first info(...) call with
        #   ValueError: I/O operation on closed file.
        # TODO: close file upon exit

        try:
            log_file = open(path_to_log_file, 'a')
        except OSError:
            raise

        console  = Console(file = log_file)
        handlers = [RichHandler(console = console)]
        # NOTE: this requires importing entire package using `import logging`
        level    = getattr(logging, log_level.upper())
        basicConfig(datefmt  = datefmt,
                    format   = format,
                    handlers = handlers,
                    level    = level,
                    style    = style)
