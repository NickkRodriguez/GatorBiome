<template>
  <v-app>
    <!-- Navbar -->
    <v-app-bar app color="primary" dark>
      <v-toolbar-title>GatorBiome</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn to="/" text>Home</v-btn>
      <v-btn to="/dashboard" text>Dashboard</v-btn>
    </v-app-bar>

    <!-- Main Content -->
    <v-main>
      <v-container>
        <router-view></router-view>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",
};
</script>

