<template>
    <div>
      <h1>Power BI Link Checker</h1>
      <button @click="checkLinks">Check Links</button>
      <ul>
        <li v-for="(status, url) in linkStatus" :key="url">
          {{ url }} - {{ status }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'LinkChecker',
    data() {
      return {
        linkStatus: {}
      };
    },
    methods: {
      async checkLinks() {
        try {
          const response = await axios.get('http://localhost:5000/api/check_links');
          this.linkStatus = response.data;
        } catch (error) {
          console.error(error);
        }
      }
    }
  }
  </script>
  
  <style scoped>
  h1 {
    font-size: 2em;
  }
  button {
    margin: 20px;
    padding: 10px 20px;
    font-size: 1em;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    margin: 5px 0;
  }
  </style>
  