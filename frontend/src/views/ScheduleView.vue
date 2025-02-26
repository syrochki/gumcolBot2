<template>
  <div>
    <h1>Расписание 📅</h1>
    <ul>
      <li v-for="lesson in lessons" :key="lesson.id">
        {{ lesson.day.day }}: {{ lesson.subject }} - {{ lesson.teacher.name }}
      </li>
    </ul>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { getLessons } from "../api";

export default {
  setup() {
    const lessons = ref([]);

    onMounted(async () => {
      lessons.value = await getLessons();
    });

    return { lessons };
  },
};
</script>
