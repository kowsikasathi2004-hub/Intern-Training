# Final Assessment Project Plan

## App Idea

Task Management Application


## Features

- User authentication
- Create tasks
- Update tasks
- Delete tasks
- View task status


## Data Model

### User Table

- id
- name
- email
- password


### Task Table

- id
- title
- description
- status
- user_id


## API Endpoints

REST APIs:

GET /tasks

POST /tasks

PUT /tasks/{id}

DELETE /tasks/{id}


WebSocket/SSE:

Real-time task updates


## React Screens

Routes:

/login

/dashboard

/tasks

/profile