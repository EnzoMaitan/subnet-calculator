import IpCalculator as ic
import SubnetCalculator as sc
import sys

# TODO Filter user input
# '152.202.34.4'
# '255.255.254.0'

# '32.20.130.0'
# '255.255.128.0'
# 41

def perfom_calculations():
    try:
        host_ip = ic.IpCalculator(input("Enter the Host IP: "))
        #host_ip = ic.IpCalculator('32.20.130.0')

        host_ip_mask = ic.IpCalculator(input("Enter the Subnet Mask: "))
        #host_ip_mask = ic.IpCalculator('255.255.128.0')
        subnet_information = sc.SubnetCalculator(host_ip, host_ip_mask)
        print_results(host_ip, host_ip_mask, subnet_information)
    except:
        print("Invalid Value")

def print_results(host_ip, host_ip_mask, subnet_information):
    print(".________________________________________IP_INFORMATION_______________________________________")
    print("| Class : " + host_ip.ip_class[0])
    print("| Borrowed bits: " + str(subnet_information.borrowed_bits))
    print("| Available Subnets: " + str(subnet_information.available_subnets))
    print("| Subnet Index: " + str(subnet_information.subnet_index))
    print("| Host Bits: " + str(subnet_information.host_bits))
    print("| Available hosts: " + str(subnet_information.available_hosts))
    print("|_____________________________________________________________________________________________")
    print("| Given Host ip".ljust(20) + "| Decimal: " + host_ip.ipv4.ljust(16) + "| Binary: " + '.'.join(
        host_ip.ip_binary_octects_list))
    print("| Given Subnet Mask".ljust(20) + "| Decimal: " + host_ip_mask.ipv4.ljust(16) + "| Binary: " + '.'.join(
        host_ip_mask.ip_binary_octects_list))
    print("| DSM".ljust(20) + "| Decimal: " + str(host_ip.ip_class[2]).ljust(16) + "| Binary: " + '.'.join(
        subnet_information.format_binary_8bit(str((host_ip.ip_class[1])))))
    print("| Network ID".ljust(20) + "| Decimal: " + '.'.join(subnet_information.subnet_id_decimal).ljust(16) + "| Binary: " + '.'.join(
        subnet_information.format_binary_8bit(subnet_information.subnet_id)))
    print("| Broadcast  ip".ljust(20) + "| Decimal: " + '.'.join(subnet_information.broadcast_address_decimal).ljust(
        16) + "| Binary: " + '.'.join(subnet_information.format_binary_8bit(subnet_information.broadcast_address)))
    print("| First Host ip".ljust(20) + "| Decimal: " + '.'.join(subnet_information.first_host_decimal).ljust(16) + "| Binary: " + '.'.join(
        subnet_information.format_binary_8bit(str(subnet_information.first_host))))
    print("| Last Host  ip".ljust(20) + "| Decimal: " + '.'.join(subnet_information.last_host_decimal).ljust(16) + "| Binary: " + '.'.join(
        subnet_information.format_binary_8bit(str(subnet_information.last_host))))
    print("\n")
    #subnet_information.calculates_all_subnets()


while True:
    print("\nc: calculate a new subnet")
    print("q: exit program")
    user_choice = input().upper()
    if user_choice == 'C':
        perfom_calculations()
    elif user_choice == 'Q':
        sys.exit()
