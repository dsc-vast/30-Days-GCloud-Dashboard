<template>
  <div id="app">
    <table>
      <tr>
        <th>ID</th>
        <th class="header" v-on:click="sortedName()">Name</th>
        <th class="header" v-on:click="sortedQuests()">Quests Completed</th>
        <th>Last Completed</th>
      </tr>
      <tr v-for="item in detail" :key="item.id">
        <th>{{ item.id }}</th>
        <th>{{ item.name }}</th>
        <th>{{ item.questscompleted }}</th>
        <th>{{ item.last }}</th>
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
      detail: '',
      status: 'name'
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
      if(! (this.status === 'quest') ){
        var data = eval(this.detail);
        var results = data;
        results.sort(function(a,b){
          if(a.questscompleted == b.questscompleted)
            return 0;
          if(a.questscompleted < b.questscompleted)
            return -1;
          if(a.questscompleted > b.questscompleted)
            return 1;
        });
        this.detail = results;
        this.status = 'quest';
      }
      else{
        this.detail = this.detail.reverse();
      }
      this.$forceUpdate();
    },
    sortedName(){
      if(! (this.status === 'name') ){
        var data = eval(this.detail);
        var results = data;
        results.sort(function(a,b){
          if(a.name.toLowerCase() == b.name.toLowerCase())
            return 0;
          if(a.name.toLowerCase() < b.name.toLowerCase())
            return -1;
          if(a.name.toLowerCase() > b.name.toLowerCase())
            return 1;
        });
      this.detail = results;
      this.status = 'name';
      }
      else{
        this.detail = this.detail.reverse();
      }
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
  margin-top: 5px;
}
table{
  border-collapse: collapse;
  border-spacing: 0;
  width: 98%;
  border: 2px solid black;
  margin: 1%;
}

th, td{
  text-align: left;
  padding: 8px;
}

tr{
  border: 1px solid black;
}
tr:nth-child(odd){
  background-color: #0C0C1E;
  color: white;
}

tr:nth-child(even){
  background-color: #1B2E3C;
  color: white;
}

.header{
  cursor: pointer;
}
</style>
