Site Content Types

Content types are managed at the site level. Creating a new content type, and then adding it to a site's collection of content types makes it become  a site content type. At this point, the content type is available to add to lists and document libraries but has not yet been added.
When creating content types, adding them to a site's content type collection, the new content type will be available to any child site and also to the site where it was created. For example, if you create a site content type at the root site of a site collection, that site content type becomes available on any site in the site hierarchy. If you add a new content type to a site that is lower down in the hierarchy, it is available in the site where you add it and in any sites below that site in the hierarchy. 
List Content Types
Just as each site has a content type collection, so too does each list or library in a site. You add a content type to a list or library by adding it to the content type collection for the list or library.
You can create a content type collection for a new list as part of the list definition before list instances are provisioned. Within the list definition's ContentTypes element, you can reference existing site content types, and you can also define new content types. In this case, the new content types are available only to list instances that are created from the same list definition. The new content types are not part of the site collection and are not available to other lists. 


[Site and List Content Types | Microsoft Learn](https://learn.microsoft.com/en-us/previous-versions/office/developer/sharepoint-2010/ms463016(v=office.14))

One is created at the list/library level (list columns), and the other one at the site level (site columns).
From a functionality perspective, they do the exact same thing. From a reusability perspective, not so much.

