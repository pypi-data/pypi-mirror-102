#!/usr/bin/env python3

"""Module containing the entry point."""

# See config module for the actual CLI arguments

import logging
import os.path
import shutil
import signal
import sys
import warnings
from typing import Optional

from appdirs import AppDirs

from . import __min_python_version__
from .command import UrlwatchCommand
from .config import CommandConfig
from .main import Urlwatch
from .storage import CacheDirStorage, CacheRedisStorage, CacheSQLite3Storage, YamlConfigStorage, YamlJobsStorage

# Check if we are installed in the system already # Legacy for apt-get type of packaging
# (prefix, bindir) = os.path.split(os.path.dirname(os.path.abspath(sys.argv[0])))
# if bindir != 'bin':
#     sys.path.insert(1, os.path.dirname(os.path.abspath(sys.argv[0])))


project_name = __package__
prefix, bindir = os.path.split(os.path.dirname(os.path.abspath(sys.argv[0])))

# directory where the config, jobs and hooks files are located
if os.name != 'nt':
    # typically ~/.config/{project_name}
    config_dir = AppDirs(project_name).user_config_dir
else:
    config_dir = os.path.expanduser(os.path.join('~', 'Documents', project_name))

# directory where the database is located
# typically ~/.cache/{project_name} or %LOCALAPPDATA%\{project_name}\{project_name}\Cache
cache_dir = AppDirs(project_name).user_cache_dir

# Ignore SIGPIPE for stdout (see https://github.com/thp/urlwatch/issues/77)
try:
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
except AttributeError:
    # Windows does not have signal.SIGPIPE
    pass

logger = logging.getLogger(project_name)


def setup_logger_verbose() -> None:
    """Set up the loggers for verbosity."""
    root_logger = logging.getLogger('')
    console = logging.StreamHandler()
    console.setFormatter(logging.Formatter('%(asctime)s %(module)s %(levelname)s: %(message)s'))
    root_logger.addHandler(console)
    root_logger.setLevel(logging.DEBUG)
    root_logger.info('turning on verbose logging mode')


def locate_storage_file(filename: str, default_dir: str, ext: Optional[str] = None) -> str:
    """Searches for file as specified and in default directory; retry with 'ext' extension.

    :param filename: The filename
    :param default_dir: Default storage directory
    :param ext: The extension, e.g. '.yaml', to add for searching if first scan fails

    :returns: The filename, either original or with path where found
    """
    search_filenames = [filename]

    # if exp is given, iterate both on raw filename and the filename with ext if different
    if ext and os.path.splitext(filename)[1] != ext:
        search_filenames.append(filename + ext)

    for file in search_filenames:
        # return if found
        if os.path.isfile(file):
            return file

        # no directory specified: add default one
        if file == os.path.basename(file):
            new_file = os.path.join(default_dir, file)
            if os.path.isfile(new_file):
                return new_file

    return filename


def migrate_from_urlwatch(config_file: str, jobs_file: str, hooks_file: str, cache_file: str) -> None:
    """Check for existence of legacy (urlwatch 2.23) config, jobs and hooks files and migrate them (i.e. make a copy to
    new folder and or naming).  Original files are not deleted."""
    uw_urlwatch_dir = os.path.expanduser(os.path.join('~', '.' + 'urlwatch'))
    uw_config_file = os.path.join(uw_urlwatch_dir, 'urlwatch.yaml')
    uw_urls_file = os.path.join(uw_urlwatch_dir, 'urls.yaml')
    uw_hooks_file = os.path.join(uw_urlwatch_dir, 'hooks.py')
    uw_cache_dir = AppDirs('urlwatch').user_cache_dir
    uw_cache_file = os.path.join(uw_cache_dir, 'cache.db')
    for old_file, new_file in zip((uw_config_file, uw_urls_file, uw_hooks_file, uw_cache_file),
                                  (config_file, jobs_file, hooks_file, cache_file)):
        if os.path.isfile(old_file) and not os.path.isfile(new_file):
            os.makedirs(os.path.dirname(new_file), exist_ok=True)
            shutil.copyfile(old_file, new_file)
            logger.warning(f"Copied urlwatch '{old_file}' file to webchanges '{new_file}'")


def main() -> None:  # pragma: no cover
    """The entry point."""
    # make sure that PendingDeprecationWarning are displayed from all modules (otherwise only those in __main__ are)
    warnings.filterwarnings('default', category=PendingDeprecationWarning)

    # Issue deprecation warning if running on minimum version supported
    if sys.version_info[0:2] == __min_python_version__:
        current_minor_version = '.'.join(str(n) for n in sys.version_info[0:2])
        next_minor_version = f'{__min_python_version__[0]}.{__min_python_version__[1] + 1}'
        warning = (f'Support for Python {current_minor_version} will be ending three years from the date Python '
                   f'{next_minor_version} was released')
        print(f'WARNING: {warning}\n')
        PendingDeprecationWarning(warning)

    # The config, jobs, hooks and cache files
    config_file = os.path.join(config_dir, 'config.yaml')
    jobs_file = os.path.join(config_dir, 'jobs.yaml')
    hooks_file = os.path.join(config_dir, 'hooks.py')
    cache_file = os.path.join(cache_dir, 'cache.db')

    # migrate legacy urlwatch 2.23 files
    migrate_from_urlwatch(config_file, jobs_file, hooks_file, cache_file)

    # load config files
    command_config = CommandConfig(project_name, config_dir, bindir, prefix, config_file, jobs_file, hooks_file,
                                   cache_file, verbose=False)

    # set up the logger to verbose if needed
    if command_config.verbose:
        setup_logger_verbose()

    # check for location of config files entered in cli
    command_config.config = locate_storage_file(command_config.config, command_config.config_dir, '.yaml')
    command_config.jobs = locate_storage_file(command_config.jobs, command_config.config_dir, '.yaml')
    command_config.hooks = locate_storage_file(command_config.hooks, command_config.config_dir, '.py')

    # setup config file API
    config_storage = YamlConfigStorage(command_config.config)  # storage.py

    # setup database API
    if command_config.database_engine == 'sqlite3':
        cache_storage = CacheSQLite3Storage(command_config.cache, command_config.max_snapshots)  # storage.py
    elif any(command_config.cache.startswith(prefix) for prefix in ('redis://', 'rediss://')):
        cache_storage = CacheRedisStorage(command_config.cache)  # storage.py
    elif command_config.database_engine == 'redis':
        raise RuntimeError("A redis URI (starting with 'redis://' or 'rediss://' needs to be specified with --cache")
    elif command_config.database_engine == 'textfiles':
        cache_storage = CacheDirStorage(command_config.cache)  # storage.py
    elif command_config.database_engine == 'minidb':
        from .storage_minidb import CacheMiniDBStorage  # legacy code imported only if needed

        cache_storage = CacheMiniDBStorage(command_config.cache)  # storage.py
    else:
        raise NotImplementedError(f'Database engine {command_config.database_engine} not implemented')

    # setup jobs file API
    jobs_storage = YamlJobsStorage(command_config.jobs)  # storage.py

    # setup urlwatch
    urlwatcher = Urlwatch(command_config, config_storage, cache_storage, jobs_storage)  # main.py
    urlwatch_command = UrlwatchCommand(urlwatcher)  # command.py

    # run urlwatch
    urlwatch_command.run()


if __name__ == '__main__':

    main()
