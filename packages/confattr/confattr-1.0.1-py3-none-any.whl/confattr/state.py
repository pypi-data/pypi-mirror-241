#!/usr/bin/env python3

#: This is set when instantiating a :class:`~confattr.configfile.ConfigFile` without passing :paramref:`~confattr.configfile.ConfigFile.config_instances`, i.e. one that should support all settings.
#: Trying to create a :class:`~confattr.config.Config` when this flag is set will raise a :class:`~confattr.config.TimingError`.
has_config_file_been_instantiated = False
