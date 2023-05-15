<script setup>
const { data: jobs } = await useFetch('http://127.0.0.1:8000/api/v1/jobs/newest/')
</script>
<template>
    <div>
        <div class="py-20  bg-teal-700 text-center">
            <h1 class="mb-12 text-5xl text-white">Find a job any where</h1>
            <NuxtLink to="/browse" class="inline-block py-4 px-8 bg-teal-900 hover:bg-teal-800 text-white rounded-xl">Browse</NuxtLink>
        </div>

        <div class="p-6">
            <h2 class="mb-6 text-2xl text-center">Newest jobs</h2>

            <div class="space-y-4">

                <job 
                v-for="job in jobs" 
                v-bind:key="job.id"
                v-bind:job="job"
                />

            </div>
        
        </div>
    </div>

</template>