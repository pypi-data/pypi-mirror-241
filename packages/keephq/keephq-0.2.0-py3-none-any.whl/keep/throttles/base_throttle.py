"""
Base class for all conditions.
"""
import abc
import logging

from keep.contextmanager.contextmanager import ContextManager


class BaseThrottle(metaclass=abc.ABCMeta):
    def __init__(
        self, context_manager: ContextManager, throttle_type, throttle_config, **kwargs
    ):
        """
        Initialize a provider.

        Args:
            **kwargs: Provider configuration loaded from the provider yaml file.
        """
        # Initalize logger for every provider
        self.logger = logging.getLogger(self.__class__.__name__)
        self.throttle_type = throttle_type
        self.throttle_config = throttle_config
        self.context_manager = context_manager

    @abc.abstractmethod
    def check_throttling(self, action_name, alert_id, **kwargs) -> bool:
        """
        Validate provider configuration.

        Args:
            action_name (str): The name of the action to check throttling for.
            alert_id (str): The id of the alert to check throttling for.
        """
        raise NotImplementedError("apply() method not implemented")
