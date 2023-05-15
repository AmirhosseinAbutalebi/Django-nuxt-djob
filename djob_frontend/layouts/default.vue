<script setup>
import { useUserStore } from '~/stores/user';

const userStore = useUserStore()
function logout(){
    userStore.removeToken()
}
</script>
<template>
    <div>
        <nav class="p-4 flex items-left justify-between bg-teal-800">
            <NuxtLink to="/" class="text-xl text-white ">Djob</NuxtLink>

            <div class="flex items-center space-x-4">
                <NuxtLink to="/" class="text-white hover:text-teal-300">Home</NuxtLink>
                <NuxtLink to="/Browse" class="text-white hover:text-teal-300">Browse</NuxtLink>
            </div>
        </nav>
        <slot />
        <footer class="p-3 flex flex-wrap items-center justify-between bg-gray-900">
            <p class="text-gray-300">Copyright (c) 2023 - Djob</p>

            <div class="flex mt-6 md:mt-0 items-center space-x-3">
                <template v-if="userStore.user.isAuthenticated">
                    <NuxtLink to="/myjobs" class="py-3 px-4 bg-teal-900 hover:bg-teal-700 text-white rounded-xl">My jobs</NuxtLink>
                    <NuxtLink to="/createjob" class="py-3 px-4 bg-teal-900 hover:bg-teal-700 text-white rounded-xl">Create job</NuxtLink>
                    <a v-on:click="logout" class="py-3 px-4 bg-rose-900 hover:bg-rose-700 text-white rounded-xl">Log out</a>
                </template>
                <template v-else>
                    <NuxtLink to="/login" class="py-3 px-4 bg-teal-900 hover:bg-teal-700 text-white rounded-xl">Login</NuxtLink>
                    <NuxtLink to="/signup" class="py-3 px-4 bg-teal-900 hover:bg-teal-700 text-white rounded-xl">Sign up</NuxtLink>
                </template>
            </div>
        </footer>
    </div>
</template>