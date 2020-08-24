<template>
  <div class="home">
    <div>
  <b-nav tabs>
    <b-nav-item active>Dashboard</b-nav-item>
    <b-nav-item>Training Programs</b-nav-item>
  </b-nav>
  <b-container class="mt-5 bg-dark text-white">
  <br><br>
    <button type="button" class="btn btn-success btn-sm" v-b-modal.modal-1>Add Data</button>
        <b-modal id="modal-1" title="Testing Data" hide-footer>
    <b-form @submit="onSubmit" @reset="onReset" >
      <b-form-group id="input-group-1" label="Your First Name:" label-for="input-1">
        <b-form-input
          id="input-1"
          v-model="form.firstName"
          required
          placeholder="Enter First Name"
        ></b-form-input>
      </b-form-group>
      <b-form-group id="input-group-2" label="Your Last Name:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="form.lastName"
          required
          placeholder="Enter Last Name"
        ></b-form-input>
      </b-form-group>
      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
        </b-modal>
    <b-card class="mt-3" header="Form Data Result">
      <pre class="m-0">{{ form }}</pre>
    </b-card>
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
import axios from 'axios';

export default {
  name: "Home",
  components: {
  },
  data() {
    return {
      tests: [],
      form: {
        firstName: '',
        lastName: ''
      },
    };
  },
  methods: {
    onReset(evt) {
      evt.preventDefault()
      this.form.firstName = ''
      this.form.lastName = ''
    },
    getTests() {
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
    postTests(payload) {
      const path = 'http://localhost:5000/';
      axios.post(path, payload)
        .then(() => {
          this.getTests();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getTests();
        });
    },
    initForm() {
      this.form.firstName = '';
      this.form.lastName = '';
    },
    onSubmit(evt) {
        evt.preventDefault();
        alert(JSON.stringify(this.form));
        const payload = {
          firstName: this.form.firstName,
          lastName: this.form.lastName
        };
        this.postTests(payload);
        this.getTests();
    },
  },
  created() {
    this.getTests();
  },
};
</script>