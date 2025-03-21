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

from json           import loads
from logging.config import dictConfig

# https://pypi.org/project/keyring
from keyring.backend import KeyringBackend
# https://pypi.org/project/platformdirs
from platformdirs    import (user_config_path,
                             user_data_path,
                             user_log_path)
# https://pypi.org/project/rich
from rich.console    import Console
from rich.logging    import RichHandler
# https://pypi.org/project/PyYAML
from yaml            import safe_load

from .ConfFileModel import ConfFileModel

from json import JSONDecodeError

from pydantic import ValidationError
from yaml     import YAMLError


class InsecureKeyringBackend(KeyringBackend):
    """
    An insecure Keyring backend that stores secrets in plain text.
    """

    # backend priority; see base class
    #   https://github.com/jaraco/keyring/blob/main/keyring/backend.py#L74
    #
    # TODO: implementing this without typing issues
    # requires importing / using custom property class:
    #   from keyring.compat import properties
    #   @properties.classproperty
    #   def priority(self) -> float:
    #       return 30
    #
    # TODO: review supressed pyright issues
    priority = 30                      # pyright: ignore[reportAssignmentType]


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

        path_to_data_file = conf.path_to_data_file

        message = f'load data file\n  {path_to_data_file}'
        try:
            data_text = path_to_data_file.read_text()
        except OSError:
            raise

        try:
            data_dict = loads(data_text)
            self._logger.info(f'{message}: OK')
        except (JSONDecodeError, UnicodeDecodeError):
            raise

        self._data_dict = data_dict


    def delete_password(self, service: str, username: str) -> None:
        """
        Delete password for <service> and <username>.

        Args:
            service:  Name of service; currently ignored.
            username: Name of user; currently ignored.

        Returns:
            Does not return; always raises NotImplementedError.

        Raises:
            NotImplementedError.
        """

        raise NotImplementedError


    def get_password(self, service: str, username: str) -> str | None:
        """
        Get password for <service> and <username>.

        Args:
            service:  Name of service to get password for.
            username: Name of user; currently ignored.

        Returns:
            The password; None if no password was found.

        Raises:
            None.
        """

        message = ( 'get_password:\n'
                   f'  service:  {service}\n'
                   f'  username: {username} (ignored)')
        self._logger.info(message)

        try:
            password = self._data_dict[service]
            message = f"found password '{password}' for service '{service}'"
            self._logger.info(message)
        except KeyError:
            message = f"failed to find a password for service '{service}'"
            self._logger.warning(message)
            return None

        return password


    def set_password(self, service: str, username: str, password: str) -> None:
        """
        Set password for <service> and <username>.

        Args:
            service:  Name of service; currently ignored.
            username: Name of user; currently ignored.

        Returns:
            Does not return; always raises NotImplementedError.

        Raises:
            NotImplementedError.
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
        path_to_data_root = user_data_path(app_name)
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

        conf.path_to_data_file = path_to_data_root / conf.path_to_data_file

        console_confs = conf.logging.consoles
        if console_confs:
            for console_conf in console_confs.values():
                if console_conf.path_to_file:
                    console_conf.path_to_file \
                     = path_to_log_root / console_conf.path_to_file

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


        # python > logging > Configuring Logging:
        #   https://docs.python.org/3/howto/logging.html#configuring-logging
        #   https://docs.python.org/3/library/ ...
        #    ... logging.config.html#logging.config.dictConfig
        try:
            # NOTE: pass by_alias to use e.g. class, not class_:
            #   https://stackoverflow.com/a/70584815
            dictConfig(conf.logging.model_dump(by_alias = True))
        except (AttributeError, ImportError, TypeError, ValueError):
            raise

        logger_name = 'keyring.backends.InsecureKeyringBackend'
        self._logger = logging.getLogger(logger_name)

        return

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

        # NOTE: the usual way to set up logging using rich would be e.g.
        #   from logging import basicConfig
        #   # (more imports for rich Console, etc., see top of file)
        #   log_file = Path('/path/to/file.log')
        #   console  = Console(file = log_file)
        #   handlers = [RichHandler(console = console)]
        #   basicConfig(datefmt  = '[%Y%m%d-%H%M%S]',
        #               format   = '$message',
        #               handlers = handlers,
        #               level    = 'INFO',
        #               style    = '$')
        # this works only as long as there is only one single backend installed
        # for keyring that uses rich; if there are two or more, logging breaks:
        # if for example both backends use a log file as done above, log content
        # for the first backend is sent to the log file of the second backend;
        # cause: both use a logger called 'rich' by default
        # fix: _add_ a logger (and a handler) with a unique name
        #
        # python > display existing loggers:
        #   https://stackoverflow.com/a/60381742
        # import logging
        # loggers  = [logging.getLogger()]
        # loggers += [logging.getLogger(name)
        #               for name in logging.root.manager.loggerDict]
        # from pprint import pprint
        # print('loggers:')
        # pprint(loggers)
        # sample log output:
        # loggers:
        # [<RootLogger root (WARNING)>,
        # <Logger keyring.backend (WARNING)>,
        # <Logger keyring (WARNING)>,
        # <Logger keyring.core (WARNING)>,
        # <Logger keyring.backends.SecretService (WARNING)>,
        # <Logger keyring.backends (WARNING)>,
        # <Logger keyring.backends.Windows (WARNING)>,
        # <Logger keyring.backends.libsecret (WARNING)>]
        #
        # NOTE: it seems importing anything from rich
        # alone already creates a logger called 'rich':
        # from rich.pretty import pretty_repr
        # print(f'loggers:\n{pretty_repr(loggers)}')
        # for some reason, keyring calls this code twice at initialization;
        # the `import pretty_repr` seems to add the logger called rich:
        # sample log output:
        # loggers:
        # [
        #     <RootLogger root (WARNING)>,
        #     <Logger keyring.backend (WARNING)>,
        #     <Logger keyring (WARNING)>,
        #     <Logger keyring.core (WARNING)>,
        #     <Logger keyring.backends.SecretService (WARNING)>,
        #     <Logger keyring.backends (WARNING)>,
        #     <Logger keyring.backends.Windows (WARNING)>,
        #     <Logger keyring.backends.libsecret (WARNING)>
        # ]
        # loggers:
        # [
        #     <RootLogger root (WARNING)>,
        #     <Logger keyring.backend (WARNING)>,
        #     <Logger keyring (WARNING)>,
        #     <Logger keyring.core (WARNING)>,
        #     <Logger keyring.backends.SecretService (WARNING)>,
        #     <Logger keyring.backends (WARNING)>,
        #     <Logger keyring.backends.Windows (WARNING)>,
        #     <Logger keyring.backends.libsecret (WARNING)>,
        #     <Logger rich (WARNING)>
        # ]

        # NOTE: this requires importing entire package using `import logging`
        level   = getattr(logging, log_level.upper())
        # from rich.pretty import pretty_repr
        # log_conf = pretty_repr(conf.logging.model_dump(by_alias = True))
        # print(f'conf.logging:\n{log_conf}')
        # sample log output:
        # conf.logging:
        # {
        #     'version': 1,
        #     'formatters': {},
        #     'filters': {},
        #     'handlers': {
        #         'rich': {
        #             'class': 'rich.logging.RichHandler',
        #             'filters': None,
        #             'formatter': None,
        #             'level': 'INFO',
        #             'console': 'rich',
        #             'log_time_format': '[%Y%m%d-%H%M%S]'
        #         }
        #     },
        #     'loggers': {
        #         'keyring.backends.InsecureKeyringBackend': {
        #             'filters': None,
        #             'handlers': ['rich'],
        #             'level': 'INFO',
        #             'propagate': None
        #         }
        #     },
        #     'root': None,
        #     'incremental': None,
        #     'disable_existing_loggers': None,
        #     'consoles': {
        #         'rich': {
        #             'path_to_file': PosixPath('/Users/ssc/Library/Logs/InsecureKeyringBackend/keyring_insecure_backend.log')
        #         }
        #     }
        # }

        # TODO: really set log level in both handler and logger ?
        console = Console(file = log_file)
        handler = RichHandler(console         = console,
                              level           = level,
                              log_time_format = datefmt)

        # TODO: get this from conf
        logger_name = 'keyring.backends.InsecureKeyringBackend'
        logger = logging.getLogger(logger_name)
        logger.setLevel(level)

        # NOTE: keyring calls this code twice;
        # add a handler only if required: once
        if not logger.hasHandlers():
            logger.addHandler(handler)

        self._logger = logger
