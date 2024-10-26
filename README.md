# word-document-processing
word document processing

# Usefull Tips#
**                                                                    **1. ERROR:**
**
Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
**1. Solution:** The error message you’re seeing indicates that Microsoft Visual C++ Build Tools are required to compile packages on Windows. This happens when Python packages need native code compilation, and hnswlib is one of them.
Here’s how to resolve it:

To resolve the error message "Microsoft Visual C++ 14.0 or greater is required", you need to ensure that the correct version of the Microsoft C++ Build Tools is installed on your system. Here’s a step-by-step guide to get rid of this error:

****Step 1: Install Microsoft C++ Build Tools
Download the Build Tools:

Go to the Microsoft Visual C++ Build Tools page.
Click on the "Download Build Tools" button.
Run the Installer:

After downloading, run the installer. It should display options for selecting workloads and components.
**Step 2:** Select Workloads
In the installer, you can choose specific workloads. To ensure you have everything you need:

Select Workloads:
Desktop Development with C++: This is the most important workload you need to select. It includes the MSVC compiler, libraries, and tools necessary for building C++ applications.
You may also consider additional workloads based on your needs (like Game Development, Mobile Development, etc.), but for the error you mentioned, Desktop Development with C++ is crucial.


**                                          **2. Error:** cl not executable**
**                                          
**2. Solution** Add environment variables C:\Program Files\Microsoft Visual Studio\2022\<Edition>\VC\Tools\MSVC\<version>\bin\Hostx64\x64

                            
                                 **3. Error**: HTTPSConnectionPool(host='files.pythonhosted.org', port=443): Read timed out.
**3. Solution**: 
1. Increase the pip Timeout (pip install <package-name> --timeout=100)

**2. Use a Different Package Mirror (Like PyPI Mirror)**
Sometimes, network issues with the default Python Package Index (PyPI) can cause this timeout. You can specify an alternate PyPI mirror like this:
pip install <package-name> --index-url=https://pypi.org/simple --timeout=100
Alternatively, you can try installing from a different country’s mirror (such as a regional mirror for faster speeds in your area). For example:
pip install <package-name> --index-url=https://pypi.tuna.tsinghua.edu.cn/simple

**3. Check Your Internet Connection**

Ensure you have a stable internet connection as intermittent connectivity can lead to timeouts.

If you’re behind a firewall or proxy, ensure that pip has the necessary permissions to connect to external servers. You can configure pip to use a proxy with:

pip install <package-name> --proxy="http://proxy.server:port"

**4. Update pip**
python -m pip install --upgrade pip

**5. Download the Package Manually**
If the above steps don’t work, you can download the package manually from PyPI. Here’s how:

Go to https://pypi.org/ and search for the package you need.

Download the .whl file for your platform and Python version.

Once downloaded, install it locally using:
pip install path/to/package.whl

                **4.ValueError: Expected where to have exactly one operator, got {'policy_type': 'Home Guard', 'country': 'Hong Kong'} python-BaseException**

                This error occurs because ChromaDB's where clause expects only a single condition with an operator (like $eq, $ne, $in, etc.) rather than multiple field-value pairs directly in the dictionary. To combine conditions like "policy_type": "Home Guard" and "country": "Hong Kong", you need to use the $and operator.




