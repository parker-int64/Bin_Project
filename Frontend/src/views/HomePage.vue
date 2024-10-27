<script setup>
import ChartCard from '../components/ChartCard.vue';
import DateTimeCard from '../components/DateTimeCard.vue';
import WeatherCard from '../components/WeatherCard.vue';
import XiaoPanelCard from '../components/XiaoPanelCard.vue';


// get all xiao's information
</script>

<template>
    <v-layout class="d-flex flex-column ma-auto pa-10">
        <v-row>
            <v-col xs="12" sm="12" md="4" lg="4" xl="4" align="center">
                <WeatherCard />
            </v-col>
            <v-col xs="12" sm="12" md="4" lg="4" xl="4" align="center">
                <DateTimeCard />
            </v-col>

            <v-col xs="12" sm="12" md="4" lg="4" xl="4" align="center">
                <ChartCard />
            </v-col>
        </v-row>

        <v-spacer style="height: 50px;"></v-spacer>

        <v-row>
            <v-col v-for="item in 4" xs="4" sm="4" md="3" lg="3" xl="3">
                <XiaoPanelCard />
            </v-col>
        </v-row>
    </v-layout>
</template>

<style></style>