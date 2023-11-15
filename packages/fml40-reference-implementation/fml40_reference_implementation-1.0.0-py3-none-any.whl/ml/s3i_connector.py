from ml import APP_LOGGER, CallbackManager
from s3i.identity_provider import IdentityProvider, TokenType
from s3i.directory import Directory
from s3i.repository import Repository
from s3i.broker import BrokerREST, BrokerAMQP
from s3i.config import Config
from s3i.event_system import EventManager, NamedEvent
from s3i.broker_message import GetValueReply, ServiceReply, SetValueReply, SubscribeCustomEventReply, \
    UnsubscribeCustomEventReply, GetValueRequest, \
    ServiceRequest, SetValueRequest, Message
from s3i.exception import raise_error_from_s3ib_msg, S3IBMessageError, S3IDittoError, S3IIdentityProviderError, \
    S3IBrokerAMQPError
from ast import literal_eval
import json
import uuid
import asyncio
import copy
from ml.tools import map_type_to_json_schema, remove_namespace
from ml.ml40.features.functionalities.functionality import Functionality
from ml.ml40.features.functionalities.events.event import Event
from ml.ml40.features.properties.values.value import Value
import inspect


class S3IParameter(object):
    """
    Defines static parameters used for connecting with S3I

    :param idp_url: url of the S3I Identity Provider
    :param idp_realm: realm of the S3I Identity Provider
    :param dir_url: url of the S3I Directory
    :param broker_host: url of the S3I Broker
    :param broker_vhost: virtual host of the S3I Broker
    :param repo_url: url of the S3I Repository
    :param repo_wws_url: url of the web socket interface of the S3I Repository
    :param repo_sync_freq: synchronization frequency to the S3I Repository
    :param dir_sync_freq: synchronization frequency to the S3I Directory
    :param broker_msg_sending_frequency: message sending frequency
    :param connection_timeout: connection timeout
    :param reconnect_interval: reconnection time interval
    """
    DEFAULT_IDP_URL = "https://idp.s3i.vswf.dev/"
    DEFAULT_IDP_REALM = "KWH"
    DEFAULT_BROKER_HOST = "rabbitmq.s3i.vswf.dev"
    DEFAULT_BROKER_VHOST = "s3i"
    DEFAULT_REPO_WWS_URL = "wss://ditto.s3i.vswf.dev/ws/2"
    DEFAULT_REPO_URL = "https://ditto.s3i.vswf.dev/api/2/"
    DEFAULT_DIR_URL = "https://dir.s3i.vswf.dev/api/2/"
    DEFAULT_REPO_SNYC_FREQ = 1  # Hz
    DEFAULT_DIR_SYNC_FREQ = 0
    DEFAULT_BROKER_SENDING_FREQ = 50
    DEFAULT_CONNECTION_TIMEOUT = 3
    DEFAULT_RECONNECT_INTERVAL = 5

    def __init__(self,
                 idp_url=None,
                 idp_realm=None,
                 dir_url=None,
                 broker_host=None,
                 broker_vhost=None,
                 repo_url=None,
                 repo_wws_url=None,
                 repo_sync_freq=None,
                 dir_sync_freq=None,
                 broker_msg_sending_frequency=None,
                 connection_timeout=None,
                 reconnect_interval=None
                 ):
        self.__idp_url = idp_url
        self.__idp_realm = idp_realm
        self.__broker_host = broker_host
        self.__broker_vhost = broker_vhost
        self.__repo_url = repo_url
        self.__repo_wws_url = repo_wws_url
        self.__dir_url = dir_url
        self.__repo_sync_freq = repo_sync_freq
        self.__dir_sync_freq = dir_sync_freq
        self.__broker_msg_sending_frequency = broker_msg_sending_frequency
        self.__connection_timeout = connection_timeout
        self.__reconnect_interval = reconnect_interval

        if self.__idp_url is None:
            self.__idp_url = self.DEFAULT_IDP_URL

        if self.__idp_realm is None:
            self.__idp_realm = self.DEFAULT_IDP_REALM

        if self.__broker_host is None:
            self.__broker_host = self.DEFAULT_BROKER_HOST

        if self.__broker_vhost is None:
            self.__broker_vhost = self.DEFAULT_BROKER_VHOST

        if self.__repo_url is None:
            self.__repo_url = self.DEFAULT_REPO_URL

        if self.__repo_wws_url is None:
            self.__repo_wws_url = self.DEFAULT_REPO_WWS_URL

        if self.__dir_url is None:
            self.__dir_url = self.DEFAULT_DIR_URL

        if self.__repo_url is None:
            self.__repo_url = self.DEFAULT_REPO_URL

        if self.__repo_sync_freq is None:
            self.__repo_sync_freq = self.DEFAULT_REPO_SNYC_FREQ

        if self.__dir_sync_freq is None:
            self.__dir_sync_freq = self.DEFAULT_DIR_SYNC_FREQ

        if self.__broker_msg_sending_frequency is None:
            self.__broker_msg_sending_frequency = self.DEFAULT_BROKER_SENDING_FREQ

        if self.__connection_timeout is None:
            self.__connection_timeout = self.DEFAULT_CONNECTION_TIMEOUT

        if self.__reconnect_interval is None:
            self.__reconnect_interval = self.DEFAULT_RECONNECT_INTERVAL

    @property
    def idp_url(self):
        return self.__idp_url

    @idp_url.setter
    def idp_url(self, value):
        self.__idp_url = value

    @property
    def idp_realm(self):
        return self.__idp_realm

    @idp_realm.setter
    def idp_realm(self, value):
        self.__idp_realm = value

    @property
    def broker_host(self):
        return self.__broker_host

    @broker_host.setter
    def broker_host(self, value):
        self.__broker_host = value

    @property
    def broker_vhost(self):
        return self.__broker_vhost

    @broker_vhost.setter
    def broker_vhost(self, value):
        self.__broker_vhost = value

    @property
    def repo_url(self):
        return self.__repo_url

    @repo_url.setter
    def repo_url(self, value):
        self.__repo_url = value

    @property
    def repo_wws_url(self):
        return self.__repo_wws_url

    @repo_wws_url.setter
    def repo_wws_url(self, value):
        self.__repo_wws_url = value

    @property
    def dir_url(self):
        return self.__dir_url

    @dir_url.setter
    def dir_url(self, value):
        self.__dir_url = value

    @property
    def repo_sync_freq(self):
        return self.__repo_sync_freq

    @repo_sync_freq.setter
    def repo_sync_freq(self, value):
        self.__repo_sync_freq = value

    @property
    def dir_sync_freq(self):
        return self.__dir_sync_freq

    @dir_sync_freq.setter
    def dir_sync_freq(self, value):
        self.__dir_sync_freq = value

    @property
    def broker_msg_sending_frequency(self):
        return self.__broker_msg_sending_frequency

    @broker_msg_sending_frequency.setter
    def broker_msg_sending_frequency(self, value):
        self.__broker_msg_sending_frequency = value

    @property
    def connection_timeout(self):
        return self.__connection_timeout

    @connection_timeout.setter
    def connection_timeout(self, value):
        self.__connection_timeout = value

    @property
    def reconnect_interval(self):
        return self.__reconnect_interval

    @reconnect_interval.setter
    def reconnect_interval(self, value):
        self.__reconnect_interval = value


