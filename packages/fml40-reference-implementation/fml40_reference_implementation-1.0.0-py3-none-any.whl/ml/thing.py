from ml.app_logger import APP_LOGGER
from ml.callback import CallbackManager
import asyncio


class Thing:
    """
    Base class to implement a ForestML4.0 Digital Twin (DT) consisting of two major parts.
    Entry (instantiated using ml.Entry) stores all ForestML4.0-conform modeling information and data to DT.
    Connector (instantiated using ml.s3i_connector) is used to connect to the IoT Infrastructure S3I
    Technically, DT runs over an asyncio event loop, which means all developer-defined functions should be added
    to the DT using different callback functions.

    :param entry: ForestML4.0-conform entry object
    :type entry: ml.Entry
    :param connector: An object used to perform DT's interconnections, e.g., via S3I
    :type connector: ml.S3IConnector
    :param loop: asyncio event loop
    :type loop: asyncio.AbstractEventLoop
    """
    _ON_THING_START_OK = "_on_thing_start_ok"
    _ON_THING_DELETE_OK = "_on_thing_delete_ok"

    def __init__(
            self,
            entry,
            connector,
            loop
    ):
        self.__entry = entry
        self.__connector = connector
        self.__loop = loop
        self.callbacks = CallbackManager()

    def __del__(self):
        """
        Deconstruct the DT
        """
        self.close()

    @property
    def entry(self):
        """
        Returns the associated instance of ml.Entry
        """
        return self.__entry

    @property
    def connector(self):
        """
        Returns the associated instance of ml.S3IConnector used to execute DT's interconnections via S3I
        """
        return self.__connector

    @property
    def loop(self):
        """
        returns the associated asyncio event loop
        """
        return self.__loop

    def run_forever(self):
        """
        Launch the DT in a persistent manner
        """
        APP_LOGGER.info("Start the thing identified as {} and named as {}".format(
            self.__entry.identifier, self.__entry.name))
        self.__setup_thing_json_sync()
        self.connector.connect()
        self.loop.run_forever()

    def close(self):
        """
        Close the DT
        """
        APP_LOGGER.info("Close the thing")
        self.callbacks.process(prefix=self._ON_THING_DELETE_OK)
        self.__loop.close()

    def __setup_thing_json_sync(self):
        """
        Start the synchronization with the ForestML 4.0-conform data stored in the instance of ml.Entry.
        """
        self.__recursively_update_dt_json()
        self.callbacks.process(prefix=self._ON_THING_START_OK)

    def __recursively_update_dt_json(self):
        """
        The attribute dt_json in the class ml40.Entry is the serialized json data of the ForestML4.0 modeling
        This function recursively synchronizes dt_json with data stored in the ml40.Entry object
        """
        self.__entry.refresh_dt_json()
        self.loop.call_later(0.01, self.__recursively_update_dt_json)

    def add_on_thing_start_ok_callback(self, callback_func, one_shot, is_async, *args, **kwargs):
        """
        Add external user-defined functions to the callback manager.
        The added functions will be processed, when the DT is started but the connection to the IoT is not built.

        :param callback_func: callback function
        :param one_shot: whether the callback function only be called once
        :type one_shot: bool
        :param is_async: whether the function is an async function
        :type is_async: bool

        """
        self.callbacks.add(
            self._ON_THING_START_OK,
            callback_func,
            one_shot,
            is_async,
            *args,
            **kwargs
        )

    def add_on_thing_delete_ok_callback(self, callback_func, one_shot, is_async, *args, **kwargs):
        """
        Add external user-defined functions to the callback manager.
        The added functions will be processes when the method close() has been called.

        :param callback_func: callback function
        :param one_shot: whether the callback function only be called once
        :type one_shot: bool
        :param is_async: whether the function is an async function
        :type is_async: bool
        """
        self.callbacks.add(
            self._ON_THING_DELETE_OK,
            callback_func,
            one_shot,
            is_async,
            *args,
            **kwargs
        )

    def add_ml40_implementation(self, impl_class, functionality, *args, **kwargs):
        """
        Add a concrete implementation of ml40/fml40 functionality to the DT

        :param impl_class: concrete implementation of ml40/fml40 functionality
        :param functionality: name of the to-be-implemented ml40/fml40 functionality
        :type functionality: str
        """
        def _add_ml40_implementation(_thing, impl_class, _functionality, *_args, **_kwargs):
            feature = _thing.entry.features.get(_functionality, None)
            if feature is None:
                APP_LOGGER.critical(
                    "Functionality %s is not one of the build-in functionalities" % _functionality
                )
            else:
                APP_LOGGER.info("Implementation object is added into the functionality %s" % _functionality)
                impl_ins = impl_class(*_args, **_kwargs)
                impl_ins.class_name = _functionality
                _thing.entry.features[_functionality] = impl_ins

        self.add_on_thing_start_ok_callback(
            _add_ml40_implementation,
            True,
            False,
            self,
            impl_class,
            functionality,
            *args,
            **kwargs
        )
