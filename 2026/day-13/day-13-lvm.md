# Day 13 – Linux Volume Management (LVM)

## 🔹 What is LVM (in simple words)?

LVM lets you manage disk space flexibly.

👉 Instead of using a disk directly, LVM creates a logical layer on top of disks so you can:

Increase disk size without downtime

Combine multiple disks into one

Resize partitions easily
Run: lsblk, pvs, vgs, lvs, df -h

## Commands used

1. lsblk → Shows all disks, partitions, and LVM devices in a tree format

2. pvs → Displays Physical Volumes used by LVM

3. vgs → Shows Volume Groups and their free/used space

4. lvs → Displays Logical Volumes and their sizes

5. df -h → Shows filesystem disk usage in human-readable format

6. sudo su → Switches to the root user with full administrative privileges

7. pvcreate → Initializes a disk or partition to be used as an LVM Physical Volume  - pvcreate /dev/<disk-or-partition>

8. pvdisplay → Shows detailed information about an LVM Physical Volume

9. vgdisplay → Shows detailed information about an LVM Volume Group

10. vgcreate → Creates a new LVM Volume Group from one or more Physical Volumes  - vgcreate <vg_name> /dev/<pv1> [/dev/<pv2> ...]

11. Creates a Logical Volume (usable disk) from free space in a Volume Group - lvcreate -L <size> -n <lv_name> <vg_name>

📌 Quick flow memory
pvcreate → vgcreate → lvcreate

## Screenshots of outputs

### Task 1: Check Current Storage

<img width="952" height="259" alt="lsblk-command" src="https://github.com/user-attachments/assets/91150826-959c-464c-8668-50c50af60ffd" />

<img width="622" height="132" alt="pvs-view-phy-vol" src="https://github.com/user-attachments/assets/b800cf19-2dcb-446b-8a52-2ccf9d8fa08a" />

<img width="943" height="290" alt="lvm" src="https://github.com/user-attachments/assets/4c04c1d6-f0d4-40bb-b115-0d2c6c603c69" />

<img width="1370" height="292" alt="Screenshot 2026-02-10 191125" src="https://github.com/user-attachments/assets/b27b5e4b-bf0b-43c1-bc1f-84238c54f4bc" />

### Task 2: Create Physical Volume

<img width="702" height="132" alt="pvcreate-phy-volu-creation" src="https://github.com/user-attachments/assets/0cdf4503-37b2-4516-9d8b-d048d09b9967" />

### Task 3,4: Create Volume Group and Logical Volume

<img width="630" height="333" alt="logical-vol-created" src="https://github.com/user-attachments/assets/619b6317-bb74-41f5-b35d-3765f8f6adb1" />

### Task 5: Format and Mount

<img width="1109" height="616" alt="mkfs-making-filesys-formating" src="https://github.com/user-attachments/assets/164d603c-f566-4400-aec1-97a168cd9ebe" />

### Task 6: Extend the Volume







