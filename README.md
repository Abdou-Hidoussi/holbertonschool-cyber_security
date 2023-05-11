Json Configuration Struct:

{    
    "Module Name": {
        "Function Name": [
            [
                "File Path",
                "Argument"
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
