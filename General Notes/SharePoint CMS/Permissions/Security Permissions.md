Managing permissions on a site
Owners can determine the level of access to the site. They can grant users access to the whole site, or to specific information on the site, such as a list or even a single file. Assigning permission levels to a specific item can help you to protect sensitive content, such as a contract or budget information, without restricting access to the rest of the site.
SharePoint groups and permission levels help you to efficiently manage access to sites. They can also add users to SharePoint groups and assign permission levels to the site and to its contents. 
By default, permissions on lists, libraries, folders within lists and libraries, items, and documents are inherited from their parent site. However, you can assign unique permissions to items at a lower level, such as subsites, libraries, or even files.
SharePoint groups
Each site comes with a default set of SharePoint groups, such as Owners. The name of the SharePoint group matches the name of the site. For example, if the name of the site is Marketing, a group will be called Marketing Owners. You can add people to these groups, so that you can later grant access to the group instead of having to grant access to each individual user. You can also create SharePoint groups to provide custom levels of access. You might want to provide more liberal or restrictive access to a specific group than you would to the default members of your site. For example, if you have a group of marketing managers that often gives confidential presentations, you might want to create a Marketing Managers group that can share information that is restricted from all other users of the site.
Permission levels
Each permission level has a set of permissions associated with it, based on the intended roles and tasks for that level. For example, the Members group has the Contribute permission level by default. As a site owner, you choose which permissions are associated with each permission level (except for Limited Access and Full Control, which cannot be customized) or add new permission levels to combine different sets of permissions. Some sites have additional groups and permission levels that are tailored to the purpose of the site, such as publishing or records management sites.

---

Read permission level
If you can view the site but not make changes to the site or to the content on it, you belong to the Visitors group, which has the Read permission level. For example, if you can view a site but cannot edit a document on the site, you have the Read permission level.
Contribute permission level
If you can view the site and change the content on the site, but not make changes to the site, you belong to Members group which has the Contribute permission level.
Full Control permission level
If you can change the content and the settings on the site you belong to the Owners group which has the Full Control permission level. One of the common tasks that a site owner performs is managing permissions.
You do not have permission to access the site
If you receive the Error: Access Denied message when you attempt to access a site, you do not have the permissions necessary to view the site. Click Request access to ask the site owner to grant you the necessary permissions.



From <https://support.microsoft.com/en-us/office/understand-groups-and-permissions-on-a-sharepoint-site-258e5f33-1b5a-4766-a503-d86655cf950d> 




Default groups for team sites :
Group name	Default permission level	Description
Visitors	Read	Use this group to grant people Read permissions to the SharePoint site.
Members	Edit	Use this group to grant people Edit permissions to the SharePoint site.
Owners	Full Control	Use this group to grant people Full Control permissions to the SharePoint site.
Viewers	View Only	Use this group to grant people View Only permissions to the SharePoint site.
Groups provided by a publishing site template :
Group name	Default permission level	Description
Restricted Readers	Restricted Read to the site, plus Limited Access to specific lists	Members of this group can view pages and documents, but cannot view historical versions or review user rights information.
Style Resource Readers	Read to the Master Page Gallery and Restricted Read to the Style Library.	Members of this group are given Read permission to the Master Page Gallery and Restricted Read permission to the Style Library. By default, all authenticated users are a member of this group.
Designers	Design, Limited Access	Members of this group can view, add, update, delete, approve, and customize the layout of site pages by using the browser or SharePoint Designer 2013.
Approvers	Approve, plus Limited Access	Members of this group can edit and approve pages, list items, and documents.
Hierarchy Managers	Manage Hierarchy, plus Limited Access	Members of this group can create sites, lists, list items, and documents.





Permission level	Description	Permissions included by default
View Only	Enables users to view application pages. The View Only permission level is used for the Excel Services Viewers group.	View Application Pages
        View Items
        View Versions
        Create Alerts
        Use Self Service Site Creation
        View Pages
        Browse User Information
        Use Remote Interfaces
        Use Client Integration Features
        Open
Limited Access	Enables users to access shared resources and a specific asset. Limited Access is designed to be combined with fine-grained permissions to enable users to access a specific list, document library, folder, list item, or document, without enabling them to access the whole site. Limited Access cannot be edited or deleted. Note: when sharing a link to a document with all users in your organization, SharePoint will assign the Limited Access permission via a group name "Limited Access System Group" that is applied the first time a user accesses the resource who does not otherwise have permission via the link	View Application Pages
        Browse User Information
        Use Remote Interfaces
        Use Client Integration Features
        Open
Read	Enables users to view pages and list items, and to download documents.	Limited Access permissions, plus:
        View Items
        Open Items
        View Versions
        Create Alerts
        Use Self-Service Site Creation
        View Pages
Contribute	Enables users to manage personal views, edit items and user information, delete versions in existing lists and document libraries, and add, remove, and update personal Web Parts.	Read permissions, plus:
        Add Items
        Edit Items
        Delete Items
        Delete Versions
        Browse Directories
        Edit Personal User Information
        Manage Personal Views
        Add/Remove Personal Web Parts
        Update Personal Web Parts
Edit	Enables users to manage lists.	Contribute permissions, plus:
        Manage Lists
Design	Enables users to view, add, update, delete, approve, and customize items or pages in the website.	Edit permissions, plus:
        Add and Customize Pages
        Apply Themes and Borders
        Apply Style Sheets
        Override List Behaviors
        Approve Items
Full Control	Enables users to have full control of the website.	All permissions

