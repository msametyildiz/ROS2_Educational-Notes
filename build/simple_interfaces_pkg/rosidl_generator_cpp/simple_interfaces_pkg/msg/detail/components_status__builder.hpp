// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from simple_interfaces_pkg:msg/ComponentsStatus.idl
// generated code does not contain a copyright notice

#ifndef SIMPLE_INTERFACES_PKG__MSG__DETAIL__COMPONENTS_STATUS__BUILDER_HPP_
#define SIMPLE_INTERFACES_PKG__MSG__DETAIL__COMPONENTS_STATUS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "simple_interfaces_pkg/msg/detail/components_status__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace simple_interfaces_pkg
{

namespace msg
{

namespace builder
{

class Init_ComponentsStatus_debug_message
{
public:
  explicit Init_ComponentsStatus_debug_message(::simple_interfaces_pkg::msg::ComponentsStatus & msg)
  : msg_(msg)
  {}
  ::simple_interfaces_pkg::msg::ComponentsStatus debug_message(::simple_interfaces_pkg::msg::ComponentsStatus::_debug_message_type arg)
  {
    msg_.debug_message = std::move(arg);
    return std::move(msg_);
  }

private:
  ::simple_interfaces_pkg::msg::ComponentsStatus msg_;
};

class Init_ComponentsStatus_motor_is_ready
{
public:
  explicit Init_ComponentsStatus_motor_is_ready(::simple_interfaces_pkg::msg::ComponentsStatus & msg)
  : msg_(msg)
  {}
  Init_ComponentsStatus_debug_message motor_is_ready(::simple_interfaces_pkg::msg::ComponentsStatus::_motor_is_ready_type arg)
  {
    msg_.motor_is_ready = std::move(arg);
    return Init_ComponentsStatus_debug_message(msg_);
  }

private:
  ::simple_interfaces_pkg::msg::ComponentsStatus msg_;
};

class Init_ComponentsStatus_lidar_is_ready
{
public:
  explicit Init_ComponentsStatus_lidar_is_ready(::simple_interfaces_pkg::msg::ComponentsStatus & msg)
  : msg_(msg)
  {}
  Init_ComponentsStatus_motor_is_ready lidar_is_ready(::simple_interfaces_pkg::msg::ComponentsStatus::_lidar_is_ready_type arg)
  {
    msg_.lidar_is_ready = std::move(arg);
    return Init_ComponentsStatus_motor_is_ready(msg_);
  }

private:
  ::simple_interfaces_pkg::msg::ComponentsStatus msg_;
};

class Init_ComponentsStatus_camera_is_ready
{
public:
  Init_ComponentsStatus_camera_is_ready()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ComponentsStatus_lidar_is_ready camera_is_ready(::simple_interfaces_pkg::msg::ComponentsStatus::_camera_is_ready_type arg)
  {
    msg_.camera_is_ready = std::move(arg);
    return Init_ComponentsStatus_lidar_is_ready(msg_);
  }

private:
  ::simple_interfaces_pkg::msg::ComponentsStatus msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::simple_interfaces_pkg::msg::ComponentsStatus>()
{
  return simple_interfaces_pkg::msg::builder::Init_ComponentsStatus_camera_is_ready();
}

}  // namespace simple_interfaces_pkg

#endif  // SIMPLE_INTERFACES_PKG__MSG__DETAIL__COMPONENTS_STATUS__BUILDER_HPP_
