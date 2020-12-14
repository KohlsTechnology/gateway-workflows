![alt text](logo.png "logo")

# BlueCat Cisco DNA IPAM Driver
The BlueCat Cisco DNA IPAM Driver consists of community BlueCat Gateway Workflow which integrates with Cisco DNA Center.
The BlueCat Integration provides the ability to see network IP address scopes and provision the scopes that the enterprise owns directly within the DNA Center or the BlueCat Address Manager interface.

Early Cisco DNA Centre releases provided a BlueCat integration capability using a fixed code path developed by Cisco directly. However, the current integration model is very tightly coupled with DNAC release cycle and Cisco have developed a newer standardised newer IPAM model which all this integration provides support for going forwards.

In SD-Access deployments, BlueCat DNA Center integration provides:

- Access to existing IP address scopes, referred to as IP address pools in Cisco DNA Center. In BlueCat Address Manager DNAC global-pools are represented as network blocks and sub-pools as Networks (subnets)

- When configuring new IP address pools in Cisco DNA Center, the pools populate to the BlueCat Address Manager, reducing manual IP address management tasks.

# System Requirements

- BlueCat Address Manager 9.0+
- BlueCat Gateway versions 19.5.1 or greater
- Cisco DNA Center

# Installation

#### Step 1. Installing the BlueCat DNA Center workflow into BlueCat Gateway™

#### Download the Cisco DNA workflow from BlueCat Labs:

https://github.com/bluecatlabs/gateway-workflows/tree/master/Community/CiscoDNA

Install the following python libary into your BlueCat Gateway install

    # sudo docker exec bluecat_gateway pip install netaddr --user 
    # sudo docker container restart bluecat_gateway

#### Tarball the DNA integration for import into your BlueCat Gateway using gzip

    # gzip CiscoDNA folder: tar -zcvf CiscoDNA.tar.gz CiscoDNA/

#### Importing the CiscoDNS workflow into BlueCat Gateway

Access the BlueCat Gateway interface using the URL address and login.
- Select Administration\Workflow Export\Import
- Click browse file and choose CiscoDNA.tar.gz created above
- Click Import button and then restart the bluecat_gateway container
- Re-login to Gateway and select Administration\Workflow Permissions
- Select ipam
- Select ipam_page
- Select all in the New Group Name field
- Click the ADD button.

#### Step 2. Enable the BlueCat IPAM integration within Cisco DNA Center™ 

The BlueCat Cisco DNA support can be either enabled when the Cisco DNA centre solution is first install OR enabled post installation via the DNA Centre System Settings

Note :- Earlier DNA centre releases will show BLUECAT as an IPAM provider, this newer intergration utilises the GENERIC Provider

- Access the Cisco DNA Center using your DNA credentials
- Go to System Settings
- Select the Settings tab and click IP Address Manager
- Select the GENERIC provider and click to View/Select
- Enter a name, for example BlueCat Gateway
- Enter the BlueCat Gateway url (either HTTP or HTTPs into the Server Url field
- Enter the Username to use with BlueCat Gateway into the Username field
- Enter the Password to use with BlueCat Gateway into the Password field
- Enterprise the BlueCat configuration name to use into the View Field

# Usage

#### Creating or Importing existing Global Pools
Import pools from BlueCat Address Manager into DNA
- Within DNA Center
- Go to Design\Network Settings\IP Address Pools tab
- Select Global from the Hierarchy
- Click Import to open the Import IP Pool dialog
- Enter the CIDR of the Network Block which already exists in BlueCat Address Manager 
- Click Retrieve to show the pools available in BlueCat Address Manager
- Select the Pools to import

Creating a new Pool from within DNA
- Within DNA Center
- Go to Design\Network Settings\IP Address Pools tab
- Select Global from the Hierarchy
- Select Add IP Pool
- Input IP Pool Name, IP Subnet, CIDR Prefix, Gateway IP Address.
- Select DHCP server, DNS server if any.
- Click Save button

The pool will be created in DNA center and added to the BlueCat Address Manager

#### Creating Sub-Pools
Preconditional requirement: the global pool has already been imported from BlueCat Address Manager or created in DNA Center.
- Within DNA Center
- Go to Design\Network Settings\IP Address Pools tab
- Select an existing location or Create a location under the Global location
- Select Reserve IP Pool
- Input IP Pool Name
- Select Type is Generic
- Select Global IP Pool
- Input IP Subnet, CIDR Prefix
- Input Gateway if any.
- Select DHCP server, DNS server if any.
- Click Reserve button.

#### IP Allocation and Deallocation 
As IP addresses are allocated or deallocated by DNA centre these are reflected dynamically within the BlueCat Address Manager


Copyright 2020 BlueCat Networks (USA) Inc. and its affiliates

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

By: Brian Shorland (bshorland@bluecatnetworks.com)
Date: 03-05-2019
Gateway Version: 18.10
Description: Gateway workflow to be IPAM interface to integrate with Cisco DNA Centre


