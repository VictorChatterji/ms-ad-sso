# Project Name

> Python application with Microsoft Active Directory Single Sign-On (SSO) integration

## Table of Contents

- [About](#about)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Configuration](#configuration)
- [Running the Project Locally](#running-the-project-locally)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## About

This project demonstrates how to implement Microsoft Active Directory (Azure AD) Single Sign-On (SSO) in a Python application. This documentation will guide you through the setup, configuration, and integration of Azure AD SSO for secure authentication.

## Getting Started

### Prerequisites

Before you start, make sure you have the following:

- **Python 3.7+**
- **Microsoft Azure Account** with permissions to register applications
- **Visual Studio Code** (or any preferred code editor)
- **Azure Active Directory** access with privileges to manage applications

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject
   ```
2. **Install Required Python Packages:**
Make sure you have a requirements.txt file listing all dependencies for your project.

```bash
pip install -r requirements.txt
```
3. **Set Up Virtual Environment:**

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
4. **Install Dependencies in the Virtual Environment:**

```bash
pip install -r requirements.txt
```
5. **Configuration**

Create an .env file in the root of the project to store environment variables used for Azure AD SSO. Your .env file should contain the following:

```
# Azure AD Configurations
CLIENT_ID=<your-client-id>
CLIENT_SECRET=<your-client-secret>
TENANT_ID=<your-tenant-id>
REDIRECT_URI=http://localhost:5000/getAToken
AUTHORITY=https://login.microsoftonline.com/<your-tenant-id>
SCOPE=https://graph.microsoft.com/.default
```


CLIENT_ID: Azure AD application (client) ID
CLIENT_SECRET: Application secret key generated in Azure AD
TENANT_ID: Azure AD tenant ID
REDIRECT_URI: URI where Azure will redirect after successful login
AUTHORITY: Azure AD authority endpoint
SCOPE: Permission scope for accessing Microsoft Graph API


6. **Running the Project Locally**
After completing the configuration, you can start the application:

```bash
python app.py
```

7. **Accessing the Application**
Visit `http://localhost:5000` in your browser.

8. **Click Sign in with Microsoft to initiate SSO.**

## Troubleshooting
*Invalid Client ID/Secret:*  Ensure your CLIENT_ID and CLIENT_SECRET in the .env file match the Azure AD registration.
Redirect URI Mismatch: The REDIRECT_URI in Azure AD must match the one specified in your app.
*Permissions Issues:* Make sure the API permissions are correctly configured and admin consent is granted.

## Contributing
Feel free to open issues or submit pull requests to improve the SSO implementation or documentation.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

