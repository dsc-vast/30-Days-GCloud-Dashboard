<template>
  <div id="app">
    <table>
      <tr>
        <th>ID</th>
        <th class="header" v-on:click="sortedName()">Name</th>
        <th class="header" v-on:click="sortedQuests()">Quests Completed</th>
      </tr>
      <tr v-for="item in detail" :key="item.id">
        <th>{{ item.id }}</th>
        <th>{{ item.name }}</th>
        <th>{{ item.questscompleted }}</th>
      </tr>
    </table>
  </div>
</template>

<script>
  import axios from 'axios';
const url = 'http://localhost:5000'; // Supply API url
export default {
  name: 'App',
  components: {
  },
  data: () => {
    return{
      detail: ''
    }
  },
  mounted(){
    var newUrl = url + '/name'; 
    axios
    .get(newUrl)
    .then( (response) => {
      this.detail = response.data
    });
  },
  methods: {
    sortedQuests(){
      var newUrl = url + '/sorted'
      axios
      .get(newUrl)
      .then( (response) => { this.detail = response.data })
      this.$forceUpdate();
    },
    sortedName(){
      var newUrl = url + '/name'
      axios
      .get(newUrl)
      .then( (response) => { this.detail = response.data })
      this.$forceUpdate();

    }
  }
}
</script>

<style>
#app{
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
table{
  border-collapse: collapse;
  border-spacing: 0;
  width: 100%;
  border: 1px solid #ddd;
}

th, td{
  text-align: left;
  padding: 8px;
}

tr:nth-child(even){background-color: #f2f2f2
}

.header{
  cursor: pointer;
}
</style>
