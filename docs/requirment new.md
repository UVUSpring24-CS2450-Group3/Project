### Functional Requirements:

1. **Customizable Color Scheme:**
   - Users can configure a primary color and an off-color for the interface.
   - The default color scheme is UVU's dark green (#4C721D) as the primary color and white (#FFFFFF) as the off-color.
   - Users can set the color scheme through a configuration interface within the application.

2. **Real-time Color Scheme Update:**
   - Changes to the color scheme take effect instantly without requiring a restart of the application.

3. **File Loading to GUI:**
   - Users can load files containing command sequences into the GUI.
   - The loaded commands are displayed in a readable format within the GUI.
   - Users have the ability to inspect, modify, add, delete, cut, copy, and paste commands within the GUI.

4. **Command Sequence Modification:**
   - Users can manually edit individual commands within the GUI.
   - The GUI ensures that the total number of commands does not exceed 100 entries (#00 - #99).

5. **Save and Load Functionality:**
   - Users can save the modified command sequence to any user-specified folder.
   - Users can load command sequences from any user-specified folder.
   - The application maintains the integrity of the loaded and saved files, ensuring that they are not corrupted during the process.

### Nonfunctional Requirements:

1. **Usability:**
   - The interface should remain intuitive and user-friendly, allowing users to easily understand and navigate the color scheme configuration and command sequence editing features.

2. **Performance:**
   - The application should respond promptly to user interactions, ensuring smooth navigation and real-time updates.

3. **Reliability:**
   - The application should handle errors gracefully, providing informative error messages and preventing data loss or corruption.

4. **Portability:**
   - The application should be compatible with different operating systems and screen resolutions, ensuring consistent functionality and appearance across platforms.

5. **Scalability:**
   - The application should be able to handle larger command sequences efficiently, ensuring that performance does not degrade significantly as the size of the input data increases.

6. **Security:**
   - The application should implement appropriate security measures to protect user-configured settings and loaded/saved files from unauthorized access or tampering.

7. **Customizability:**
   - The application should allow users to customize not only the color scheme but also other aspects of the interface, such as font size and style, to cater to individual preferences.
