# generated from rosidl_generator_py/resource/_idl.py.em
# with input from simple_interfaces_pkg:msg/ComponentsStatus.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_ComponentsStatus(type):
    """Metaclass of message 'ComponentsStatus'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('simple_interfaces_pkg')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'simple_interfaces_pkg.msg.ComponentsStatus')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__components_status
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__components_status
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__components_status
            cls._TYPE_SUPPORT = module.type_support_msg__msg__components_status
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__components_status

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class ComponentsStatus(metaclass=Metaclass_ComponentsStatus):
    """Message class 'ComponentsStatus'."""

    __slots__ = [
        '_camera_is_ready',
        '_lidar_is_ready',
        '_motor_is_ready',
        '_debug_message',
    ]

    _fields_and_field_types = {
        'camera_is_ready': 'boolean',
        'lidar_is_ready': 'boolean',
        'motor_is_ready': 'boolean',
        'debug_message': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.camera_is_ready = kwargs.get('camera_is_ready', bool())
        self.lidar_is_ready = kwargs.get('lidar_is_ready', bool())
        self.motor_is_ready = kwargs.get('motor_is_ready', bool())
        self.debug_message = kwargs.get('debug_message', str())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.camera_is_ready != other.camera_is_ready:
            return False
        if self.lidar_is_ready != other.lidar_is_ready:
            return False
        if self.motor_is_ready != other.motor_is_ready:
            return False
        if self.debug_message != other.debug_message:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def camera_is_ready(self):
        """Message field 'camera_is_ready'."""
        return self._camera_is_ready

    @camera_is_ready.setter
    def camera_is_ready(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'camera_is_ready' field must be of type 'bool'"
        self._camera_is_ready = value

    @builtins.property
    def lidar_is_ready(self):
        """Message field 'lidar_is_ready'."""
        return self._lidar_is_ready

    @lidar_is_ready.setter
    def lidar_is_ready(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'lidar_is_ready' field must be of type 'bool'"
        self._lidar_is_ready = value

    @builtins.property
    def motor_is_ready(self):
        """Message field 'motor_is_ready'."""
        return self._motor_is_ready

    @motor_is_ready.setter
    def motor_is_ready(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'motor_is_ready' field must be of type 'bool'"
        self._motor_is_ready = value

    @builtins.property
    def debug_message(self):
        """Message field 'debug_message'."""
        return self._debug_message

    @debug_message.setter
    def debug_message(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'debug_message' field must be of type 'str'"
        self._debug_message = value
