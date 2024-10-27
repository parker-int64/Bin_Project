<script setup>

import { onMounted, ref } from 'vue';


const binStatus = ref("null")

const statusWord = {
    "null": "未知",
    "empty": "空空如也~",
    "alert": "即将满溢",
    "full": "已满，立即清理"
}

</script>

<template>
    <v-card class="mx-auto" elevation="12">
        <v-card-item title="XIAO 检测系统">
            <template v-slot:subtitle>
                当前垃圾桶情况
            </template>
        </v-card-item>

        <v-card-text class="py-0">
            <v-row align="center" justify="center">
                <v-col align="center">
                    <v-icon v-if="binStatus === 'empty'" icon="mdi-delete" color="green" size="88" />
                    <v-icon v-else-if="binStatus === 'alert'" icon="mdi-delete-alert" color="yellow" size="88" />
                    <v-icon v-else-if="binStatus === 'full'" icon="mdi-delete-empty" color="red" size="88" />
                    <v-icon v-else icon="mdi-help" color="#BDBDBD" size="88" />
                </v-col>
            </v-row>
            <v-row align="center" no-gutters>
                <v-col class="text-h6" align="center">
                    {{ statusWord[binStatus] }}
                </v-col>
            </v-row>
        </v-card-text>

        <v-card-actions>
            <v-btn text="查看详情" append-icon="mdi-chevron-right"></v-btn>
        </v-card-actions>
    </v-card>
</template>

<style scoped></style>
