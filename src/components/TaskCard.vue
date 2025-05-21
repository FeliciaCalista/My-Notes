<template>
  <div :class="['task-card', `category-${task.category.toLowerCase()}`, { done: task.status === 'Done', deleted: task.status === 'Deleted' }]">
    
    <div class="task-header">
      <div class="title">{{ task.title }}</div>
      <div class="task-actions" v-if="task.status !== 'Done' && task.status !== 'Deleted'">
        <button @click="$emit('edit-task', task)" title="Edit">✏️</button>
        <button @click="$emit('delete-task', this.task.id)" title="Delete">🗑️</button>
        <button @click="$emit('mark-as-done', task.id)" title="Mark as Done">✅</button>
      </div>
    </div>
    <hr class="divider">
    <div class="bottom">
      <p class="description">{{ truncateDescription(task.description) }}</p>
      <span class="updated">Updated: {{ formatDate(task.last_updated) }}</span>
      <div class="status-label">
        <span :class="`status-${task.status.toLowerCase()}`">{{ task.status }}</span>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  name: 'TaskCard',
  props: {
    task: {
      type: Object,
      required: true
    }
  },
  methods: {
    truncateDescription(desc) {
      return desc.length > 100 ? `${desc.substring(0, 100)}...` : desc;
    },
    formatDate(date) {
      return date 
        ? new Date(date).toLocaleString()  
        : 'N/A';
    }
  }
};
</script>


<style scoped>
.task-card {
  border-radius: 8px;
  padding: 8px 16px; 
  margin-bottom: 12px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  font-family: 'Comic Sans MS';
}
.category-urgent {
  background-color: #FF6164;
}
.category-important {
  background-color: #FFA361;
}
.category-regular {
  background-color: #6186FF;
}
.task-card.done {
  opacity: 0.7;
  background-color: #cccccc;
  pointer-events: none;
}
.task-card.deleted {
  opacity: 0.7;
  background-color: #f1f1f1; 
  pointer-events: none; 
}
.task-card.done .task-actions, .task-card.deleted .task-actions {
  display: none; 
}
.task-actions {
  display: flex;
  flex-direction: row; 
  align-items: center;
  gap: 0.5rem;
}
.task-actions button {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: white;
  border: none;
  cursor: pointer;
  font-size: 1rem;
  padding: 0.5rem;
  margin-top: 7px;
  margin-bottom: 7px;
  border-radius: 0.5rem;
}
.task-header {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between; 
  gap: 1rem;
}
.title {
  font-size: 20px;
  font-weight: bold;
  color: white;
}
.status-label {
  font-size: 14px;
  background-color: rgb(255, 255, 255, 0.3);
  border-radius: 20px;
  color: white;
  margin-top: 5px;
  width: 60px;
  text-align: center;
  margin-top: 10px;
}
.divider {
  color: white;
  margin: 8px 0; 
}
.bottom {
  margin: 0 0 12px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.description {
  color: white;
  font-size: 18px;
  margin-top: 4px;
  margin-bottom: 20px;
}
.updated {
  color: white;
  opacity: 0.7;
  font-size: 10px;
}

</style>