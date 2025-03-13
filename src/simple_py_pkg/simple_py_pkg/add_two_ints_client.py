#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
# kütüphaneleri ekledik 


def main(args = None):   
    rclpy.init(args=args)
    node = Node("add_two_ints_client") # düğüm oluşturduk

    client_ = node.create_client(AddTwoInts,"add_two_int") # düğüm içerisnde client oluşturduk . client adı servis adı ile aynı olmalı
    
    #bu servisin serverı beklemesi için bir blok yazıyoruz yoksa hata alınır 
    while not client_.wait_for_service(1.0):
        node.get_logger().warn("Waiting for Server - [Addd Two Ints]")
        #"[INFO]" "[WARNING]"


    # request edeceğim değerleri giriyoruz
    request = AddTwoInts.Request()
    request.a = 15
    request.b = 4

    # call_async ile servisimden request ediyoruz
    future = client_.call_async(request)
    # server'ım işlemi yapıp geri değer döndürene kadar benim node'um spin ediyor
    rclpy.spin_until_future_complete(node,future)

    # eğer bir şey döndüremez ise "Service call failed" ile uyarı mesajı veriyor
    try:
        response = future.result()
        node.get_logger().info("Result: "+str(response.sum))
    except Exception as e:
        node.get_logger().error("Service call failed %r" % (e,))


    rclpy.shutdown()


if __name__ == "__main__":
    main()

