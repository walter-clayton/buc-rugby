<template>
  <div class="about">
    <h1>This the data page</h1>
    <alert :message="message" v-if="showMessage"/>
    <div class="d-flex justify-content-around p-4 bg-white">
      <button type="button" class="btn btn-success btn-lg" v-b-modal.add-data>Add Data</button>
      <button type="button" class="btn btn-warning btn-lg">Submit All Data To Database</button>
      <router-link to="/alldata"><button type="button" class="btn btn-danger btn-lg">Show me all of the data</button></router-link>
    </div>
    <b-modal id="add-data" title="Add Data" ref="addTestModal" hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" >
        <b-form-datepicker id="input-group-1" label="Pick Date" label-for="input-1" v-model="form.date">
        </b-form-datepicker>
        <b-form-group>
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
        <b-form-group id="input-group-3" label="Your Body Fat:" label-for="input-3">
          <b-form-input
            id="input-3"
            v-model="form.bodyFat"
            required
            placeholder="Enter your Body Fat"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="input-group-4" label="Your Body Mass:" label-for="input-4">
          <b-form-input
            id="input-4"
            v-model="form.bodyMass"
            required
            placeholder="Enter your Body Mass"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="input-group-5" label="Your Height:" label-for="input-5">
          <b-form-input
            id="input-5"
            v-model="form.height"
            required
            placeholder="Enter your Height"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="input-group-6" label="Your Position:" label-for="input-6">
          <b-form-input
            id="input-6"
            v-model="form.position"
            required
            placeholder="Enter your Position"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="input-group-7" label="Your 10 Second Sprint:" label-for="input-7">
          <b-form-input
            id="input-7"
            v-model="form.tenSprint"
            required
            placeholder="Enter your 10 Second Sprint"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="input-group-8" label="Your 30 Second Sprint:" label-for="input-8">
          <b-form-input
            id="input-8"
            v-model="form.thirtySprint"
            required
            placeholder="Enter your 30 Second Sprint"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="input-group-9" label="Your 20 Second Sprint:" label-for="input-9">
          <b-form-input
            id="input-9"
            v-model="form.twentySprint"
            required
            placeholder="Enter your 20 Second Sprint"
          ></b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
    <b-modal id="update-data" title="Update Data" ref="editTestModal" hide-footer>
      <input type="text" v-model="editForm.id">
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
        <b-form-group id="input-group-3" label="Your Body Fat:" label-for="input-3">
          <b-form-input
            id="input-3"
            v-model="editForm.bodyFat"
            required
            placeholder="Enter your Body Fat"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="input-group-4" label="Your Body Mass:" label-for="input-4">
          <b-form-input
            id="input-4"
            v-model="editForm.bodyMass"
            required
            placeholder="Enter your Body Mass"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="input-group-5" label="Your Height:" label-for="input-5">
          <b-form-input
            id="input-5"
            v-model="editForm.height"
            required
            placeholder="Enter your Height"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="input-group-6" label="Your Position:" label-for="input-6">
          <b-form-input
            id="input-6"
            v-model="editForm.position"
            required
            placeholder="Enter your Position"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="input-group-7" label="Your 10 Second Sprint:" label-for="input-7">
          <b-form-input
            id="input-7"
            v-model="editForm.tenSprint"
            required
            placeholder="Enter your 10 Second Sprint"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="input-group-8" label="Your 30 Second Sprint:" label-for="input-8">
          <b-form-input
            id="input-8"
            v-model="editForm.thirtySprint"
            required
            placeholder="Enter your 30 Second Sprint"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="input-group-9" label="Your 20 Second Sprint:" label-for="input-9">
          <b-form-input
            id="input-9"
            v-model="editForm.twentySprint"
            required
            placeholder="Enter your 20 Second Sprint"
          ></b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
  <b-container>
    <div class="mt-5">
      <b-input-group size="sm">
        <b-form-input
          id="filter-input"
          v-model="filter"
          type="search"
          placeholder="Type to Search"
        ></b-form-input>
        <b-input-group-append>
          <b-button :disabled="!filter" @click="filter = ''">Clear</b-button>
        </b-input-group-append>
      </b-input-group>
      <b-table
      sortable
      striped
      :filter="filter"
      :filter-included-fields="filterOn"
      :items="tests"
      :fields="fields"
      class="bg-dark text-white">
        <template #cell(actions)="test">
            <b-button v-b-modal.update-data @click="editTest(test)" variant="primary" size="sm">Edit</b-button>
            <b-button @click="onDeleteTest(test)" v-b-modal="'edit-modal'" variant="danger" size="sm">Delete</b-button>
        </template>
      </b-table>
    </div>
  </b-container>
  </div>
