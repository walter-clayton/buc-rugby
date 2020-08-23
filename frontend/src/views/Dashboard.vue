<template>
  <div class="home">
    <div>
  <b-nav tabs>
    <b-nav-item active>Dashboard</b-nav-item>
    <b-nav-item>Training Programs</b-nav-item>
  </b-nav>
  <b-container class="mt-5 bg-dark text-white">
  <Testing />
  <br><br>
      <table class="table table-hover text-white">
      <thead>
        <tr>
          <th scope="col">First Name</th>
          <th scope="col">Last Name</th>
          <th scope="col"></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(test, index) in tests" :key="index">
          <td>{{ test.firstName }}</td>
          <td>{{ test.lastName }}</td>
          <td>
            <div class="btn-group" role="group">
              <button type="button" class="btn btn-warning btn-sm">Update</button>
              <button type="button" class="btn btn-danger btn-sm">Delete</button>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </b-container>
</div>
  </div>
</template>

<script>
import Testing from "@/components/modules/Testing.vue";
import axios from 'axios';

export default {
  name: "Home",
  components: {
    Testing,
  },
  data() {
    return {
      tests: [],
    };
  },
    methods: {
    getMessage() {
      const path = 'http://localhost:5000/';
      axios.get(path)
        .then((res) => {
          this.tests = res.data.tests;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>