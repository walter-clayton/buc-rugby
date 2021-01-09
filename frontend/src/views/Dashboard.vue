<template>
  <div class="home">
    <div>
      <b-container class="mt-5 bg-dark text-white">
        <br><br>
          <alert :message="message" v-if="showMessage"/>
          <div class="d-flex justify-content-around p-4 bg-white">
            <button type="button" class="btn btn-success btn-lg" v-b-modal.add-data>Add Data</button>
            <button type="button" class="btn btn-warning btn-lg">Submit All Data To Database</button>
            <router-link to="/alldata"><button type="button" class="btn btn-danger btn-lg">Show me all of the data</button></router-link>
          </div>
          <b-modal id="add-data" title="Add Data" ref="addTestModal" hide-footer>
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
          <b-modal id="update-data" title="Update Data" ref="editTestModal" hide-footer>
            <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" >
              <b-form-group id="input-group-1" label="Your First Name:" label-for="input-1">
                <b-form-input
                  id="input-1"
                  v-model="editForm.firstName"
                  required
                  placeholder="Enter First Name"
                ></b-form-input>
              </b-form-group>
              <b-form-group id="input-group-2" label="Your Last Name:" label-for="input-2">
                <b-form-input
                  id="input-2"
                  v-model="editForm.lastName"
                  required
                  placeholder="Enter Last Name"
                ></b-form-input>
              </b-form-group>
              <b-button type="submit" variant="primary">Submit</b-button>
              <b-button type="reset" variant="danger">Reset</b-button>
            </b-form>
          </b-modal>
        <table class="table table-hover text-white">
          <thead>
            <tr>
              <th scope="col">First Name</th>
              <th scope="col">Last Name</th>
              <th scope="col">EDIT</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(test, index) in tests" :key="index">
              <td>{{ test.firstName }}</td>
              <td>{{ test.lastName }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm" v-b-modal.update-data @click.passive="editTest(test)">Update</button>
                  <button type="button" class="btn btn-danger btn-sm" @click.passive="onDeleteTest(test)">Delete</button>
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
import Alert from '@/components/modules/Alert.vue';

export default {
  name: "Home",
  components: {
    alert: Alert,
  },
  data() {
    return {
      tests: [],
      form: {
        id: '',
        firstName: '',
        lastName: ''
      },
      editForm: {
        id: '',
        firstName: '',
        lastName: '',
      },
      message: '',
      showMessage: false,
    };
  },
  methods: {
    initForm() {
      this.form.id = '';
      this.form.firstName = '';
      this.form.lastName = '';
      this.editForm.id = '';
      this.editForm.firstName = '';
      this.editForm.lastName = ''; 
    },
    getTests() {
      const path = 'http://localhost:5000/dashboard';
      axios.get(path)
        .then((res) => {
          this.tests = res.data.tests;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addTest(payload) {
      const path = 'http://localhost:5000/dashboard';
      axios.post(path, payload)
        .then(() => {
          this.getTests();
          this.message = 'Data added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getTests();
        });
    },
    onSubmit(evt) {
      evt.preventDefault();
        this.$refs.addTestModal.hide();
        alert(JSON.stringify(this.form));
        const payload = {
          id: this.form.id,
          firstName: this.form.firstName,
          lastName: this.form.lastName
        };
        this.addTest(payload);
        this.getTests();
    },
    onReset(evt) {
      evt.preventDefault()
      this.$refs.addTestModal.hide();
      this.initForm();
    },
    editTest(test){
      this.editForm = test;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editTestModal.hide();
      const payload = {
        id: this.editForm.id,
        firstName: this.editForm.firstName,
        lastName: this.editForm.lastName,
      };
      this.updateTest(payload, this.editForm.id);
    },
    updateTest(payload, testID) {
      const path = `http://localhost:5000/dashboard/${testID}`;
      axios.put(path, payload)
        .then(() => {
          this.getTests();
          this.message = 'Data updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getTests();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editTestModal.hide();
      this.initForm();
      this.getTests();
    },
    removeTest(testID) {
      const path = `http://localhost:5000/dashboard/${testID}`;
      axios.delete(path)
        .then(() => {
          this.getTests();
          this.message = 'Test removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getTests();
        });
    },
    onDeleteTest(test) {
      this.removeTest(test.id);
    },
  },
  created() {
    this.getTests();
  },
};
</script>