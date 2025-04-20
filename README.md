# 🐧 Learning Linux Commands  
Learning Linux commands so I can do some actual engineering – one terminal at a time.

---

## 🧑‍💻 User & Permissions
- `whoami` — Display the current user  
- `id` — Display user and group information  
  Example output:  
  `uid=1000(labex) gid=1000(labex) groups=1000(labex),4(adm),27(sudo)...`  
- `sudo` — Superuser do (run commands as another user, default is root)

---

## 📁 Navigating the File System
- `pwd` — Show current working directory  
- `cd` — Change directory  
- `ls` — List directory contents  
  - `ls -a` — Show hidden files  
  - `ls -l` — Long listing format  
  - `ls -r` — Reverse order  
- `~` — Shortcut for home directory

---

## 📂 Creating and Managing Files/Directories
- `touch` — Create a file  
- `mkdir` — Create a directory  
  - `mkdir -p` — Create parent directories as needed
- `cp` — Copy a file or directory  
  - `cp -r` — Recursively copy directories  
- `mv` — Move or rename a file/directory  
- `rm` — Remove a file  
  - `rm -i` — Prompt before every removal  
  - `rm -f` — Force removal without prompt  
- `rmdir` — Remove empty directories

---

## 🗃️ File Content & Comparison
- `cat` — Display the entire content of a file 
    - `cat-n`: to number all output lines.
- `head` — View the beginning of a file  
    - `head -n 1`: Show only the first line of the file.  
    - `head -c 1`: Show only the first byte (character) of the file.  
- `tail` — View the end of a file  
    - `tail -n 1`: Show only the last line of the file.  
    - `tail -c 1`: Show only the last byte (character) of the file.  
- `diff` — Compare content of two files
    - `diff -r`: The `-r` option tells `diff`difff to recursively compare subdirectories as well.

---

## 🔐 File Permissions
- `ls -l example.txt` — Display detailed info about a file  
    - Example: `-rw-rw-r-- 1 root root 0 Jul 29 15:11 example.txt`  
        - `-rw-rw-r--`:  
            - `-` — Regular file (`d` for directory, `l` for symlink)  
            - `rw-` — Owner can read & write  
            - `rw-` — Group can read & write  
            - `r--` — Others can only read  
        - `root` — File owner  
        - `root` — File group  
        - `0` — File size in bytes  
        - `Jul 29 15:11` — Last modified time  
        - `example.txt` — File name

- `sudo chown root:root example.txt` — Change file owner and group  
    - `sudo` — Run with superuser privileges  
    - `chown` — Command to change ownership  
    - `root:root` — New owner:group  
    - `example.txt` — Target file  

- `sudo chmod 700 example.txt` — Set file permissions  
    - `7` — Owner: read (4) + write (2) + execute (1) = `rwx`  
    - `0` — Group: no permission = `---`  
    - `0` — Others: no permission = `---`  
    - Final: `rwx------`

- `ls -ld ~/test-dir` — Show permission info for a directory  
    - Example: `drwx------ 2 labex labex 4096 Jul 29 15:45 /home/labex/test-dir`  
        - `d` — Indicates a directory  
        - `rwx------` — Owner can read/write/execute; group and others have no access  
            - `Read (r)` — Allows listing contents  
            - `Write (w)` — Allows creating/deleting files  
            - `Execute (x)` — Allows entering the directory (`cd`)
---

## 🧑‍💻 User Account Management

- **Creating a New User**  
    - `sudo useradd joker`  
        - `sudo` — Grants superuser privileges  
        - `useradd` — Command to create a new user  
        - `joker` — The username being created  

    - `sudo grep -w 'joker' /etc/passwd`  
        - Example output: `joker:x:5001:5001::/home/joker:/bin/sh`  
            - `Username:` joker  
            - `Password:` x (actual password is stored securely in `/etc/shadow`)  
            - `User ID:` 5001  
            - `Group ID:` 5001  
            - `Home Directory:` /home/joker (not created yet)  
            - `Default Shell:` /bin/sh

- **Creating a User with a Home Directory**  
    - Add the `-m` flag to create the home directory:  
        - `sudo useradd -m bob`  
    - Check directory: `sudo ls -ld /home/bob`  
        - Example output: `drwxr-x--- 2 bob bob 57 Jan 19 13:33 /home/bob`  
            - `d` — Indicates it's a directory  
            - `rwxr-x---` — Permissions (owner: rwx, group: r-x, others: ---)  
            - `bob bob` — User and group ownership  
            - `57` — Directory size in bytes  
            - `Jan 19 13:33` — Creation date/time  
            - `/home/bob` — Path to the home directory

- **Setting a User Password**  
    - `sudo passwd joker`  
        - Sets or changes the user’s password  
        - Passwords are securely stored in `/etc/shadow`

- **Modifying User Properties**  
    - `sudo usermod -d /home/wayne joker`  
        - `usermod` — Modify user account settings  
        - `-d /home/wayne` — New home directory path  
        - `joker` — Target user

- **Changing User Shell**  
    - Default shell might be `/bin/sh`, but `/bin/bash` is often preferred for features  
    - `sudo usermod -s /bin/bash joker` — Set bash as default shell  
    - Verify with: `sudo grep -w 'joker' /etc/passwd`

- **Adding a User to a Group**  
    - `sudo usermod -aG sudo joker`  
        - `usermod` — Modify user account  
        - `-aG` — Append user to a group  
        - `sudo` — Target group  
        - `joker` — Target user  

    - Validate:  
        - `groups joker` — Show group memberships  
        - `su - joker` — Switch to joker's shell  
        - `exit` — Return to previous user

- **Locking and Unlocking User Accounts**  
    - `sudo passwd -l joker` — Lock user account  
    - `sudo passwd -u joker` — Unlock user account

- **Deleting a User**  
    - `sudo userdel -r bob` — Delete user and home directory  
    - Verify:  
        - `sudo grep -w 'bob' /etc/passwd`  
        - `sudo ls -ld /home/bob`

---

## 📦 Package Management
- `apt install <package>` — Install a package using APT (Debian-based distros)

---

## 🔍 Hidden Files

- Files starting with `.` are hidden  
  Example: `.zshrc`, `.bash_profile`cd 

