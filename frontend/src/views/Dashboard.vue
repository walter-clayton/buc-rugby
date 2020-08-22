<template>
  <div class="home">
    <div>
  <b-nav tabs>
    <b-nav-item active>Dashboard</b-nav-item>
    <b-nav-item>Training Programs</b-nav-item>
  </b-nav>
  <b-container class="mt-5 bg-dark text-white">
  <Testing />
  <p>{{ msg }}</p>
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
      msg: '',
    };
  },
    methods: {
    getMessage() {
      const path = 'http://localhost:5000/';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
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