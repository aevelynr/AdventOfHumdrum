#!/bin/bash

YEAR=2021

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
  (cd problems/$YEAR/$1/ && python3 main.py)
}

Download()
{
  if [[ "$(python3 utils/cookies.py)" =~ 'session='([0-9a-z]+) ]]
  then
    mkdir -p problems/$Year/$1
    curl -b "session=${BASH_REMATCH[1]}" https://adventofcode.com/$YEAR/day/$1/input -o problems/$YEAR/$1/data.txt
  else
    echo "No Cookies"
  fi
}

Setup()
{
  python3 setup.py $YEAR "$1"
}

############################################################
############################################################
# Main program                                             #
############################################################
############################################################
# Get the options
while getopts "hr:d:s:" option; do
   case $option in
      h) # display Help
         Help
         exit;;
      r)
        Run "$OPTARG"
        exit;;
      d)
        Download "$OPTARG";;
      s)
        Setup "$OPTARG";;
      ?)
        echo "Invalid option: -${OPTARG}."
        exit 2
        ;;
   esac
done
