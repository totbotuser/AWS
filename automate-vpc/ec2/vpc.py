from src.ec2.vpc import VPC
from src.client_locator import Ec2Client


def main():
    # Create a VPC
    ec2_client = Ec2Client().get_client()
    vpc = VPC(ec2_client)

    vpc_response = vpc.create_vpc()

    print('VPC Created' + str(vpc_response))

    # Add a name tag to VPC
    vpc_name = 'test-vpc-1'
    vpc_id = vpc_response['Vpc']['VpcId']
    vpc.add_name_tag(vpc_id, vpc_name)

    print('Added ' + vpc_name + ' to ' + vpc_id)

    # Create an IGW
    igw_response = vpc.create_internet_gateway()
    igw_id = igw_response['InternetGateway']['InternetGatewayId']
    vpc.attach_igw_to_vpc(vpc_id, igw_id)
    print('Attached Internet gateway' + igw_id + ' to vpc :' + vpc_id)

    # Create a public subnets
    public_subnet_response = vpc.create_Subnet(vpc_id, '10.0.1.0/24', 'us-east-1a')
    public_subnet_id1 = public_subnet_response['Subnet']['SubnetId']
    print('Public Subnet created for vpc ' + vpc_id + ' : subnet id ' + public_subnet_id1)

    # Add a name tag to public subnet
    public_subnet_name1 = 'PublicSubnet1'
    vpc.add_name_tag(public_subnet_id1, public_subnet_name1)

    public_subnet_response = vpc.create_Subnet(vpc_id, '10.0.3.0/24', 'us-east-1c')
    public_subnet_id2 = public_subnet_response['Subnet']['SubnetId']
    print('Public Subnet created for vpc ' + vpc_id + ' : subnet id ' + public_subnet_id2)

    # Add a name tag to public subnet
    public_subnet_name2 = 'PublicSubnet2'
    vpc.add_name_tag(public_subnet_id2, public_subnet_name2)

    public_subnet_response = vpc.create_Subnet(vpc_id, '10.0.5.0/24', 'us-east-1f')
    public_subnet_id3 = public_subnet_response['Subnet']['SubnetId']
    print('Public Subnet created for vpc ' + vpc_id + ' : subnet id ' + public_subnet_id3)

    # Add a name tag to public subnet
    public_subnet_name3 = 'PublicSubnet3'
    vpc.add_name_tag(public_subnet_id3, public_subnet_name3)

    # Create a route table
    public_route_table_response = vpc.create_public_route_table(vpc_id)
    print('Route table created for vpc ' + vpc_id)
    rtb_id = public_route_table_response['RouteTable']['RouteTableId']

    # Adding a public Route
    add_public_route_response = vpc.create_igw_route_to_public_route_table(rtb_id, igw_id)

    # Associating subnet with public route table
    associate_route_tab_response = vpc.associate_subnet_with_route_table(public_subnet_id1, rtb_id)
    associate_route_tab_response = vpc.associate_subnet_with_route_table(public_subnet_id2, rtb_id)
    associate_route_tab_response = vpc.associate_subnet_with_route_table(public_subnet_id3, rtb_id)

    # Allow auto-assign public ip in public subnet resources
    allow_auto_assign_ip_address_for_subnet_response = vpc.allow_auto_assign_ip_address_for_subnet(public_subnet_id1)
    allow_auto_assign_ip_address_for_subnet_response = vpc.allow_auto_assign_ip_address_for_subnet(public_subnet_id2)
    allow_auto_assign_ip_address_for_subnet_response = vpc.allow_auto_assign_ip_address_for_subnet(public_subnet_id3)

    # Create a private subnet
    private_subnet_response = vpc.create_Subnet(vpc_id, '10.0.2.0/24', 'us-east-1b')
    private_subnet_id = private_subnet_response['Subnet']['SubnetId']
    print('Private Subnet created for vpc ' + vpc_id + ' : subnet id ' + private_subnet_id)

    # Add a name tag to private subnet
    private_subnet_name = 'PrivateSubnet'
    vpc.add_name_tag(private_subnet_id, private_subnet_name)


if __name__ == '__main__':
    main()
