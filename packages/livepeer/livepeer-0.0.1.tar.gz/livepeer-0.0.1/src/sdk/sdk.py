"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .access_control import AccessControl
from .asset import Asset
from .metrics import Metrics
from .multistream_target import MultistreamTarget
from .playback import Playback
from .sdkconfiguration import SDKConfiguration
from .session import Session
from .stream import Stream
from .task import Task
from .transcode import Transcode
from .webhook import Webhook
from sdk import utils
from sdk.models import components
from typing import Callable, Dict, Union

class SDK:
    r"""Livepeer API Reference: Welcome to the Livepeer API reference docs. Here you will find all the
    endpoints exposed on the standard Livepeer API, learn how to use them and
    what they return.
    """
    stream: Stream
    multistream_target: MultistreamTarget
    webhook: Webhook
    asset: Asset
    metrics: Metrics
    session: Session
    access_control: AccessControl
    task: Task
    transcode: Transcode
    playback: Playback

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 api_key: Union[str,Callable[[], str]],
                 server_idx: int = None,
                 server_url: str = None,
                 url_params: Dict[str, str] = None,
                 client: requests_http.Session = None,
                 retry_config: utils.RetryConfig = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param api_key: The api_key required for authentication
        :type api_key: Union[str,Callable[[], str]]
        :param server_idx: The index of the server to use for all operations
        :type server_idx: int
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: Dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session
        :param retry_config: The utils.RetryConfig to use globally
        :type retry_config: utils.RetryConfig
        """
        if client is None:
            client = requests_http.Session()
        
        security = components.Security(api_key = api_key)
        
        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        self.sdk_configuration = SDKConfiguration(client, security, server_url, server_idx, retry_config=retry_config)
       
        self._init_sdks()
    
    def _init_sdks(self):
        self.stream = Stream(self.sdk_configuration)
        self.multistream_target = MultistreamTarget(self.sdk_configuration)
        self.webhook = Webhook(self.sdk_configuration)
        self.asset = Asset(self.sdk_configuration)
        self.metrics = Metrics(self.sdk_configuration)
        self.session = Session(self.sdk_configuration)
        self.access_control = AccessControl(self.sdk_configuration)
        self.task = Task(self.sdk_configuration)
        self.transcode = Transcode(self.sdk_configuration)
        self.playback = Playback(self.sdk_configuration)
    