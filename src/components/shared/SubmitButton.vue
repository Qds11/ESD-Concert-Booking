<template>
    <v-btn variant="tonal">{{ action }}</v-btn>
</template>

<script>
export default{
    name:"SubmitButton",
    props: ['action']
}
</script>

<style>
.btn{
    color: black;
}
</style>