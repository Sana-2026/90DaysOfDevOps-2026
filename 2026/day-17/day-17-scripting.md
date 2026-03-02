## Day 17 – Shell Scripting: Loops, Arguments & Error Handling

## Challenge Tasks

### Task 1: For Loop
1. Create for_loop.sh that:

<img width="1318" height="472" alt="correct-for-loop-script" src="https://github.com/user-attachments/assets/5d3bfee8-83eb-4f10-a105-2068fe934449" />

2. Loops through a list of 5 fruits and prints each one

<img width="943" height="423" alt="for_loop-script" src="https://github.com/user-attachments/assets/81c4fce6-1b47-4e0b-a8f9-3b906ee04e2d" />

<img width="847" height="280" alt="for-loop-scrpt-output" src="https://github.com/user-attachments/assets/5d181ead-6fd4-421f-b773-4cb1d3bd916a" />

3. Create count.sh that:
   Prints numbers 1 to 10 using a for loop

   <img width="1360" height="514" alt="count-script" src="https://github.com/user-attachments/assets/6ff34aef-d63a-4693-8c41-e38e91ff3936" />
   
<img width="710" height="369" alt="count-script-output" src="https://github.com/user-attachments/assets/73cc19b3-6b4b-4120-bf79-ea78b7612870" />


### Task 2: While Loop

1. Create countdown.sh that:
    - Takes a number from the user
    - Counts down to 0 using a while loop
    - Prints "Done!" at the end
      
<img width="1348" height="595" alt="count-down-scrpt" src="https://github.com/user-attachments/assets/62a0bae6-3c56-4a92-9bd0-6346410a6f9d" />

<img width="836" height="313" alt="count-down-output" src="https://github.com/user-attachments/assets/5ae98e73-dcef-46e8-bc1c-70b34af46720" />

### Task 3: Command-Line Arguments

1. Create greet.sh that:

    - Accepts a name as $1
    - Prints Hello, <name>!
    - If no argument is passed, prints "Usage: ./greet.sh "
    - 
<img width="1335" height="413" alt="greet-script" src="https://github.com/user-attachments/assets/48bc7d16-6a30-46d3-b90c-ff116a412e51" />

<img width="652" height="199" alt="greet-script-output" src="https://github.com/user-attachments/assets/152b45bf-e268-4848-a4dc-95d4daf20828" />

2. Create args_demo.sh that:

    - Prints total number of arguments ($#)
    - Prints all arguments ($@)
    - Prints the script name ($0)
      
<img width="990" height="310" alt="args-demo" src="https://github.com/user-attachments/assets/ce21330e-1bad-4c8b-8eb3-d62eb9df5d33" />

<img width="888" height="286" alt="output-args sh" src="https://github.com/user-attachments/assets/f78757f5-a74d-42d7-b1a6-02f056e8130d" />



## Task 4: Install Packages via Script

1. Create install_packages.sh that:
   
   - Defines a list of packages: nginx, curl, wget
   - Loops through the list
   - Checks if each package is installed (use dpkg -s or rpm -q)
   - Installs it if missing, skips if already present
   - Prints status for each package
   - Run as root: sudo -i or sudo su
   - 
<img width="1015" height="707" alt="install-pkg-sc" src="https://github.com/user-attachments/assets/12dc031f-fdf9-4a2a-af2c-8370ef889713" />

<img width="659" height="286" alt="package-sc-output" src="https://github.com/user-attachments/assets/94187ddf-4dcd-4bb9-a35f-b549247c8416" />



## Task 5: Error Handling

1. Create safe_script.sh that:
   
- Uses set -e at the top (exit on error)
- Tries to create a directory /tmp/devops-test
- Tries to navigate into it
- Creates a file inside
- Uses || operator to print an error if any step fails
- Example:
- mkdir /tmp/devops-test || echo "Directory already exists"
- Modify your install_packages.sh to check if the script is being run as root — exit with a message if not.

<img width="1071" height="480" alt="safe-script" src="https://github.com/user-attachments/assets/78f132cf-17fe-4d91-b493-0c56611df6ba" />

<img width="548" height="131" alt="output-safe-script" src="https://github.com/user-attachments/assets/e0145789-d656-4857-9d97-da2cd237725a" />

