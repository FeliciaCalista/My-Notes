<template>
  <div class="container">
    <header class="header">
      <h1>Task Manager</h1>
      <button class="logout-btn" @click="logout" title="Logout">↩</button>
    </header>
    
    <div class="filter-bar">
      <label class="label-important"><input type="checkbox" v-model="filters.category" value="Important" /> Important</label>
      <label class="label-urgent"><input type="checkbox" v-model="filters.category" value="Urgent" /> Urgent</label>
      <label class="label-regular"><input type="checkbox" v-model="filters.category" value="Regular" /> Regular</label>
    </div>

    <div class="columns-container">
      <TaskColumn
        v-for="day in days"
        :key="day"
        :day-name="day"
        :tasks="tasksByDay(day)"
        @add-task="openAddModal"
        @edit-task="openEditModal"  
        @delete-task="deleteTask"    
        @mark-as-done="completeTask" 
      />

    </div>

    <div class="pop-up">
      <TaskEntry
        v-if="modalVisible"
        :task-data="form"
        :is-edit="isEdit"
        @save-task="saveTaskFromChild"  
        @close="modalVisible = false"
      />

    </div>
  </div>
</template>

<script>
import TaskColumn from '@/components/TaskColumn.vue'
import TaskEntry from '@/components/modal/TaskEntry.vue'

import { 
  get_tasks, 
  add_task, 
  update_task, 
  markAsDone, 
  delete_task,
  logout 
} from '../services/api';

export default {
  components: {
    TaskColumn,
    TaskEntry
  },
  data() {
    return {
      tasks: [],
      days: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
      filters: {
        category: [],
        day: ''
      },
      modalVisible: false,
      isEdit: false,
      form: {
        title: '',
        description: '',
        day: 'Monday',
        category: 'Regular',
        status: 'Active'
      }
    }
  },
  props: {
    taskData: Object
  },
  computed: {
    filteredTasks() {
      return this.tasks.filter(task => {
        const categoryMatch = this.filters.category.length === 0 || 
          this.filters.category.includes(task.category)
        const dayMatch = !this.filters.day || task.day === this.filters.day
        return categoryMatch && dayMatch && task.status !== 'Deleted'
      })
    }
  },
  methods: {
    async fetchTasks() {
      try {
        const response = await get_tasks();
        this.tasks = response.data;
      } catch (error) {
        console.error('Error fetching tasks:', error);
        alert('Failed to load tasks');
      }
    },

    async saveTaskFromChild(emittedForm) {
      this.form = { ...emittedForm }; 
      await this.saveTask();          
    },

    async saveTask() {
      if (!this.form.title.trim()) {
        alert('Title is required');
        return;
      }

      try {
        if (this.isEdit) {
          await update_task(this.form.id, this.form);
        } else {
          await add_task(this.form);
        }
        this.modalVisible = false;
        await this.fetchTasks();
      } catch (error) {
        console.error('Error saving task:', error);
        alert('Failed to save task');
      }
    },

    async deleteTask(id) {
      const task = this.tasks.find(t => t.id === id);
      if (task.status === 'Done') {
        alert('Completed tasks cannot be deleted');
        return;
      }

      if (!confirm('Are you sure?')) return;

      try {
        await delete_task(id);
        await this.fetchTasks();
      } catch (error) {
        console.error('Error deleting task:', error);
        alert('Failed to delete task');
      }
    },

    async completeTask(id) {
      try {
        await markAsDone(id);
        const task = this.filteredTasks.find(t => t.id === id);
        if (task) {
          task.status = 'Done';
          task.last_updated = new Date().toISOString(); // optional
        }
      } catch (error) {
        console.error('Error completing task:', error);
        alert('Failed to complete task');
      }
    },

    tasksByDay(day) {
      return this.filteredTasks.filter(task => task.day === day);
    },

    openAddModal(day) {
      this.resetForm();
      this.form.day = day;
      this.modalVisible = true;
      this.isEdit = false;
    },

    openEditModal(task) {
      if (task.status === 'Done') {
        alert("Can't edit completed tasks");
        return;
      }
      this.form = { ...task };
      this.isEdit = true;
      this.modalVisible = true;
    },

    truncateDescription(desc) {
      return desc.length > 100 ? desc.substring(0, 100) + '...' : desc;
    },

    formatDate(dateString) {
      if (!dateString) return '';
      const date = new Date(dateString);
      return date.toLocaleString();
    },

    async logout() {
      try {
        await logout();
        window.location.href = '/login';
      } catch (error) {
        console.error('Logout error:', error);
        window.location.href = '/login';
      }
    },

    resetForm() {
      this.form = {
        title: '',
        description: '',
        day: 'Monday',
        category: 'Regular',
        status: 'Active'
      };
    }
  },
  mounted() {
    this.fetchTasks()
  }
}
</script>

<style scoped>

*,
*::before,
*::after {
  box-sizing: border-box;
}

.container {
  display: flex;
  flex-direction: column;
  margin: auto;
  padding: 20px;
  font-family: 'Comic Sans MS', cursive, sans-serif;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;  
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 80px; 
  padding: 0 20px;

}

.header h1 {
  font-size: 2rem;
  color: white;
  white-space: nowrap; 
  width: auto;         
}

.filter-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 20px;
  padding: 10px;
  background: #f5f5f5;
  border-radius: 5px;
  flex-shrink: 0;
  margin-top: 80px;
  margin-bottom: 5px;
}

.category-filters label {
  margin-right: 15px;
  font-weight: 500;
  justify-content: center;
}

.label-important {
  color: #FFA361;
}

.label-urgent {
  color: #FF6164;
}

.label-regular {
  color: #6186FF;
}

.logout-btn {
  background: none;
  width: 100px;
  border: none;
  cursor: pointer;
  font-size: 2rem;
  color: white;
  padding: 5px;
  margin-bottom: 7px;
}


.columns-container {
  display: flex;
  gap: 16px; 
  padding: 16px;
  overflow-x: auto; 
  width: 100%;
  scrollbar-width: thin; 
  flex-grow: 1;
}

/* Style scrollbar (opsional) */
.columns-container::-webkit-scrollbar {
  height: 8px;
}
.columns-container::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 4px;
}
</style>
