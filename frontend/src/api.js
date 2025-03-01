import axios from "axios";

const API_URL = "http://127.0.0.1:8000/api/"; // API бека

export async function getLessons() {
  try {
    const response = await axios.get(`${API_URL}lessons/`);
    return response.data;
  } catch (error) {
    console.error("Ошибка при загрузке данных:", error);
    return [];
  }
}

export async function getGroups() {
  try {
    const response = await axios.get(`${API_URL}groups/`);
    return response.data;
  } catch (error) {
    console.log("Ошибка при загрузке данных групп:", error);
    return [];
  }
}

export async function getDays() {
  try {
    const response = await axios.get(`${API_URL}days/`);
    return response.data;
  } catch (error) {
    console.log("Ошибка при загрузке данных дней:", error);
    return [];
  }
}
