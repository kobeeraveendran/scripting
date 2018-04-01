# Using autoclearDownloadsv2
Before beginning, download *start.bat* and *autoclearDownloadsv2.py*, and place them in the same directory.
If you'd like to auto-clear another folder, specify the path by opening *autoclearDownloads.py* and changing the value of
the `directory` variable near the top of the file. If you don't it will clear the folders/files in the path `D:/Downloads`, so 
change the path as you see fit before anything else.

### Running the script
To just auto-clear a folder once, put *start.bat* and *autoclearDownloadsv2.py* in the same directory (different from the one you're clearing) 
and double-click on *start.bat*. Make sure you've specified the desired path to the folder you want to clear, as the default is `D:/Downloads`.

### Scheduling the task to occur periodically
1. Search for **Task Scheduler** from the Start menu.
2. In the *Actions* tab, select **Create Basic Task...**.
3. In the pop-up window, give the task a name (and optionally, a description), such as "Clear Downloads".
4. Select how frequently you want this task to be executed.
5. Fill out the fields on the next screen as appropriate.
6. Select an action to perform; in this case, select **Start a program**.
7. Under "Programs/scripts," click **Browse** and select the *start.bat* file.
8. Click **Finish**. This task will now execute at the days/times you specified.
