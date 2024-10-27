<script setup>

</script>

<template>
    <v-spacer style="height: 20px"></v-spacer>
    <v-card class="mx-auto " elevation="16" max-width="600">
        <v-card-item>
            <v-card-title class="d-flex flex-row align-center">
                <v-icon size="24">mdi-cog</v-icon>
                <p class="text-body2 font-weight-black pl-2">设置</p>
            </v-card-title>

            <v-card-subtitle>
                杂项设置
            </v-card-subtitle>
        </v-card-item>

        <v-card-text>
            <v-list>
                <v-list-item two-line>
                    <v-list-item-content>
                        <v-list-item-title class="d-flex flex-row">
                            <v-icon>mdi-server</v-icon>
                            <p class="font-weight-black pl-2">MQTT</p>
                        </v-list-item-title>
                        <v-list-item-subtitle class="d-flex flex-row  pt-5">
                            <v-text-field :rules="rules" hide-details="auto" label="Server"></v-text-field>
                            <v-text-field class="ml-10" :rules="rules" hide-details="auto" label="Port"></v-text-field>
                        </v-list-item-subtitle>
                        <div class="d-flex justify-end">
                            <v-btn append-icon="mdi-check" color="primary" class="mt-5">保存</v-btn>
                        </div>
                    </v-list-item-content>
                </v-list-item>

                <v-spacer style="height: 20px;"></v-spacer>

            </v-list>
        </v-card-text>
    </v-card>
</template>