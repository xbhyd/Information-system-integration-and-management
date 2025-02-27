<template>
  <div id="login_box">
    <h2>欢迎来到武汉大学招聘信息收集网站</h2>
    <form @submit.prevent="handleLogin">
    <div id="input_box">
      <input type="text" v-model="username" placeholder="请输入用户名" />
    </div>
    <div class="input_box">
      <input type="password" v-model="password" placeholder="请输入密码" />
    </div>
    <button @click="handleLogin">登录</button><br>
    </form>
    <p v-if="message" :class="{ 'error': errorMessage }">{{ message }}</p>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return{
      username:'',
      password:'',
      message: '',
      errorMessage: false
    };
  },
  methods: {
    async handleLogin() {
      try {
        const response = await axios.post('http://localhost:2020/login', {
          username: this.username,
          password: this.password,
        },{
          headers: {
            'Content-Type': 'application/json'
          }
        });
        if (response.data === true) {
          this.message = '登录成功！';
          this.errorMessage = false;
          this.$router.push({name: 'mapcomponent'});
        } else {
          this.message = '用户名或密码错误';
          this.errorMessage = true;
        }
      } catch (error) {
        console.error('登录失败:', error);
        this.message = '登录失败，请稍后再试';
        this.errorMessage = true;
      }
    },
  },
};
</script>

<style scoped>
body {
  background: url('https://www.geosceneonline.cn/static/introduce.35141283.jpg') no-repeat;
  background-size: 100% 130%;
}

#login_box {
  width: 20%;
  height: 400px;
  background-color: rgba(0, 0, 0, 0.23);
  margin: auto;
  margin-top: 10%;
  text-align: center;
  border-radius: 10px;
  padding: 50px 50px;
}

h2 {
  color: #ffffff90;
  margin-top: 5%;
}

#input_box {
  margin-top: 5%;
}

span {
  color: #fff;
}

input {
  border: 0;
  width: 60%;
  font-size: 15px;
  color: #fff;
  background: transparent;
  border-bottom: 2px solid #fff;
  padding: 5px 10px;
  outline: none;
  margin-top: 10px;
}

button {
  margin-top: 50px;
  width: 60%;
  height: 30px;
  border-radius: 10px;
  border: 0;
  color: #fff;
  text-align: center;
  line-height: 30px;
  font-size: 15px;
  background-image: linear-gradient(to right, #30cfd0, #330867);
}

#sign_up {
  margin-top: 45%;
  margin-left: 60%;
}

a {
  color: #b94648;
}
</style>
