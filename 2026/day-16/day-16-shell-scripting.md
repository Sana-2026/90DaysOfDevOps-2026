# Day 16 – Shell Scripting Basics

## Task 1: Your First Script

<img width="855" height="174" alt="first-scriot" src="https://github.com/user-attachments/assets/7acc976e-576c-43a2-9d71-98755079646b" />

<img width="653" height="220" alt="running-script" src="https://github.com/user-attachments/assets/1718a10e-5af1-4e18-b05e-33f750948db5" />


<img width="780" height="404" alt="hello sh" src="https://github.com/user-attachments/assets/05791f19-2d11-4b02-be7f-b641b1f602b7" />

### What happens if you remove the shebang line?

- Shebang tells the OS which shell to use to run the script (bash, sh, etc.).

- Without shebang, ./script.sh may fail or behave differently.

- Running with bash script.sh works even without shebang.

## Task 2: Variables

<img width="796" height="268" alt="variable-script" src="https://github.com/user-attachments/assets/93d1a336-2906-461b-becd-ed8c675db92f" />

<img width="1220" height="486" alt="vim-number sh" src="https://github.com/user-attachments/assets/87b5a466-94c3-46c8-b49d-bd6fa3524bc9" />

### Try using single quotes vs double quotes — what's the difference?

Double quotes → variables are expanded

Single quotes → variables are treated as literal text

name="Sana"

echo "$name"   # Output: Sana

echo '$name'   # Output: $name

## Task 3: User Input with read

<img width="687" height="309" alt="greet-script" src="https://github.com/user-attachments/assets/7ce0b209-9061-4ada-94a1-9a2b940ac1a6" />

<img width="870" height="448" alt="vim-greet" src="https://github.com/user-attachments/assets/7d4b659c-f959-439e-adb7-4076740e39b0" />

## Task 4: If-Else Conditions

<img width="880" height="642" alt="check-number-scrpt" src="https://github.com/user-attachments/assets/8fbc33fd-6570-43b7-9d02-eea976c1ac1d" />

<img width="1220" height="486" alt="vim-number sh" src="https://github.com/user-attachments/assets/d6671d6a-5232-4161-a395-cfcdf5146ec2" />

<img width="960" height="383" alt="file-chk" src="https://github.com/user-attachments/assets/bde979c6-772d-480f-9be0-c447214d3294" />

<img width="572" height="364" alt="file-chk-run" src="https://github.com/user-attachments/assets/9c3e432e-f352-4b1e-a96b-12d86698ce8d" />


## Task 5: Combine It All
<img width="877" height="655" alt="server-chk-script" src="https://github.com/user-attachments/assets/96f9a78f-0838-436f-8408-3ce3cec02b24" />

<img width="1355" height="576" alt="server-script-output" src="https://github.com/user-attachments/assets/2378f547-5783-4018-b36c-e860de009611" />

<img width="1346" height="448" alt="server-scrt-output2" src="https://github.com/user-attachments/assets/b4397d85-8280-4c38-a171-5c3946f08f69" />

## What I Learned

- Shebang (#!/bin/bash) defines the shell used to run a script
  Commands learned: bash script.sh, chmod +x script.sh, ./script.sh

- Variables, input, and output help make scripts interactive
  Commands learned: echo, read, read -p

- Decision making with if-else allows scripts to act based on conditions
  Commands / operators learned: if, else, fi, -eq, -gt, -lt, =



