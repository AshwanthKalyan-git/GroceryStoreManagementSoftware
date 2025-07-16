# Grocery Store Management Software

A simple Python-based store management system that handles product inventory using SQLite. Designed for basic CRUD operations and quick integration into small retail environments.

---

## Features

- Add products to the store database
- Persistent storage with SQLite (`store.db`)
- Lightweight, Python-based script (`addtodb.py`)
- Simple and readable codebase — ideal for learning or extending

---

## Tech Stack

- **Language:** Python 3.x
- **Database:** SQLite (`store.db`)
- **Files:**
  - `addtodb.py` — main script to manage the database
  - `store.db` — SQLite database file
  - `store.db-journal` — temporary journal file (auto-managed by SQLite)
  - `Empty.txt` — placeholder/test file

---

## Requirements

Make sure Python is installed on your system.

### Install Dependencies
No external libraries are required — uses Python's built-in `sqlite3` module.

---

## How to Run

1. **Clone the repository**

```bash
git clone https://github.com/AshwanthKalyan-git/GroceryStoreManagementSoftware.git
cd GroceryStoreManagementSoftware
