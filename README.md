# About My-Notes

My-Notes is a simple and interactive task management web application built to demonstrate the use of Vue.js (Frontend) and FastAPI + SQL (Backend). This project serves as a learning experience in full-stack web development, especially focusing on modern frontend technologies with Vue 3 and backend API development with FastAPI.

## Use Case Descriptions

### 1. Login & Logout

* The app includes basic authentication simulation.
* No actual user database is used.
* Credentials are hardcoded on the server (FastAPI):
  * Username: admin
  * Password: abcdef

This allows quick access control simulation without the complexity of account management.

### 2. Task Monitoring

* Users can view all tasks for the entire week: Monday to Sunday.
* Tasks are classified into three categoris:
  * Important
  * Urgent
  * Regular
* Users can filter tasks based on these categories
Each task (displayed as a card) includes:
* Title
* Description
* Last Updated Time
* Status (Active, Deleted, Done)
* Actions (Edit, Delete, Mark as Done)
If a specific day has no tasks, a "Task Entry" UI appears to let the user input a new task.
Once a task is marked as Done, it becomes locked and cannot be edited or deleted.

### 3. Task Entry
This section allows users to add a new task or edit an existing one.
Form fields include:
* Title
* Day of the week
* Description
* Day: Monday - Sunday
* Category: Important, Urgent, or Regular
Available actions:
* Save - Adds or updates the task on the server
* Cancel - Returns to the Task Monitoring screen

## Page Setup
### Frontend (Vue 3 + Vite)
1. Navigate to the frontend folder:
```sh
cd my-notes
```

2. Install dependencies:
```sh
npm install
```

3. Start the development server:
```sh
npm run dev
```

### Backend (FastAPI + SQL)
1. Navigate to the backend folder:
```sh
cd my-notes/my-api
```

2. Run the FastAPI server:
```sh
python app.py
```

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Customize configuration

See [Vite Configuration Reference](https://vite.dev/config/).

## License

This project is licensed under the **MIT License** – you are free to use, modify, and distribute this project with attribution.

## Acknowledgements

Special thanks to Grace Devina for her contribution to the frontend development and for designing an attractive user interface. 

## Contact
* Email: fckfelicia04@gmail.com
