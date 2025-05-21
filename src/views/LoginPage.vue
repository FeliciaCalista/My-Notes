<template>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <div class="container">
    <header class="header">
      <h1>My Notes</h1>
    </header>

    <main class="login-box">
      <h2>Login</h2>
      <form @submit.prevent="handleLogin">
        <label for="userid">User ID</label>
        <input type="text" id="userid" v-model="userid" required />

        <label for="password">Password</label>
        <input type="password" id="password" v-model="password" required />

        <button type="submit">Log In</button>
      </form>
    </main>

    <footer class="footer">"The future belongs to those who believe in the beauty of their dreams."</footer>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      userid: '',
      password: ''
    };
  },
  methods: {
    async handleLogin() {
      try {
        const response = await axios.post(
          'http://localhost:5000/login',
          {
            username: this.userid,
            password: this.password
          },
          { withCredentials: true }
        );

        localStorage.setItem('isAuthenticated', 'true'); 
          this.$router.push({ 
          name: 'TaskMonitoring', 
          query: { from: 'login' } 
        });
    
      } catch (error) {
        alert("Invalid login");
      }
    }
  }
};
</script>


<style>
*,
*::before,
*::after {
  box-sizing: border-box;
}
.container {
  min-height: calc(100vh - 120px);
  padding-top: 60px; 
  padding-bottom: 60px; 
  box-sizing: border-box;
  overflow-y: auto;
  height: 100vh;
  width: 100vw;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #f8f9fc;
  font-family: 'Comic Sans MS', cursive, sans-serif;
}

.header {
  background-color: #7c5cf5;
  color: white;
  padding: 15px 20px;
  text-align: center;
  width: 100%;
  position: fixed;
  left: 0;
  right: 0;
  top: 0;
}

.header h1 {
  margin: 0;
  font-size: 2.5rem;
  text-align: center;
}

.login-box {
  box-sizing: border-box;
  flex: 1;
  width: 100%;
  max-width: 600px; 
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 20px;
}


.login-box h2 {
  font-size: 2rem;
  font-weight: bold;
  margin-bottom: 40px;
  color: #333;
}

form {
  box-sizing: border-box;
  width: 100%;
  max-width: 100%; 
  padding: 20px;
  background: white;
  border-radius: 20px;
  box-shadow: 0 5px 25px rgba(0,0,0,0.1);
}

label {
  margin: 15px 10px 0;
  font-weight: bold;
  font-size: 1.1rem;
  color: #555;
}

input[type='text'],
input[type='password'] {
  width: 100%;
  padding: 15px;
  margin-top: 8px;
  margin-bottom: 20px;
  border: 2px solid #ddd;
  border-radius: 10px;
  font-size: 1rem;
  background-color: #fff;
  transition: border-color 0.3s;
}

input[type='text']:focus,
input[type='password']:focus {
  border-color: #7c5cf5;
  outline: none;
}

button {
  background-color: #ff5f8d;
  color: white;
  border: none;
  padding: 15px;
  border-radius: 10px;
  font-size: 1.1rem;
  font-weight: bold;
  cursor: pointer;
  margin-top: 20px;
  transition: background-color 0.3s;
  width: 100%;
  font-family: inherit;
}

button:hover {
  background-color: #e04c78;
}

.footer {
  padding: 20px;
  text-align: center;
  color: white;
  width: 100%;
  background-color: #7c5cf5; 
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
}

html {
  font-size: 16px;
}

@media (max-height: 600px) {
  html {
    font-size: 14px;
  }
}
</style>
