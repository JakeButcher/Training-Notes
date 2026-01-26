## Overview:
	- Deployment and management service, enables to create, update and delete resources

## Key Terminology:
	- Resource - service in Azure (e.g. VMs, DBs, Storage accounts, etc.)
	- Resource Groups - container for resources
	- Resource Provider - Family of related Azure resources
	- Resource Manager Template - JSON file that contains resources

## Benefits:
	- Manage Infrastructure through JSON templates (Includes properties for the infrastructure to deploy)
	- Deploy resources in the correct order (Dependencies between resources)
	- Centrally Deploy, Manage and Monitor all resources
	- Apply Tags to resources for organization
	- Clear billing and costs at organizational level
	
## Templates:
	- Declarative Syntax
		○ Deploy an entire infrastructure (vNET, VMs, storage, etc.)
	- Deployment Orchestration
		○ Orchestrate the deployment of interdependent resources, so they are deployed in the correct order
	- Template is first validated and then deployed
	- Create any resource in Azure and also supports integration with CI/CD tools

<img width="1662" height="652" alt="image" src="https://github.com/user-attachments/assets/b36ae468-bbaa-438e-bed1-9fc29ab09f43" />
