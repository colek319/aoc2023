#!/bin/bash

# Initialize variables
DAY=""
INPUT_PATTERN="*.txt"  # Default pattern to select all .txt files
PART="a"

# Parse command line argument for the day
for i in "$@"
do
case $i in
    --day=*)
    DAY="${i#*=}"
    shift # past argument=value
    ;;
    --input=*)
    INPUT_PATTERN="${i#*=}"
    shift # past argument=value
    ;;
    --part=*)
    PART="${i#*=}"
    shift # past argument=value
    ;;
    *)
          # unknown option
    ;;
esac
done

# Define the directory
DIR="d$DAY"

# Check if directory exists
if [ -d "$DIR" ]; then
    # Run main.py for each file in the directory matching the input pattern
    for file in $DIR/$INPUT_PATTERN; do
        if [ -f "$file" ]; then
            # Note: Using absolute path for main.py and passing the correct variables
            echo "Running $file:"
            python3 "$(pwd)/main.py" "d$DAY" "$file" $PART
            echo ""
        else
            echo "No files found matching $INPUT_PATTERN in $DIR."
            break
        fi
    done
else
    echo "Directory $DIR does not exist."
fi
