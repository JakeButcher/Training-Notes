## Overview:
	- Encryption is the process of encoding a message or information in such a way that only authorized parties can access it
	- To use or read the encrypted data, it must be decrypted, which requires a secret key
	- 2 types of encryption
		○ Symmetric
			§ Same key is used to encrypt and decrypt
		○ Asymmetric
			§ Public key and Private key pair used; both can encrypt, but only decrypt with paired key
			§ More Secure
			§ Used in HTTPS environments (PKI and certificates)
	- Encryption at rest
		○ Data at rest is the data that has been stored on a physical medium; data is not moving or traveling
		○ Encryption of data at rest ensures the data stored is unreadable without the decryption keys
	- Encryption in transit
		○ Data in transit is data actively moving from one location to another' to on-prem DC, through internet
		○ Protects the data from outside observers, and provides a mechanism to transmit data securely

## Encryption in Azure:
	- Azure Storage Service Encryption
		○ Protect data at rest
		○ Data is automatically encrypted before storing it to Azure Storage and decrypted before retrieval
	- Azure Transparent Data Encryption (TDE)
		○ Real-time encryption and decryption for DBs - Azure SQL DB and Azure Data Warehouse
		○ Enabled by default
	- Azure key vault - encrypt the actual keys
	
## Azure Key Vault:
	- Ensure keys are secure and store in a centralized cloud service
	- Common Use Cases:
		○ Secrets Management - store tokens, passwords etc
		○ Key Management - create and control encryption keys
		○ Certificate Management - provision, manage and deploy private or public certificates
