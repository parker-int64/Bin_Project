<script setup>

import { onMounted, ref } from 'vue';
import dayjs from "dayjs"

const curDate = ref("1月1日 周一")
const curTime = ref("00:00:00")


const day = {
    "0": "日",
    "1": "一",
    "2": "二",
    "3": "三",
    "4": "四",
    "5": "五",
    "6": "六"
}

const updateDateAndTime = () => {
    setInterval(() => {
        let dateNow = dayjs(Date.now())
        let week_num = dateNow.format("d")

        curDate.value = `${dateNow.format("M月D日") + " 周" + day[week_num]}`
        curTime.value = `${dateNow.format("HH:mm:ss")}`
        console.log(dayjs)
    }, 1000)
}


onMounted(() => {
    updateDateAndTime()
})

</script>

<template>
    <v-card class="mx-auto" max-width="368">
        <v-card-item title="北京时间">
            <template v-slot:subtitle>
                UTC +8
            </template>
        </v-card-item>

        <v-card-text class="py-0">
            <v-row align="center" justify="center">
                <v-col class="text-h2" align="center">
                    {{ curTime }}
                </v-col>
            </v-row>
            <v-row align="center" no-gutters>
                <v-col class="text-h6" align="center">
                    {{ curDate }}
                </v-col>
            </v-row>



        </v-card-text>
    </v-card>
</template>

<style scoped></style>
