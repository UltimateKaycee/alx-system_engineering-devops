#HOW I PERFORMED THE UPLOAD OF THE COMPLETED "COMMAND LINE FOR THE WIN" CHALLENGE

# THIS README.md FILE DESCRIBES OR DEMONSTRATES THE PROCEDURE I FOLLOWED FOR THE UPLOAD TASK DONE USING SFTP (SECURE FILE TRANSFER PROTOCOL)



#INTRODUCTION

The task was to do a challenge and then upload screenshots of the completed tasks.
First, after completing the tasks, I took screenshots of them and saved the 3 files in PNG Image format in a folder “Command Line for The Win” on my local machine.



#UPLOAD PROCEDURE

To upload the files, I first reached out for the sandbox SFTP credentials provided on my intranet page. Namely;
-	SFTP Hostname
-	Username
-	Password
I use virtualized Ubuntu on my Windows PC – Ubuntu 20, running on Oracle VirtualBox. I had created and shared directories as needed, to enable my Ubuntu (VirtualBox) and Windows PC talk to each other and share files easily.
Hence, given this, I have always used the SSH connection to connect my virtualized Ubuntu, to my sandbox, using the following credentials;
-	SSH Hostname
-	Username
-	Password


For this very task (Command Line for The Win), I needed to use SFTP as instructed in the project information, in order to perform a file transfer.
As mentioned earlier, on my Shell prompt, I copied the relevant credentials (SFTP). Namely;
-	SFTP Hostname
-	Username
-	Password
On establishing an SFTP connection with the sandbox, I navigated to the relevant Repo/Dir. While there (on the remote location), I used the local-host shell commands to navigate accordingly to my local PC where the screenshots were saved. 
The I used lpwd to find the current local working directory
On finding this and while still inside/on or connected to the remote server, I ran the appropriate commands to upload the files from my local system to the remote sandbox location.



#THE COMMANDS ARE BELOW:

(put “my-local-path/0-first_9_tasks.png”)
(put “my-local-path/1-next_9_tasks.png”)
(put “my-local-path/2-next_9_tasks.png”)
Consider “my-local-path” to be the actual path to the local location where the screenshots were saved. Quite a long one 😊



#CONFIRMATION OF UPLOAD
After this process and in order to confirm that my files were really uploaded to my Sandbox. I listed (ls) the files in the current (remote) working directory and found that the files were really uploaded and present.



#DOUBLE CONFIRMATION

To be double sure, I also used SSH this time, to establish another connection to the Sandbox as I usually do, and navigated to the relevant sandbox directory – “command_line_for_the_win” which is located in the “alx-system_engineering_devops” Repository and lo and behold, they were also confirmed to be present.

Same will also go for this README.md file which will be in the root of the “command_line_for_the_win” directory.

The final step was to push to Github accordingly.



Thank you for reading :).