class S3IConnector:
    """
    Builds a connector to connect with S3I, consisting of the service of IdP, Dir, Repo, and Broker

    :param loop: asyncio event loop
    :type loop: asyncio.AbstractEventLoop
    :param dt_entry_ins: an instance of the ml.Entry class
    :type dt_entry_ins: ml.Entry
    :param oauth2_id: oauth2 identifier
    :type oauth2_id: string
    :param oauth2_secret: oauth2 secret
    :type oauth2_secret: string
    :param is_repository: Whether the DT has connection to the S3I Repository
    :type is_repository: bool
    :param is_broker: Whether the DT has connection to the S3I Broker
    :type is_broker: bool
    :param is_broker_rest: Whether the communication to broker is via REST
    :type is_broker_rest: bool
    :param listening_event_topics: event topics the DT listen to
    :type listening_event_topics: list
    :param s3i_parameter: Static connection parameters
    :type s3i_parameter: S3IParameter

    """
    _ON_IDP_START_OK = "_on_idp_start_ok"
    _ON_IDP_TOKEN_REFRESHED = "_on_idp_token_refreshed"
    _ON_DIRECTORY_START_OK = "_on_directory_start_ok"
    _ON_REPOSITORY_START_OK = "_on_repository_start_ok"
    _ON_BROKER_START_OK = "_on_broker_start_ok"
    _ON_EVENT_BROKER_START_OK = "_on_event_broker_start_ok"
    _ON_EVENT_SYSTEM_START_OK = "_on_event_system_start_ok"

    def __init__(self,
                 loop,
                 dt_entry_ins,
                 oauth2_id,
                 oauth2_secret,
                 is_repository=False,
                 is_broker=False,
                 is_broker_rest=False,
                 listening_event_topics=[],
                 s3i_parameter=S3IParameter()):
        self.__loop = loop
        self.__client_id = oauth2_id
        self.__client_secret = oauth2_secret
        self.__is_repository = is_repository
        self.__is_broker = is_broker
        self.__is_broker_rest = is_broker_rest
        self.__listening_event_topics = listening_event_topics
        self.__broker_message_endpoint = None
        self.__broker_event_endpoint = None
        self.__s3i_parameter = s3i_parameter
        self.broker_msg_list_to_be_sent = []
        self.broker_event_msg_list_to_be_sent = []
        self.broker_msg_list_received = []
        self.broker_event_msg_list_received = []
        self.__token = None
        self.__res_get_value = []
        self.__dt_entry_ins = dt_entry_ins
        self.__repo_json = {
            "thingId": "",
            "policyId": "",
            "attributes": {}
        }
        self.__dir_json = {
            "thingId": "",
            "policyId": "",
            "attributes": {
                "name": "",
                "dataModel": "fml40"
            }
        }
        self.__callback_manager = CallbackManager()
        self.__idp_loop_timer_handler = None
        self.__idp_loop_refresh_token_timer_handler = None
        self.__dir_loop_timer_handler = None
        self.__repo_loop_timer_handler = None
        self.__broker_loop_sending_msg_timer_handler = None
        self.__broker_loop_sending_event_msg_timer_handler = None

        self.__dir = None
        self.__repo = None
        self.__idp = None
        self.__config = None
        self.__broker = None
        self.__event_broker = None
        self.__event_manager = None

    @property
    def dt_entry_ins(self):
        return self.__dt_entry_ins

    @property
    def loop(self):
        """
        Returns the event loop

        :rtype: asyncio.AbstractEventLoop
        """
        return self.__loop

    @property
    def token(self):
        """
        Returns the current access token

        :rtype: string
        """
        return self.__token

    @property
    def repo_json(self):
        """
        Returns the current state of the DT (conform to the S3I Repository)

        :rtype: dict
        """
        return self.__repo_json

    @property
    def dir_json(self):
        """
        Returns the current information model of the DT (conform to the S3I Directory)

        :rtype: dict
        """
        return self.__dir_json

    @property
    def idp(self):
        """
        Returns an instance to connect with the S3I IdentityProvider

        :rtype: IdentityProvider
        """
        return self.__idp

    @property
    def dir(self):
        """
        Returns an instance to connect with the S3I Directory

        :rtype: Directory
        """
        return self.__dir

    @property
    def repo(self):
        """
        Returns an instance to connect with the S3I Repository

        :rtype: Repository
        """
        return self.__repo

    @property
    def broker(self):
        """
        Return an instance to connect with the S3I Broker regarding sending/receiving normal S3I-B messages

        :rtype: BrokerAMQP
        """
        return self.__broker

    @property
    def event_broker(self):
        """
        Returns an instance to connect with the S3I Broker regarding event exchange

        :rtype: BrokerAMQP
        """
        return self.__event_broker

    @property
    def config(self):
        """
        Returns an instance to connect with the S3I Config REST API

        :rtype: Config
        """
        return self.__config

    @property
    def event_manager(self):
        """
        Returns the event manager instance

        :rtype: EventManager
        """
        return self.__event_manager

    def connect(self):
        """
        Connects to the S3I and adds various callback functions which will be called if the IdP has been started
        """

        self.add_on_idp_start_ok_callback(self.__setup_config, False, False)
        self.add_on_idp_start_ok_callback(self.__setup_directory, False, False)
        self.add_on_idp_start_ok_callback(self.__setup_event_system, False, False)
        if self.__is_repository:
            self.add_on_idp_start_ok_callback(self.__setup_repository, False, False)
        if self.__is_broker:
            self.add_on_idp_start_ok_callback(self.__setup_broker, False, False)
        self.add_on_idp_token_refreshed_callback(self.__refresh_s3i_with_new_token, False, False)
        self.__setup_identity_provider()

    def __setup_identity_provider(self):
        """
        Connects to the S3I IdentityProvider and builds a IdP instance self.idp
        """
        self.__idp = IdentityProvider(
            grant_type="client_credentials",
            identity_provider_url=self.__s3i_parameter.idp_url,
            realm=self.__s3i_parameter.idp_realm,
            client_id=self.__client_id,
            client_secret=self.__client_secret
        )

        try:
            self.__token = self.__idp.get_token(TokenType.ACCESS_TOKEN)
            APP_LOGGER.info("[S3I][IdentityProvider]: Connection built")
        except S3IIdentityProviderError as err:
            APP_LOGGER.error(
                "[S3I][IdentityProvider]: {}, reconnect in {} seconds".format(err.error_msg,
                                                                              self.__s3i_parameter.reconnect_interval))
            if isinstance(self.__idp_loop_timer_handler, asyncio.TimerHandle):
                self.__idp_loop_timer_handler.cancel()
            self.__loop.call_later(self.__s3i_parameter.reconnect_interval, self.__setup_identity_provider)
        else:
            APP_LOGGER.info("[S3I][IdentityProvider]: Access Token granted")
            self.__idp_loop_timer_handler = self.__loop.call_later(self.__get_remaining_time_to_refresh(),
                                                                   self.__recursively_refresh_token)
            self.__callback_manager.process(self._ON_IDP_START_OK)

    def __recursively_refresh_token(self):
        """
        Recursively refreshes access token, if it expires.
        """
        APP_LOGGER.info("[S3I][IdentityProvider]: Get refreshed access token from Identity Provider")
        try:
            self.__idp._refresh_token(self.__idp.get_token(TokenType.REFRESH_TOKEN))
            if self.__idp._token_bundle["expires_in"] < 60:
                self.__idp._authenticate(scope="openid")

        except S3IIdentityProviderError as err:
            APP_LOGGER.error(
                "[S3I][IdentityProvider]: {}, reconnect in {} seconds".format(err.error_msg,
                                                                              self.__s3i_parameter.reconnect_interval))
            if isinstance(self.__idp_loop_refresh_token_timer_handler, asyncio.TimerHandle):
                self.__idp_loop_refresh_token_timer_handler.cancel()
            self.__loop.call_later(self.__s3i_parameter.reconnect_interval, self.__setup_identity_provider)
        else:
            self.__token = self.__idp._token_bundle["access_token"]
            self.__idp_loop_refresh_token_timer_handler = self.__loop.call_later(self.__get_remaining_time_to_refresh(),
                                                                                 self.__recursively_refresh_token)
            self.__callback_manager.process(self._ON_IDP_TOKEN_REFRESHED)

    def __get_remaining_time_to_refresh(self):
        """
        Calculates the remaining time until token expiration
        """
        remaining_time = self.__idp._time_until_token_valid()
        safety_margin = 5
        return remaining_time - safety_margin

    def __refresh_s3i_with_new_token(self):
        """
        Passes the new/refreshed token to every S3I Object
        """
        # refresh s3i object
        if isinstance(self.__dir, Directory):
            self.__dir.pass_refreshed_token(self.__token)
            APP_LOGGER.info("[S3I][Directory]: Token refreshed")

        if isinstance(self.__config, Config):
            self.__config.token = self.__token
            APP_LOGGER.info("[S3I][Config]: Token refreshed")

        if self.__is_repository:
            if isinstance(self.__repo, Repository):
                self.__repo.pass_refreshed_token(self.__token)
            APP_LOGGER.info("[S3I][Repository]: Token refreshed")

        if self.__is_broker:
            if isinstance(self.__broker, BrokerAMQP):
                self.__broker.reconnect_token_expired(self.__token)
            if isinstance(self.__event_broker, BrokerAMQP):
                self.__event_broker.reconnect_token_expired(self.__token)
            APP_LOGGER.info("[S3I][Broker]: Token refreshed")

    def __setup_directory(self):
        """
        Connects to the S3I Directory and builds a directory instance self.dir
        """
        self.__dir = Directory(
            s3i_dir_url=self.__s3i_parameter.dir_url,
            token=self.__token
        )
        res = self.__recursively_update_directory(frequency=self.__s3i_parameter.dir_sync_freq)
        if res:
            APP_LOGGER.info("[S3I][Directory]: Connection built")
            self.__callback_manager.process(self._ON_DIRECTORY_START_OK)

    def __setup_broker(self):
        """
        Connects to the S3I Broker via a broker instance self.broker to send/receive normal S3I-B messages
        """
        # TODO Bug: if endpoint is not given, the broker does not throw a error
        # TODO Bug: by network disconnect the connection to broker keeps still connected
        # TODO allow having more channels + consumers
        # TODO send via BrokerREST()
        if self.__is_broker_rest:
            self.__broker = BrokerREST(token=self.__token)
            APP_LOGGER.info("[S3I][Broker]: Connection built via REST")
        else:
            self.__broker_message_endpoint = self.find_msg_broker_endpoint(thing_id=self.__client_id)
            if self.__broker_message_endpoint is None:
                APP_LOGGER.error("[S3I][Broker]: "
                                 "Cannot find a corresponding broker endpoint, reconnect in {} seconds".format(
                    self.__s3i_parameter.reconnect_interval))
                self.__loop.call_later(self.__s3i_parameter.reconnect_interval, self.__setup_broker)
            else:
                self.__broker = BrokerAMQP(
                    token=self.__token,
                    endpoint=self.__broker_message_endpoint,
                    callback=self.on_broker_message_callback,
                    loop=self.__loop
                )
                self.__callback_manager.process(self._ON_BROKER_START_OK)

                try:
                    self.__broker.connect()
                    APP_LOGGER.info("[S3I][Broker]: Connection built via AMQP")
                except S3IBrokerAMQPError as e:
                    APP_LOGGER.error("[S3I][Broker]: Connection failed: {}, "
                                     "reconnect in {} seconds".format(e.error_msg,
                                                                      self.__s3i_parameter.reconnect_interval))
                    self.__loop.call_later(self.__s3i_parameter.reconnect_interval, self.__setup_broker)
                else:
                    self.__broker.add_on_channel_open_callback(
                        self.__recursively_send_broker_messages, True,
                        self.__s3i_parameter.broker_msg_sending_frequency
                    )
                    self.__broker.add_on_channel_open_callback(
                        self.__callback_manager.process,
                        True,
                        self._ON_BROKER_START_OK
                    )

    def __setup_event_broker(self):
        """
        Connects to the S3I Broker via a second broker instance which is specially used for the event exchange.
        """
        response = self.__config.create_broker_event_queue(thing_id=self.__client_id,
                                                           topic=self.__listening_event_topics)
        self.__broker_event_endpoint = response.json().get("queue_name")
        self.__event_broker = BrokerAMQP(
            token=self.__token,
            endpoint=self.__broker_event_endpoint,
            callback=self.on_broker_message_callback,
            loop=self.loop
        )

        try:
            self.__event_broker.connect()
            APP_LOGGER.info("[S3I][EventBroker]: Connection built via AMQP")
        except S3IBrokerAMQPError as e:
            APP_LOGGER.error("[S3I][EventBroker]: Connection failed: {}, "
                             "reconnect in {} seconds".format(e.error_msg,
                                                              self.__s3i_parameter.reconnect_interval))
            self.__loop.call_later(self.__s3i_parameter.reconnect_interval, self.__setup_event_broker)
        else:
            self.__event_broker.add_on_channel_open_callback(
                self.__recursively_send_broker_event_message,
                True,
                self.__s3i_parameter.broker_msg_sending_frequency
            )
            self.__event_broker.add_on_channel_open_callback(
                self.__callback_manager.process,
                True,
                self._ON_EVENT_BROKER_START_OK
            )
            self.__callback_manager.process(self._ON_EVENT_BROKER_START_OK)

    def __setup_repository(self):
        """
        Connects to the S3I Repository and build a Repository instance
        """
        self.__repo = Repository(
            s3i_repo_url=self.__s3i_parameter.repo_url,
            token=self.__token
        )
        res = self.__recursively_update_repository(frequency=self.__s3i_parameter.repo_sync_freq)
        if res:
            APP_LOGGER.info("[S3I][Repository]: Connection built")
            self.__callback_manager.process(self._ON_REPOSITORY_START_OK)

    def __setup_config(self):
        """
        Connects to the S3I Config REST API and build a Config instance
        """
        self.__config = Config(token=self.token)
        APP_LOGGER.info("[S3I][Config]: Connection built")

    def __setup_event_system(self):
        """
        Connects to the S3I Event System and build a event manager instance
        """
        APP_LOGGER.info("[S3I][EventSystem]: Setup event system")
        # TODO implement event system
        self.__event_manager = EventManager(
            json_entry=self.__dt_entry_ins.dt_json
        )
        named_events = self.dir_json["attributes"].get("events")
        if named_events is not None:
            for key in named_events.keys():
                APP_LOGGER.info("[S3I][EventSystem]: add named event {}".format(key))
                self.__event_manager.add_named_event(
                    "{}.{}".format(self.__client_id, key), named_events[key].get("schema")
                )
        self.__setup_event_broker()
        self.__event_broker.add_on_channel_open_callback(
            self.__callback_manager.process,
            True,
            self._ON_EVENT_SYSTEM_START_OK
        )

    def refresh_directory_entry(self, current_dir_json):
        """
        Refreshes the directory entry locally according to the current state of the imported Entry instance

        :returns: refreshed directory entry
        :rtype: dict

        """
        if self.dt_entry_ins.identifier is not None:
            current_dir_json["thingId"] = self.dt_entry_ins.identifier
            current_dir_json["policyId"] = self.dt_entry_ins.identifier
        if self.dt_entry_ins.name is not None:
            current_dir_json["attributes"]["name"] = self.dt_entry_ins.name
        current_dir_json["attributes"]["dataModel"] = "fml40"
        current_dir_json["attributes"]["thingStructure"] = {
            "class": "ml40::Thing",
            "links": []
        }
        for key in self.dt_entry_ins.roles.keys():
            role_entry = {
                "association": "roles",
                "target": self.dt_entry_ins.roles[key].to_json()
            }
            current_dir_json["attributes"]["thingStructure"]["links"].append(role_entry)
        services = []
        values = []
        events = {}
        for feature_str in self.dt_entry_ins.features.keys():
            # values and events may have same naming
            if isinstance(self.dt_entry_ins.features[feature_str], Value):
                value_target = {
                    "class": self.dt_entry_ins.features[feature_str].to_json()["class"],
                }
                values.append(value_target)

            # check Event first, since it is subclass of functionality
            if isinstance(self.dt_entry_ins.features[feature_str], Event):
                event_entry = {}
                topic = ""
                if self.dt_entry_ins.features[feature_str].topic is not None:
                    topic = self.dt_entry_ins.features[feature_str].topic
                else:
                    topic = remove_namespace(self.dt_entry_ins.features[feature_str].class_name)

                event_entry["description"] = self.dt_entry_ins.features[feature_str].description
                schema = {"properties": {}}
                member_list = [member for member in dir(self.dt_entry_ins.features[feature_str])
                               if "__" not in member
                               if not callable(getattr(self.dt_entry_ins.features[feature_str], member))
                               if member not in ["topic", "description", "_abc_impl", "class_name", "identifier",
                                                 "json_out", "name", "parent", "namespace", "subFeatures", "frequency"]]

                for member in member_list:
                    type_str = map_type_to_json_schema(type(getattr(self.dt_entry_ins.features[feature_str], member)))
                    schema["properties"][member] = {"type": type_str}
                event_entry["schema"] = schema
                events[topic] = event_entry

            # map functionalities and methods to services
            elif isinstance(self.dt_entry_ins.features[feature_str], Functionality):

                # get service endpoint (default s3ib endpoint)
                service_endpoint = ""
                for endpoint in current_dir_json["attributes"]["allEndpoints"]:
                    if ("s3ib://" in endpoint or "s3ibs://" in endpoint) and "event" not in endpoint:
                        service_endpoint = endpoint

                # get public methods of functionality instance and ignore standard util functions
                method_list = [method for method in dir(self.dt_entry_ins.features[feature_str])
                               if callable(getattr(self.dt_entry_ins.features[feature_str], method))
                               if "__" not in method and
                               "to_json" not in method and
                               "get_my_thing" not in method]

                for method in method_list:
                    service_entry = {"endpoints": [service_endpoint], "serviceType": feature_str + "/" + method}
                    method_signature = inspect.signature(getattr(self.dt_entry_ins.features[feature_str], method))
                    paramTypes = {}

                    for param in method_signature.parameters.keys():
                        param_type = method_signature.parameters[param].annotation
                        paramTypes[param] = map_type_to_json_schema(param_type)

                    return_type = method_signature.return_annotation
                    resultTypes = map_type_to_json_schema(return_type)

                    service_entry["parameterTypes"] = paramTypes
                    service_entry["resultTypes"] = resultTypes
                    services.append(service_entry)

        current_dir_json["attributes"]["thingStructure"]["services"] = services
        current_dir_json["attributes"]["thingStructure"]["values"] = values
        current_dir_json["attributes"]["thingStructure"]["events"] = events
        self.__dir_json = current_dir_json
        return current_dir_json

    @staticmethod
    def __refresh_sub_thing_dir_entry(entry):
        """
        Refreshes the entry of a subordinate things locally which is conform to the S3I Directory modeling

        :param entry:  instance for subordinate thing
        :type entry: ml.Entry
        :returns: directory entry of the subordinate thing
        :rtype: dict

        """
        json_out = {"class": "ml40::Thing", "links": []}
        if entry.identifier:
            json_out["identifier"] = entry.identifier
        for key in entry.roles.keys():
            role_entry = {"association": "roles", "target": entry.roles[key].to_json()}
            json_out["links"].append(role_entry)
        for key in entry.features.keys():
            feature_target = {
                "class": entry.features[key].to_json()["class"]
            }
            if entry.features[key].to_json().get("identifier") is not None:
                feature_target["identifier"] = entry.features[key].to_json()["identifier"]
            feature_entry = {"association": "features", "target": feature_target}
            json_out["links"].append(feature_entry)
        return json_out

    def __recursively_update_directory(self, frequency):
        """
        Recursively updates the directory entry to the S3I Directory
        """
        if frequency != 0:
            self.__dir_loop_timer_handler = self.__loop.call_later(1 / frequency,
                                                                   self.__recursively_update_directory,
                                                                   frequency
                                                                   )
        try:
            current_dir_json = self.__dir.queryThingIDBased(self.__client_id)
            self.refresh_directory_entry(current_dir_json)
            self.__dir.updateThingIDBased(thingID=self.__client_id, payload=self.__dir_json)

        except S3IDittoError as err:
            APP_LOGGER.error(
                "[S3I][Directory]: {} and reconnect in {} seconds".format(err.error_msg,
                                                                          self.__s3i_parameter.reconnect_interval))
            self.__dir_loop_timer_handler.cancel()
            self.__loop.call_later(self.__s3i_parameter.reconnect_interval, self.__setup_directory)
            return False

        else:
            return True

    def __recursively_update_repository(self, frequency):
        """
        Recursively updates the repository entry to the S3I Repository
        """
        if frequency:
            self.__repo_loop_timer_handler = self.__loop.call_later(1 / frequency,
                                                                    self.__recursively_update_repository,
                                                                    frequency
                                                                    )
        try:
            if self.__repo_json != self.__dt_entry_ins.dt_json:
                self.__repo.updateThingIDBased(thingID=self.__client_id, payload=self.__dt_entry_ins.dt_json)
        except S3IDittoError as err:
            APP_LOGGER.error(
                "[S3I][Repository]: {} and reconnect in {} seconds".format(err.error_msg,
                                                                           self.__s3i_parameter.reconnect_interval))
            self.__repo_loop_timer_handler.cancel()
            self.__loop.call_later(self.__s3i_parameter.reconnect_interval, self.__setup_repository)
            return False
        else:
            self.__repo_json = copy.deepcopy(self.__dt_entry_ins.dt_json)
            return True

    def __recursively_send_broker_messages(self, frequency):
        """
        Recursively checks the list self.broker_msg_list_to_be_sent and sends messages to the S3I Broker
        """
        if frequency:
            self.__broker_loop_sending_msg_timer_handler = self.__loop.call_later(
                1 / frequency,
                self.__recursively_send_broker_messages,
                frequency)
        try:
            if self.broker_msg_list_to_be_sent:
                res = self.__broker.send(
                    endpoints=self.broker_msg_list_to_be_sent[0].get("endpoints"),
                    msg=json.dumps(self.broker_msg_list_to_be_sent[0].get("message"))
                )
                self.broker_msg_list_to_be_sent.pop(0)
        except S3IBrokerAMQPError as e:
            APP_LOGGER.error("[S3I][Broker]: Sending message failed due to {}".format(e.error_msg))
            self.__broker_loop_sending_msg_timer_handler.cancel()
            self.__loop.call_later(self.__s3i_parameter.reconnect_interval, self.__setup_broker)

    def __recursively_send_broker_event_message(self, frequency):
        """
        Recursively checks the list self.broker_event_msg_list_to_be_sent and sends event messages to the S3I Broker

        """
        if frequency:
            self.__broker_loop_sending_event_msg_timer_handler = self.__loop.call_later(
                1 / frequency,
                self.__recursively_send_broker_event_message,
                frequency)
        try:
            if self.broker_event_msg_list_to_be_sent:
                self.__event_manager.emit_named_event(
                    publisher=self.__event_broker,
                    topic=self.broker_event_msg_list_to_be_sent[0].get("topic"),
                    content=self.broker_event_msg_list_to_be_sent[0].get("content")
                )
                self.broker_event_msg_list_to_be_sent.pop(0)
        except S3IBrokerAMQPError as e:
            self.__broker_loop_sending_event_msg_timer_handler.cancel()
            self.__loop.call_later(self.__s3i_parameter.reconnect_interval, self.__setup_broker)

    def __check_and_send_custom_event(self):
        for key in self.__event_manager.custom_event_dict.keys():
            if self.__event_manager.custom_event_dict[key].check_filter:
                self.__event_manager.emit_custom_event(publisher=self.__event_broker,
                                                       topic=self.__event_manager.custom_event_dict[key].topic)

    def add_on_idp_start_ok_callback(self, callback_func, one_shot, is_async, *args, **kwargs):
        """
        Adds callback functions which will be called if the connection to has been built

        :param callback_func: callback function
        :param one_shot: whether the callback function only be called once
        :type one_shot: bool
        :param is_async: whether the function is an async function
        :type is_async: bool
        """
        self.__callback_manager.add(
            self._ON_IDP_START_OK,
            callback_func,
            one_shot,
            is_async,
            *args,
            **kwargs
        )

    def add_on_idp_token_refreshed_callback(self, callback_func, one_shot, is_async, *args, **kwargs):
        """
        Adds callback functions which will be called if the access token has been refreshed

        :param callback_func: callback function
        :param one_shot: whether the callback function only be called once
        :type one_shot: bool
        :param is_async: whether the function is an async function
        :type is_async: bool
        """
        self.__callback_manager.add(
            self._ON_IDP_TOKEN_REFRESHED,
            callback_func,
            one_shot,
            is_async,
            *args,
            **kwargs
        )

    def add_on_directory_start_ok_callback(self, callback_func, one_shot, is_async, *args, **kwargs):
        """
        Adds callback functions which will be called if the connection to the S3I Directory has been built

        :param callback_func: callback function
        :param one_shot: whether the callback function only be called once
        :type one_shot: bool
        :param is_async: whether the function is an async function
        :type is_async: bool
        """
        self.__callback_manager.add(
            self._ON_DIRECTORY_START_OK,
            callback_func,
            one_shot,
            is_async,
            *args,
            **kwargs
        )

    def add_on_repository_start_ok_callback(self, callback_func, one_shot, is_async, *args, **kwargs):
        """
        Adds callback functions which will be called if the connection to the S3I Repository has been built

        :param callback_func: callback function
        :param one_shot: whether the callback function only be called once
        :type one_shot: bool
        :param is_async: whether the function is an async function
        :type is_async: bool
        """
        self.__callback_manager.add(
            self._ON_REPOSITORY_START_OK,
            callback_func,
            one_shot,
            is_async,
            *args,
            **kwargs
        )

    def add_on_broker_start_ok_callback(self, callback_func, one_shot, is_async, *args, **kwargs):
        """
        Adds callback functions which will be called if the connection to the S3I Broker has been built

        :param callback_func: callback function
        :param one_shot: whether the callback function only be called once
        :type one_shot: bool
        :param is_async: whether the function is an async function
        :type is_async: bool
        """
        self.__callback_manager.add(
            self._ON_BROKER_START_OK,
            callback_func,
            one_shot,
            is_async,
            *args,
            **kwargs
        )

    def add_on_event_system_start_ok_callback(self, callback_func, one_shot, is_async, *args, **kwargs):
        """
        Adds callback functions which will be called if the event system
        (i.e., the instance of event manager and the connection to event broker) has been built

        :param callback_func: callback function
        :param one_shot: whether the callback function only be called once
        :type one_shot: bool
        :param is_async: whether the function is an async function
        :type is_async: bool


        """
        self.__callback_manager.add(
            self._ON_EVENT_SYSTEM_START_OK,
            callback_func,
            one_shot,
            is_async,
            *args,
            **kwargs
        )

    def find_msg_broker_endpoint(self, thing_id):
        """
        Finds the S3I-B endpoint

        :param thing_id: identifier of the searched thing
        :rtype: string
        """
        thing_json = self.__dir.queryThingIDBased(thing_id)
        all_endpoints = thing_json["attributes"].get("allEndpoints", None)
        if all_endpoints:
            for ep in all_endpoints:
                if "s3ib" in ep and "event" not in ep:
                    return ep

    def find_event_broker_endpoint(self, thing_id):
        """
        Finds the S3I-B event endpoint

        :param thing_id: identifier of the searched thing
        :rtype: string
        """

        thing_json = self.__dir.queryThingIDBased(thing_id)
        all_endpoints = thing_json["attributes"].get("allEndpoints", None)
        if all_endpoints:
            for ep in all_endpoints:
                if "s3ib" in ep and "event" in ep:
                    return ep

    def add_broker_message_to_send(self, endpoints, message):
        """
        Adds to-be-sent S3I-B message to a list
        which will be sent if the broker connection is available

        :param endpoints: endpoints to which the message should be sent
        :type endpoints: list
        :param message: S3I-B message
        :type message: dict

        """
        if not isinstance(endpoints, list):
            APP_LOGGER.error("[S3I][Broker]: Endpoints should be typed as list")

        self.broker_msg_list_to_be_sent.append(
            {
                "endpoints": endpoints,
                "message": message
            }
        )

    def add_broker_event_message_to_send(self, topic, content):
        """
        Adds to-be-sent S3I-B event message to the a list
        which will be sent if the broker connection is available

        :param topic: topic to which the event should be sent
        :type topic: string
        :param content: The content the event should describe
        :type content: dict

        """
        if not isinstance(topic, str):
            APP_LOGGER.error("[S3I][EventBroker]: Topic should be typed as string")
        if not isinstance(content, dict):
            APP_LOGGER.error("[S3I][EventBroker]: content should be typed as dict")

        self.broker_event_msg_list_to_be_sent.append(
            {
                "topic": topic,
                "content": content
            }
        )

    def on_broker_message_callback(self, ch, method, properties, body):
        """
        Parses body (content of a S3I-B message) and delegates the
        processing of the message to a separate method. The method is
        selected according to the message's type.

        :param body: S3I-B message
        :type body: byte

        """
        try:
            decoded_body = body.decode('utf-8')
            body = literal_eval(decoded_body)
        except UnicodeDecodeError:
            # Its a GZIP-based Byte message
            body_obj = Message(gzip_msg=body)
            body_obj.decompress(body_obj.gzip_msg)
            body = body_obj.base_msg
        except ValueError:
            body = json.loads(body)
        except SyntaxError:
            APP_LOGGER.error("[S3I]: Invalid type of received message")
        # Add S3I-B Message validate
        finally:
            try:
                body = raise_error_from_s3ib_msg(body, S3IBMessageError)
            except S3IBMessageError as e:
                APP_LOGGER.error("[S3I]: Receiving a message, but {}".format(e))
            else:
                self.broker_msg_list_received.append(body)
                message_type = body.get("messageType")

                __log = "[S3I]: Received a S3I-B {}: {}".format(
                    message_type, json.dumps(body, indent=2)
                )
                APP_LOGGER.info(__log)

                if message_type == "userMessage":
                    self.on_user_message(body)
                elif message_type == "serviceRequest":
                    self.__loop.create_task(self.on_service_request(body))
                elif message_type == "getValueRequest":
                    self.on_get_value_request(body)
                elif message_type == "setValueRequest":
                    self.on_set_value_request(body)
                elif message_type == "subscribeCustomEventRequest":
                    self.on_subscribe_custom_event_request(body)
                elif message_type == "getValueReply":
                    self.on_get_value_reply(body)
                elif message_type == "serviceReply":
                    self.on_service_reply(body)
                elif message_type == "subscribeCustomEventReply":
                    self.on_subscribe_custom_event_reply(body)
                elif message_type == "eventMessage":
                    self.on_event_message(body)
                elif message_type == "unsubscribeCustomEventRequest":
                    self.on_unsubscribe_custom_event_request(body)
                elif message_type == "unsubscribeCustomEventReply":
                    self.on_unsubscribe_custom_event_reply(body)
                else:
                    pass

    def on_user_message(self, msg):
        """Handles incoming S³I-B UserMessages.

        :param msg: S³I-B UserMessages

        """
        pass

    def on_get_value_request(self, msg):
        """Handles incoming GetValueRequest message. Looks up the value specified in msg and
        sends a GetValueReply message back to the sender.

        :param msg: GetValueRequest
        :type msg: dict

        """
        req = GetValueRequest(base_msg=msg)
        request_sender = req.base_msg.get("sender")
        request_msg_id = req.base_msg.get("identifier")
        request_sender_endpoint = req.base_msg.get("replyToEndpoint")
        attribute_path = req.base_msg.get("attributePath")
        reply_msg_uuid = "s3i:" + str(uuid.uuid4())

        try:
            __log = "[S3I]: Search the given attribute path: {}".format(attribute_path)
            APP_LOGGER.info(__log)
            value = self._uriToData(attribute_path)
        except KeyError:
            value = "Invalid attribute path"
            __log = "[S3I]: " + value
            APP_LOGGER.critical(__log)

        get_value_reply = GetValueReply()
        get_value_reply.fillGetValueReply(
            sender=self.__client_id,
            receivers=[request_sender],
            message_id=reply_msg_uuid,
            replying_to_msg=request_msg_id,
            value=value
        )
        self.broker_msg_list_to_be_sent.append(
            {
                "endpoints": [request_sender_endpoint],
                "message": get_value_reply.base_msg
            }
        )

    def _uriToData(self, uri):
        """Returns a copy of the value found at uri.

        :param uri: Path to value
        :rtype: Feature

        """

        if uri == "":
            return self.__dt_entry_ins.dt_json
        else:
            uri_list = uri.split("/")
            if uri_list[0] == "features":
                try:
                    return self.__dt_entry_ins.dt_json[uri]
                except KeyError:
                    return "Invalid attribute path"

            try:
                self._getValue(self.__dt_entry_ins.dt_json, uri_list)
            except Exception:
                return "Invalid attribute path"
            if self.__res_get_value.__len__() == 0:
                return "Invalid attribute path"
            response = copy.deepcopy(self.__res_get_value)
            self.__res_get_value.clear()
            if response.__len__() == 1:
                return response[0]
            else:
                return response

    def _getValue(self, source, uri_list):
        """Searches for the value specified by uri_list in source and stores
        the result in __resGetValue.

        :param source: Object that is scanned
        :param uri_list: List containing path

        """

        # ??? What if the uri points to a Value object?
        # Shouldn't it be serialized?!
        value = source[uri_list[0]]
        if uri_list.__len__() == 1:
            # if is ditto-feature
            if isinstance(value, str):
                try:
                    stringValue_split = value.split(":")
                    if stringValue_split[0] == "ditto-feature":
                        value = self.__dt_entry_ins.dt_json["features"][stringValue_split[1]][
                            "properties"
                        ][uri_list[0]]
                except Exception:
                    pass
            self.__res_get_value.append(value)
            return
        if isinstance(value, dict):
            # ??? uri_list.pop(0) better?!
            del uri_list[0]
            self._getValue(value, uri_list)
        if isinstance(value, list):
            if isinstance(value[0], (str, int, float, bool, list)):
                return value
            if isinstance(value[0], dict):
                for item in value:
                    if item["class"] == "ml40::Thing":
                        for i in item["roles"]:
                            if self._findValue(i, uri_list[1]):
                                uri_list_1 = copy.deepcopy(uri_list)
                                del uri_list_1[:2]
                                self._getValue(item, uri_list_1)
                        _f = self._findValue({"identifier": item.get("identifier")}, uri_list[1]) or \
                             self._findValue({"name": item.get("name")}, uri_list[1])
                        if _f:
                            uri_list_1 = copy.deepcopy(uri_list)
                            del uri_list_1[:2]
                            self._getValue(item, uri_list_1)
                    else:
                        if self._findValue(item, uri_list[1]):
                            uri_list_1 = copy.deepcopy(uri_list)
                            del uri_list_1[:2]
                            if not uri_list_1:
                                self.__res_get_value.append(item)
                                return
                            else:
                                self._getValue(item, uri_list_1)
        if isinstance(value, (str, int, float, bool)):
            # if is ditto-feature
            if isinstance(value, str):
                try:
                    stringValue_split = value.split(":")
                    if stringValue_split[0] == "ditto-feature":
                        value = self.__dt_entry_ins.dt_json["features"][stringValue_split[1]][
                            "properties"
                        ][uri_list[0]]
                except Exception:
                    pass
            self.__res_get_value.append(value)

    def _findValue(self, dic, value):
        """Returns true if value has been found in json, otherwise returns false.

        :param dic: dictionary
        :param value:
        :returns:
        :rtype:

        """

        for val in dic.values():
            if val == value:
                return True
        return False

    async def on_service_request(self, msg):
        """Handles S³I-B ServiceRequests. Executes the method of the
        functionality specified in serviceType and send a ServiceReply
        back to the sender.

        :param msg: ServiceRequest
        :type msg: dict

        """
        req = ServiceRequest(base_msg=msg)
        service_type = req.base_msg.get("serviceType")
        parameters = req.base_msg.get("parameters")
        request_sender = req.base_msg.get("sender")
        request_id = req.base_msg.get("identifier")

        service_reply = ServiceReply()
        service_functionality = service_type.split('/')[0]
        service_functionality_obj = self.__dt_entry_ins.features.get(service_functionality)
        if service_functionality_obj is None:
            APP_LOGGER.error(
                "[S3I]: Undefined functionality '%s' as serviceType in %s!"
                % (service_functionality, self.__dt_entry_ins.name)
            )
            service_reply.fillServiceReply(
                sender=self.__client_id,
                receivers=[request_sender],
                service_type=service_type,
                results={"error": "undefined functionality as serviceType: {}".format(service_functionality)},
                replying_to_msg=request_id,
                message_id="s3i:{}".format(uuid.uuid4())
            )
        else:
            try:
                method = getattr(service_functionality_obj, service_type.split('/')[1])
            except AttributeError:
                APP_LOGGER.error(
                    "[S3I]: Undefined functionality method '%s' as serviceType in %s!" % (
                        service_type.split('/')[1], self.__dt_entry_ins.name)
                )
                service_reply.fillServiceReply(
                    sender=self.__client_id,
                    receivers=[request_sender],
                    service_type=service_type,
                    replying_to_msg=request_id,
                    message_id="s3i:{}".format(uuid.uuid4()),
                    results={"error": "undefined functionality method as serviceType{}".format(service_type)},
                )
            except IndexError:
                APP_LOGGER.error(
                    "[S3I]: ServiceType should contain functionality and method like <functionality>/method>"
                )
                service_reply.fillServiceReply(
                    sender=self.__client_id,
                    receivers=[request_sender],
                    service_type=service_type,
                    replying_to_msg=request_id,
                    results={
                        "error": "ServiceType should contain functionality and method like <functionality>/method>"},
                    message_id="s3i:{}".format(uuid.uuid4())
                )
            else:
                __log = "[S3I]: Execute the function {0} of the class {1}".format(service_type.split('/')[1],
                                                                                  service_type.split('/')[0])
                APP_LOGGER.info(__log)
                try:
                    result = await method(**parameters)
                except TypeError as e:
                    APP_LOGGER.error("[S3I]: {}".format(e))
                    service_reply.fillServiceReply(
                        sender=self.__client_id,
                        receivers=[request_sender],
                        service_type=service_type,
                        replying_to_msg=request_id,
                        results={"error": "%s" % (e)},
                        message_id="s3i:{}".format(uuid.uuid4())
                    )
                else:
                    if isinstance(result, bool):
                        result = {"ok": result}
                    elif result is None:
                        result = "None"
                    service_reply.fillServiceReply(
                        sender=self.__client_id,
                        receivers=[request_sender],
                        service_type=service_type,
                        replying_to_msg=request_id,
                        results=result,
                        message_id="s3i:{}".format(uuid.uuid4())
                    )
        """
        if sys.getsizeof(service_reply.base_msg["results"]) > self.__s3i_parameter.broker_msg_compress_threshold:
            service_reply.compress(msg_json=service_reply.base_msg, level=6)
            res = self.broker.send(
                endpoints=[body_json.get("replyToEndpoint", None)],
                msg=service_reply.gzip_msg
            )
        """
        self.broker_msg_list_to_be_sent.append(
            {
                "endpoints": [msg.get("replyToEndpoint", None)],
                "message": service_reply.base_msg
            }

        )

    def on_set_value_request(self, msg):
        """Handles incoming S³I-B SetValueRequest.

        :param msg: GetValueReply
        :type msg: dict

        """
        set_value_reply = SetValueReply()

        req = SetValueRequest(base_msg=msg)

        request_sender = req.base_msg.get("sender")
        request_msg_id = req.base_msg.get("identifier")
        request_sender_endpoint = req.base_msg.get("replyToEndpoint")
        attribute_path = req.base_msg.get("attributePath")
        new_value = req.base_msg.get("newValue")
        reply_msg_uuid = "s3i:" + str(uuid.uuid4())

        try:
            __log = "[S3I]: Search for the given attribute path: {}".format(attribute_path)
            APP_LOGGER.info(__log)
            old_value = self._uriToData(attribute_path)
            ins = self._uriToIns(attribute_path)
            APP_LOGGER.info("[S3I]: Change value from {} to {}".format(old_value, new_value))
            result = self._set_value_req(ins, new_value, attribute_path)

        except Exception:
            __log = "[S3I]: Invalid attribute path"
            APP_LOGGER.critical(__log)
            result = False

        set_value_reply.fillSetValueReply(
            sender=self.__client_id,
            receivers=[request_sender],
            ok=result,
            replying_to_msg=request_msg_id,
            message_id=reply_msg_uuid
        )
        self.broker_msg_list_to_be_sent.append(
            {
                "endpoints": [request_sender_endpoint],
                "msg": set_value_reply.base_msg
            }
        )

    def _set_value_req(self, ins, new_value, attribute_path):
        if not isinstance(new_value, dict):
            attr_list = attribute_path.split("/")
            if attr_list.__len__() <= 2:
                APP_LOGGER.info("Not allowed to set attribute {}".format(attribute_path))
                return False
            else:
                if hasattr(ins, attr_list[attr_list.__len__() - 1]):
                    setattr(ins, attr_list[attr_list.__len__() - 1], new_value)
                    return True
                APP_LOGGER.info("{} is not one of the attributes".format(attr_list[attr_list.__len__() - 1]))
                return False
        else:
            for key in new_value.keys():
                if hasattr(ins, key):
                    setattr(ins, key, new_value[key])
                else:
                    APP_LOGGER.info("{} is not one of the attributes".format(key))
                    return False
            return True

    def _uriToIns(self, uri):
        if not uri:
            return None
        uri_list = uri.split("/")
        uri_list.pop(0)  # delete first element "attributes"
        return self._getInstance(self, uri_list)

    def _getInstance(self, source_obj, uri_list):
        if uri_list.__len__() == 0 or uri_list.__len__() == 1:
            ### the original uri was "attributes/features"
            return source_obj

        if "ml40" in uri_list[0]:
            _uri = uri_list[0]
            uri_list.pop(0)
            return self._getInstance(source_obj.features[_uri], uri_list)

        elif uri_list[0] == "features":
            uri_list.pop(0)
            return self._getInstance(source_obj, uri_list)

        elif uri_list[0] == "targets":
            uri_list.pop(0)
            for key in source_obj.targets.keys():
                subthing_dict = source_obj.targets[key].to_subthing_json()
                if subthing_dict.get("name", "") == uri_list[0] or subthing_dict.get("identifier", "") == uri_list[0] \
                        or subthing_dict.get("class", "") == uri_list[0]:
                    uri_list.pop(0)
                    return self._getInstance(source_obj.targets[key], uri_list)

        elif uri_list[0] == "subFeatures":
            uri_list.pop(0)
            for key in source_obj.subFeatures.keys():
                subfeature_dict = source_obj.subFeatures[key].to_json()
                if subfeature_dict.get("name", "") == uri_list[0] or subfeature_dict.get("identifier", "") == uri_list[
                    0] \
                        or subfeature_dict.get("class", "") == uri_list[0]:
                    uri_list.pop(0)
                    return self._getInstance(source_obj.subFeatures[key], uri_list)

    def on_subscribe_custom_event_request(self, msg):
        """Handles incoming S³I-B SubscribeCustomEventRequest.

        :param msg: SubscribeCustomEventRequest
        :type msg: dict

        """
        subscription_status, topic = self.__event_manager.add_custom_event(
            rql_expression=msg.get("filter"),
            attribute_paths=msg.get("attributePaths")
        )
        __log = "[S3I][Broker]: Validation of RQL syntax: {}".format(subscription_status)
        APP_LOGGER.info(__log)
        event_sub_reply = SubscribeCustomEventReply()
        event_sub_reply.fillSubscribeCustomEventReply(
            sender=self.__client_id,
            receivers=[msg.get("sender")],
            topic=topic,
            replying_to_msg=msg.get("identifier"),
            message_id="s3i:" + str(uuid.uuid4()),
            status="ok" if subscription_status else "invalid request"
        )
        self.broker_msg_list_to_be_sent.append(
            {
                "endpoints": [msg.get("replyToEndpoint")],
                "message": event_sub_reply.base_msg
            }
        )

    def on_unsubscribe_custom_event_request(self, msg):
        """Handles incoming S³I-B UnsubscribeCustomEventRequest.

        :param msg: UnsubscribeCustomEventRequest
        :type msg: dict

        """
        unsubscribe_status = self.__event_manager.delete_custom_event(
            topic=msg.get("topic")
        )
        __log = "[S3I][Broker]: Status of unsubscribe: {}".format(unsubscribe_status)
        APP_LOGGER.info(__log)
        event_unsub_reply = UnsubscribeCustomEventReply()
        event_unsub_reply.fillUnsubscribeCustomEventReply(
            sender=self.__client_id,
            receivers=[msg.get("sender")],
            topic=msg.get("topic"),
            replying_to_msg=msg.get("identifier"),
            message_id="s3i:" + str(uuid.uuid4()),
            status="ok" if unsubscribe_status else "invalid request"
        )
        self.broker_msg_list_to_be_sent.append(
            {
                "endpoints": [msg.get("replyToEndpoint")],
                "message": event_unsub_reply.base_msg
            }
        )

    def on_get_value_reply(self, msg):
        """Handles incoming S³I-B GetValueReply.

        :param msg: GetValueReply
        :type msg: dict

        """
        pass

    def on_service_reply(self, msg):
        """Handles incoming S³I-B ServiceReply.

        :param msg: ServiceReply
        :type msg: dict

        """
        pass

    def on_subscribe_custom_event_reply(self, msg):
        """Handles incoming S³I-B SubscribeCustomEventReply.

        :param msg: SubscribeCustomEventReply
        :type msg: dict

        """
        pass

    def on_unsubscribe_custom_event_reply(self, msg):
        """Handles incoming S³I-B UnsubscribeCustomEventReply.

        :param msg: UnsubscribeCustomEventReply
        :type msg: dict

        """
        pass

    def on_set_value_reply(self, msg):
        """Handles incoming S³I-B SetValueReply.

        :param msg: SetValueReply
        :type msg: dict

        """
        pass

    def on_event_message(self, msg):
        """Handles incoming S³I-B EventMessage.

        :param msg: EventMessage
        :type msg: dict

        """
        pass
