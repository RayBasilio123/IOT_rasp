#!/bin/bash
# Define bash global variable
# This variable is global and can be used anywhere in this bash script
VAR="global variable"

tunnell (){
# Define bash local variable
# This variable is local to bash function only
local VAR="$1"
echo $VAR
}


tunnell $1
