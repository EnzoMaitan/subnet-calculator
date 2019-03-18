import SubnetCalculator as sc
import IpCalculator as ic


class SubnetListCalculator:
    subnet_calculator: sc

    def __init__(self, subnet_calculator):
        self.subnet_calculator = subnet_calculator

    def calculate_new_network_address(self, network):
        new_SID = ic.IpCalculator('.'.join(network))
        for index, a in reversed(list(enumerate(new_SID.ip_decimal_octects_list))):
            if 255 > a > 0:
                new_SID.ip_decimal_octects_list[index] += 1
                break
        new_SID.ipv4 = '.'.join(str(i) for i in new_SID.ip_decimal_octects_list)
        return new_SID.ipv4

    def calculate_all_subnets(self):
        print("Possible Networks / Showing 20")
        print("+-----------------+-----------------+-----------------+-------------------+")
        print("| Network Address | First Host IP   | Last Host Ip    | Broadcast Address |")
        print("+-----------------+-----------------+-----------------+-------------------+")

        network = self.subnet_calculator.subnet_id_decimal

        for x in range(0, 20):
            new = ic.IpCalculator(self.calculate_new_network_address(network))
            network = [str(i) for i in new.ip_decimal_octects_list]
            new_calculator = sc.SubnetCalculator(new, self.subnet_calculator.host_ip_mask)

            print("| " + '.'.join([str(i) for i in new.ip_decimal_octects_list]).ljust(15) + " | " + '.'.join(
                new_calculator.first_host_decimal).ljust(15) + " | " + '.'.join(new_calculator.last_host_decimal).ljust(
                15) + " | " + '.'.join(new_calculator.broadcast_address_decimal).ljust(18) + "|")
        print("+-----------------+-----------------+-----------------+-------------------+")