</template>
<script>
import axios from 'axios';
import Alert from '@/components/modules/Alert.vue';

export default {
  name: "AllData",
  components: {
    alert: Alert,
  },
  data() {
    return {
      totalRows: 1,
      sortBy: '',
      filter: null,
      filterOn: [],
      tests: [],
      fields: [
        {
          key: 'id',
          sortable: true,
        },
        {
          key: 'date',
          sortable: true,
        },
        {
          key: 'firstName',
          sortable: true,
        },
        {
          key: 'lastName',
          sortable: true
        },
        {
          key: 'bodyFat',
          sortable: true
        },
        {
          key: 'height',
          sortable: true
        },
        {
          key: 'position',
          sortable: true
        },
        {
          key: 'tenSprint',
          sortable: true
        },
        {
          key: 'twentySprint',
          sortable: true
        },
        {
          key: 'thirtySprint',
          sortable: true
        },
        'actions',
      ],
      form: {
        id: '',
        date: '',
        firstName: '',
        lastName: '',
        bodyFat: '',
        bodyMass: '',
        heigth: '',
        position: '',
        tenSprint: '',
        thirtySprint: '',
        twentySprint: '',
  },
      editForm: {
        id: '',
        date: '',
        firstName: '',
        lastName: '',
        bodyFat: '',
        bodyMass: '',
        heigth: '',
        position: '',
        tenSprint: '',
        thirtySprint: '',
        twentySprint: '',
      },
      message: '',
      showMessage: false,
    };
  },
  computed: {
    sortOptions() {
      // Create an options list from our fields
      return this.tests
        .filter(f => f.sortable)
        .map(f => {
          return { text: f.label, value: f.key }
        })
    }
  },
  methods: {
    initForm() {
      this.form.date = '';
      this.form.firstName = '';
      this.form.lastName = '';
      this.form.bodyFat = '';
      this.form.bodyMass = '';
      this.form.height = '';
      this.form.position = '';
      this.form.tenSprint = '';
      this.form.thirtySprint = '';
      this.form.twentySprint = '';
      this.editForm.id = '';
      this.editForm.date = '';
      this.editForm.firstName = '';
      this.editForm.lastName = '';
      this.editForm.bodyFat = '';
      this.editForm.bodyMass = '';
      this.editForm.height = '';
      this.editForm.position = '';
      this.editForm.tenSprint = '';
      this.editForm.thirtySprint = '';
      this.editForm.twentySprint = '';
    },
    getTests() {
      const path = 'http://127.0.0.1:5000/alldata';
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
      const path = 'http://127.0.0.1:5000/alldata';
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
          date: this.form.date,
          firstName: this.form.firstName,
          lastName: this.form.lastName,
          bodyFat: this.form.bodyFat,
          bodyMass: this.form.bodyMass,
          height: this.form.bodyMass,
          position: this.form.position,
          tenSprint: this.form.tenSprint,
          thirtySprint: this.form.thirtySprint,
          twentySprint: this.form.twentySprint,
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
      console.log(this.form.date)
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editTestModal.hide();
      const payload = {
          id: this.form.id,
          date: this.form.date,
          firstName: this.form.firstName,
          lastName: this.form.lastName,
          bodyFat: this.form.bodyFat,
          bodyMass: this.form.bodyMass,
          height: this.form.bodyMass,
          position: this.form.position,
          tenSprint: this.form.tenSprint,
          thirtySprint: this.form.thirtySprint,
          twentySprint: this.form.twentySprint,
      };
      this.updateTest(payload, this.editForm.id);
    },
    updateTest(payload, testID) {
      const path = `http://127.0.0.1:5000/alldata/${testID}`;
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
      const path = `http://127.0.0.1:5000/alldata/${testID}`;
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