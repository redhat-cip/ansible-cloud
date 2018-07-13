# Ansible Cloud

The purpose of this project is to offer a variety of roles to accomplish action on Clouds, no matter who the cloud provider is.

Most often than not, we generally do the same actions on cloud platforms, no matter who the provider is. For example: upload an ssh key, boot a server, create security groups, ...

Ansible provides many provider-specific modules to accomplish those tasks. The idea here is to provide generic roles so one can write a playbook once and run it on every supported cloud providers.

## Matrix of roles per provider

|                                                                                       | [Vultr](https://www.vultr.com) | [Digital Ocean](https://www.digitalocean.com) | [OpenStack](https://www.openstack.org/) | [Amazon](https://aws.amazon.com) |
| ------------------------------------------------------------------------------------- | ------------------------------ | --------------------------------------------- | --------------------------------------- | -------------------------------- |
| [cloud-sshkey](https://github.com/redhat-cip/ansible-role-cloud-sshkey)               | OK                             | OK                                            | OK                                      | OK                               |
| [cloud-securitygroup](https://github.com/redhat-cip/ansible-role-cloud-securitygroup) | OK                             | -                                             | OK                                      | -                                |
| [cloud-firewallrule](https://github.com/redhat-cip/ansible-role-cloud-firewallrule)   | OK                             | -                                             | OK                                      | -                                |
| [cloud-server](https://github.com/redhat-cip/ansible-role-cloud-server)               | OK                             | -                                             | OK                                      | -                                |

## Pre-requisites per provider

### Amazon

Global variable: `ansible_cloud_provider: amazon`

**(Required)** Environment variables:

  * `AWS_ACCESS_KEY`
  * `AWS_SECRET_KEY`

If the cloud provider is Amazon, one needs to have the `boto` and `boto3` python modules installed on the controller.

### Digital Ocean

Global variable: `ansible_cloud_provider: digitalocean`

**(Required)** Environment variables:

  * `DO_API_KEY`

### OpenStack

Global variable: `ansible_cloud_provider: openstack`

**(Required)** Environment variables:

  * `OS_USERNAME`
  * `OS_PASSWORD`
  * `OS_AUTH_URL`
  * `OS_TENANT_NAME`

If the cloud provider is OpenStack, one needs to have the `openstacksdk` python module installed on the controller.


### Vultr

Global variable: `ansible_cloud_provider: vultr`

**(Required)** Environment variables:

  * `VULTR_API_KEY`

## License

Apache 2.0

## Authors Information

  - Ricardo Carrillo Cruz  <ricarril@redhat.com>
  - Yanis Guenane  <yguenane@redhat.com>
