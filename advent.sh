#!/bin/bash

YEAR=2022

############################################################
# Help                                                     #
############################################################
Help()
{
   # Display Help
   echo "Syntax: advent.sh [-h|r|d|s] <problem number>"
   echo "options:"
   echo "h     Print this Help."
   echo "r     Run the main.py for an advent of code problem"
   echo "d     Download the data file for an advent of code problem"
   echo "s     Run the setup.py script for an advent of code problem"
   echo
}

Run()
{
  (cd problems/$YEAR/$1 && python3 main.py)
}

Download()
{
  if [[ "$(python3 utils/cookies.py)" =~ 'session='([0-9a-z]+) ]]
  then
    mkdir -p problems/$YEAR/$1
    curl -b "session=${BASH_REMATCH[1]}" https://adventofcode.com/$YEAR/day/$1/input -o problems/$YEAR/$1/data.txt
  else
    echo "No Cookies"
  fi
}

Setup()
{
  mkdir -p problems/$YEAR/$1
  if [[ ! -f problems/$YEAR/$1/main.py ]]
  then
    python3 setup.py $YEAR $1
  fi
}

############################################################
############################################################
# Main program                                             #
############################################################
############################################################

# advent.sh -d 1
# advent.sh -dsr 1
# advent.sh -s -d -r 1
problem_number="${@: -1}"
if [[ "$*" =~ \-.{,2}h ]]
then
  Help
  exit
fi

if [[ "$problem_number" =~ 1?[1-9]|2[0-5] ]]
then
  if [[ "$*" =~ \-.{,2}s ]]
  then
    Setup $problem_number
  fi

  if [[ "$*" =~ \-.{,2}d ]]
  then
    Download $problem_number
  fi

  if [[ "$*" =~ \-.{,2}r ]]
  then
    Run $problem_number
    exit
  fi
fi



# Get the options
#while getopts ":hrds" option; do
#  # advent.sh -r 1
#  # advent.sh -ds 1
#   case $option in
#      h) # display Help
#         Help
#         exit;;
#      r)
#        Run "$OPTARG"
#        exit;;
#      d)
#        Download "$OPTARG";;
#      s)
#        Setup "$OPTARG";;
#      ?)
#        echo "Invalid option: -${OPTARG}."
#        exit 2
#        ;;
#   esac
#done
