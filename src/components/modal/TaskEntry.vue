<template>
  <transition name="modal">
    <div class="modal-backdrop" @click.self="close">
      <div class="modal">
        <h2>{{ isEdit ? 'Edit Task' : 'Add Task' }}</h2>
        
        <form @submit.prevent="submit">
          <div class="form-group">
            <label>Title</label>
            <input v-model="form.title" required placeholder="Task title" />
          </div>
          
          <div class="form-group">
            <label>Description</label>
            <textarea v-model="form.description" placeholder="Task description"></textarea>
          </div>
          
          <div class="form-group">
            <label>Day</label>
            <select v-model="form.day" :disabled="isEdit" required>
              <option v-for="day in days" :value="day" :key="day">{{ day }}</option>
            </select>
          </div>
          
          <div class="form-group">
            <label>Category</label>
            <select v-model="form.category" required>
              <option value="Important">Important</option>
              <option value="Urgent">Urgent</option>
              <option value="Regular">Regular</option>
            </select>
          </div>
          
          <div class="btn-row">
            <button class="btn-cancel" type="button" @click="close">Cancel</button>
            <button class="btn-update" type="submit">{{ isEdit ? 'Update' : 'Add' }}</button>
          </div>
        </form>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  props: {
    taskData: {
      type: Object,
      default: null
    },
    isEdit: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      days: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
      form: {
        title: '',
        description: '',
        day: 'Monday',
        category: 'Regular'
      }
    }
  },
  created() {
    if (this.taskData) {
      this.form = { ...this.taskData }
    }
  },
  methods: {
    submit() {
      this.$emit('save-task', this.form)
      this.close()
    },
    close() {
      this.$emit('close')
    }
  }
}
</script>

<style scoped>
.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  font-family: 'Comic Sans MS', cursive, sans-serif;
}

.modal {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  width: 90%;
  max-width: 500px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.form-group {
  margin-bottom: 1rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
}

.form-group input,
.form-group textarea,
.form-group select {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.btn-row {
  display: flex;
  justify-content: flex-end;
  gap: 0.5rem;
  margin-top: 1rem;
}

/* Transition effects */
.modal-enter-active, .modal-leave-active {
  transition: opacity 0.3s;
}
.modal-enter, .modal-leave-to {
  opacity: 0;
}

.btn-cancel {
  background-color: #ff5f8d; 
  color: white; 
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-family: 'Comic Sans MS', cursive, sans-serif; /* Comic Sans */
  font-size: 1rem;
}

.btn-cancel:hover {
  background-color: #e04c78; 
}

.btn-update {
  background-color: #4CAF50; 
  color: white; 
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-family: 'Comic Sans MS', cursive, sans-serif; 
  font-size: 1rem;
}

.btn-update:hover {
  background-color: #388e3c; 
}
</style>