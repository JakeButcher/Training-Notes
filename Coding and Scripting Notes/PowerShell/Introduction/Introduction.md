PowerShell scripting - the process of writing a set of statements in the PowerShell language and storing those statements in a text file. 

Why - When you repeat something frequently, it's probably a good idea to automate it: to store it in such a way that makes it easy to reuse.


The steps to automate your task usually include calls to cmdlets, functions, variables, and more. To store these steps, you create a file that ends in .ps1 and save it. You then have a script you can run.

An overview of the features of the PowerShell scripting language:
    • Variables. You can use variables to store values. You can also use variables as arguments to commands.
    • Functions. A function is a named list of statements. Functions produce an output that display in the console. You can also use functions as input for other commands.
 Note
Many of the tasks you'd use PowerShell for are about side effects or modifications to system state (local or otherwise). Often the output is a secondary concern (reporting data, for example).
    • Flow control. Flow control is how you control various execution paths by using constructs like If, ElseIf, and Else.
    • Loops. Loops are constructs that let you operate on arrays, inspect each item, and do some kind of operation on each item. But loops are about more than array iteration. You can also conditionally continue to run a loop by using Do-While loops. For more information, see About Do.
    • Error handling. It's important to write scripts that are robust and can handle various types of errors. You need to know the difference between terminating and nonterminating errors. You use constructs like Try and Catch. We cover this topic in the last conceptual unit of this module.
    • Expressions. You frequently use expressions in PowerShell scripts. For example, to create custom columns or custom sort expressions. Expressions are representations of values in PowerShell syntax.
    • .NET and .NET Core integration. PowerShell provides powerful integration with .NET and .NET Core. This integration is beyond the scope of this module.



Run a script
Some scripts aren't safe. If you find a script on the internet, you shouldn't run it on your computer unless you understand exactly what it does. 

Even with scripts you consider safe, there might be a risk. For example, imagine a script that cleans things up in a test environment. That script might be harmful in a production environment. You need to understand what a script does, whether it was written by you or by a colleague or if you got it from the internet.

PowerShell attempts to protect you from doing things unintentionally in two main ways:
    • Requirement to run scripts by using a full path or relative path. When you run a script, you always need to provide the script's path. Providing the path helps you to know exactly what you're running. For example, there could be commands and aliases on your computer you don't intend to run, but that have the same name as your script. Including the path provides an extra check to ensure you run exactly what you want to run.
    • Execution policy. An execution policy is a safety feature. Like requiring the path of a script, a policy can stop you from doing unintentional things. You can set the policy on various levels, like the local computer, current user, or particular session. You can also use a Group Policy setting to set execution policies for computers and users.
These two mechanisms don't stop you from opening a file, copying its contents, placing the contents in a text file, and running the file. They also don't stop you from running the code via the console. These mechanisms help to stop you from doing something unintentional. They aren't a security system.

From <https://learn.microsoft.com/en-us/training/modules/script-with-powershell/2-introduction-scripting> 
