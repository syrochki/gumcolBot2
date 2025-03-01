<template>
  <div>
    <h1>Расписание 📅</h1>
    <ul>
      <li v-for="lesson in lessons" :key="lesson.id">
        {{ lesson.day }}: {{ lesson.subject }} - {{ lesson.teacher }}. Время:
        {{ lesson.lesson_starts_time }} -- {{ lesson.lesson_ends_time }}
      </li>
    </ul>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { getLessons } from "../api";

export default {
  name: "ScheduleView",
  setup() {
    const lessons = ref([]);

    onMounted(async () => {
      lessons.value = await getLessons();
    });

    return { lessons };
  },
};
</script>
<style scoped>
h1 {
  text-align: center;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  padding: 8px 0;
  border-bottom: 1px solid #eee;
}
</style>
