import axios from "axios";

const API_URL = "http://127.0.0.1:8000/api/lessons/";

export async function getLessons() {
  try {
    const response = await axios.get(API_URL);
    return response.data;
  } catch (error) {
    console.error("Ошибка при загрузке данных:", error);
    return [];
  }
}
