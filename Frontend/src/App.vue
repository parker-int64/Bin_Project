<script setup>
import { RouterView, RouterLink } from 'vue-router';
</script>

<template>
  <v-app id="dashboard">
    <v-layout>
      <v-navigation-drawer class="pt-4" color="grey-lighten-3" model-value expand-on-hover rail>
        <v-list density="compact" nav>
          <router-link to="/"><v-list-item prepend-icon="mdi-home" title="面板" value="home"></v-list-item></router-link>
          <router-link to="/profile"> <v-list-item prepend-icon="mdi-account" title="账号"
              value="account"></v-list-item></router-link>
          <router-link to="/settings"><v-list-item prepend-icon="mdi-cog" title="设置"
              value="settings"></v-list-item></router-link>
        </v-list>
      </v-navigation-drawer>

      <v-main>
        <router-view></router-view>
      </v-main>
    </v-layout>

  </v-app>
</template>

<style scoped>
/* cancel the default style of router */
.router-link-active {
  text-decoration: none;
  color: #474646;
}

a {
  text-decoration: none;
  color: #121212;
}
</style>
