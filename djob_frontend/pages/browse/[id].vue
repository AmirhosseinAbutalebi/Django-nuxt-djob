<script setup>
const route = useRoute()
const { data: job } = await useFetch('http://127.0.0.1:8000/api/v1/jobs/' + route.params.id + '/')
useSeoMeta({
    title: job.value.title,
    ogTitle: job.value.ogTitle,
    description: job.value.description,
})
</script>
<template>
    <div class="py-10 px-6 grid md:grid-cols-4 gap3">
        <div class="md:col-span-3">
            <h1 class="mb-6 text-3xl">{{ job.title }}</h1>

            <p>
                {{ job.description }}
            </p>

            <a v-bind:href="'mailto:' + job.company_email" class="inline-block mt-6 py-4 px-4 bg-teal-700 text-white rounded-xl hover:bg-teal-600">Apply</a>
        </div>

        <div class="md:col-span-1 p-6 bg-teal-700 text-white rounded-xl">
            <h3 class="mb-4 text-2xl">company</h3>
            <p class="mb-1">{{ job.company_name }}</p>
            <p>{{ job.company_location}}</p>

            <hr class="my-3 opacity-50">
            <h3 class="mb-4 text-2xl">Position</h3>
            <p class="mb-1">{{ job.position_location}}</p>
            <p>{{ job.position_salary}}</p>

            <hr class="my-2 opacity-50">
            <p>Posted : {{ job.created_at_formatted }}</p>
        </div>
    </div>
</template>