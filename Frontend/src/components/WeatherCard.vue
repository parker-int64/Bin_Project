<script setup>


</script>

<template>
  <v-card class="mx-auto" max-width="368">
    <v-card-item title="深圳">
      <template v-slot:subtitle>
        <v-icon class="me-1 pb-1" color="error" icon="mdi-alert" size="18"></v-icon>

        超强台风警告
      </template>
    </v-card-item>

    <v-card-text class="py-0">
      <v-row align="center" no-gutters>
        <v-col class="text-h2" cols="6">
          23&deg;C
        </v-col>

        <v-col class="text-right" cols="6">
          <v-icon color="error" icon="mdi-weather-hurricane" size="88"></v-icon>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>

<style scoped></style>
