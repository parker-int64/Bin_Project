<script setup>

import { onMounted, ref } from 'vue';
import dayjs from "dayjs"
import { getLunarDate, getSolarTerms } from 'chinese-days';
const curDate = ref("1月1日 周一")
const curTime = ref("00:00:00")
const curLunarDate = ref("农历")
const curSolarTerm = ref("") // Term，节气

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

        let lunar = getLunarDate(dateNow.format("YYYY-MM-DD"))
        let term = getSolarTerms(dateNow.format("YYYY-MM-DD"))[0]

        curDate.value = `${dateNow.format("M月D日") + " 周" + day[week_num]}`
        curTime.value = `${dateNow.format("HH:mm:ss")}`

        curLunarDate.value = `${lunar["lunarMonCN"] + lunar["lunarDayCN"]}`


        if (term) {
            curSolarTerm.value = `${term["name"]}`
        }
    }, 1000)
}


const jumpToTimeIs = () => {
    window.open("https://time.is/zh/")
}

const jumpToTimeIsCalendar = () => {
    window.open("https://time.is/zh/calendar")
}

onMounted(() => {
    updateDateAndTime()
})

</script>

<template>
    <v-card class="card" elevation="12">
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
            <v-row align="center">
                <v-col class="text-h6" align="center">
                    {{ curDate }}
                </v-col>
            </v-row>
            <div class="d-flex py-3 justify-space-between">
                <v-list-item density="compact" prepend-icon="mdi-calendar-today">
                    <v-list-item-subtitle>{{ "农历" + " " + curLunarDate + " " + curSolarTerm }}</v-list-item-subtitle>
                </v-list-item>
            </div>

        </v-card-text>
        <v-card-actions>
            <v-btn text="查看时间" append-icon="mdi-clock" @click=jumpToTimeIs></v-btn>
            <v-btn text="查看日历" append-icon="mdi-calendar" @click=jumpToTimeIsCalendar></v-btn>
        </v-card-actions>
    </v-card>
</template>

<style scoped>
.card {
    height: 300px;
}
</style>
