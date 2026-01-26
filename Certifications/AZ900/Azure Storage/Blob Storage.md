Blobs are scalable object stores

## BLOB - Binary Large Objects
Unstructured Data (usually Text or Binary)

Suitable for:
	- Images and Files
	- Stream video and audio
	- Log Files
	- Data for Backup and Restore (Disaster Recovery)

Any type of Data

Highly Scalable
Supports Azure Data Lake Storage Gen2


## Azure DLS Gen2

	- Provides data analiytics for Azure storage
	- Scalable, cost effective


## Access Tiers:

HOT - Frequently Accessed Data
COOL - Infrequently Accessed Data (Stored min. 30 days)
ARCHIVE - Rarely Accessed Data (Stored min. 180 days)

Policy: HOT > COOL > ARCHIVE


## Azure Storage Encryption:

Microsoft Managed Encryption Keys
(Azure Storage Service Encryption-SSE)

Customer Encryption Keys
(Client-side Encryption)


## Storage Replication:

-Azure Replicates Data in the storage account to ensure high availability / -durability
-Data can be replicated within the same FC, across zonal DCs within the same region or across geographies
-Multiple redundancy options can be selected when creating the storage account

	- Locally Redundant Storage (LRS) replicates 3x within a single DC
	- Zone-Redundant Storage (ZRS) replicates 3x storage clusters in a single region
	- Geo-Redundant Storage (GRS) replicates to a secondary region (Min. 300 miles away)
	- ReadAccess-GRS provides read-only access to the data in the secondary location, in addition to geo-replication across 2 regions
	- Geo-Zone-Redundant Storage (GZRS) combines ZRS and GRS, data in 3 Azs (1st region) and in a 2nd region
	- ReadAccess GZRS - enables read access to data in the secondary region
<img width="1016" height="270" alt="image" src="https://github.com/user-attachments/assets/1fabed07-9cde-4ca8-919d-5aacddffd7b6" />

