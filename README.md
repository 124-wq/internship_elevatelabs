# 🚀 ElevateLabs Internship – Python Projects Collection

This repository contains a collection of **hands-on Python projects** developed during my internship at **ElevateLabs**.
The goal of these projects was to build strong foundations in **core programming, backend development, file handling, automation, data processing, and APIs** by implementing real working applications instead of only theoretical exercises.

Each project focuses on a different practical concept — from command-line utilities to REST APIs and data analysis.

---

## 👩‍💻 What I Learned

Through this internship, I practiced and applied:

* Python fundamentals (loops, functions, conditionals)
* File handling & persistent storage
* Working with external libraries
* Web scraping
* REST API development
* Backend development using Flask
* Data analysis using Pandas
* Visualization using Matplotlib
* Image processing using Pillow

---

## 🧰 Tech Stack

| Category         | Technologies                              |
| ---------------- | ----------------------------------------- |
| Language         | Python 3                                  |
| Backend          | Flask                                     |
| Web Scraping     | Requests, BeautifulSoup                   |
| Data Analysis    | Pandas, Matplotlib                        |
| Image Processing | Pillow (PIL)                              |
| Testing          | Postman                                   |
| Environment      | VS Code, Command Prompt, Jupyter Notebook |

---

## 📂 Projects Included

---

### 🧮 1. Calculator (CLI Application)

A simple interactive command-line calculator that performs arithmetic operations continuously until the user exits.

**Features**

* Addition
* Subtraction
* Multiplication
* Division
* Modulus
* Continuous input loop
* Exit using `x`

**Run**

```bash
python calculator.py
```

---

### 📋 2. To-Do List Manager

A command-line task manager that stores tasks permanently using file handling.

**Features**

* Add tasks
* View tasks
* Delete tasks by number
* Automatic loading of saved tasks
* Persistent storage using a text file
* Uses both memory (lists) and storage (files)

**Concepts Used**

* Lists
* File I/O
* User input handling

**Run**

```bash
python todo_list.py
```

---

### 📰 3. News Headlines Parser (Web Scraper)

A Python script that fetches top news headlines from a website and saves them locally.

**Features**

* Fetch news using a URL
* Parse HTML using BeautifulSoup
* Extract headline text
* Store results in a text file

**Libraries Used**

* requests
* beautifulsoup4

**Run**

```bash
python news.py
```

---

### 🌐 4. REST API using Flask

A backend API that performs CRUD (Create, Read, Update, Delete) operations on users.

**Features**

* Create a user
* View all users
* Update user details
* Delete a user
* JSON responses
* Tested using Postman

**Concepts Used**

* Routing
* HTTP methods (GET, POST, PUT, DELETE)
* JSON handling

**Run**

```bash
python app.py
```

---

### 📊 5. CSV Data Analysis

Data analysis performed in Jupyter Notebook using a dataset.

**Features**

* Load CSV dataset
* Perform grouping using `groupby()`
* Calculate sums and statistics
* Plot graphs

**Libraries Used**

* pandas
* matplotlib

---

### 🌍 6. Flask Portfolio Website

A simple personal portfolio website built using Flask backend.

**Features**

* Web routing
* HTML templates
* Dynamic rendering using Flask

---

### 🖼️ 7. Image Resizer (Pillow)

A Python automation tool that resizes all images in a folder.

**Features**

* Batch image processing
* Resizes images to 100×100
* Saves resized copies to another folder

**Libraries Used**

* Pillow (PIL)

---
### 8. Chatbot using if-else
- Use input/output loops
- Use simple if-elif-else for responses

---
## ⚙️ Requirements

Install dependencies:

```bash
pip install flask requests beautifulsoup4 pandas matplotlib pillow
```

---

## 🚀 How to Run the Repository

### 1. Clone the repository

```bash
git clone https://github.com/124-wq/internship_elevatelabs.git
```

### 2. Move into the project folder

```bash
cd internship_elevatelabs
```

### 3. Run any project

Example:

```bash
python calculator.py
```

---

## 👨‍💻 Author

**Lovely Bisht**

---

## 📄 License

This project is open-source and intended for learning and educational purposes.
