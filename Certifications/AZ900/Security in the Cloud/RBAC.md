## Overview:
	- An authorization system built on ARM to provide granular access to Azure resources
	- RBAC helps manage WHO has access to Azure resources, WHAT they can do with the resources and WHAT areas they have access to
	- Best Practice - rule of least privilege  (minimum permissions)

## Common Use Cases:
	- Allow a user to manage resources in a subscription
	- Allow applications access to resources in an RG
	- Allow a user to manage all resources in an RG
	- Allow the DBs team to manage the SQL DBs in a subscription

## How it Works:
	- Can control access to resources using role assignments
	- A role assignment consists of 3 elements:
		○ Security principle
		○ Role definition
		○ Scope
	- We need to define each of the components, and then we can decide role assignments

## Security Principle:
	- An object that is requesting access to a resource (User, group, service principle or managed identity)
		○ User - individuals profile
		○ Group - a set of users
		○ Security Principle - security identity of an app or service
		○ Managed Identity - identity in Azure AD

## Role Definition:
	- A collection of permissions
	- Custom/built-in roles:
		○ Owner - Full admin
		○ Contributor - create / manage resources but can't assign access
		○ Reader - can view existing resources
	- Other roles available, targeting specific resources

## Scope:
	- Scope is a set of resources that access applies to
	- Can further limit actions of a role through defining a scope
	- Can specify at multiple levels (parent-child relationship)
	- Any access granted to the parent scope, the child scope inherits
	

