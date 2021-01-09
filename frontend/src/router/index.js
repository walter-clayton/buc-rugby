import Vue from "vue";
import VueRouter from "vue-router";
import Dashboard from "@/views/Dashboard.vue";
import About from "@/views/About.vue";
import AllData from "@/views/AllData.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/dashboard",
    name: "Dashboard",
    component: Dashboard
  },
  {
    path: "/about",
    name: "About",
    component: About
  },
  {
    path: "/alldata",
    name: "AllData",
    component: AllData
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
