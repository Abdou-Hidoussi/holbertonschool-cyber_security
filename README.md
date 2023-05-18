Json Configuration Struct:

{    
    "Module Name": {

        "Function Name": [

            [
                "File Path",
                "Argument",
                "True if task is a requirment"
            ],

        ]

    }

}

Module Name: name of the module that contains the checker function 

Function Name: name of the checker function

File Path: file to check

Argument: argumant if any or None


Json Output Structure:

[
    {
        "check": Check Function Name,
        "status": Success or Failed,
        "error": Error if any,
        "desc": Description of the check function,
        "arg": The provided arguments if any,
    },
]

use of checker example:


task_list = ["Task0", "Task1"]

file_list = ["README.md", "Task0.bash", "Task1.sh"]

check_repo("Abdou-Hidoussi", "testing_sc", "0x03_nmap_live_hosts_discovery", file_list, task_list)
