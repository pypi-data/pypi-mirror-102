"""
Module for entities implemented using the
input_text platform (https://www.home-assistant.io/integrations/input_text/).
"""

import logging

from hahomematic.entity import Entity
from hahomematic.const import OPERATION_READ

LOG = logging.getLogger(__name__)

# pylint: disable=invalid-name
class input_text(Entity):
    """
    Implementation of a input_text.
    This is a default platform that gets automatically generated.
    """
    # pylint: disable=too-many-arguments
    def __init__(self, interface_id, unique_id, address, parameter, parameter_data):
        super().__init__(interface_id, "input_text.{}".format(unique_id),
                         address, parameter, parameter_data)

    @property
    def STATE(self):
        try:
            if self._state is None and self.operations & OPERATION_READ:
                self._state = self.proxy.getValue(self.address, self.parameter)
        # pylint: disable=broad-except
        except Exception as err:
            LOG.info("input_text: Failed to get state for %s, %s, %s: %s",
                     self.device_type, self.address, self.parameter, err)
            return None
        return self._state

    @STATE.setter
    def STATE(self, value):
        try:
            self.proxy.setValue(self.address, self.parameter, str(value))
        # pylint: disable=broad-except
        except Exception:
            LOG.exception("input_text: Failed to set state for: %s, %s, %s, %s",
                          self.device_type, self.address, self.parameter, value)
