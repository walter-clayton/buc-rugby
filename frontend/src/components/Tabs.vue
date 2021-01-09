<template>
        <b-nav tabs>
        <b-nav-item active>
          <router-link to="/dashboard">Dashboard</router-link>
        </b-nav-item>
        <b-nav-item>
          <router-link to="/alldata">Go to all data</router-link>
        </b-nav-item>
      </b-nav>
</template>

<script>
export default {
  name: "Tabs",
}
</script>