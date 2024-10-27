<script setup>
import dayjs from 'dayjs';
import { onMounted, ref } from 'vue';
import "qweather-icons/font/qweather-icons.css"
import keyJson from '../../key.json'

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
  title: ref(""),    // warning title
  type: ref(""),    // warning icon
  severity: ref(""),  // warning severity
  severityColor: ref("") // warning severity color
}

const warningColorTable = {
  "White": "grey",
  "Blue": "blue",
  "Green": "green",
  "Yellow": "yellow",
  "Orange": "orange",
  "Red": "error",
  "Black": "black"
}

const key = keyJson["privateKey"]

const getWeatherData = async () => {
  let url = `https://devapi.qweather.com/v7/weather/now?location=101280604&lang=zh&key=${key}`

  const response = await fetch(url)

  const weatherDataRaw = await response.json()

  return weatherDataRaw

}


const getWeatherWarning = async () => {
  let url = `https://devapi.qweather.com/v7/warning/now?location=101280604&lang=zh&key=${key}`

  const response = await fetch(url)

  const weatherWarningDataRaw = await response.json()

  return weatherWarningDataRaw
}


const parseWeatherData = (wdr, wwdr) => {
  console.log("Parse the raw weather data from qweather")
  weatherData["fxLink"] = wdr["fxLink"]
  for (const [key, value] of Object.entries(wdr["now"])) {

    // console.log(`Key: ${key}, Value: ${value}`)
    // console.log(`${weatherData.hasOwnProperty(key)}`)

    if (weatherData.hasOwnProperty(key)) {
      weatherData[key].value = value
    }
  }

  console.log("Parse the raw weather \"warning\" data from qweather")

  // If we have the warning information
  if (wwdr["warning"][0]) {
    for (const [key, value] of Object.entries(wwdr["warning"][0])) {
      if (weatherData.hasOwnProperty(key)) {
        weatherData[key].value = value
      }
    }
  }

}

const getQiIcon = (icon) => {
  return `qi-${icon}`
}

const getWarningColor = (color) => {
  return warningColorTable[color]
}


const jumpToQWeather = () => {
  window.open(weatherData["fxLink"])
}

const updateWeatherData = async () => {
  const wdr = await getWeatherData() // raw weather data from qweather
  const wwdr = await getWeatherWarning() // raw weather warning data from qweather
  if (wdr, wwdr) {
    parseWeatherData(wdr, wwdr)
  }
}

onMounted(async () => {
  await updateWeatherData()  // when mount the components, update the weather data immediately
  setInterval(async () => {
    await updateWeatherData()
  }, 3600000)   // auto update the weather data every hour

})

</script>

<template>
  <v-card class="card" elevation="12">
    <v-card-item title="深圳·南山">
      <template v-slot:subtitle>
        <v-icon class="me-1 pb-1" :color=getWarningColor(weatherData.severityColor.value)
          :icon=getQiIcon(weatherData.type.value) size="18"></v-icon>
        {{ weatherData.title.value }}
      </template>
    </v-card-item>

    <v-card-text class="py-0">
      <v-row align="center" no-gutters>
        <v-col class="text-h2" cols="6">
          {{ weatherData.temp.value + "&deg;C" }}
        </v-col>

        <v-col class="text-right" cols="6">
          <v-icon :icon=getQiIcon(weatherData.icon.value) size="88"></v-icon>
        </v-col>
      </v-row>
    </v-card-text>

    <div class="d-flex py-3 justify-space-between">
      <v-list-item density="compact" prepend-icon="mdi-weather-windy">
        <v-list-item-subtitle>{{ `${weatherData.windDir.value} ${weatherData.windSpeed.value}km/h`
          }}</v-list-item-subtitle>
      </v-list-item>

      <v-list-item density="compact" prepend-icon="mdi-humidity-high">
        <v-list-item-subtitle>48%</v-list-item-subtitle>
      </v-list-item>
    </div>
    <!--Open in QWeather-->
    <v-card-actions>
      <v-btn text="在和风天气中查看" append-icon="qi-qweather-fill" @click=jumpToQWeather></v-btn>
    </v-card-actions>
  </v-card>
</template>

<style scoped>
.card {
  height: 300px;
}
</style>
