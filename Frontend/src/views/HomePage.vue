<script setup>
import DateTimeCard from '../components/DateTimeCard.vue';
import WeatherCard from '../components/WeatherCard.vue';
</script>


<template>
    <v-row>
        <v-col>
            <WeatherCard />
        </v-col>
        <v-col>
            <DateTimeCard />
        </v-col>
    </v-row>

</template>

<style></style>