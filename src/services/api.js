import axios from 'axios';

const API = axios.create({
  baseURL: 'http://localhost:5000',
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  }
});

export const login = (credentials) => {
  return API.post('/login', credentials); 
};

export const getTaskMonitoring = () => {
  return API.get('/taskMonitoring');
};

export const logout = () => {
  return API.post('/logout');
};

export const get_tasks = () => {
  return API.get('/api/tasks');
};

export const add_task = (taskData) => {
  return API.post('/api/tasks', taskData);
};

export const update_task = (task_id, updatedData) => {
  return API.put(`/api/tasks/${task_id}`, updatedData);
};

export const markAsDone = (task_id) => {
  return API.patch(`/api/tasks/${task_id}`, { status: 'Done' });
};

export const delete_task = (task_id) => {
  return API.delete(`/api/tasks/${task_id}`);
};
