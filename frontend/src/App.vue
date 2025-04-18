<template>
  <v-app>
    <!-- Navbar -->
    <v-app-bar app color="primary" dark>
      <v-toolbar-title>GatorBiome</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn to="/" text>Home</v-btn>
      <v-btn to="/visualizations" text>Visualizations</v-btn>
      <!-- <v-btn to="/datasets" text>Datasets</v-btn> -->
      <v-btn to="/models" text>Model Comparison</v-btn>
      <v-btn to="/about" text>About</v-btn>
      <!-- Dashboard hidden for now -->
      <!-- <v-btn to="/dashboard" text>Dashboard</v-btn> -->

      <v-switch
        v-model="darkMode"
        inset
        hide-details
        color="white"
        :label="darkMode ? 'Dark' : 'Light'"
        class="ml-6"
      />
    </v-app-bar>

    <!-- Main Content -->
    <v-main>
      <v-container>
        <router-view />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      darkMode: false,
    };
  },
  watch: {
    darkMode(val) {
      this.$vuetify.theme.global.name = val ? 'dark' : 'light';
      localStorage.setItem("darkMode", val);
    },
  },
  mounted() {
    const saved = localStorage.getItem("darkMode");
    this.darkMode = saved === null
      ? window.matchMedia('(prefers-color-scheme: dark)').matches
      : saved === "true";

    this.$vuetify.theme.global.name = this.darkMode ? 'dark' : 'light';
  },
};
</script>

<style>
.v-btn {
  text-transform: none;
}
</style>
