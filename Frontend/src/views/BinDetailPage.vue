<script setup>

import { onMounted, ref, watch } from 'vue';

import { useRouter, useRoute } from 'vue-router';

import mdiLocationOn from "@/assets/mdi-location-on.svg"

import faMicroChip from "@/assets/fa-mircochip.svg"


const props = defineProps({
    binInfo: Object
})

const detailInfo = {
    binName: ref("unknown"),
    xiaoId: ref("unknown"),
    xiaoBat: ref("0%"),
    binLoc: ref("门前大桥下"),
    binStats: ref("满了！"),
}

const statsImg = ref(null)

const router = useRouter()

const returnToHome = () => {
    router.push("/")
}


onMounted(() => {
    const route = useRoute()
    const param = JSON.parse(route.query.item)
    detailInfo.binName.value = param["Device_Name"]
    detailInfo.xiaoId.value = param["Device_ID"]
    detailInfo.xiaoBat.value = param["Device_Battery"]
    detailInfo.binLoc.value = param["Device_Position"]
    detailInfo.binStats.value = param["Device_Status"]
    // statsImg.value = "/received_images/400x300.svg"
    statsImg.value = param["Picture_File_Name"]
})

</script>

<template>
    <v-btn elevation="2" icon="mdi-arrow-left" class="mt-5 ml-5" @click=returnToHome></v-btn>
    <v-card class="mx-auto " elevation="16" max-width="600">
        <v-card-item>
            <v-card-title class="d-flex flex-row align-center">
                <v-icon size="24">mdi-information</v-icon>
                <p class="text-body2 font-weight-black pl-2">详细信息</p>

            </v-card-title>

            <v-card-subtitle>
                {{ "这里显示的是" + detailInfo.binName.value + "桶子的信息" }}
            </v-card-subtitle>
        </v-card-item>

        <v-card-text>
            <v-list>
                <v-list-item two-line>
                    <v-list-item-content>
                        <v-list-item-title class="d-flex flex-row align-center">
                            <img :src="faMicroChip" class="svg-icon"></img>
                            <p class="font-weight-black pl-2">ID</p>
                        </v-list-item-title>
                        <v-list-item-subtitle class="pt-5">{{ detailInfo.xiaoId }}</v-list-item-subtitle>
                    </v-list-item-content>
                </v-list-item>

                <v-spacer style="height: 20px;"></v-spacer>

                <v-list-item two-line>
                    <v-list-item-content>
                        <v-list-item-title class="d-flex flex-row align-center">
                            <img :src="mdiLocationOn" class="svg-icon"></img>
                            <p class="font-weight-black pl-2">位置</p>
                        </v-list-item-title>
                        <v-list-item-subtitle class="pt-5">{{ detailInfo.binLoc }}</v-list-item-subtitle>
                    </v-list-item-content>
                </v-list-item>

                <v-spacer style="height: 20px;"></v-spacer>


                <v-list-item two-line>
                    <v-list-item-content>
                        <v-list-item-title class="d-flex flex-row align-center">
                            <v-icon>mdi-delete</v-icon>
                            <p class="font-weight-black">剩余电量</p>
                        </v-list-item-title>
                        <v-list-item-subtitle class="pt-5">{{ detailInfo.xiaoBat.value + "%" }}</v-list-item-subtitle>
                    </v-list-item-content>
                </v-list-item>

                <v-spacer style="height: 20px;"></v-spacer>

                <v-list-item two-line>
                    <v-list-item-content>
                        <v-list-item-title class="d-flex flex-row align-center">
                            <v-icon>mdi-delete</v-icon>
                            <p class="font-weight-black">桶子状态</p>
                        </v-list-item-title>
                        <v-list-item-subtitle class="pt-5">{{ detailInfo.binStats }}</v-list-item-subtitle>
                    </v-list-item-content>
                </v-list-item>

                <v-spacer style="height: 20px;"></v-spacer>


                <v-list-item two-line>
                    <v-list-item-content>
                        <v-list-item-title class="d-flex flex-row align-center">
                            <v-icon>mdi-image</v-icon>
                            <p class="font-weight-black">图片</p>
                        </v-list-item-title>
                        <v-list-item-subtitle class="d-flex justify-center pt-5">
                            <img :src="statsImg == null ? 'https://placehold.co/400x300' : statsImg"></img>
                        </v-list-item-subtitle>
                    </v-list-item-content>
                </v-list-item>

                <v-spacer style="height: 20px;"></v-spacer>
            </v-list>
        </v-card-text>
    </v-card>
</template>


<style>
.svg-icon {
    width: 20px;
    height: 20px;
}

.bin-image {
    width: 400px;
    height: 300px
}
</style>