<template>
    <div>
        <p>
            {{ msg }}
        </p>
    </div>
</template>

<script>
export default {
    name:'TestComponent',
    data() {
        return {
            msg : "trying not to kill myself"
        };
    }
}
</script>