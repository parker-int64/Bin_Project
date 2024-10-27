<script setup>
import * as echarts from "echarts";
import { nextTick, onMounted } from "vue";

const initLineChart = () => {
    var chart = echarts.init(document.getElementById("chart"))
    var option = {
        title: {
            text: "监测系统",
            left: "center",
        },
        xAxis: {
            type: 'category',
            data: ["10.24", "10.25", "10.26", "10.27"],
        },

        yAxis: {
            type: "value"
        },

        series: [
            {
                data: [10, 8, 7, 6],
                type: "line"
            }
        ]
    }

    chart.setOption(option)
}


// When mounted the components, add the charts
onMounted(() => {
    nextTick(() => {
        initLineChart()
    })
})


</script>
<template>
    <v-card class="card" elevation="12">
        <v-card-text class="ma-auto" id="chart" style="height: 300px">

        </v-card-text>
    </v-card>

</template>

<style>
.card {
    height: 300px;
}
</style>