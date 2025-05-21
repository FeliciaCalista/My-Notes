<template>
    <div class="task-column">
        <div class="column-header">
          <h2>{{ dayName }}</h2>
          <div class="header-actions">
            <button class="add-btn" @click="$emit('add-task', dayName)">✚</button>
            <span class="task-count">
              {{ filteredTasks.length }} {{ filteredTasks.length === 1 ? 'task' : 'tasks' }}
            </span>
          </div>
        </div>
        <div class="tasks-list">
        <TaskCard
            v-for="task in filteredTasks"
            :key="task.id"
            :task="{
            ...task,
            category: task.category || 'Regular', 
            last_updated: task.last_updated || new Date().toISOString() 
            }"
            @edit-task="$emit('edit-task', task)"
            @delete-task="$emit('delete-task', task.id)"
            @mark-as-done="$emit('mark-as-done', task.id)"
        />
        
        <div v-if="filteredTasks.length === 0" class="empty-state">
            Free from Task
        </div>
        </div>
    </div>
</template>

<script>
import TaskCard from './TaskCard.vue'

export default {
  components: { TaskCard },
  props: {
    dayName: {  
      type: String,
      required: true,
      validator: value => [
        'Monday', 
        'Tuesday', 
        'Wednesday', 
        'Thursday', 
        'Friday', 
        'Saturday', 
        'Sunday'
      ].includes(value)
    },
    tasks: {
      type: Array,
      default: () => [],
      validator: value => value.every(task => 
        task.id && task.title && task.day
      )
    }
  },
  computed: {
    filteredTasks() {
      return this.tasks
        .filter(task => task.day === this.dayName)
        .filter(task => task.status !== 'Deleted') 
        .sort((a, b) => new Date(b.last_updated) - new Date(a.last_updated)) 
    }
  }
}
</script>

<style scoped>
.task-column {
  min-width: 280px; 
  flex-shrink: 0; 
  background: #f5f5f5;
  border-radius: 8px;
  padding: 12px;
  font-family: 'Comic Sans MS', cursive, sans-serif;
}

.column-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
  padding-bottom: 10px;
  border-bottom: 1px solid #dee2e6;
}

.header-actions {
  display: flex;
  align-items: center; 
  gap: 0.5rem;
}


.column-header h2 {
  margin: 0;
  font-size: 1.1rem;
  color: #333;
}   
.task-count {
  background: #e9ecef;
  padding: 3px 3px;
  border-radius: 12px;
  font-size: 0.8rem;
}
.add-btn {
  background: #e9ecef;
  padding: 3px 3px;
  margin-bottom: 19px;
  background-color: #ff5f8d;
  font-size: 0.8rem;
  width: 30px;
}
.add-btn:hover {
  background-color: #e04c78;
}
.tasks-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.empty-state {
  color: #6c757d;
  font-size: 0.9rem;
  text-align: center;
  padding: 10px;
  font-style: italic;
}
</style>