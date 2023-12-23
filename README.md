# Currency-Converter

IMPORTANT NOTE

To fully utilize this program, you will need to generate your own API key from exchangeratesapi.io and add this to your system:

Setting an environment variable permanently on Windows can be done through the System Properties. Here's a step-by-step guide:

### Setting Environment Variable on Windows

1. **Search for Environment Variables**:
   - Right-click on the 'Start' button and select 'System'.
   - Click on 'About', then click on 'Advanced system settings' on the right side.
   - This opens the 'System Properties' window. Go to the 'Advanced' tab.
   - Click on the 'Environment Variables...' button.

2. **Add New Environment Variable**:
   - Under the 'System variables' section (for all users) or the 'User variables' section (for the current user only), click on the 'New...' button.
   - In the 'New System Variable' or 'New User Variable' dialog, enter the name of the variable (e.g., `EXCHANGE_RATES_API_KEY`) and its value (your actual API key).

3. **Save and Apply**:
   - Click 'OK' to close the dialog boxes and apply the changes.

4. **Verify the Variable**:
   - To verify that the environment variable is set, open Command Prompt or PowerShell and type:
     ```cmd
     echo %EXCHANGE_RATES_API_KEY%
     ```
     This should output the value of your API key.

5. **Use in Python**:
   - Now, in your Python code, you can access this variable using:
     ```python
     import os
     api_key = os.getenv('EXCHANGE_RATES_API_KEY')
     ```

### Note:
- Setting environment variables this way will require a restart of any command prompts, IDEs, or applications that need to access the new variable. In some cases, you might even need to restart your computer.
- Be careful with sensitive data like API keys. Ensure that only the necessary users or applications have access to it, especially on shared or public systems.

By using an environment variable, you keep your API key out of your source code, which is a good security practice.

LINUX:

Setting an environment variable permanently on Linux involves editing shell configuration files. The exact file depends on the shell you are using. For most users, this will be either Bash or Zsh. Here are the steps for each:

### Setting Environment Variable in Bash (Common in Linux)

1. **Open Bash Configuration File**:
   - Open a terminal.
   - Type `nano ~/.bashrc` to edit the `.bashrc` file in your home directory with `nano` editor. You can use other text editors like `vim` or `gedit` if you prefer.

2. **Add Environment Variable**:
   - Scroll to the end of the file.
   - Add a new line with the export command: `export EXCHANGE_RATES_API_KEY='your_api_key_here'`.
   - Replace `'your_api_key_here'` with your actual API key.

3. **Save and Exit**:
   - Save the file and exit the editor. In `nano`, you can do this by pressing `Ctrl + O`, `Enter` to save and `Ctrl + X` to exit.

4. **Apply Changes**:
   - For the changes to take effect, you can either:
     - Close the terminal and open a new one.
     - Or source the `.bashrc` file by typing `source ~/.bashrc` in the terminal.

5. **Verify the Variable**:
   - In the terminal, type `echo $EXCHANGE_RATES_API_KEY`.
   - This should display the value of your API key.

### Setting Environment Variable in Zsh

1. **Open Zsh Configuration File**:
   - Open a terminal.
   - Type `nano ~/.zshrc` if you use Zsh.

2. **Add Environment Variable**:
   - Add `export EXCHANGE_RATES_API_KEY='your_api_key_here'` at the end of the `.zshrc` file.

3. **Save and Apply**:
   - Save the changes and exit.
   - Apply changes with `source ~/.zshrc` or open a new terminal.

### Notes
- **Shell Check**: To check which shell you are using, type `echo $SHELL` in the terminal.
- **Security**: Be cautious when adding API keys or other sensitive information to your environment variables, especially on shared or public systems.
- **Restart Applications**: After setting the environment variable, you might need to restart any applications or development environments that should have access
