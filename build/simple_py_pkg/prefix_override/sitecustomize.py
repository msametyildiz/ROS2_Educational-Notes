import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/muhammed-samet-yildiz/ros2_ws/install/simple_py_pkg'
