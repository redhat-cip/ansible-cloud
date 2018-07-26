# Ansible Cloud

The purpose of this project is to offer a variety of roles to accomplish action on Clouds, no matter who the cloud provider is.

Most often than not, we generally do the same actions on cloud platforms, no matter who the provider is. For example: upload an ssh key, boot a server, create security groups, ...

Ansible provides many provider-specific modules to accomplish those tasks. The idea here is to provide generic roles so one can write a playbook once and run it on every supported cloud providers.

- [The idea behind ansible-cloud](#the-idea-behind-ansible-cloud)
- [How does it work](#how-does-it-work)
- [Matrix of provider supported resources](#matrix-of-provider-supported-resources)
- [Provider specific requirements](#provider-specific-requirements)
  * [Amazon](#amazon)
  * [Digial Ocean](#digital-ocean)
  * [OpenStack](#openstack)
  * [Vultr](#vultr)
- [License](#license)
- [Authors](#authors-information)

## The idea behind ansible-cloud

Most people use Ansible to configure their applications stacks. They usually do that on pre-spawned infrastructure.
Ansible provide cloud-provider specific modules for one to manage its infrastructure the same way she manages her application stack.

ansible-cloud goes a step further, and offers generic roles rather than cloud-provider specific modules, for one to describe its infrastructure and spawn it in every ansible-cloud supported provider. Trying to get to the meta: write it once, run it everywhere - and making hybrid cloud a reality.

## How does it work?

ansible-cloud provides a generic `cloud.yml` playbook that should remain untouched. Everything is data-driven and should happen in a variable files, where one would describe its infrastructure. Cloud specific values like flavor, regions, ... are maintained by ansible-cloud for each cloud provider. One can find them in `inventory/host_vars/<provider>`.

This is a sample of a variable file:

```
ansible_host: localhost
ansible_connection: local

sshkeys:
  - { 'name': ansiblecloud-key, 'content': 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC+ZFQv3MyjtL1BMpSA0o0gIkzLVVCewtrqwrewqrewqrqNowQ7FSvVWUdAbTq00U7Xzak1ANIYLJyn+0r7olsdG4XEiUR0dqgC99kbT/QhY5mLe5lpl7JUjW9ctn00hNmt+TswpatCKWPNwdeAJT2ERynZaqPobENgvIq7jfOFWQIVew7qFeZygxsPVn36EUr2Cdq7Nb7U0XFXh3x1p0v0+MbL4tiJwPlMAGvFTKIMt+EaA+AsRIxiOo9CMk5ZuOl9pT8h5vNuEOcvS0qx4v44EAD2VOsCVCcrPNMcpuSzZP8dRTGU9wRREAWXngD0Zq9YJMH38VTxHiskoBw1NnPz me@home' }

securitygroups:
  - { 'name': ansiblecloud-web }


firewallrules:
  - { 'group_name': 'ansiblecloud-web', 'protocol': tcp, 'start_port': 22, 'end_port': 23, 'remote_cidr': '0.0.0.0/0' }
  - { 'group_name': 'ansiblecloud-web', 'protocol': tcp, 'start_port': 80, 'end_port': 81, 'remote_cidr': '0.0.0.0/0' }

servers:
  - { 'name': web,
      'image': '{{ server_image }}',
      'flavor': '{{ server_flavor }}',
      'region': '{{ server_region }}',
      'security_group': ansiblecloud-web,
      'sshkey': ansiblecloud-key
    }
```

The above file **describes** what my cloud infrastructure should look like.

To deploy that on "the cloud", one would run the following command:

```
#> ANSIBLE_CLOUD_PROVIDER=openstack ansible-playbook -i inventory/hosts cloud.yml
```

Here `openstack` has been specified, but one could replace it by `vultr`, `amazon` or any other supported cloud platform.
Each provider has a minimum set of requirements one can find in the [Provider specific requirements](#provider-specific-requirements) section.

Once the infrastructure is deployed, a user can rely on dynamic inventories to provision their application stack on the proper nodes.
In the above scenario a server called 'web' has been spawned, it seems fairly reasonable that the following play could apply:

```
- hosts: web
  roles:
    - httpd
```

This is how a user could deploy this play using dynamic inventories:

```
#> ansible-playbook -i inventory/openstack.py play.yml
```

### Summary

With the following two commands, a user should be able to deploy its infrastructure (including application stack) on any ansible-cloud supported cloud,
making hybrid cloud a reality.

```
## Deploying the infrastructure
#> ANSIBLE_CLOUD_PROVIDER=provider ansible-playbook -i inventory/hosts cloud.yml

## Deploying the application stack
#> ansible-playbook -i inventory/provider.py application.yml
```

## Matrix of provider supported resources

|                                                                                       | [Vultr](https://www.vultr.com) | [Digital Ocean](https://www.digitalocean.com) | [OpenStack](https://www.openstack.org/) | [Amazon](https://aws.amazon.com) |
| ------------------------------------------------------------------------------------- | ------------------------------ | --------------------------------------------- | --------------------------------------- | -------------------------------- |
| [cloud-sshkey](https://github.com/redhat-cip/ansible-role-cloud-sshkey)               | OK                             | OK                                            | OK                                      | OK                               |
| [cloud-securitygroup](https://github.com/redhat-cip/ansible-role-cloud-securitygroup) | OK                             | -                                             | OK                                      | -                                |
| [cloud-firewallrule](https://github.com/redhat-cip/ansible-role-cloud-firewallrule)   | OK                             | -                                             | OK                                      | -                                |
| [cloud-server](https://github.com/redhat-cip/ansible-role-cloud-server)               | OK                             | -                                             | OK                                      | -                                |
| [cloud-volume](https://github.com/redhat-cip/ansible-role-cloud-volume)               | -                              | OK                                             | OK                                      | -                                |

## Provider specific requirements

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
