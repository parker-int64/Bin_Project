<script setup>

import dayjs from 'dayjs';
import { ref } from 'vue';
import "qweather-icons/font/qweather-icons.css"


const weatherData = {
  date: ref(dayjs(Date.now()).format("M月:D日")),
  temp: ref("0"),
  icon: ref(""),
  text: ref("加载中..."),
  fxLink: ref(""),
  wind360: ref(""),
  windDir: ref(""),
  windSpeed: ref(""),
  humidity: ref(""),
  pressure: ref(""),
  vis: ref(""),
  cloud: ref(""),
  dew: ref(""),

}

</script>

<template>
  <v-card class="mx-auto" max-width="368">
    <v-card-item title="深圳">
      <template v-slot:subtitle>
        <v-icon class="me-1 pb-1" color="error" icon="mdi-alert" size="18"></v-icon>

        It's raining <i class="qi-307"></i> and cold <i class="qi-901"></i>
      </template>
    </v-card-item>

    <v-card-text class="py-0">
      <v-row align="center" no-gutters>
        <v-col class="text-h2" cols="6">
          {{ weatherData.temp.value + "&deg;C" }}
        </v-col>

        <v-col class="text-right" cols="6">
          <v-icon :icon=weatherData.icon.value size="88"></v-icon>
        </v-col>
      </v-row>
    </v-card-text>

    <div class="d-flex py-3 justify-space-between">
      <v-list-item density="compact" prepend-icon="mdi-weather-windy">
        <v-list-item-subtitle>123 km/h</v-list-item-subtitle>
      </v-list-item>

      <v-list-item density="compact" prepend-icon="mdi-weather-pouring">
        <v-list-item-subtitle>48%</v-list-item-subtitle>
      </v-list-item>
    </div>
    <!--Open in QWeather-->
    <v-card-actions>
      <v-btn text="在和风天气中查看" append-icon="qi-qweather-fill"></v-btn>
    </v-card-actions>
  </v-card>
</template>

<style scoped></style>
