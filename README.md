# Ansible Cloud

The purpose of this project is to offer a variety of modules to accomplish action on Clouds, no matter who the cloud provider is.

Most often than not, we generally do the same actions on cloud platforms, no matter who the provider is. For example: upload an ssh key, boot a server, create security groups, ...

Ansible provides many provider-specific modules to accomplish those tasks. The idea here is to provide generic module so one can write a playbook once and run it on every supported cloud providers.


## Supported Cloud Providers

  * Amazon
  * Digital Ocean
  * OpenStack
  * Vultr

## License

Apache 2.0

## Authors Information

  - Ricardo Carrillo Cruz  <ricarril@redhat.com>
  - Yanis Guenane  <yguenane@redhat.com>
