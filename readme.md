# NewBreak Church Application ✨

This repository contains a desktop application built with Python's **Tkinter** library, designed to serve as a digital presence for "NewBreak Church." The application includes a secure login system, an interactive blog display, and a comprehensive main church information page.

---

## 📖 Table of Contents

* [🌟 Features](#features)
* [🚀 Installation](#installation)
* [🖥️ Usage](#usage)
* [📂 File Structure](#file-structure)
* [🔗 Dependencies](#dependencies)
* [🤝 Contributing](#contributing)
* [📜 License](#license)

---

## 🌟 Features

* **User Authentication**: A robust login and signup system using **SQLite** for secure user management.
* **Church Home Page**: Displays essential information about NewBreak Church, including menu items, a prominent main image, and a footer with the church's mission statement.
* **Interactive Blog**: A dedicated blog section showcasing weekly articles, engaging images, and categorized tags for effortless navigation.
* **Responsive Design (Tkinter)**: Basic UI elements are thoughtfully structured to provide a consistent and user-friendly experience.

---

## 🚀 Installation

To get this application up and running on your local machine, follow these simple steps:

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/your-username/NewBreak-Church-App.git](https://github.com/your-username/NewBreak-Church-App.git)
    cd NewBreak-Church-App
    ```

2.  **Install dependencies:** This project requires `tkinter` (usually bundled with Python) and `Pillow` (PIL Fork) for effective image handling.

    ```bash
    pip install Pillow
    ```

3.  **Prepare image assets:** Ensure you have the following image files in the same directory as your Python scripts, or update the `image_folder` variable in `blog.py` to point to their correct location:

    * `church.jpg` (for `NewBreak_Church.py`)
    * `meeting.jpg` (for `blog.py`)
    * `content.jpg` (for `blog.py`)
    * `Blog.jpg` (for `blog.py`)
    * `virtual photography.jpg` (for `blog.py`)

    **Note:** The `blog.py` currently uses a hardcoded path `C:/Pyhton project` for images. **You should change this to a relative path or the actual path where your images are stored for the application to function correctly.**

---

## 🖥️ Usage

1.  **Run the login application:**

    ```bash
    python login.py
    ```

2.  **Sign Up or Log In:**
    * If you're a new user, click "SIGN UP" to create a new account.
    * If you have an existing account, enter your username and password, then click "LOGIN."

3.  **Navigate the Application:**
    * Upon successful login, the blog page (`blog.py`) will be displayed automatically.
    * The `NewBreak_Church.py` script can be run independently to view the main church page without logging in.

---

## 📂 File Structure

├── blog.py
├── login.py
├── NewBreak_Church.py
├── top.py (empty/placeholder)
├── users.db (generated after first run of login.py)
├── church.jpg
├── meeting.jpg
├── content.jpg
├── Blog.jpg
└── virtual photography.jpg

* `blog.py`: Contains the code for the church's blog page, responsible for displaying articles and images.
* `login.py`: Manages all user authentication processes (signup and login) and interacts with the **SQLite** database. This serves as the primary entry point for the application.
* `NewBreak_Church.py`: Implements the main home page for the church, showcasing general information and branding.
* `top.py`: An empty file, potentially a placeholder for future features or modules.
* `users.db`: The **SQLite** database file, automatically created upon the first run of `login.py` to store user credentials securely.
* `*.jpg`: Various image assets utilized throughout the application's different sections.

---

## 🔗 Dependencies

* **Python 3.x**
* **tkinter** (standard Python library, usually bundled with Python)
* **Pillow** (PIL Fork) - Install via `pip install Pillow`
* **sqlite3** (standard Python library for seamless database operations)

---

## 🤝 Contributing

We welcome contributions to enhance the NewBreak Church Application! If you'd like to contribute, please follow these steps:

1.  **Fork** the repository.
2.  **Create a new branch**: `git checkout -b feature/your-feature-name`
3.  **Make your changes**.
4.  **Commit your changes**: `git commit -m 'Add new feature'`
5.  **Push to the branch**: `git push origin feature/your-feature-name`
6.  **Open a Pull Request**.

---

## 👥 Our Project Team

### 🧠 Muqadas Jamil
*Role:* **Team Leader**

### 🎨 Hamza Noor
*Role:* **Frontend Developer**

### 🧾 Fayzan
*Role:* **UI/UX Designer**

### 📚 Iman
*Role:* **Documentation Specialist**

### 🛠️ Hammad Khan
*Role:* **Backend Developer (SQL)**
