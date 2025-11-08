## Overview:
	- A service you can use to create, assign, and manage policies
	- Establishes rules/conventions that resources must comply with
	
## Definition / Assignment:
	- Create the policy
		○ Define the policy - conditions and effect
		○ Policy Assignment - assign definition to a specific scope (where policy is enforced)
    
<img width="963" height="331" alt="image" src="https://github.com/user-attachments/assets/3421a871-371d-4211-86c8-1e852cc3e944" />

	- Assigned to take place within a specific scope (from management group, down to a resource)
	- Policy's are inherited by all child resources (e.g. Resources have RG Policy enforced)
  
<img width="1060" height="413" alt="image" src="https://github.com/user-attachments/assets/c2d8c06d-2b02-42d3-877a-d392737b1f05" />

## Built-In Azure Policies:
	- Allowed locations
		○ New resources deployed to be deployed in specific locations
	- Allowed VM SKUs
		○ Only specific VM SKUs to be used
	- Enforce tag and its value
		○ Enforces a required tag and its value to a resource

## Initiative Definitions:
	- Simplify managing and assigning policy definitions, by grouping a set of policies as one single item - initiative

<img width="1277" height="391" alt="image" src="https://github.com/user-attachments/assets/e86fd107-df30-410a-b184-371d51626256" />
